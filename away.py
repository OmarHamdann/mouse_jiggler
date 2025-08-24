#pip install pyautogui
#python mouse_jiggler.py

import pyautogui
import time

#  (in seconds) between movements
interval = 8

# A mouse moves is less noticeable.
distance = 50

print("Mouse Jiggler script is running. Press Ctrl+C to stop.")

try:
    while True:
        current_x, current_y = pyautogui.position()
        pyautogui.moveTo(current_x + distance, current_y + distance, duration=0.25)
        pyautogui.moveTo(current_x, current_y, duration=0.25)
        time.sleep(interval)

except KeyboardInterrupt:
    print("\nMouse Jiggler script stopped.")