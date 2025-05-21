import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt Example')
window.setGeometry(100, 100, 280, 80)
label = QLabel('<center>Hello, PyQt!</center>', parent=window)
window.show()
sys.exit(app.exec())
