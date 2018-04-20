# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import print_function, unicode_literals

import pytest


def dummy_func(value):
    return value


class Test_Name(object):

    @pytest.mark.parametrize(["value", "expected"], [
        ["this test always fails", ""],
    ])
    def test_normal(self, value, expected):
        assert dummy_func(value) == expected

    @pytest.mark.parametrize(["value", "expected"], [
        [None, ValueError],
    ])
    def test_exception(self, value, expected):
        with pytest.raises(expected):
            dummy_func(value)
