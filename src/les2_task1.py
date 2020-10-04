def find_max_xor(tuple_of_num):
    result_tuple = tuple()
    for index, num in enumerate(tuple_of_num):
        if index % 2 == 0:
            result_tuple = result_tuple + ((num * 2),)
        elif index % 2 == 1:
            result_tuple = result_tuple + ((num - 2),)
    if not tuple_of_num:
        return "Tuple is empty"
    return result_tuple
