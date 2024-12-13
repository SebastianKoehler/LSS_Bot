import pyautogui
import pyautogui as pag
import time


def create_raw_base_ui_screenshot():
    pag.screenshot('screenshots/raw/raw_base_ui.png')

def get_mouse_position_coordinates():
    time.sleep(3)
    mouse_x, mouse_y = pyautogui.position()
    print(f"Mouse positions: X:{mouse_x}; Y:{mouse_y}")

def go_to_location():
    location = pag.locateOnScreen("screenshots/buildings/production/farm.PNG", confidence=0.8)

    if location:
        print(f"gefunden bei: {location}")
        center = pag.center(location)
        pag.moveTo(center)
    else:
        print(location)

def main():
    go_to_location()

if __name__ == "__main__":
    main()
