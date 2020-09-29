def find_index_in_list(list_of_num, target):
    for index_1, value_1 in enumerate(list_of_num):
        for index_2, value_2 in enumerate(list_of_num):
            if index_1 == index_2:
                continue
            sum = value_1 + value_2
            if sum == target:
                return [index_1, index_2]

if __name__ == "__main__":
    input_list = input("Give a list of numbers to find max XOR: ")
    target = int(input("Target amount: "))

    if input_list and target:
        input_list = list(map(int, input_list[1:-1].split(',')))
    else:
        raise ValueError("Please enter the values correctly.")

    result = find_index_in_list(input_list, target)
    print(f"Indices of numbers giving the target amount: {result}")
