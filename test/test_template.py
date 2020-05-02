import pytest

from project_name import do_something, failed_func


class Test_Name:
    @pytest.mark.parametrize(["value", "expected"], [["dummy test", "dummy test"]])
    def test_normal(self, value, expected):
        assert do_something(value) == expected

    @pytest.mark.parametrize(["value", "expected"], [["nop", ValueError]])
    def test_exception(self, value, expected):
        with pytest.raises(expected) as e:
            failed_func(value)

        assert "always failed" in str(e.value)
