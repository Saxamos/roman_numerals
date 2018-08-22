DECREASING_POWER_OF_10 = [1000, 100, 10, 1]
ROMAN_TO_NUMERAL = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}


def convert(number):
    assert isinstance(number, int) and 0 < number < 3000
    return ''.join([convert_power_of_ten_to_roman(number, power_of_10) for power_of_10 in DECREASING_POWER_OF_10])


def convert_power_of_ten_to_roman(number, power_of_10):
    number %= (power_of_10 * 10)
    quotient = int(number / power_of_10)

    if quotient <= 3:
        return ROMAN_TO_NUMERAL[power_of_10] * quotient

    elif quotient == 4:
        return ROMAN_TO_NUMERAL[power_of_10] + ROMAN_TO_NUMERAL[power_of_10 * 5]

    elif quotient == 5:
        return ROMAN_TO_NUMERAL[power_of_10 * 5]

    elif 6 <= quotient <= 8:
        return ROMAN_TO_NUMERAL[power_of_10 * 5] + ROMAN_TO_NUMERAL[power_of_10] * (quotient - 5)

    return ROMAN_TO_NUMERAL[power_of_10] + ROMAN_TO_NUMERAL[power_of_10 * 10]
