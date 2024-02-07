from PyQt5.QtWidgets import QApplication, QFileDialog  # 导入所需的模块
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon  # 引入QIcon
from PyQt5.QtCore import Qt


class showImage:  # 定义一个名为showImage的类

    def __init__(self):  # 类的初始化方法
        # 从文件中加载UI定义
        self.ui = uic.loadUi("main.ui")  # 加载名为main.ui的UI文件
        self.ui.button.clicked.connect(self.openimage)  # 将按钮的点击事件与openimage方法连接

    def openimage(self):  # 定义openimage方法
        # 使用 QFileDialog 获取用户选择的文件路径
        file_dialog = QFileDialog()  # 创建一个QFileDialog对象
        file_dialog.setViewMode(QFileDialog.Detail)  # 设置文件对话框的视图模式为详细模式
        file_path, _ = file_dialog.getOpenFileName(None, '选择图片', '', 'Images (*.png *.xpm *.jpg *.bmp)')  # 获取用户选择的图片文件路径

        # 如果用户选择了文件路径，则加载并显示图片
        if file_path:  # 判断文件路径是否存在
            self.showImage(file_path)  # 调用showImage方法显示图片

    def showImage(self, file_path):  # 定义showImage方法，用于显示图片
        # 使用 QPixmap 加载图片并设置给 QLabel 显示
        pixmap = QPixmap(file_path)  # 使用QPixmap加载图片
        pixmap = pixmap.scaled(self.ui.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 使用scaled方法保持原始比例
        self.ui.label.setPixmap(pixmap)  # 将加载的图片设置给QLabel显示
        self.ui.label.setAlignment(Qt.AlignCenter)  # 设置图片居中显示

        
if __name__ == '__main__':
    app = QApplication([])  # 创建一个QApplication对象
    app.setWindowIcon(QIcon('2.bmp'))  # 设置窗口图标
    window = showImage()  # 创建showImage对象
    window.ui.show()  # 显示UI界面
    app.exec_()  # 运行应用程序的事件循环
