from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys
import sqlite3
from PyQt6 import uic


class sqliteViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui")

        self.connection = sqlite3.connect("coffee.sqlite")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        self.res = self.connection.cursor().execute("""SELECT * FROM charcoffee""")
        for i, row in enumerate(self.res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = sqliteViewer()
    ex.show()
    sys.exit(app.exec())
