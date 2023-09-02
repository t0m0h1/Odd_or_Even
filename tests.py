import unittest
from main import odd_even

class TestMainFunctions(unittest.TestCase):
    
    def test_even_number(self):
        result = odd_even(4)
        self.assertEqual(result, "Even")

    def test_odd_number(self):
        result = odd_even(7)
        self.assertEqual(result, "Odd")

    # Add more test methods as needed...

if __name__ == "__main__":
    unittest.main()
