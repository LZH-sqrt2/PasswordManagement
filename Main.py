from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

app = QApplication([])

widget = QWidget()
widget.setGeometry(300,300,400,650)

layout = QHBoxLayout(widget)

button1=QPushButton("创建新密码集合")
button2=QPushButton('增删改查已有的密码集合')
button3=QPushButton('语言')

layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)

widget.show()
app.exec()