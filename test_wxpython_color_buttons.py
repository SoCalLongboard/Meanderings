import unittest
import wx
import time
from wxpython_color_buttons import ColorFrame


# OopCompanion:suppressRename

class TestColorFrame(unittest.TestCase):
    """Test cases for the ColorFrame class"""
    
    def setUp(self):
        """Set up the test environment before each test"""
        self.app = wx.App(False)
        self.frame = ColorFrame(None)
        # Don't show the frame to avoid UI popping up during tests
        # self.frame.Show()
    
    def tearDown(self):
        """Clean up after each test"""
        if self.frame:
            self.frame.Destroy()
        self.app.Destroy()
        wx.Yield()  # Process pending events
    
    def test_initial_state(self):
        """Test the initial state of the application"""
        # Check that all buttons exist
        self.assertEqual(len(self.frame.buttons), 4)
        self.assertIn("red", self.frame.buttons)
        self.assertIn("green", self.frame.buttons)
        self.assertIn("blue", self.frame.buttons)
        self.assertIn("quit", self.frame.buttons)
        
        # Check initial window properties
        self.assertEqual(self.frame.GetTitle(), "Color Buttons Example")
        self.assertEqual(self.frame.GetSize(), (300, 200))
        
        # Check that the frame is not closed
        self.assertFalse(self.frame.closed)
    
    def test_color_buttons(self):
        """Test that clicking color buttons changes the background color"""
        # Get initial color
        initial_color = self.frame.get_background_color()
        
        # Test red button
        result = self.frame.simulate_button_click("red")
        self.assertEqual(result, wx.Colour(255, 0, 0))
        self.assertEqual(self.frame.get_background_color(), wx.Colour(255, 0, 0))
        
        # Test green button
        result = self.frame.simulate_button_click("green")
        self.assertEqual(result, wx.Colour(0, 255, 0))
        self.assertEqual(self.frame.get_background_color(), wx.Colour(0, 255, 0))
        
        # Test blue button
        result = self.frame.simulate_button_click("blue")
        self.assertEqual(result, wx.Colour(0, 0, 255))
        self.assertEqual(self.frame.get_background_color(), wx.Colour(0, 0, 255))
    
    def test_quit_button(self):
        """Test that clicking the quit button closes the application"""
        self.assertFalse(self.frame.closed)
        result = self.frame.simulate_button_click("quit")
        self.assertTrue(result)
        self.assertTrue(self.frame.closed)
    
    def test_invalid_button(self):
        """Test behavior with an invalid button label"""
        result = self.frame.simulate_button_click("nonexistent")
        self.assertFalse(result)
        # Background color should not change
        self.assertNotEqual(self.frame.get_background_color(), wx.Colour(255, 0, 0))
        self.assertNotEqual(self.frame.get_background_color(), wx.Colour(0, 255, 0))
        self.assertNotEqual(self.frame.get_background_color(), wx.Colour(0, 0, 255))

if __name__ == "__main__":
    unittest.main()