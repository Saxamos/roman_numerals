DECREASING_POWER_OF_10 = [1000, 100, 10, 1]
ROMAN_TO_NUMERAL = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}


def convert(number):
    assert isinstance(number, int) and 0 < number < 3000

    roman, remainder = '', number
    for power_of_10 in DECREASING_POWER_OF_10:
        remainder, roman = convert_power_of_ten_to_roman(remainder, roman, power_of_10)

    return roman


def convert_power_of_ten_to_roman(number, roman, i):
    remainder = number % i
    if remainder != number:
        if int(number / i) < 4:
            roman += ROMAN_TO_NUMERAL[i] * int(number / i)
        elif int(number / i) == 4:
            roman += ROMAN_TO_NUMERAL[i] + ROMAN_TO_NUMERAL[i * 5]
        elif int(number / i) == 5:
            roman += ROMAN_TO_NUMERAL[i * 5]
        elif 5 < int(number / i) < 9:
            roman += ROMAN_TO_NUMERAL[i * 5] + ROMAN_TO_NUMERAL[i] * (int(number / i) - 5)
        else:
            roman += ROMAN_TO_NUMERAL[i] + ROMAN_TO_NUMERAL[i * 10]
    return remainder, roman
