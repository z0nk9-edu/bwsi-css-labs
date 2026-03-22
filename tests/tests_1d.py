"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1c.py.
"""
import pytest
from labs.lab_1.lab_1d import two_sum
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]          # Test case from the problem statement
    assert two_sum([3, 2, 4], 6) == [1, 2]               # Test for different target
    assert two_sum([3, 3], 6) == [0, 1]                  # Test for duplicate numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4] # Test for negative numbers
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]          # Test for zeros
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]               # Test for larger target
if __name__ == "__main__":
    pytest.main()