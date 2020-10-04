def find_total_amount(dict):
    total_amount = 0
    for val in dict.values():
        amount = int(val[:-1])
        total_amount += amount
    return f"Total money we have is {total_amount}"


def find_most_reach(dict):
    person, amount = '', 0
    for key, val in dict.items():
        if int(val[:-1]) > amount:
            person, amount = key, int(val[:-1])
    return f"{person} is the most reach person. He has {amount}"


def key_val_replacement(dict):
    for key, val in dict.items():
        dict[val] = key
        elem = dict.pop(key)
    return dict
