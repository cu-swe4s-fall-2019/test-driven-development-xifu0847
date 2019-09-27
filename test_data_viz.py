import data_viz
import os
import random
import time
import unittest


class TestDataViz(unittest.TestCase):

    # data preparation
    def setUp(self):
        self.testdata = []
        for i in range(1000):
            self.testdata.append(random.randint(1, 10000))

    # delete test figures
    def tearDown(self):
        time.sleep(1)
        if os.path.exists('test_boxplot.png'):
            os.remove('test_boxplot.png')
        if os.path.exists('test_histogram.png'):
            os.remove('test_histogram.png')
        if os.path.exists('test_combo.png'):
            os.remove('test_combo.png')
        if os.path.exists('test_already_exists.png'):
            os.remove('test_already_exists.png')

    # test boxplot
    def test_boxplot(self):
        self.assertFalse(os.path.exists('test_boxplot.png'))
        data_viz.boxplot(self.testdata, 'test_boxplot.png')
        self.assertTrue(os.path.exists('test_boxplot.png'))

    # test histogram
    def test_histogram(self):
        self.assertFalse(os.path.exists('test_histogram.png'))
        data_viz.histogram(self.testdata, 'test_histogram.png')
        self.assertTrue(os.path.exists('test_histogram.png'))

    # test combo
    def test_combo(self):
        self.assertFalse(os.path.exists('test_combo.png'))
        data_viz.combo(self.testdata, 'test_combo.png')
        self.assertTrue(os.path.exists('test_combo.png'))

    # test already exists
    def test_already_exist(self):
        data_viz.boxplot(self.testdata, 'test_already_exists.png')
        self.assertRaises(FileExistsError, data_viz.boxplot,
                          self.testdata, 'test_already_exists.png')


if __name__ == '__main__':
    unittest.main()
