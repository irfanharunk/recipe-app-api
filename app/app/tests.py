"""
sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        """ adding numbers together"""

        res = calc.add(5, 6)
        self.assertEqual(res, 11)


    def test_substract_numbers(self):
        """ substract numbers together"""

        res = calc.substract(10, 15)
        self.assertEqual(res, 5)