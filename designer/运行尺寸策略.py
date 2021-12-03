import sys
import 尺寸策略

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = 尺寸策略.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())