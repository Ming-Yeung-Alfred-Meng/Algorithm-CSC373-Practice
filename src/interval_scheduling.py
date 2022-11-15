from typing import Tuple

"""
Return a maximum subset of intervals.
"""
def find_schedule(intervals: list[(int, int)]) -> list[(int, int)]:
    schedule = []
    latest_finish_time = 0
    sorted_intervals = sort_by_earliest_finish_time(intervals, 0, len(intervals) - 1)

    for i in range(len(intervals)):
        if sorted_intervals[i][0] >= latest_finish_time:
            schedule.append(sorted_intervals[i])
            latest_finish_time = sorted_intervals[i][1]

    return schedule


"""
Return a copy of intervals sorted by earliest finish time.
"""
def sort_by_earliest_finish_time(intervals: list[(int, int)], start: int, end: int) -> list[(int, int)]:
    if start == end:
        return [intervals[start]]

    else:
        left_list = sort_by_earliest_finish_time(intervals, start, (end + start - 1) // 2)
        right_list = sort_by_earliest_finish_time(intervals, (start + end + 1) // 2, end)

        sortedList = []
        leftIndex = 0
        rightIndex = 0

        while leftIndex < len(left_list) and rightIndex < len(right_list):
            if left_list[leftIndex][1] <= right_list[rightIndex][1]:
                sortedList.append(left_list[leftIndex])
                leftIndex += 1

            else:
                sortedList.append(right_list[rightIndex])
                rightIndex += 1

        appendRemainders(sortedList, left_list, leftIndex)
        appendRemainders(sortedList, right_list, rightIndex)

        return sortedList


"""
Append to list numbers in remainders starting at index.
"""
def appendRemainders(list: list[int], remainders: list[int], index: int) -> None:

    while index < len(remainders):
        list.append(remainders[index])
        index += 1
