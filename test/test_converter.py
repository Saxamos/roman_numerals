import pytest

from app.converter import convert


class TestConvert:
    def test_raise_error_if_number_not_int(self):
        # Given
        number = 1.2

        # When
        with pytest.raises(AssertionError):
            # Then
            convert(number)

    def test_raise_error_if_lower_than_1(self):
        # Given
        number = 0

        # When
        with pytest.raises(AssertionError):
            # Then
            convert(number)

    def test_raise_error_if_greater_than_2999(self):
        # Given
        number = 3000

        # When
        with pytest.raises(AssertionError):
            # Then
            convert(number)

    def test_return_associated_roman_number_when_number_with_1_given(self):
        # Given
        number_list = [1000, 1100, 1110, 1111]
        expected = ['M', 'MC', 'MCX', 'MCXI']

        # When
        result = [convert(number) for number in number_list]

        # Then
        assert result == expected

    def test_return_associated_roman_number_when_number_with_2_or_3_given(self):
        # Given
        number_list = [20, 1200, 1320, 2312]
        expected = ['XX', 'MCC', 'MCCCXX', 'MMCCCXII']

        # When
        result = [convert(number) for number in number_list]

        # Then
        assert result == expected

    def test_return_associated_roman_number_when_number_with_4_given(self):
        # Given
        number_list = [1400, 444, 1340, 2414]
        expected = ['MCD', 'CDXLIV', 'MCCCXL', 'MMCDXIV']

        # When
        result = [convert(number) for number in number_list]

        # Then
        assert result == expected

    def test_return_associated_roman_number_when_number_with_5_given(self):
        # Given
        number_list = [1500, 555, 1345, 2454]
        expected = ['MD', 'DLV', 'MCCCXLV', 'MMCDLIV']

        # When
        result = [convert(number) for number in number_list]

        # Then
        assert result == expected

    def test_return_associated_roman_number_when_number_with_6_7_or_8_given(self):
        # Given
        number_list = [1867, 678]
        expected = ['MDCCCLXVII', 'DCLXXVIII']

        # When
        result = [convert(number) for number in number_list]

        # Then
        assert result == expected

    def test_return_associated_roman_number_when_number_with_9_given(self):
        # Given
        number_list = [1999, 309, 92]
        expected = ['MCMXCIX', 'CCCIX', 'XCII']

        # When
        result = [convert(number) for number in number_list]

        # Then
        assert result == expected
