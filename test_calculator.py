"""
Unit tests for calculator library
"""

import calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(4, calculator.add(2, 2))

    def test_subtraction(self):
        self.assertEqual(2, calculator.subtract(4, 2))

    def test_multiply(self):
        self.assertEqual(16, calculator.multiply(8, 2))

    def test_divide(self):
        self.assertEqual(8, calculator.divide(16, 2))
        self.assertIsNone(calculator.divide(16, 0))
