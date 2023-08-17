#!/bin/python3
"""
Unittest for Rectangle.py
By: Enock dev
"""
import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    class for testing base rectangle.py
    """
    def test_pep8(self):
        """
        testing format of rectangle.py
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
