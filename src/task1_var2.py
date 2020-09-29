def find_max_xor(list_of_num):
    max_xor = 0
    list_of_num.sort()

    elem_1 = list_of_num[-1]

    for i in list_of_num[::-1]:
        xor = elem_1 ^ i
        if xor > max_xor:
            max_xor = xor
    return max_xor

if __name__ == "__main__":
    input_list = input("Give a list of numbers to find max XOR: ")

    if input_list:
        input_list = list(map(int, input_list[1:-1].split(', ')))
    else:
        raise ValueError("You must enter a list with numbers. Ex: [3, 10, 5]")

    result = find_max_xor(input_list)
    print(f"The maximum xor for two integers from this list is {result}")
