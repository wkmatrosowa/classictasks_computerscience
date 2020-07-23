import unittest

from task1 import fibonacci

class FibonacciTest(unittest.TestCase):

    def test_1(self):
        result = fibonacci(1)
        self.assertEqual(result, 1)

    def test_2(self):
        result = fibonacci(0)
        self.assertEqual(result, 0)

    def test_3(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)

    def test_4(self):
        result = fibonacci(60)
        self.assertEqual(result, 1548008755920)

if __name__ == '__main__':
    unittest.main()
