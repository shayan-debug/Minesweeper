import sys
from PyQt5.QtWidgets import QApplication
from minesweeper import MineSweeperWindow

app = QApplication(sys.argv)

mine_sweeper = MineSweeperWindow()

sys.exit(app.exec_())