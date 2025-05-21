import unittest
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QColor
from pyqt6_color_buttons import ColorFrame


# OopCompanion:suppressRename

class TestColorFrame(unittest.TestCase):
    """Test cases for the ColorFrame class"""

    def setUp(self):
        """Set up the test environment before each test"""
        self.app = QApplication(sys.argv)
        self.frame = ColorFrame()
        # Don't show the frame to avoid UI popping up during tests
        self.frame.hide()

    def tearDown(self):
        """Clean up after each test"""
        if self.frame:
            self.frame.close()
        self.app.quit()

    def test_initial_state(self):
        """Test the initial state of the application"""
        # Check that all buttons exist
        self.assertEqual(len(self.frame.buttons), 4)
        self.assertIn("red", self.frame.buttons)
        self.assertIn("green", self.frame.buttons)
        self.assertIn("blue", self.frame.buttons)
        self.assertIn("quit", self.frame.buttons)

        # Check initial window properties
        self.assertEqual(self.frame.windowTitle(), "Color Buttons Example")
        self.assertEqual(self.frame.width(), 300)
        self.assertEqual(self.frame.height(), 200)

        # Check that the frame is not closed
        self.assertFalse(self.frame.closed)

    def test_color_buttons(self):
        """Test that clicking color buttons changes the background color"""
        # Get initial color
        initial_color = self.frame.get_background_color()

        # Test red button
        result = self.frame.simulate_button_click("red")
        self.assertEqual(result, QColor(255, 0, 0))
        self.assertEqual(self.frame.get_background_color(), QColor(255, 0, 0))

        # Test green button
        result = self.frame.simulate_button_click("green")
        self.assertEqual(result, QColor(0, 255, 0))
        self.assertEqual(self.frame.get_background_color(), QColor(0, 255, 0))

        # Test blue button
        result = self.frame.simulate_button_click("blue")
        self.assertEqual(result, QColor(0, 0, 255))
        self.assertEqual(self.frame.get_background_color(), QColor(0, 0, 255))

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
        # Background color should not change to any of the defined colors
        bg_color = self.frame.get_background_color()
        self.assertNotEqual(bg_color, QColor(255, 0, 0))
        self.assertNotEqual(bg_color, QColor(0, 255, 0))
        self.assertNotEqual(bg_color, QColor(0, 0, 255))


if __name__ == "__main__":
    unittest.main()
