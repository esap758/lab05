import maths
import unittest
 
class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        num = 10
        factor = maths.factorial(num)
        
        self.assertEqual(factor, 3628800)
        
        
if __name__ == '__main__':
    unittest.main()