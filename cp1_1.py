import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
win = QWidget()

win.setWindowTitle('PyQt5 GUI')
win.resize(400, 300)

win.show()
sys.exit(app.exec_())