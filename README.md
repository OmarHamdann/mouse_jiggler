

## Mouse Jiggler

This is a simple Python script that prevents your computer from going into sleep mode or changing your status to "Away" on applications like Microsoft Teams, Slack, or other communication platforms. It watches for real mouse activity and only jiggles the mouse a few pixels once you've been idle for a while — so it stays out of your way while you're actually working.

### Features

  * **Smart:** Pauses the moment you move the mouse yourself, and only jiggles again once you've gone idle.
  * **Lightweight:** A minimal script that uses very little system resources.
  * **Customizable:** Easily change the idle threshold, check frequency, and mouse movement distance to suit your needs.
  * **Simple to use:** Requires only a single Python library to run.
  * **macOS support:** Uses native CoreGraphics calls on macOS for reliable mouse movement.

-----

## How to Install and Run

### Step 1: Install Python

If you don't have Python installed, download it from the official website: [**python.org**](https://www.python.org/downloads/).

During installation on Windows, make sure to check the box that says **"Add Python to PATH"** to make it easier to run the script from the command line.

### Step 2: Install the `pyautogui` Library

This script uses the `pyautogui` library to control the mouse. You can install it using `pip`, Python's package installer.
Open your **Command Prompt** (on Windows) or **Terminal** (on macOS/Linux) and run the following command:

```bash
pip3 install pyautogui
```

### Step 3: Run the Script

1.  Open your Command Prompt or Terminal.
2.  Navigate to the directory where you saved this repository. For example, if you saved it on your Desktop, type `cd Desktop/mouse_jiggler`.
3.  Execute the script with this command:

```bash
python3 away.py
```

The script will now be running and watching for activity in the background. You'll see it print a message in the terminal when it starts.

**macOS only:** the first time you run it, macOS may prompt you to grant Accessibility permission to Terminal (or Python) under **System Settings > Privacy & Security > Accessibility**. Without this, mouse movement will be silently blocked.

-----

## Running It With a Keyboard Shortcut (macOS)

This repo includes [`run_jiggler.sh`](run_jiggler.sh), which opens a Terminal window and starts the script — handy for binding to a keyboard shortcut via the **Shortcuts** app:

1. Open **Shortcuts.app** and create a new shortcut.
2. Add a **"Run Shell Script"** action, set Shell to `/bin/zsh`, and point it at `run_jiggler.sh`.
3. Open the shortcut's Details (ⓘ) and choose **Add Keyboard Shortcut** to bind it to a key combo.

`run_jiggler.sh` has the project path hardcoded near the top — update `JIGGLER_DIR` if you move the repo.

-----

## How to Stop the Script

To stop the script at any time, go back to the terminal window and press **`Ctrl+C`**.

-----

## Customization

You can adjust how the jiggler behaves by opening `away.py` in a text editor and modifying the following variables near the top of the file:

  * **`idle_threshold`**: How many seconds of no real mouse movement must pass before the script jiggles the mouse. The default is `20`.
  * **`poll_interval`**: How often, in seconds, the script checks whether the mouse has moved. The default is `1`.
  * **`distance`**: The number of pixels the mouse will move during a jiggle. The default is `520`.

For example, to wait 2 minutes of inactivity before jiggling:

```python
idle_threshold = 120  # 2 minutes
```

## Disclaimer
This script is provided for personal use.
