# test_helmetsecurity.py
"""
Tests for HelmetSecurity module.
"""

import unittest
from helmetsecurity import HelmetSecurity

class TestHelmetSecurity(unittest.TestCase):
    """Test cases for HelmetSecurity class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HelmetSecurity()
        self.assertIsInstance(instance, HelmetSecurity)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HelmetSecurity()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
