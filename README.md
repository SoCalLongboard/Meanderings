# wxPython Color Buttons Application

A simple wxPython application that displays a window with four buttons in a 2x2 grid layout. The buttons are labeled "red", "green", "blue", and "quit". Clicking on a color button changes the background color of the window to that color, and clicking the "quit" button closes the application. The application logs all button clicks to stdout, providing information about user interactions.

## Running the Application

To run the application, execute:

```bash
python wxpython_color_buttons.py
```

## Testing

The application includes automated tests to verify its functionality. The tests use Python's unittest framework and are designed to run without displaying the GUI, making them suitable for continuous integration environments.

### Test Coverage

The tests cover the following functionality:

1. **Initial State**: Verifies that the application starts with the correct configuration (buttons, window properties).
2. **Color Buttons**: Tests that clicking each color button changes the background color correctly.
3. **Quit Button**: Tests that clicking the quit button closes the application.
4. **Error Handling**: Tests the behavior when an invalid button label is provided.

### Running the Tests

To run the tests, execute:

```bash
python test_wxpython_color_buttons.py
```

### Testing Approach

The application was refactored to make it more testable:

1. **Separation of UI Logic**: The button click handling logic was separated from the event handling to allow programmatic testing.
2. **Button References**: Button references are stored in a dictionary for easier access during testing.
3. **Testing Methods**: Methods were added to get the current background color and simulate button clicks.
4. **State Tracking**: A 'closed' flag was added to track when the application is closed.

This approach allows testing the application's functionality without actually displaying the GUI, making the tests faster and more reliable.

## Logging Feature

The application logs all button interactions to stdout (console). For each button click, the following information is logged:

1. **Button Identification**: Shows which button was clicked (e.g., "Button clicked: red")
2. **Action Taken**: 
   - For color buttons: Shows the color change action with RGB values (e.g., "Action: Changing background color to red (255, 0, 0)")
   - For the quit button: Shows the application closing action (e.g., "Action: Closing application")
   - For invalid buttons: Shows an error message (e.g., "Action: Invalid button - no action taken")

This logging feature is useful for:
- Monitoring user interactions with the application
- Debugging issues related to button functionality
- Tracking application usage patterns

The logs appear in the console from which the application was launched.

## Requirements

- Python 3.x
- wxPython
