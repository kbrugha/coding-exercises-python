invalidPostcodes = [
    "",
    "wrong",
    "also wrong",
    "ab10 1xg",   # Invalid lower case
    "QB10 1XG",   # Position 1 invalid
    "AI10 1XG",   # Position 2 invalid
    "COZ 9XG",    # Position 3 invalid
    "AB1C 1XG",   # Position 4 invalid
    "AB10 1CG",   # Group 2 Position -2 invalid
    "AB10 1XI",   # Group 2 Position -1 invalid
    "A 1XG",      # Group 1 too short
    "AB10 1X",    # Group 2 too short
    "AB101 1XG",  # Group 1 too long
    "AB10 1XGG",  # Group 2 too long
    "101 1XG",    # Group 1 invalid
    "10 1XG",     # Group 1 invalid
    "1 1XG",      # Group 1 invalid
    "ABB 1XG",    # Group 1 digit invalid
    "AB 1XG",     # Group 1 digit invalid
    "A 1XG",      # Group 1 digit Invalid
    "AB10 1X",    # Group 2 invalid
    "AB10 1",     # Group 2 invalid
]

validPostcodes = [
    "AB10 1XG",
    "CO3 9XG",
    "FK11 7AN",
    "EX20 1NA",
    "RM15 6BQ",
    "PL95 8BS",
    "OX16 0QX",
    "SY23 5DP",
    "PE30 4EE",
    "B73 5EA",
    "AB53 6TU",
    "NE3 4HA",
    "EH46 7BZ",
    "NE44 6DG",
    "IV55 8WU",
    "PA19 1RX",
    "PH25 3AB",
    "W10 4HJ",
    "KA5 6HF",
    "BD3 9DS",
]
