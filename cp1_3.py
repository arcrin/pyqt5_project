import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QHBoxLayout, QVBoxLayout, QWidget, QGridLayout
from PyQt5.Qt import QLabel, QPushButton, Qt
from PyQt5.QtGui import QIcon



class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')

        self.resize(400, 300)
        self.add_menus_and_status()

        self.layout_using_grid()

    def layout_using_grid(self):
        label_1 = QLabel('First label')
        label_2 = QLabel('Another label')

        button_1 = QPushButton('Click 1')
        button_2 = QPushButton('Click 2')

        grid_layout = QGridLayout()

        grid_layout.addWidget(label_1, 0, 0)
        grid_layout.addWidget(button_1, 0, 1)
        grid_layout.addWidget(label_2, 1, 0)
        grid_layout.addWidget(button_2, 1, 1)

        grid_layout.setAlignment(Qt.AlignBottom)
        grid_layout.setAlignment(label_1, Qt.AlignRight)
        grid_layout.setAlignment(label_2, Qt.AlignRight)

        layout_widget = QWidget()
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)

    def horizontal_vertial_box_layout(self):
        label_1 = QLabel('First label')
        label_2 = QLabel('Another label')

        button_1 = QPushButton('Click 1')
        button_2 = QPushButton('Click 2')

        hbox_1 = QHBoxLayout()
        hbox_1.addStretch()
        hbox_2 = QHBoxLayout()
        hbox_2.addStretch()

        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)

        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)

        vbox = QVBoxLayout()
        vbox.addStretch()

        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        layout_widget = QWidget()
        layout_widget.setLayout(vbox)

        self.setCentralWidget(layout_widget)

    def positional_widget_layout(self):
        label_1 = QLabel('label_1', self)

        print(self.menuBar().size())
        mbar_height = self.menuBar().height()
        print(mbar_height)
        label_1.move(10, mbar_height)

        label_2 = QLabel('Another label', self)
        label_2.move(10, mbar_height * 2)

        button_1 = QPushButton('click 1', self)
        button_2 = QPushButton('click 2', self)

        button_1.move(label_1.width(), label_1.height())
        button_2.move(label_1.width(), label_1.height() * 2)

    def add_menus_and_status(self):
        self.statusBar().showMessage('Text in status bar')
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')

        new_icon = QIcon('icon/editadd.png')
        new_action = QAction(new_icon, 'New', self)
        new_action.setStatusTip('New File')
        file_menu.addAction(new_action)

        file_menu.addSeparator()

        exit_icon = QIcon('icon/editdelete.png')
        exit_action = QAction(exit_icon, 'Exit', self)
        exit_action.setStatusTip('Click to exit the application')
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())