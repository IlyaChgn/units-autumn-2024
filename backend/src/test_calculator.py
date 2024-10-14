import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Test addition
    def test_add_positive(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_mixed(self):
        self.assertEqual(self.calculator.addition(-1, 2), 1)

    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_add_float(self):
        self.assertEqual(self.calculator.addition(0.5, 0.5), 1)

    def test_add_none_types(self):
        with self.assertRaises(TypeError):
            self.calculator.addition(None, None)

    def test_add_mixed_types(self):
        with self.assertRaises(TypeError):
            self.calculator.addition("a", "b")
            self.calculator.addition([1, 2], {"c": 3})
            self.calculator.addition(None, "string")
            self.calculator.addition("x", 5)
            self.calculator.addition(5, "y")

    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.addition(-math.inf, 5), -math.inf)

    # Test multiplications
    def test_multiply_positive(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)

    def test_multiply_mixed(self):
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calculator.multiplication(5, 0), 0)

    def test_multiply_float(self):
        self.assertEqual(self.calculator.multiplication(0.5, 0.5), 0.25)

    def test_multiply_none_types(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication(None, None)

    def test_multiply_mixed_types(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication("a", "b")
            self.calculator.multiplication([1, 2], {"c": 3})
            self.calculator.multiplication(None, "string")
            self.calculator.multiplication("x", 5)
            self.calculator.multiplication(5, "y")

    def test_multiply_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.multiplication(-math.inf, 5), -math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -math.inf), -math.inf)

    # Test subtraction
    def test_subtract_positive(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.calculator.subtraction(-5, -3), -2)

    def test_subtract_mixed(self):
        self.assertEqual(self.calculator.subtraction(-5, 3), -8)

    def test_subtract_zero(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_subtract_float(self):
        self.assertEqual(self.calculator.subtraction(0.5, 0.25), 0.25)

    def test_subtract_fraction(self):
        self.assertAlmostEqual(self.calculator.subtraction(1/3, 0.3), 0.03333333333333333)
        self.assertAlmostEqual(self.calculator.subtraction(1/9, 1/18), 0.055555555555555)

    def test_subtract_none_types(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction(None, None)

    def test_subtract_mixed_types(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction("a", "b")
            self.calculator.subtraction([1, 2], {"c": 3})
            self.calculator.subtraction(None, "string")
            self.calculator.subtraction("x", 5)
            self.calculator.subtraction(5, "y")

    def test_subtract_inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, 5), -math.inf)
        self.assertEqual(self.calculator.subtraction(math.inf, -math.inf), math.inf)

    # Test division
    def test_divide_positive(self):
        self.assertEqual(self.calculator.division(6, 2), 3)

    def test_divide_negative(self):
        self.assertEqual(self.calculator.division(-6, -2), 3)

    def test_divide_mixed(self):
        self.assertEqual(self.calculator.division(-6, 2), -3)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calculator.division(5, 0))

    def test_zero_division(self):
        self.assertEqual(self.calculator.division(0, 5), 0)
        self.assertEqual(self.calculator.division(0, 0.5), 0)

    def test_division_float(self):
        self.assertEqual(self.calculator.division(0.5, 0.25), 2)

    def test_divide_none_types(self):
        with self.assertRaises(TypeError):
            self.calculator.division(None, None)

    def test_divide_mixed_types(self):
        with self.assertRaises(TypeError):
            self.calculator.division("a", "b")
            self.calculator.division([1, 2], {"c": 3})
            self.calculator.division(None, "string")
            self.calculator.division("x", 5)
            self.calculator.division(5, "y")

    def test_divide_inf(self):
        self.assertEqual(self.calculator.division(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.division(-math.inf, 5), -math.inf)
        self.assertAlmostEqual(self.calculator.division(5, math.inf), 0)

    # Test absolute
    def test_absolute_positive(self):
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-5), 5)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_float(self):
        self.assertEqual(self.calculator.absolute(-0.25), 0.25)

    def test_absolute_none_types(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute(None)

    def test_absolute_mixed_types(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute("a")
            self.calculator.absolute([1, 2])
            self.calculator.absolute({"c": 3})

    def test_absolute_inf(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)
        self.assertEqual(self.calculator.absolute(-math.inf), math.inf)

    # Test degree
    def test_degree_positive_base_positive_power(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_positive_base_negative_power(self):
        self.assertAlmostEqual(self.calculator.degree(2, -3), 0.125)

    def test_degree_negative_base_even_power(self):
        self.assertEqual(self.calculator.degree(-2, 2), 4)

    def test_degree_negative_base_odd_power(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_degree_zero_base_nonzero_power(self):
        self.assertEqual(self.calculator.degree(0, 5), 0)

    def test_degree_nonzero_base_zero_power(self):
        self.assertEqual(self.calculator.degree(5, 0), 1)

    def test_degree_float_base(self):
        self.assertEqual(self.calculator.degree(4, 0.5), 2)

    def test_degree_float(self):
        self.assertEqual(self.calculator.degree(0.5, 3), 0.125)

    def test_degree_none_types(self):
        with self.assertRaises(TypeError):
            self.calculator.degree(None, None)

    def test_degree_mixed_types(self):
        with self.assertRaises(TypeError):
            self.calculator.degree("a", "b")
            self.calculator.degree([1, 2], {"c": 3})
            self.calculator.degree(None, "string")
            self.calculator.degree("x", 5)
            self.calculator.degree(5, "y")

    def test_degree_inf(self):
        self.assertEqual(self.calculator.degree(math.inf, 5), math.inf)
        self.assertEqual(self.calculator.degree(-math.inf, 5), -math.inf)
        self.assertEqual(self.calculator.degree(math.inf, -5), 0)

    # Test ln
    def test_ln_positive(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)

    def test_ln_one(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    def test_ln_less_than_one(self):
        self.assertLess(self.calculator.ln(0.2), 0)

    def test_ln_float(self):
        self.assertAlmostEqual(self.calculator.ln(0.5), -0.693147181)

    def test_ln_none_types(self):
        with self.assertRaises(TypeError):
            self.calculator.ln(None)

    def test_ln_mixed_types(self):
        with self.assertRaises(TypeError):
            self.calculator.ln("a")
            self.calculator.ln([1, 2])
            self.calculator.ln({"c": 3})

    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)
        with self.assertRaises(ValueError):
            self.calculator.ln(-math.inf)

    # Test log
    def test_log_positive_base_and_number(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)

    def test_log_one_as_base(self):
        self.assertAlmostEqual(self.calculator.log(1, 10), 0)

    def test_log_float_base(self):
        self.assertAlmostEqual(self.calculator.log(0.25, 0.5), 2)

    def test_log_one_as_number(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.log(10, 1)

    def test_log_invalid_input(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0.5, 10)
            self.calculator.log(100, 0)

    def test_log_none_types(self):
        with self.assertRaises(TypeError):
            self.calculator.log(None, None)

    def test_log_mixed_types(self):
        with self.assertRaises(TypeError):
            self.calculator.log("a", "b")
            self.calculator.log([1, 2], {"c": 3})
            self.calculator.log(None, "string")
            self.calculator.log("x", 5)
            self.calculator.log(5, "y")

    def test_log_inf(self):
        self.assertEqual(self.calculator.log(math.inf, math.e), math.inf)
        self.assertEqual(self.calculator.log(100, math.inf), 0)

    # Test sqrt
    def test_sqrt_positive(self):
        self.assertAlmostEqual(self.calculator.sqrt(16), 4)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_float(self):
        self.assertEqual(self.calculator.sqrt(0.25), 0.5)

    def test_sqrt_negative(self):
        result = self.calculator.sqrt(-1)
        self.assertIsInstance(result, complex)
        self.assertAlmostEqual(result.real, 0)
        self.assertAlmostEqual(result.imag, 1)

    def test_sqrt_none_types(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt(None)

    def test_sqrt_mixed_types(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt("a")
            self.calculator.sqrt([1, 2])
            self.calculator.sqrt({"c": 3})

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertEqual(self.calculator.sqrt(-math.inf), math.inf)
