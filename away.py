import time
import platform
import ctypes

try:
    import pyautogui
except ModuleNotFoundError:
    print("pyautogui is not installed. Run: python3 -m pip install pyautogui")
    raise SystemExit(1)

# Time in seconds between movements.
interval = 5

# Distance in pixels for each mouse movement.
distance = 520

# Moving the mouse to a screen corner stops pyautogui as an emergency fail-safe.
pyautogui.FAILSAFE = True

system_name = platform.system()


class CGPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]


def move_mouse_macos(x, y):
    core_graphics = ctypes.cdll.LoadLibrary(
        "/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics"
    )
    core_foundation = ctypes.cdll.LoadLibrary(
        "/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation"
    )

    core_graphics.CGWarpMouseCursorPosition.argtypes = [CGPoint]
    core_graphics.CGWarpMouseCursorPosition.restype = ctypes.c_int32
    core_graphics.CGEventCreateMouseEvent.argtypes = [
        ctypes.c_void_p,
        ctypes.c_uint32,
        CGPoint,
        ctypes.c_uint32,
    ]
    core_graphics.CGEventCreateMouseEvent.restype = ctypes.c_void_p
    core_graphics.CGEventPost.argtypes = [ctypes.c_uint32, ctypes.c_void_p]
    core_foundation.CFRelease.argtypes = [ctypes.c_void_p]

    point = CGPoint(x, y)
    result = core_graphics.CGWarpMouseCursorPosition(point)
    event = core_graphics.CGEventCreateMouseEvent(None, 5, point, 0)
    if event:
        core_graphics.CGEventPost(0, event)
        core_foundation.CFRelease(event)
    return result == 0

if system_name == "Darwin":
    print("macOS detected. Allow Terminal/Python in System Settings > Privacy & Security > Accessibility if prompted.")
elif system_name == "Linux":
    print("Linux detected. This needs a graphical desktop session; Wayland may require X11/XWayland support.")

print("Mouse Jiggler script is running. Press Ctrl+C to stop.")

try:
    while True:
        current_x, current_y = pyautogui.position()
        screen_width, screen_height = pyautogui.size()

        x_distance = distance if current_x + distance < screen_width else -distance
        y_distance = distance if current_y + distance < screen_height else -distance

        if system_name == "Darwin":
            if not move_mouse_macos(current_x + x_distance, current_y + y_distance):
                print("macOS blocked mouse movement. Check Accessibility permission for Terminal/Python.")
            time.sleep(0.25)
            move_mouse_macos(current_x, current_y)
        else:
            pyautogui.moveRel(x_distance, y_distance, duration=0.25)
            pyautogui.moveRel(-x_distance, -y_distance, duration=0.25)
        time.sleep(interval)

except KeyboardInterrupt:
    print("\nMouse Jiggler script stopped.")
except pyautogui.FailSafeException:
    print("\nMouse Jiggler stopped by fail-safe. Move the mouse away from the screen corner and run it again.")
