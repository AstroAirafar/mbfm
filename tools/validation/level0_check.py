# tools/validation/level0_check.py

import sys
from pathlib import Path

# Add foundation/ to PYTHONPATH
FOUNDATION_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(FOUNDATION_ROOT))

from level0.governance.contracts import WINDOWS, EMBEDDINGS


def run_level0_check():
    assert set(WINDOWS.values()) == {5, 15, 60}
    for name, spec in EMBEDDINGS.items():
        assert "dim" in spec
        assert "version" in spec
    print("✅ Level 0 validation passed")


if __name__ == "__main__":
    run_level0_check()
