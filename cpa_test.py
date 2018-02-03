import unittest
import numpy as np

from utils import Utils

THRESHOLD = 1e-6

class TestCorrelation(unittest.TestCase):
    def setUp(self):
        self.utils = Utils()

    def testCorrelation(self):
        X = np.random.rand(1000) * 2 - 1
        Y = np.random.rand(1000) * 2 - 1
        ans = np.corrcoef(X, Y)[0][1]
        ret = self.utils.cuCalCorr(X, Y)
        self.assertAlmostEqual(ans, ret)

    def testHandmade(self):
        X = np.random.rand(10) * 2 - 1
        Y = np.random.rand(10) * 2 - 1
        ans = np.corrcoef(X, Y)[0][1]
        ret = self.utils.handCalCorr(X, Y)
        self.assertAlmostEqual(ans, ret)

if __name__ == "__main__":
    unittest.main()
