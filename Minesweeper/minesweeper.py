from PyQt5 import QtWidgets
from mine_ui import Ui_MainWindow
from random import randint

class MineSweeperWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.board = [ \
            self.pushButton_1, \
            self.pushButton_2, \
            self.pushButton_3, \
            self.pushButton_4, \
            self.pushButton_5, \
            self.pushButton_6, \
            self.pushButton_7, \
            self.pushButton_8, \
            self.pushButton_9, \
            self.pushButton_10, \
            self.pushButton_11, \
            self.pushButton_12, \
            self.pushButton_13, \
            self.pushButton_14, \
            self.pushButton_15, \
            self.pushButton_16, \
            self.pushButton_17, \
            self.pushButton_18, \
            self.pushButton_19, \
            self.pushButton_20, \
            self.pushButton_21, \
            self.pushButton_22, \
            self.pushButton_23, \
            self.pushButton_24, \
            self.pushButton_25, \
        ]

        self.bomb_setter() #chooses 5 random places to set the bombs
        #self.disp_bombs() #this is to check wheter bombs are in the right place or not

        self.pushButton_1.clicked.connect(self.pressed)
        self.pushButton_2.clicked.connect(self.pressed)
        self.pushButton_3.clicked.connect(self.pressed)
        self.pushButton_4.clicked.connect(self.pressed)
        self.pushButton_5.clicked.connect(self.pressed)
        self.pushButton_6.clicked.connect(self.pressed)
        self.pushButton_7.clicked.connect(self.pressed)
        self.pushButton_8.clicked.connect(self.pressed)
        self.pushButton_9.clicked.connect(self.pressed)
        self.pushButton_10.clicked.connect(self.pressed)
        self.pushButton_11.clicked.connect(self.pressed)
        self.pushButton_12.clicked.connect(self.pressed)
        self.pushButton_13.clicked.connect(self.pressed)
        self.pushButton_14.clicked.connect(self.pressed)
        self.pushButton_15.clicked.connect(self.pressed)
        self.pushButton_16.clicked.connect(self.pressed)
        self.pushButton_17.clicked.connect(self.pressed)
        self.pushButton_18.clicked.connect(self.pressed)
        self.pushButton_19.clicked.connect(self.pressed)
        self.pushButton_20.clicked.connect(self.pressed)
        self.pushButton_21.clicked.connect(self.pressed)
        self.pushButton_22.clicked.connect(self.pressed)
        self.pushButton_23.clicked.connect(self.pressed)
        self.pushButton_24.clicked.connect(self.pressed)
        self.pushButton_25.clicked.connect(self.pressed)

    def bomb_setter(self):
        rand = []
        while len(rand) != 5:
            r = randint(0,24)
            if r not in rand:
                rand.append(r)
        for i in rand:
            self.board[i].setObjectName("bomb")

    def disp_bombs(self):
        for i in self.board:
            if i.objectName() == "bomb":
                i.setStyleSheet("background-color: black;")
    

    def pressed(self):
        button = self.sender()
        if button.objectName() == "bomb":
            self.disp_bombs()
            self.label.setText("Game Over!")
            self.dis_all()
        else:
            place = self.board.index(button)
            bomb_number = 0
            if (place == 0) or ((place % 5) == 0):
                if (place + 1) in range(0,25) and self.board[place + 1].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place + 5) in range(0,25) and self.board[place + 5].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place + 6) in range(0,25) and self.board[place + 6].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place - 4) in range(0,25) and self.board[place - 4].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place - 5) in range(0,25) and self.board[place - 5].objectName() == "bomb":
                    bomb_number = bomb_number + 1
            elif ((place + 1) % 5) == 0:
                if (place - 1) in range(0,25) and self.board[place - 1].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place - 5) in range(0,25) and self.board[place - 5].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place - 6) in range(0,25) and self.board[place - 6].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place + 4) in range(0,25) and self.board[place + 4].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place + 5) in range(0,25) and self.board[place + 5].objectName() == "bomb":
                    bomb_number = bomb_number + 1
            else:
                if (place - 1) in range(0,25) and self.board[place - 1].objectName() == "bomb": 
                    bomb_number = bomb_number + 1
                if (place - 4) in range(0,25) and self.board[place - 4].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place - 5) in range(0,25) and self.board[place - 5].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place - 6) in range(0,25) and self.board[place - 6].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place + 1) in range(0,25) and self.board[place + 1].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place + 4) in range(0,25) and self.board[place + 4].objectName() == "bomb":
                    bomb_number = bomb_number + 1
                if (place + 5) in range(0,25) and self.board[place + 5].objectName() == "bomb":
                    bomb_number = bomb_number + 1    
                if (place + 6) in range(0,25) and self.board[place + 6].objectName() == "bomb":
                    bomb_number = bomb_number + 1
            if bomb_number == 0:
                button.setStyleSheet("background-color: yellow;")
            else:
                button.setStyleSheet("background-color: yellow;")
                button.setText(str(bomb_number))
        check = 0
        for i in range(0,25):
            if self.board[i].styleSheet() == "background-color: yellow;":
                check += 1
        if check == 20:
            self.label.setText("You Won!")
            self.dis_all()

    def dis_all(self):
        for i in range(0,25):
                self.board[i].disconnect()