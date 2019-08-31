import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        result = maths.add(5,5)
        self.assertEqual(result, 10, "The add function returned an incorrect value!")

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        result = maths.fibonacci(5)
        self.assertEqual(result, 5, "The fibonacci function returned an incorrect value!")
        
    def test_convert_base(self):
        '''Tests the convert base function '''
        result1 = maths.convert_base(9, 2)
        self.assertEqual(result1, '1001')
        
        result2 = maths.convert_base(11,16)
        self.assertEqual(result2, 'B')

    def test_add_and_convert_base(self):
        result = maths.add(10,3,16)
        
        self.assertEquals(result, 'D')

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
