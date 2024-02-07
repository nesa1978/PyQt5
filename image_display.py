import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class ImageDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Display App')
        self.setGeometry(1200, 600, 600, 400)

        # 创建一个 QLabel 用于显示图片
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(400, 400)
        self.image_label.setAlignment(Qt.AlignCenter)

        # 创建一个按钮用于选择图片
        self.select_button = QPushButton('选择图片', self)
        self.select_button.clicked.connect(self.showDialog)

        # 创建一个布局，并将 QLabel 和按钮添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.select_button)

        # 创建一个主窗口中心的部件，并将布局设置为该部件的布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def showDialog(self):
        # 使用 QFileDialog 获取用户选择的文件路径
        file_dialog = QFileDialog()
        # file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_path, _ = file_dialog.getOpenFileName(self, '选择图片', '', 'Images (*.png *.xpm *.jpg *.bmp)')

        # 如果用户选择了文件路径，则加载并显示图片
        if file_path:
            self.showImage(file_path)

    def showImage(self, file_path):
        # 使用 QPixmap 加载图片并设置给 QLabel 显示
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('南昌.bmp'))
    window = ImageDisplayApp()
    window.show()
    sys.exit(app.exec_())
