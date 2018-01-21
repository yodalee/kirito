import unittest
import numpy as np

from cpa import npCalCorr

THRESHOLD = 1e-6

class TestCorrelation(unittest.TestCase):
    def isEqual(self, x, y):
        """If difference of x and y < 1e-6, judge as equal"""
        return abs(x - y) < THRESHOLD

    def testCorrelation(self):
        X = np.random.rand(10000) * 2 - 1
        Y = np.random.rand(10000) * 2 - 1
        ans = np.corrcoef(X, Y)[0][1]
        ret = npCalCorr(X, Y)
        return self.isEqual(ans, ret)

if __name__ == "__main__":
    unittest.main()
