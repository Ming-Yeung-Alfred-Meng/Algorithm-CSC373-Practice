import math
from typing import Tuple


"""
Return the item ranked k-th in the list.
Assume list is non-empty and 1 <= k <= len(list)
"""
def quickSelect(list: list[int], k: int) -> int:

    if len(list) == 1:
        return list[0]

    else:
        sortEveryFive(list)
        medians = findMedians(list)
        medianOfMedians = quickSelect(medians, math.ceil(len(medians) / 2))
        smaller, larger = partition(list, medianOfMedians)
        
        if k <= len(smaller):
            return quickSelect(smaller, k)
        
        else:
            return quickSelect(larger, k - len(smaller))


"""
Return two lists, respectively, containing numbers in list
that are smaller (or equal to) and larger than pivot.
"""
def partition(list, pivot) -> Tuple[list[int], list[int]]:

    smaller = []
    larger = []

    for number in list:
        if number <= pivot:
            smaller.append(number)
        else:
            larger.append(number)

    return smaller, larger


"""
Return a list containing the median of every five numbers in list.
Assume list is sorted within every group of five.
Use lower median when a group has less than five numbers.
"""
def findMedians(list: list[int]) -> list[int]:

    i = 2
    medians = []

    for _ in range(len(list) // 5):
        medians.append(list[i])
        i += 5

    i -= 2
    medians.append(list[i + math.ceil(len(list[i:]) / 2) - 1])

    return medians


"""
Sort every five elements in list in non-decreasing order,
in-place and using insertion sort.
"""
def sortEveryFive(list: list[int]) -> None:
    
    for i in range(0, len(list), 5):
        insertionSortFive(list, i)


"""
Use insertion sort to sort the next five elements in list,
starting at the specified index.
"""
def insertionSortFive(list: list[int], index: int) -> None:

    i = 1
    while i < 5 and i < len(list):
        j = i

        while j > 0 and list[j] < list[j - 1]:
            larger = list[j - 1]
            list[j - 1] = list[j]
            list[j] = larger
            j -= 1

        i += 1
