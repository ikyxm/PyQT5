import sys
import tab顺序

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = tab顺序.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())