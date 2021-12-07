import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px微软雅黑字体。
        QToolTip.setFont(QFont('Microsoft YaHei', 10))

        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('这是一个<b>QWidget</b>小部件')

        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('按钮', self)
        btn.setToolTip('这是一个<b>QWidget</b>小部件')

        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())

        # 移动窗口的位置
        btn.move(200, 75)

        self.setGeometry(700, 350, 500, 300)
        self.setWindowTitle('提示语')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())