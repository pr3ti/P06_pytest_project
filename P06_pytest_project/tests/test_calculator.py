from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 20
        b = 30
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 600
        assert result == expected

    def test_divide(self):
        # arrange
        a = 100
        b = 25
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4
        assert result == expected

    def test_divide_by_zero(self):
        # arrange
        a = 100
        b = 0
        cal = Calculator()

        # act & assert
        try:
            cal.divide(a, b)
        except ZeroDivisionError as e:
            assert str(e) == "Division by zero error"
