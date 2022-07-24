#!/usr/bin/python3

import argparse
import re
import sys


def validate_postcode(postcode):
    postcode = postcode.rstrip()

    if (len(postcode) < 6 or len(postcode) > 8):
        return False, "invalid length"

    if not postcode.isupper():
        return False, "invalid lower case"

    postcode_arr = postcode.split(" ")

    if len(postcode_arr) != 2:
        return False, "invalid number of spaces"

    if len(postcode_arr[1]) != 3:
        return False, "invalid group 2 length"

    #  Exceptions
    # The letters Q, V and X are not used in the first position.
    # The letters I, J and Z are not used in the second position.
    # The only letters to appear in the third position are
    #       A, B, C, D, E, F, G, H, J, K, P, S, T, U and W when the structure starts with A9A.
    # The only letters to appear in the fourth position are
    #       A, B, E, H, M, N, P, R, V, W, X and Y when the structure starts with AA9A.
    # The final two letters do not use
    #       C, I, K, M, O or V, so as not to resemble digits or each other when hand-written.
    exceptions = ["QVX", "IJZ", "ABCDEFGHJKPSTUW", "ABEHMNPRVWXY", "CIKMOV"]

    if postcode[0] in exceptions[0]:
        return False, "invalid character position 1"

    if postcode[1] in exceptions[1]:
        return False, "invalid character position 2"

    excep_pos = 2
    if len(postcode_arr[0]) == 4:
        excep_pos += 1

    if postcode[excep_pos].isalpha() and postcode[excep_pos] not in exceptions[excep_pos]:
        excep_pos += 1
        return False, f"invalid character position {excep_pos}"

    if postcode[-1] in exceptions[4] or postcode[-2] in exceptions[4]:
        return False, "invalid character group 2"

    pattern = r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) "\
        "?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} "\
        "?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"

    try:
        re.compile(pattern)
    except re.error:
        print("Invalid regex pattern")
        sys.exit()

    if not re.fullmatch(pattern, postcode):
        return False, "invalid mismatch pattern"

    return True, "valid"


def format_postcode(postcode):
    postcode = postcode.upper()

    if (len(postcode) < 6 or len(postcode) > 8):
        return None, "invalid postcode: Wrong length"

    postcode = postcode[:-3] + " " + postcode[-3:]

    is_valid, message = validate_postcode(postcode)

    if not is_valid:
        return None, "invalid postcode: " + message

    return postcode, "success"


def print_format_postcode(postcode):
    formatted, message = format_postcode(postcode)
    if formatted is not None:
        print(f"Postcode formatted'{postcode}' -> '{formatted}'")
    else:
        print(f"Formatting '{postcode}' failed, {message}")


def print_postcode(postcode):
    is_valid, message = validate_postcode(postcode)
    if is_valid:
        print(f"'{postcode}' is a valid postcode")
    else:
        print(f"'{postcode}' is NOT a valid postcode: {message}")


def main():
    parser = argparse.ArgumentParser(description="...")

    parser.add_argument('-v', "--validate", nargs='+', type=str)
    parser.add_argument('-f', "--format", nargs='+', type=str)

    args = parser.parse_args()

    if args.validate is not None:
        for postcode_arg in args.validate:
            print_postcode(postcode_arg)
    elif args.format is not None:
        for postcode_arg in args.format:
            print_format_postcode(postcode_arg)
    else:
        parser.print_help(sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
