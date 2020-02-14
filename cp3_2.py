from mainwindow3_2 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


def set_table_items(item1='item1', item2='item2', item3='item3'):
    row = 0
    ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(item1))
    ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(item2))
    ui.tableWidget.setItem(2, 2, QtWidgets.QTableWidgetItem(item3))


def button_clicked():
    set_table_items(item2='item2-changed')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    set_table_items()

    ui.pushButton.clicked.connect(button_clicked)
    ui.pushButton.clicked.connect(lambda : ui.pushButton.setText('Button was licked!'))

    MainWindow.show()
    sys.exit(app.exec_())