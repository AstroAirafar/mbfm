# level0/governance/contracts.py

# --------------------
# Temporal Windows (seconds)
# --------------------
WINDOWS = {
    "micro": 5,
    "interaction": 15,
    "state": 60,
}

ALLOWED_WINDOWS = set(WINDOWS.values())

# --------------------
# Embedding Contracts
# --------------------
EMBEDDINGS = {
    "pose": {
        "dim": 128,
        "version": "v1",
        "dtype": "float32",
    },
    "vision": {
        "dim": 256,
        "version": "v1",
        "dtype": "float32",
    },
    "audio": {
        "dim": 128,
        "version": "v1",
        "dtype": "float32",
    },
    "graph": {
        "dim": 128,
        "version": "v1",
        "dtype": "float32",
    },
}

# --------------------
# Privacy Rules
# --------------------
RAW_DATA_FORBIDDEN_AFTER_EXTRACTION = True
