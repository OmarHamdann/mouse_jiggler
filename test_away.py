import sys
from unittest.mock import MagicMock

# away.py talks to the real display via pyautogui. Stub it out before import so
# tests run on any CI runner without a GUI/display attached.
## To run: python3 -m pytest -v
pyautogui_stub = MagicMock()
pyautogui_stub.FAILSAFE = False
pyautogui_stub.FailSafeException = Exception
sys.modules.setdefault("pyautogui", pyautogui_stub)

import away  # noqa: E402


def test_compute_jiggle_offsets_moves_positive_with_room_on_screen():
    x, y = away.compute_jiggle_offsets(0, 0, 1920, 1080, 520)
    assert (x, y) == (520, 520)


def test_compute_jiggle_offsets_flips_negative_near_screen_edge():
    x, y = away.compute_jiggle_offsets(1900, 1060, 1920, 1080, 520)
    assert (x, y) == (-520, -520)


def test_is_idle_false_before_threshold():
    assert away.is_idle(last_activity_time=0, now=19.9, threshold=20) is False


def test_is_idle_true_once_threshold_elapsed():
    assert away.is_idle(last_activity_time=0, now=20, threshold=20) is True


def test_default_settings_are_sane():
    assert away.idle_threshold > 0
    assert away.poll_interval > 0
    assert away.distance > 0
