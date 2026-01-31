# level0/governance/rules.py

FORBIDDEN = {
    "custom_window_sizes": True,
    "raw_data_access_outside_extraction": True,
    "embedding_dim_mutation": True,
}

REQUIRED = {
    "use_feature_cache": True,
    "schema_validation": True,
    "window_alignment": True,
}
