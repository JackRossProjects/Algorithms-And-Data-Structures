# Write code to convert integers from 1-1000 to Roman Numerals
"""
I = 1
IV = 4
V = 5
IX = 9
X = 10
XI = 11
L = 50
C = 100
D = 500
M = 1000
"""





import sys

ROMAN_NUMERAL_TABLE = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100),  ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),
    ("IX", 9),   ("V", 5),    ("IV", 4),
    ("I", 1)
]

'''
def convert_to_roman(number):
    """ Convert an integer to Roman
    >>> print(convert_to_roman(45))
    XLV """
    roman_numerals = []
    for numeral, value in ROMAN_NUMERAL_TABLE:
        count = number // value
        number -= count * value
        roman_numerals.append(numeral * count)

    print(''.join(roman_numerals))
'''

# OR

def convert_to_roman(number):
    roman_numerals = []
    for numeral, value in ROMAN_NUMERAL_TABLE:
        while value <= number:
            number -= value
            roman_numerals.append(numeral)

    print(''.join(roman_numerals))

convert_to_roman(int(input("Enter an integer from 1 to 1000: ")))
