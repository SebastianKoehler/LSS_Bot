import random

import pyautogui as pag
import pygetwindow as pgw
import time
import os
import cv2
import numpy as np


def create_raw_screenshot():
    pag.screenshot('screenshots/raw/raw_base_ui.png')


def get_mouse_position_coordinates():
    time.sleep(5)
    mouse_x, mouse_y = pag.position()
    print(f"Mouse positions: X:{mouse_x}; Y:{mouse_y}")


def find_image_absolute_path(image_name: str) -> str:
    for root, dirs, files in os.walk("screenshots"):
        if image_name in files:
            return os.path.join(root, image_name)
    return ""


def locate_on_screen(image_name: str, confidence: float = 0.8) -> bool:
    try:
        image_abs_path = find_image_absolute_path(image_name)
        location = pag.locateOnScreen(image_abs_path, confidence=confidence)

        center = pag.center(location)
        pag.moveTo(center)
        pag.click()
        time.sleep(1)
        return True
    except pag.ImageNotFoundException:
        print("No image found!")
        return False
    except IOError:
        print("IOError: Failed to read  because file is missing, has improper permissions, or is an unsupported or invalid format")
        return False


def check_for_close_button():
    locate_on_screen("offer_close_button_1.PNG")
    time.sleep(10)
    locate_on_screen("offer_close_button_2.PNG")


def get_all_lss_instances():
    all_windows = pgw.getAllWindows()
    filtered_windows = [lss_instance for lss_instance in all_windows if lss_instance.title.startswith("Invi")]
    return filtered_windows


# Überprüfe Bildschirm ob plot vorhanden ist
# Falls nicht, bewege den Bildschirm in eine Himmelsrichtung, überprüfe erneut
# Erkenne einen Plot,
# Prüfe wie viele APC maximal zur Verfügung stehen
# und wie viele überhaupt Frei sind,
# ebenso die Dura min. 10
# prüfe ob Verfügbar oder occupied, wenn Frei,
# prüfe das Level -> min. 5

# Wenn Plot vorhanden, Plot frei, Plot min. lvl 5, 1 APC mit min. 10 Dura frei, Automatische Bereitstellung, Marsch

def reset_mouse_to_window_center():
    window_x, window_y = pag.size()[0] // 2, pag.size()[1] // 2
    return window_x, window_y


def move_random_direction():

    directions = ["north", "south", "east", "west"]
    direction = random.choice(directions)

    start_x, start_y = reset_mouse_to_window_center()
    pag.moveTo(start_x, start_y)

    offset = 400
    if direction == "north":
        end_x, end_y = start_x, start_y - offset
    elif direction == "south":
        end_x, end_y = start_x, start_y + offset
    elif direction == "east":
        end_x, end_y = start_x + offset, start_y
    else: # west
        end_x, end_y = start_x - offset, start_y

    pag.mouseDown(start_x, start_y)
    time.sleep(0.2)
    pag.moveTo(end_x, end_y, duration=1)
    pag.mouseUp()
    time.sleep(1)


def check_plot_level():
    pass


def find_ress_plot(plot_type: str, confidence: float = 0.7):
    attempts = 0
    while attempts <= 10:
        attempts += 1
        success = locate_on_screen(plot_type, confidence)
        if success:
            mouse_x, mouse_y = pag.position()
            pag.moveTo(mouse_x, mouse_y)
            print(f"Found at X:{mouse_x};Y:{mouse_y}")
            break
        move_random_direction()
        time.sleep(1)


def main():
    lss_instances = get_all_lss_instances()

    for instance in lss_instances:
        instance.activate()

        # pag.hotkey("F11")

        # time.sleep(5)
        # locate_on_screen("lss_game_icon.PNG")
        # time.sleep(20)
        # check_for_close_button()
        # time.sleep(3)
        # locate_on_screen("map_icon.PNG")
        # time.sleep(5)


        # find_ress_plot("iron_plot.PNG", 0.8)
        # time.sleep(1)
        # locate_on_screen("map_gathering_button.PNG", 0.8)
        locate_on_screen("apcs_button.PNG", 0.8)

if __name__ == "__main__":
    main()
