def find_repeated_element_var1(list_of_nums):
    elem_amount = len(list_of_nums)
    for i in range(elem_amount):
        for j in range(i+1, elem_amount):
            if list_of_nums[i] == list_of_nums[j]:
                return list_of_nums[i]
    else:
        return "No repetitions in the list"


def find_repeated_element_var2(list_of_nums):
    unique_list_of_nums = []
    for elem in list_of_nums:
        if elem in unique_list_of_nums:
            return elem
        else:
            unique_list_of_nums.append(elem)
    else:
        return "No repetitions in the list"


def find_repeated_element_var3(list_of_nums):
    unique_list_of_nums = [set(list_of_nums)]
    difference = list_of_nums - unique_list_of_nums
    if difference:
        return difference
    else:
        return "No repetitions in the list"


def find_repeated_element_var4(list_of_nums):
    elem_amount = len(list_of_nums)
    for i in range(elem_amount):
        elem = list_of_nums.pop(i)
        if elem in list_of_nums:
            return elem
    else:
        return "No repetitions in the list"
