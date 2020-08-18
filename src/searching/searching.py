def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:
        middle = (first + last) // 2
        guess = arr[middle]

        if guess == target:
            return middle
        if guess > target:
            last = middle - 1
        else:
            first = middle + 1

    return -1  # not found
