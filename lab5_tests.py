import data
import lab5
import unittest


# Write your test cases for each part below.

class TestLab5Functions(unittest.TestCase):
    # Test for time_add
    def test_time_add(self):
        t1 = data.Time(1, 59, 30)
        t2 = data.Time(2, 30, 45)
        result = lab5.time_add(t1, t2)
        self.assertEqual(result, data.Time(4, 30, 15))

    # Test for is_descending
    def test_is_descending(self):
        self.assertTrue(lab5.is_descending([5.0, 4.0, 3.0, 2.0]))
        self.assertFalse(lab5.is_descending([5.0, 3.0, 4.0, 2.0]))

    # Test for largest_between
    def test_largest_between(self):
        self.assertEqual(lab5.largest_between([1, 3, 7, 2, 5], 1, 3), 2)
        self.assertIsNone(lab5.largest_between([1, 3, 7], 3, 1))
        self.assertEqual(lab5.largest_between([10, 20, 5, 7], 1, 10), 1)

    # Test for furthest_from_origin
    def test_furthest_from_origin(self):
        points = [data.Point(1, 2), data.Point(3, 4), data.Point(0, 0)]
        self.assertEqual(lab5.furthest_from_origin(points), 1)
        self.assertIsNone(lab5.furthest_from_origin([]))
if __name__ == '__main__':
    unittest.main()