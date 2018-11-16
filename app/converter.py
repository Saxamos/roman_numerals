DECREASING_POWER_OF_10 = [1000, 100, 10, 1]
ROMAN_TO_NUMERAL = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}


def convert(number):
    assert isinstance(number, int) and 0 < number < 3000

    decreasing_remain_list = [int(number % (power_of_10 * 10) / power_of_10) for power_of_10 in DECREASING_POWER_OF_10]
    roman_array = [_convert_power_of_ten_to_roman(power_of_10, digit) for power_of_10, digit in
                   zip(DECREASING_POWER_OF_10, decreasing_remain_list)]

    return ''.join(roman_array)


def _convert_power_of_ten_to_roman(power_of_10, quotient):
    if quotient <= 3:
        roman = ROMAN_TO_NUMERAL[power_of_10] * quotient
    elif quotient == 4:
        roman = ROMAN_TO_NUMERAL[power_of_10] + ROMAN_TO_NUMERAL[power_of_10 * 5]
    elif quotient == 5:
        roman = ROMAN_TO_NUMERAL[power_of_10 * 5]
    elif 6 <= quotient <= 8:
        roman = ROMAN_TO_NUMERAL[power_of_10 * 5] + ROMAN_TO_NUMERAL[power_of_10] * (quotient - 5)
    else:
        roman = ROMAN_TO_NUMERAL[power_of_10] + ROMAN_TO_NUMERAL[power_of_10 * 10]
    return roman
