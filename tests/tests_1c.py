"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""
import pytest
from labs.lab_1.lab_1c import max_subarray_sum
def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6  # Test case from the problem statement
    assert max_subarray_sum([1]) == 1                        # Test for single element
    assert max_subarray_sum([-1]) == -1                      # Test for single negative element
    assert max_subarray_sum([-2,-3,-1]) == -1               # Test for all negative numbers
    assert max_subarray_sum([5,4,-1,7,8]) == 23             # Test for all positive numbers
    assert max_subarray_sum([0,0,0]) == 0                    # Test for all zeros
    assert max_subarray_sum([-2,-3,4,-1,-2,1,5,-3]) == 7   # Test for mixed numbers
if __name__ == "__main__":
    pytest.main()