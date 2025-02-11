import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_non_integer(self):
        with self.assertRaises(ValueError):
            factorial(3.5)

if __name__ == '__main__':
    unittest.main()
