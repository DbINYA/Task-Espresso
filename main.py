import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.correct()

    def correct(self):
        res = self.connection.cursor().execute("SELECT * FROM coffee").fetchall()
        self.text = []
        for i in res:
            k = []
            for j in range(len(i)):
                k.append(str(i[j]))
            self.text.append(k)
        self.connection.close()


    def run(self):
        for i in self.text:
            self.textEdit.setText(' '.join(i))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())