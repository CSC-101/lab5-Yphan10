import math
from typing import Any

# Representation of time as hours, minutes, and seconds
class Time:
    # Initialize a new Time object.
    # input: hour as an int
    # input: minute as an int
    # input: second as an int
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    # Provide a developer-friendly string representation of the object.
    # output: string representation
    def __repr__(self) -> str:
        return f'Time({self.hour:02d}, {self.minute:02d}, {self.second:02d})'

    # Compare the Time object with another value to determine equality.
    # input: another Time object or any other value
    # output: boolean indicating equality
    def __eq__(self, other: Any) -> bool:
        return (other is self or
                isinstance(other, Time) and
                self.hour == other.hour and
                self.minute == other.minute and
                self.second == other.second)

# Representation of a two-dimensional point.
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    # Provide a developer-friendly string representation of the object.
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)

    # Compare the Point object with another value to determine equality.
    # output: boolean indicating equality
    def __eq__(self, other: Any) -> bool:
        return (other is self or
                isinstance(other, Point) and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))
