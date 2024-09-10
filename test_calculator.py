import unittest
import calculator

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculator.sum(3,5), 8)

    # This test is designed to fail for demonstration purposes.
    def test_sub(self):
        self.assertEqual(calculator.sub(5,3),2 )

if __name__ == '__main__':
    unittest.main()