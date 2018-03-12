"""
Validation Exercises

These functions return ``True`` or ``False`` depending on whether the
string passes a condition.

"""
import re


def has_vowel(string):
    """Return True iff the string contains one or more vowels."""

    val=bool(re.search(r'[aeiou]', string))
    return val


def is_integer(string):
    """Return True iff the string represents a valid integer."""

    val = bool(re.search(r'^-?\d+$', string))
    return val

def is_fraction(string):
    """Return True iff the string represents a valid fraction."""

    val = bool(re.search(r'^-?\d+\/[1-9](\d+)?$', string))
    return val


def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""

    val = bool(re.search(r'^\d{4}\-(0\d|1[0-2])\-(0\d|[12]\d|3[01])$', string))
    return val


def is_number(string):
    """Return True iff the string represents a decimal number."""

    val = bool(re.search(r'^-?[\d]+\.?[\d]+$', string))
    return val

def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""

    val = bool(re.search(r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', string))
    return val
