def find_index_in_list(list_of_num, target):
    """
    Find a pair of elements (indices of the two numbers) from a given 
    list_of_num whose sum equals the target number
    """
    dict_of_nums = {}

    for i, num in enumerate(list_of_num):
        if (target - num) in dict_of_nums:
            return [dict_of_nums[target - num], i]
        dict_of_nums[num] = i
    else:
            raise ValueError("Can't find any matches to get target in sum")


if __name__ == "__main__":
    input_list = input("Give a list of numbers to find max XOR: ")
    target = int(input("Target amount: "))

    if input_list and target:
        input_list = list(map(int, input_list[1:-1].split(',')))
    else:
        raise ValueError("Please enter the values correctly.")

    result = find_index_in_list(input_list, target)
    print(f"Indices of numbers giving the target amount: {result}")
