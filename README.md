Mouse Jiggler
This is a simple Python script that simulates mouse movement to prevent your computer from going to sleep or your status on applications like Microsoft Teams from changing to "away."

Features
Lightweight: A simple script with minimal dependencies.

Configurable: Easily adjust the time interval and mouse movement distance.

Non-invasive: Moves the mouse just enough to trick the system without interrupting your work.

Prerequisites
Before running the script, make sure you have the following installed:

Python 3.x: If you don't have it, you can download it from python.org.

The pyautogui library.

Installation
Open your terminal or command prompt.

Install the pyautogui library using pip:

pip install pyautogui

Usage
Save the script as mouse_jiggler.py.

Open your terminal or command prompt and navigate to the directory where you saved the file.

Run the script using the following command:

python mouse_jiggler.py

The script will start running and you will see the message: "Mouse Jiggler script is running. Press Ctrl+C to stop."

To stop the script, simply go back to your terminal and press Ctrl+C.

Configuration
You can easily customize the behavior of the script by editing the following variables at the top of the file:

Interval: The number of seconds between each mouse movement (default is 300 seconds, or 5 minutes).

distance: The number of pixels the mouse will move (default is 5 pixels).

#You can adjust the interval (in seconds) between movements
interval = 300

#You can adjust the distance (in pixels) the mouse moves
distance = 5

Disclaimer
This script is provided for personal use.
