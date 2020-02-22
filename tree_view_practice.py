import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from ui_tree_view_practice import Ui_MainWindow


class CustomNode(object):
    def __init__(self, data):
        self._data = data
        if type(data) == tuple:
            self._data = list(data)
        if type(data) is str or not hasattr(data, '__getitem__'):
            self._data = [data]

        self._columncount = len(self._data)
        self._children = []
        self._parent = None
        self._row = 0
        self.display_color = "red"

    def data(self, column):
        if 0 <= column < len(self._data):
            return self._data[column]

    def columnCount(self):
        return self._columncount

    def childCount(self):
        return len(self._children)

    def child(self, row):
        if 0 <= row < self.childCount():
            return self._children[row]

    def parent(self):
        return self._parent

    def row(self):
        return self._row

    def addChild(self, child):
        child._parent = self
        child._row = len(self._children)
        self._children.append(child)
        self._columncount = max(child.columnCount(), self._columncount)


class CustomModel(QtCore.QAbstractItemModel):
    def __init__(self, nodes):
        super(CustomModel, self).__init__()
        self._root = CustomNode(None)
        for node in nodes:
            self._root.addChild(node)

    def rowCount(self, index):
        if index.isValid():
            return index.internalPointer().childCount()
        return self._root.childCount()

    def addChild(self, node, _parent_index):
        if not _parent_index or not _parent_index.isValid():
            parent = self._root
        else:
            parent = _parent_index.internalPointer()
        parent.addChild(node)

    def index(self, row, column, _parent=None):
        if not _parent or not _parent.isValid():
            parent = self._root
        else:
            parent = _parent.internalPointer()

        if not QtCore.QAbstractItemModel.hasIndex(self, row, column, _parent):
            return QtCore.QModelIndex()

        child = parent.child(row)
        if child:
            return QtCore.QAbstractItemModel.createIndex(self, row, column, child)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        if index.isValid():
            p = index.internalPointer().parent()
            if p:
                return QtCore.QAbstractItemModel.createIndex(self, p.row(), 0, p)
        return QtCore.QModelIndex()

    def columnCount(self, index):
        if index.isValid():
            return index.internalPointer().columnCount()
        return self._root.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()
        if role == QtCore.Qt.DisplayRole:
            return node.data(index.column())
        if role == QtCore.Qt.BackgroundColorRole:
            if node.display_color == 'red':
                return QtGui.QColor(QtCore.Qt.red)
            elif node.display_color == 'green':
                return QtGui.QColor(QtCore.Qt.green)
        return None

    def insertRow(self, parent_index=None, *args, **kwargs):
        self.addChild(CustomNode([1,2,3]), parent_index)


class MyTree(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyTree, self).__init__()
        self.setupUi(self)
        self._tree_items = []
        for i in '1234567890':
            self._tree_items.append(CustomNode(i))
            # self._tree_items[-1].addChild(CustomNode(['d']))
            # self._tree_items[-1].addChild(CustomNode(['d', 'e', 'f']))
            # self._tree_items[-1].addChild(CustomNode(['g', 'h', 'i']))

            test_run_node = CustomNode('Test Run')
            for i in range(5):
                test_run_node.addChild(CustomNode(['parameter', 'expected', 'measured', 'description']))
            self._tree_items[-1].addChild(test_run_node)
        self.treeView.setModel(CustomModel(self._tree_items))
        self.pushButton.clicked.connect(self.add_item)

    def add_item(self):
        if self.treeView.selectedIndexes():
            parent_node_index = self.treeView.currentIndex()
            print(parent_node_index.internalPointer()._data)
            parent_node_index.internalPointer().display_color = 'green'
            # self.treeView.model().beginResetModel()
            self.treeView.model().insertRow(parent_index=parent_node_index)
            # self.treeView.model().endResetModel()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyTree()
    ui.show()
    app.exec_()