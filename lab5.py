import data
import math

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.

# Task 3: Add two Time objects
def time_add(t1: data.Time, t2: data.Time) -> data.Time:
    total_seconds = t1.second + t2.second
    total_minutes = t1.minute + t2.minute + (total_seconds // 60)
    total_hours = t1.hour + t2.hour + (total_minutes // 60)

    return data.Time(total_hours, total_minutes % 60, total_seconds % 60)

# Task 4: Check if list is in strictly descending order
def is_descending(lst: list[float]) -> bool:
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

# Task 5: Find index of largest value between two indexes
def largest_between(lst: list[int], lower: int, upper: int) -> int:
    if lower > upper or lower >= len(lst) or upper < 0:
        return None
    # Bound the range to valid indexes
    lower = max(0, lower)
    upper = min(len(lst) - 1, upper)
    # Find the index of the maximum value in the specified range
    max_index = lower
    for i in range(lower, upper + 1):
        if lst[i] > lst[max_index]:
            max_index = i

    return max_index

# Task 6: Find the point furthest from the origin
def furthest_from_origin(points: list[data.Point]) -> int:
    if not points:
        return None

    max_index = 0
    max_distance = points[0].distance_from_origin()

    for i in range(1, len(points)):
        distance = points[i].distance_from_origin()
        if distance > max_distance:
            max_distance = distance
            max_index = i

    return max_index