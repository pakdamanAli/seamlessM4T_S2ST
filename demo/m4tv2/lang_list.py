# Language dict
language_code_to_name = {
    "arb": "Modern Standard Arabic",
    "eng": "English",
    "pes": "Western Persian",
}
LANGUAGE_NAME_TO_CODE = {v: k for k, v in language_code_to_name.items()}

# Source langs: S2ST / S2TT / ASR don't need source lang
# T2TT / T2ST use this
text_source_language_codes = [
    "arb",
    "eng",
    "pes"
]
TEXT_SOURCE_LANGUAGE_NAMES = sorted([language_code_to_name[code] for code in text_source_language_codes])

# Target langs:
# S2ST / T2ST
s2st_target_language_codes = [
    "eng",
    "arb",
    "pes"
]
S2ST_TARGET_LANGUAGE_NAMES = sorted([language_code_to_name[code] for code in s2st_target_language_codes])
T2ST_TARGET_LANGUAGE_NAMES = S2ST_TARGET_LANGUAGE_NAMES
