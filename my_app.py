#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Студент
#
# Created:     22.10.2024
# Copyright:   (c) Студент 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from inst import *
from second_win import *

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.connects()
    self.show()
  def initUI(self):
    self.btn_next = QPushButton(txt_next, self)
    self.hello_text = QLabel(txt_hello)
    self.instruction = QLabel(txt_instruction)

    self.layout_line = QVBoxLayout()
    self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
    self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
    self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
    self.setLayout(self.layout_line)
  def connects(self):
    self.btn_next.clicked.connect(self.next_click)
  def next_click(self):
    self.hide()
    self.tw = TestWin()
  def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()


