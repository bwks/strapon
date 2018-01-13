from itertools import groupby
from operator import itemgetter


def compress_int_list(data, prefix=''):
    """
    Compress a list of integers and apply an optional prefix
    :param data: A list of integers.
    :param prefix: Apply an optional prefix to list elements.
    :return: A list of compressed strings.

    >>> data = [1, 4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
    >>> compress_int_list(data, 'swp')
    >>> ['swp1', 'swp4-6', 'swp10', 'swp15-18', 'swp22', 'swp25-28']
    """
    if not isinstance(data, list):
        raise ValueError('data must be a [list, of, integer(s)]')
    if len(data) == 1:
        return '{}{}'.format(prefix, data[0])

    compressed_list = []
    for key, value in groupby(enumerate(set(data)), lambda i: i[0] - i[1]):
        group = ([i for i in map(itemgetter(1), value)])
        if len(group) > 1:
            compressed_list.append('{}{}-{}'.format(prefix, group[0], group[-1]))
        else:
            compressed_list.append('{}{}'.format(prefix, data[0]))

    return compressed_list
