from typing import Tuple
import math

"""
Append to list numbers in remainders starting at index.
"""
def appendRemainders(list: list[int], remainders: list[int], index: int) -> None:

    while index < len(remainders):
        list.append(remainders[index])
        index += 1


"""
Return a sorted list of either x- or y-coordinates of points. 
Sort x-coordinates if "coordinate" is 0, y-cooridnates if it is 1.
"""
def mergeSort(points: set[(int, int)], start: int, end: int, coordinate: int) -> list[int]:

    if start == end:
        return [points[start][coordinate]]

    else:
        leftList = mergeSort(points, start, (end + start - 1) // 2, coordinate)
        rightList = mergeSort(points, (start + end + 1) // 2, end, coordinate)

        sortedList = []
        leftIndex = 0
        rightIndex = 0

        while leftIndex < len(leftList) and rightIndex < len(rightList):
            if leftList[leftIndex] <= rightList[rightIndex]:
                sortedList.append(leftList[leftIndex])
                leftIndex += 1
            
            else:
                sortedList.append(rightList[rightIndex])
                rightIndex += 1

        appendRemainders(sortedList, leftList, leftIndex)
        appendRemainders(sortedList, rightList, rightIndex)

        return sortedList


"""
Given a set of (2D) points, return the closest pair.
"""
def closestPair(points: list[(int, int)]) -> Tuple[int, int]:

    X = mergeSort(points, 0, len(points) - 1, 0)
    Y = mergeSort(points, 0, len(points) - 1, 1)

    return closestPairHelper(points, X, Y)


"""
"""
def closestPairHelper(points: list[(int, int)], X: list[int], Y: list[int]) -> Tuple[int, int]:

    if len(points) <= 3:
        return bruteForce(points)

    else:
        leftPoints, rightPoints, leftX, leftY, rightX, rightY, x_median = divide(points, X, Y)
        leftPair = closestPairHelper(leftPoints, leftX, leftY)
        rightPair = closestPairHelper(rightPoints, rightX, rightY)
        crossPair = findCrossPair()

        if 


def divide(points: list[(int, int)], X: list[int], Y: list[int]) -> Tuple(list[(int, int)], list[(int, int)], list[int], list[int], list[int], list[int], int):

    x_median = X[( len(X) // 2 ) - 1]

    for point in points:
        if 

"""
Return the distance between x and y.
"""
def distance(x: Tuple[int, int], y: Tuple[int, int]) -> float:

    return math.sqrt((x[0] - y[0]) ^ 2 + (x[1] - y[1]) ^ 2)


"""
Return the pair of points that have minimum distance,
across all pairs, by comparing every pair.
"""
def bruteForce(points: list[(int, int)]) -> Tuple[int, int]:
    x = points[0]
    y = points[1]

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if distance(points[i], points[j]) < distance(x, y):
                x = points[i]
                y = points[j]

    return (x, y)





