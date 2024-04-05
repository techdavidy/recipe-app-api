"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_add_2(self):
        """Test adding numbers together."""
        res = calc.add(1, 1)
        self.assertEqual(res, 2)
