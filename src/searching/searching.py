def linear_search(arr, target):

    for index, item in enumerate(arr, 0):
        if item == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    min = 0
    max = len(arr) - 1

    while min <= max:
        middle = max + min // 2
        if arr[middle] == target:
            return middle

        if target > middle:
            min = middle + 1
        else:
            max = middle - 1

    return -1  # not found
