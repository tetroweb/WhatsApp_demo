from PyQt5.QtWidgets  import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.main_vbox = QVBoxLayout(self)
        self.main_vbox.setContentsMargins(0,0,0,0)
        self.main_vbox.setSpacing(0)
        
        # main window hbox top
        self.main_hbox_top = QHBoxLayout()
        self.main_hbox_top.setSpacing(0)
        
        self.widget = QLabel()
        
        #-----------------------------top logo--------------------------------------
        self.logo_label = QLabel()
        pixmap =QPixmap( r"C:\Users\berka\OneDrive\Masaüstü\WhattsApp demo\images\whatsApp_main_logo.png")
        pixmap = pixmap.scaled(50,50)
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.logo_label.setStyleSheet("background-color:#252B48; color:white;")
        
        
        
        #------------------------------top title------------------------------------
        self.title_layout = QHBoxLayout()
        
        self.large_title = QLabel("WhatsApp")
        self.large_title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.large_title.setFont(QFont("Tahoma",10))
        self.large_title.setMaximumWidth(100)
        self.large_title.setFixedHeight(50)
        self.large_title.setStyleSheet("background-color:#252B48; color:white;")
        
        self.small_title = QLabel("Beta")
        self.small_title.setFont(QFont("Tahoma",6))
        self.small_title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.small_title.adjustSize()
        self.small_title.setStyleSheet("background-color:#252B48; color:white;")
        
        
        self.title_layout.addWidget(self.large_title)
        self.title_layout.addWidget(self.small_title)
        self.small_title.setMaximumWidth(30)
        self.small_title.setFixedHeight(50)
        #----------------------------------------------------------------------------
        
        #--------------------------------Filler Layout-------------------------------
        self.filler_widget=QLabel()
        self.filler_widget.setStyleSheet("background-color:#252B48;")
        self.filler_widget.setFixedWidth(1610)
        self.filler_widget.setFixedHeight(50)
        
        self.filler_widget.setAlignment(Qt.AlignLeft)
        
        #----------------------------------------------------------------------------
        
        #--------------------------------Button layout-------------------------------
        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(0)

        #minimize
        self.minimize_button = QToolButton()
        self.minimize_button.setIcon(QIcon(r"C:\Users\berka\OneDrive\Masaüstü\WhattsApp demo\images\minimize.png"))
        self.minimize_button.setStyleSheet("QToolButton{background-color:#252B48; border:none;}QToolButton:hover{background-color:#445069}")
        
        self.minimize_button.setFixedWidth(50)
        self.minimize_button.setFixedHeight(50)
        
        self.button_layout.addWidget(self.minimize_button)
        
        #maximize
        self.maximize_button = QToolButton()
        self.maximize_button.setIcon(QIcon(r"C:\Users\berka\OneDrive\Masaüstü\WhattsApp demo\images\maximize.png"))
        self.maximize_button.setStyleSheet("QToolButton{background-color:#252B48;border:none;}QToolButton:hover{background-color:#445069;}")
        
        
        self.maximize_button.setFixedWidth(50)
        self.maximize_button.setFixedHeight(50)
        
        self.button_layout.addWidget(self.maximize_button)
        
        #close
        self.close_button = QToolButton()
        self.close_button.setIcon(QIcon(r"C:\Users\berka\OneDrive\Masaüstü\WhattsApp demo\images\close.png"))
        self.close_button.setStyleSheet("QToolButton{background-color:#252B48;  border:none;}QToolButton:hover{background-color:#CD1818;}")
        self.button_layout.addWidget(self.close_button)
        

        self.close_button.setFixedWidth(50)
        self.close_button.setFixedHeight(50)
        
        
        self.maximize_button.clicked.connect(self.showMaximized)
        self.close_button.clicked.connect(self.close)
        self.minimize_button.clicked.connect(self.showMinimized)
        
        
        #----------------------------------------------------------------------------
        
        
        self.main_hbox_top.addWidget(self.logo_label)
        self.main_hbox_top.addLayout(self.title_layout)
        
        self.main_hbox_top.addWidget(self.filler_widget)
        self.main_hbox_top.addLayout(self.button_layout)
        
        
        
        
        #main window vbox at bottom side
        self.main_vbox_bottom = QVBoxLayout()
        
        self.label2 = QLabel()
        self.label2.setStyleSheet("background-color:pink;")
        self.main_vbox_bottom.addWidget(self.label2)
        self.label2.setFixedHeight(1000)
        
        #add main_vbox
        self.main_vbox.addLayout(self.main_hbox_top)
        self.main_vbox.addLayout(self.main_vbox_bottom)
        
        
        
        
        self.showMaximized() 
        
        
app = QApplication([])
window = main()
app.exec()