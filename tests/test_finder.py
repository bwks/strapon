import pytest

from strapon.utils import finder


def setup_base(data=None):
    return finder.find_missing_items(data)


def test_raise_value_error():
    with pytest.raises(ValueError):
        setup_base('')


def test_list_of_one_item_returns_list_of_one_item():
    data = [1]
    assert setup_base(data) == [1]


def test_list_data():
    data = [801, 803, 804, 807, 808, 809]
    assert setup_base(data) == [802, 805, 806]