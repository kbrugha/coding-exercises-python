from src.exercises.postcodes import validate_postcode, format_postcode
from tests.postcodes_data import validPostcodes, invalidPostcodes


def test_validate_postcode():

    for code in validPostcodes:
        is_valid, message = validate_postcode(code)
        message = message+code
        assert is_valid is True, message

    for code in invalidPostcodes:
        is_valid, message = validate_postcode(code)
        message = message+code
        assert is_valid is False, message


def test_format_postcode():

    formatted, message = format_postcode("ab101xg")
    assert formatted == "AB10 1XG"
    assert message == "success"

    formatted, message = format_postcode("abc")
    assert formatted is None
    assert message == "invalid postcode: Wrong length"

    formatted, message = format_postcode("coz9xg")
    assert formatted is None
    assert message == "invalid postcode: invalid character position 3"

    formatted, message = format_postcode("ab1c1xg")
    assert formatted is None
    assert message == "invalid postcode: invalid character position 4"


if __name__ == "__main__":
    pass
