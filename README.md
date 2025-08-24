

## Mouse Jiggler

This is a simple Python script that prevents your computer from going into sleep mode or changing your status to "Away" on applications like Microsoft Teams, Slack, or other communication platforms. It works by periodically moving the mouse a few pixels, simulating user activity.

### Features

  * **Lightweight:** A minimal script that uses very little system resources.
  * **Customizable:** Easily change the time interval and mouse movement distance to suit your needs.
  * **Simple to use:** Requires only a single Python library to run.

-----

## How to Install and Run

### Step 1: Install Python

If you don't have Python installed, download it from the official website: [**python.org**](https://www.python.org/downloads/).

During installation on Windows, make sure to check the box that says **"Add Python to PATH"** to make it easier to run the script from the command line.

### Step 2: Install the `pyautogui` Library

This script uses the `pyautogui` library to control the mouse. You can install it using `pip`, Python's package installer.
Open your **Command Prompt** (on Windows) or **Terminal** (on macOS/Linux) and run the following command:

```bash
pip install pyautogui
```

### Step 3: Run the Script

1.  Save the provided code in a file named `mouse_jiggler.py`.
2.  Open your Command Prompt or Terminal.
3.  Navigate to the directory where you saved the file. For example, if you saved it on your Desktop, type `cd Desktop`.
4.  Execute the script with this command:

<!-- end list -->

```bash
python mouse_jiggler.py
```

The script will now be running. It will move your mouse every 5 minutes by default. You can see the script is active in the terminal.

-----

## How to Stop the Script

To stop the script at any time, go back to the terminal window and press **`Ctrl+C`**.

-----

## Customization

You can easily adjust the script to change the movement frequency or distance. Open the `mouse_jiggler.py` file in a text editor and modify the following two variables at the top of the file:

  * **`interval`**: The time in seconds between each mouse movement. The default is `300` (5 minutes).
  * **`distance`**: The number of pixels the mouse will move. The default is `5`.

For example, to make the mouse move every minute, change the `interval` to `60`:

```python
interval = 60  # 1 minute
```

## Disclaimer
This script is provided for personal use.
