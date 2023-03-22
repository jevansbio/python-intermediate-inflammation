"""Tests for view functions within the views layer."""

import numpy as np
import pytest


@pytest.mark.parametrize(
    "test, expected",
    [
        ({'average': np.array([0, 1, 3])},
         "0. average: [0 1 3]")
    ])
def test_textoutput(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.views import textoutput
    output = textoutput(test)
    assert output == expected
