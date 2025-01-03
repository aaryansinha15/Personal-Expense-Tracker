import os
import unittest
from utils.file_operation_file import read, write  

class TestFileOperation(unittest.TestCase):

    def setUp(self):
        
        self.test_file = "test_expenses.json"  
        self.sample_data = [{'category': "Food", 'amount': 50}]  

        
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read(self):
        
        write(self.test_file, self.sample_data)  
        data = read(self.test_file)
        self.assertEqual(data, self.sample_data) 

    def test_write(self):
        
        write(self.test_file, self.sample_data)  
        self.assertTrue(os.path.exists(self.test_file))  

if __name__ == "__main__":
    unittest.main()

