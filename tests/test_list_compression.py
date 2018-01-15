import pytest

from strapon.utils import list_compression


def setup_base(data=None, prefix=''):
    return list_compression.compress_list_items(data, prefix)


def test_compress_list_items_with_prefix():
    data = [1, 4, 5, 6, 10, 15, 16, 17, 18, 22, 25, 26, 27, 28]
    assert setup_base(data, 'swp') == ['swp1', 'swp4-6', 'swp10', 'swp15-18', 'swp22', 'swp25-28']


def test_compress_list_items_without_prefix():
    data = [1, 4, 5, 6, 10, 15, 16, 17, 18, 22, 25, 26, 27, 28]
    assert setup_base(data) == ['1', '4-6', '10', '15-18', '22', '25-28']


def test_list_with_one_element():
    data = [1]
    assert setup_base(data) == ['1']


def test_empty_list_returns_empty_list():
    data = []
    assert setup_base(data) == []


def test_raise_value_error():
    with pytest.raises(ValueError):
        setup_base('', 'swp')
