import unittest
from src.main import solution
import pytest


class TestMain(unittest.TestCase):
    def test_solution(self):
        self.assertTrue(solution(''))
        self.assertFalse(solution('(()'))
        self.assertTrue(solution(')(()'))
