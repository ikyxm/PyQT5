import sys
import 垂直布局

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    # 创建QApplication类实例
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = 垂直布局.Ui_MainWindow()
    ui.setupUi(mainWindow)
    # 显示窗口
    mainWindow.show()
    # 进入程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())