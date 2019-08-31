import unittest     # Import the Python unit testing framework
from logger import Logger

class Target:
    def __init__(self, text=""):
        self.text = text
        
    def set_text(self, text=None):
        self.text = text
    
    def get_text(self):
        return self.text

class LoggerTest(unittest.TestCase):
    
    def test_info(self):
        t = Target()
        Log = Logger(t.set_text)
        
        Log.info("Some information")
        self.assertEquals(t.get_text(), "[INFO] Some information")
    
    def test_error(self):
        t = Target()
        Log = Logger(t.set_text)

        Log.error("This is a warning message")
        
        self.assertEqual(t.get_text(), "[WARNING] This is a warning message")
        
if __name__ == '__main__':
    unittest.main()
