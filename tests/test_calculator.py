import pytest

from calculator import add, multiply, subtract


@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_total_fee(fees):
    assert sum(fees) == 297


def test_write_file(tmp_path):
    output = tmp_path / "result.txt"
    output.write_text("5", encoding="utf-8")
    assert output.read_text(encoding="utf-8") == "5"


def test_invalid_integer():
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12
