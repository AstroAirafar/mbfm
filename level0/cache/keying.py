# level0/cache/keying.py

def make_cache_key(modality, window, version, sample_id):
    return f"{modality}|{window}s|{version}|{sample_id}"
