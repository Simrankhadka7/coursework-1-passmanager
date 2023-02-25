import unittest
from unittest.mock import patch
import passwordmanager.py
from password_manager import passCreator, getPass, writeInFile, structureData, storeData

class TestPasswordManager(unittest.TestCase):
    
    def test_passCreator_createPass(self):
        # Test passCreator.createPass() returns a string of the expected length
        length = 8
        pc = passCreator(length)
        password = pc.createPass()
        self.assertIsInstance(password, str)
        self.assertEqual(len(password), length)
    
    def test_getPass(self):
        # Test getPass(length) returns a string of the expected length
        length = 12
        password = getPass(length)
        self.assertIsInstance(password, str)
        self.assertEqual(len(password), length)
    
    def test_writeInFile(self):
        # Test writeInFile(content) writes the expected content to the file
        content = "test content"
        with patch("builtins.open", create=True) as mock_file:
            mock_file.return_value.write.return_value = None
            writeInFile(content)
            mock_file.assert_called_once_with("passDb.txt", "a")
            mock_file.return_value.write.assert_called_once_with(content + "\n")
    
    def test_structureData(self):
        # Test structureData(email, website, password) returns a string in the expected format
        email = "test@example.com"
        website = "www.example.com"
        password = "testpassword"
        expected = "test@example.com: www.example.com:1@*t"
        result = structureData(email, website, password)
        self.assertEqual(result, expected)
    
    def test_storeData(self):
        # Test storeData() returns True when both email and website fields are non-empty, False otherwise
        email.set("test@example.com")
        website.set("www.example.com")
        password[0] = "testpassword"
        result = storeData()
        self.assertTrue(result)
        email.set("")
        website.set("www.example.com")
        result = storeData()
        self.assertFalse(result)
