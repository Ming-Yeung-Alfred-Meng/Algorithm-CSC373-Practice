from typing import Tuple

"""
Given an array A, count the number of pairs such that i < j, but A[i] > A[j].
"""
def countInversions(list: list[int], start: int, end: int) -> Tuple[int, list[int]]:
    
    if start == end:
        return (0, list[start:start + 1])

    else:
        leftCount, leftList = countInversions(list, start, (end + start - 1) // 2)
        rightCount, rightList = countInversions(list, (end + start + 1) // 2, end)
        crossCount, sortedList = mergeAndCount(leftList, rightList)
        
        return(leftCount + rightCount + crossCount, sortedList)


"""
Return the number of inversions that have one number from listList and one number from rightList.
Also return a sorted list of numbers from leftList and rightList (non-decreasing).
Assume leftList and rightList are sorted in non-decreasing order.
"""
def mergeAndCount(leftList: list[int], rightList: list[int]) -> Tuple[int, list[int]]:

    count = 0
    sortedList = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(leftList) and rightIndex < len(rightList):

        if leftList[leftIndex] > rightList[rightIndex]:
            count += len(leftList) - leftIndex
            sortedList.append(rightList[rightIndex])
            rightIndex += 1

        else:
            sortedList.append(leftList[leftIndex])
            leftIndex += 1

    appendRemainders(sortedList, leftList, leftIndex)
    appendRemainders(sortedList, rightList, rightIndex)

    return count, sortedList


"""
Append to sortedList the numbers in remainders starting at index.
"""
def appendRemainders(sortedList: list[int], remainders: list[int], index: int):

    while index < len(remainders):
        sortedList.append(remainders[index])
        index += 1