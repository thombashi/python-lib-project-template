import pytest


def dummy_func(value: str) -> str:
    return value


def failed_func(value: str) -> None:
    raise ValueError("always failed")


class Test_Name:
    @pytest.mark.parametrize(["value", "expected"], [["dummy test", "dummy test"],])
    def test_normal(self, value, expected):
        assert dummy_func(value) == expected

    @pytest.mark.parametrize(["value", "expected"], [["nop", ValueError],])
    def test_exception(self, value, expected):
        with pytest.raises(expected):
            failed_func(value)
