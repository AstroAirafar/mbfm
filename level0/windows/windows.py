# level0/windows/windows.py

from level0.governance.contracts import WINDOWS

def get_window_seconds(name: str) -> int:
    return WINDOWS[name]
