def explode_list_items(data, delimiter=',', range_char='-'):
    """
    Takes a string and expands it to a list
    Adapted from code by greg.mueller @ network.toCode slack channel
    :param data: String of data EG: 801,803-809
    :param delimiter: String used as the delimiting character.
    :param range_char: String used as the range identifier.
    :return: List of integers

    >>> input_vlans = '801,803-809'
    >>> explode_list_items(input_vlans)
    >>> [801, 803, 804, 805, 806, 807, 808, 809]
    """
    if not isinstance(data, str):
        raise ValueError('data must be a string')

    if not data:
        return [data]

    items = []
    for item in data.split(delimiter):
        if item.isdigit():
            items.append(int(item))
        elif range_char in item:
            start, end = [int(i) for i in item.split(range_char)]
            items += [i for i in (range(start, end + 1))]
    return items
