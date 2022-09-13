import sys

__phone_words_numbers_map__ = {
    " ": "0",
    "a": "2",
    "b": "2",
    "c": "2",
    "d": "3",
    "e": "3",
    "f": "3",
    "g": "4",
    "h": "4",
    "i": "4",
    "j": "5",
    "k": "5",
    "l": "5",
    "m": "6",
    "n": "6",
    "o": "6",
    "p": "7",
    "q": "7",
    "r": "7",
    "s": "7",
    "t": "8",
    "u": "8",
    "v": "8",
    "w": "9",
    "x": "9",
    "y": "9",
    "z": "9",
}


def array_elements_to_string(array: list):
    return [str(x) for x in array]


def words_to_number(words: str):
    numbers = []
    for letter in words.lower():
        number = __phone_words_numbers_map__.get(letter, None)
        if number is not None:
            numbers.append(number)
        else:
            numbers.append(letter)
    return ''.join(numbers)


def phone_format(raw_phone: str):
    return '({}) {}-{}'.format(raw_phone[:3], raw_phone[3:6], raw_phone[6:])


def string_phone_formatter(value):
    """
    Formats a phone number as a string.
    """

    if len(value) < 10:
        raise ValueError('Invalid phone number')

    phone = words_to_number(value)
    return phone_format(phone)


def array_phone_formatter(array: list):
    if not isinstance(array, list):
        raise ValueError('array_phone_formatter must be a list')
    letters = array_elements_to_string(array)
    return string_phone_formatter(''.join(letters))


if __name__ == '__main__':
    try:
        phone = string_phone_formatter(''.join(sys.argv[1:]))
        print(phone)
    except ValueError as e:
        print(e)
