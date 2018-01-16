import pytest

from strapon.utils import list_explosion


def setup_base(data=None, delimiter=',', range_char='-'):
    return list_explosion.explode_list_items(data=data, delimiter=',', range_char='-')


def test_raise_value_error():
    with pytest.raises(ValueError):
        setup_base([])


def test_empty_string_returns_empty_list():
    data = ''
    assert setup_base(data) == ['']


def test_explode_list_items():
    data = '801,803-809'
    assert setup_base(data) == [801, 803, 804, 805, 806, 807, 808, 809]

