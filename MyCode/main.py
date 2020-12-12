import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setGeometry(200, 200, 600, 600)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            self.btn.hide()
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(random.randint(3, 6)):
            x = random.randint(0, 200)
            y = random.randint(100, 300)
            d = random.randint(10, 100)
            x1 = x + d
            y1 = x + d
            qp.drawEllipse(x, y, x1, y1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())