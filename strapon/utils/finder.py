def find_missing_items(data):
    """
    Finds missing integers within a list
    :param data: A list of integers.
    :return: A list of missing items.

    >>> int_list = [801, 803, 804, 807, 808, 809]
    >>> find_missing_items(int_list)
    >>> [802, 805, 806]
    """
    if not isinstance(data, list):
        raise ValueError('data must be a [list, of, integer(s)]')

    if len(data) <= 1:
        return data

    # Remove duplicates and order list.
    original_set = set(data)

    # Create a super set of all items from smallest to largest
    full_set = set(range(min(original_set), max(original_set) + 1))

    # Missing items are the ones that are in the full_set, but not in
    # the original_set
    return sorted(full_set - original_set)
