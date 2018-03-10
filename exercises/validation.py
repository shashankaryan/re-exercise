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
    
    val = bool(re.search(r'^-?\d*$', string))
    return val

def is_fraction(string):
    """Return True iff the string represents a valid fraction."""


def is_valid_date(string):
    """Return True iff the string represents a valid YYYY-MM-DD date."""


def is_number(string):
    """Return True iff the string represents a decimal number."""


def is_hex_color(string):
    """Return True iff the string represents an RGB hex color code."""
