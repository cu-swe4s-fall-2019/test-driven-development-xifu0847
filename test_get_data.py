import get_data
import io
import unittest

from unittest.mock import patch


class TestGetData(unittest.TestCase):

    # test with a empty input
    @patch("sys.stdin", None)
    def test_none(self):
        self.assertRaises(ValueError, get_data.read_stdin_col, 0)

    # test with a negative col num
    @patch("sys.stdin", io.StringIO("1 2 3\n4 5 6"))
    def test_neg_col_num(self):
        self.assertRaises(ValueError, get_data.read_stdin_col, -1)

    # test with a overflow col num
    @patch("sys.stdin", io.StringIO("1 2 3\n4 5 6"))
    def test_col_num_overflow(self):
        self.assertRaises(ValueError, get_data.read_stdin_col, 100)

    # test with good test set 1
    @patch("sys.stdin", io.StringIO("1 2 3\n4 5 6"))
    def test_success_set1(self):
        result = get_data.read_stdin_col(0)
        self.assertEqual(result, [1, 4])

    # test with good test set 1
    @patch("sys.stdin", io.StringIO("1 2 3\n4 5 6"))
    def test_success_set1(self):
        result = get_data.read_stdin_col(2)
        self.assertNotEqual(result, [1, 4])
        self.assertEqual(result, [3, 6])


if __name__ == '__main__':
    unittest.main()
