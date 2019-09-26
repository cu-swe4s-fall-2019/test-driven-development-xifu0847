import math_lib
import random
import statistics
import unittest


class TestMathLib(unittest.TestCase):

    # data preparation
    def setUp(self):
        self.empty_list = []
        self.int_static_list = [1, 2, 3, 4, 5, 6]
        self.float_static_list = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]

    # test if the list is empty
    def test_empty_list(self):
        self.assertRaises(ZeroDivisionError,
                          math_lib.list_mean, self.empty_list)
        self.assertRaises(ZeroDivisionError,
                          math_lib.list_stdev, self.empty_list)

    # test if the static list has all interger numbers
    def test_int_static_list(self):
        self.assertAlmostEqual(
            math_lib.list_mean(self.int_static_list),
            statistics.mean(self.int_static_list), 5)
        self.assertAlmostEqual(
            math_lib.list_stdev(self.int_static_list),
            statistics.stdev(self.int_static_list), 5)

    # test if the static list has all float numbers
    def test_float_static_list(self):
        self.assertAlmostEqual(
            math_lib.list_mean(self.float_static_list),
            statistics.mean(self.float_static_list), 5)
        self.assertAlmostEqual(
            math_lib.list_stdev(self.float_static_list),
            statistics.stdev(self.float_static_list), 5)

    # test 100 iterations of arrays with random interger numbers in the list
    def test_random_list(self):
        for i in range(100):
            testdata = []
            for j in range(20):
                testdata.append(random.randint(1, 100))
            self.assertAlmostEqual(
                math_lib.list_mean(testdata),
                statistics.mean(testdata), 5)
            self.assertAlmostEqual(
                math_lib.list_stdev(testdata),
                statistics.stdev(testdata), 5)


if __name__ == '__main__':
    unittest.main()
