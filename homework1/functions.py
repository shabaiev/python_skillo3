l1 = [22, "Word", True, 345.2, "V"]


def transform_to_string(list1):
    """Initiating new string. After that iterating through the all elements in the list l1
    Then converting every element to the String data type and adding it to the the new_str variable.
    Finally,returning new_str"""
    new_str = " "

    for element in list1:
        new_str += str(element)
    return new_str


print(transform_to_string.__doc__)
print(transform_to_string(l1))
print(type(transform_to_string(l1)))

l2 = [3, 5, 5, 4, 22, 4, 5, 9]


def get_unique_elements(list2):
    """Creating new list. Iterating through every element and
    if current element (e) is not in the list adding it there."""
    new_list = []

    for e in list2:
        if e not in new_list:
            new_list.append(e)
    return new_list


print(get_unique_elements.__doc__)
print(get_unique_elements(l2))
print(type(get_unique_elements(l2)))

l3 = ([55, 2, 4, "v", 5, True])


def break_list_by_value(list3):
    """Creating 2 empty lists. Adding first half of list to  temp_list,
    then adding all parameters from temp_list to main_list and deleting everything from
    temp_list(lemp_list.clear()). Adding the second part of the list (after "v" separator) to temp_list again.
    If temp_list has value in it
    adding temp_list to main list and returning both list in a tuple."""
    value = "v"
    main_list = []
    temp_list = []
    for e in list3:
        if e is value:
            main_list.append(temp_list[:])
            temp_list.clear()
        else:
            temp_list.append(e)
    if len(temp_list) > 0:
        main_list.append(temp_list)
    return tuple(main_list)


print(break_list_by_value.__doc__)
print(break_list_by_value(l3))
print(type(break_list_by_value(l3)))
