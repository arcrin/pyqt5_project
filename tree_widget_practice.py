from ui_tree_widget import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtGui import QColor
import sys


class MyTreeWidget(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(MyTreeWidget, self).__init__()
        self.setupUi(self)
        self.treeWidget.setHeaderLabels(['a', 'b', 'c', 'd'])
        self.top_item_list = []
        for i in range(5):
            tc = QTreeWidgetItem(['test {}'.format(i)], type=3)
            # tc.setText(0, 'test {}'.format(i))
            # tr = QTreeWidgetItem(tc)
            # tr.setText(0, 'Test Run')
            # tc.addChild(tr)
            self.top_item_list.append(tc)
            # self.treeWidget.addTopLevelItem(tc)
        self.treeWidget.addTopLevelItems(self.top_item_list)

        self.add_test_run_button.clicked.connect(self.add_test_run_button_clicked)
        self.clear_button.clicked.connect(self.clear_button_clicked)

    def clear_button_clicked(self):
        print("clear button pressed")
        self.treeWidget.clear()
        self.top_item_list = []

    def add_test_run_button_clicked(self):
        selected_item = self.treeWidget.selectedItems()[0]
        print(selected_item.type())
        tr = QTreeWidgetItem(['test run'])  # list of strings
        # tr = QTreeWidgetItem(selected_item)  # set parent
        tr.setText(0, 'Test Run')  # set text for column 0
        # parameter = QTreeWidgetItem(['parameter', 'expected', 'measured', 'description'])
        # parameter.setBackground(0, QColor(QtCore.Qt.green))
        # tr.addChild(parameter)
        # tr.setBackground(0, QColor(QtCore.Qt.green))
        selected_item.addChild(tr)




        # selected_item.setBackground(0, QColor(QtCore.Qt.green))


        # self.treeWidget.child(0).text()

    def add_pass_button_clicked(self):
        selected_item = self.treeWidget.selectedItems()[0]
        selected_item.type = 1

    def add_failure_button_clicked(self):
        pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MyTreeWidget()
    ui.show()
    sys.exit(app.exec_())
