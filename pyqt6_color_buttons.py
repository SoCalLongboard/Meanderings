import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt6.QtGui import QColor


class ColorFrame(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.init_ui()
        
        # For testing purposes
        self.closed = False

    def init_ui(self):
        # Create layout
        grid = QGridLayout()
        self.setLayout(grid)
        
        # Button labels and corresponding colors
        self.buttons_config = [
            ("red", QColor(255, 0, 0)),
            ("green", QColor(0, 255, 0)),
            ("blue", QColor(0, 0, 255)),
            ("quit", None)
        ]
        
        self.buttons = {}  # Store button references for testing
        
        # Create buttons and add to grid
        positions = [(i, j) for i in range(2) for j in range(2)]
        
        for position, (label, color) in zip(positions, self.buttons_config):
            button = QPushButton(label)
            button.clicked.connect(lambda checked, l=label: self.handle_button_click(l))
            button.color = color  # Custom attribute
            grid.addWidget(button, *position)
            self.buttons[label] = button  # Store button reference
        
        # Set window properties
        self.setWindowTitle("Color Buttons Example")
        self.setGeometry(300, 300, 300, 200)  # x, y, width, height
        self.show()

    def handle_button_click(self, button_label):
        """Handle button click by label - can be called programmatically for testing"""
        print(f"Button clicked: {button_label}")
        
        if button_label == "quit":
            print("Action: Closing application")
            self.close()
            self.closed = True
            return True
        else:
            btn = self.buttons.get(button_label)
            if btn and btn.color:
                color_str = f"({btn.color.red()}, {btn.color.green()}, {btn.color.blue()})"
                print(f"Action: Changing background color to {button_label} {color_str}")
                self.setStyleSheet(f"background-color: {btn.color.name()}")
                return btn.color
            else:
                print(f"Action: Invalid button - no action taken")
        return False
    
    def get_background_color(self):
        """Get the current background color - useful for testing"""
        # Extract color from stylesheet
        style = self.styleSheet()
        if "background-color:" in style:
            color_str = style.split("background-color:")[1].strip().split(";")[0].strip()
            return QColor(color_str)
        return QColor(240, 240, 240)  # Default Qt background color
    
    def simulate_button_click(self, button_label):
        """Simulate clicking a button - useful for testing"""
        return self.handle_button_click(button_label)
    
    def closeEvent(self, event):
        """Handle window close event"""
        self.closed = True
        event.accept()


def run_app():
    app = QApplication(sys.argv)
    frame = ColorFrame()
    app.exec()
    return app


if __name__ == "__main__":
    run_app()