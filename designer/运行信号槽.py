import sys
import 信号槽

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = 信号槽.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())