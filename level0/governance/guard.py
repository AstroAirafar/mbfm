# level0/governance/guard.py

import os

def forbid_raw_access(path: str):
    if "raw" in path.lower():
        raise RuntimeError(
            "❌ Raw data access blocked by Level 0 governance"
        )

def enforce_no_raw_env():
    for v in os.environ.values():
        if "raw" in str(v).lower():
            raise RuntimeError("❌ Raw data path leaked into environment")
