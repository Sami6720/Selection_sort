from typing import List, Any

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    sorted_array: list[Any] = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        sorted_array.append(arr.pop(smallest_index))
    return sorted_array


print(str(selection_sort([1, 21000, 7001, 11, 44])))
