# test_esbuildbundle.py
"""
Tests for EsbuildBundle module.
"""

import unittest
from esbuildbundle import EsbuildBundle

class TestEsbuildBundle(unittest.TestCase):
    """Test cases for EsbuildBundle class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EsbuildBundle()
        self.assertIsInstance(instance, EsbuildBundle)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EsbuildBundle()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
