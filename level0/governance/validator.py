# level0/governance/validator.py

from .contracts import ALLOWED_WINDOWS, EMBEDDINGS

def validate_window(window_sec: int):
    if window_sec not in ALLOWED_WINDOWS:
        raise ValueError(f"Invalid window size: {window_sec}")

def validate_embedding(name: str, tensor):
    spec = EMBEDDINGS[name]
    if tensor.shape[-1] != spec["dim"]:
        raise ValueError(
            f"{name} dim mismatch: expected {spec['dim']}, got {tensor.shape[-1]}"
        )

def validate_level0_config(window_sec: int, embeddings: dict):
    validate_window(window_sec)
    for name, tensor in embeddings.items():
        validate_embedding(name, tensor)
