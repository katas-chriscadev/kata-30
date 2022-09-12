import re
import string
import sys

__phone_words_numbers_map__ = {
    "0": " ",
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def words_to_number(words: str):
    numbers = ""
    for letter in words:
        for number, letters in __phone_words_numbers_map__.items():
            if number == letter or letter.lower() in letters:
                numbers += number
    return numbers


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


def array_phone_formatter(arr):
    if not isinstance(arr, list):
        raise ValueError('array_phone_formatter must be a list')
    letters = [str(x) for x in arr]
    return string_phone_formatter(''.join(letters))


if __name__ == '__main__':
    print(string_phone_formatter(''.join(sys.argv[1:])))
