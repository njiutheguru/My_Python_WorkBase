import math
import unittest


def square_root(num):
    return math.sqrt(num)

class Testclass(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(square_root(121),11, " The result should be 11")

    def test_case2(self):
        self.assertEqual(square_root(144),12, " The result should be 12")

    def test_case3(self):
        self.assertEqual(square_root(169),13, " The result should be 13")

    def test_case4(self):
        self.assertEqual(square_root(196),14, " The result should be 14")

    def test_case5(self):
        self.assertEqual(square_root(225),16, " The result should be 15")

if __name__=='__main__':
    unittest.main()
    