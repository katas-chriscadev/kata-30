from phones import string_phone_formatter, array_phone_formatter


def test_string_to_phone():
    assert string_phone_formatter("123LLAMEYA") == "(123) 552-6392"


def test_array_to_phone():
    array_phone = [1, 2, 3, "L", "L", "A", "M", "E", "Y", "A"]
    assert array_phone_formatter(array_phone) == "(123) 552-6392"
