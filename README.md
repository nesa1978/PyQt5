学习使用PyQt5

py程序打包命令

~~~
pyinstaller -w -i "xxx.ico" xxx.py
pyinstaller -w -F -i "xxx.ico" xxx.py
# 这两行命令都是使用PyInstaller来打包一个Python程序，但是有一些不同的选项：

pyinstaller -w -i "xxx.ico" xxx.py：这个命令会打包xxx.py，并且使用xxx.ico作为程序的图标。-w选项会阻止一个控制台窗口的出现。这个命令会生成一个包含多个文件的目录，包括你的程序、依赖的库以及其他资源。

pyinstaller -w -F -i "xxx.ico" xxx.py：这个命令和上一个命令几乎相同，但是它使用了-F（或者--onefile）选项。这个选项会指示PyInstaller将你的程序和所有依赖项打包成一个单一的可执行文件。这样做加载相对较慢。

在这两个命令中，-i "xxx.ico"选项设置了程序的图标，xxx.ico应该是你的图标文件的路径。如果你不提供这个选项，程序将使用默认的图标。
~~~



image_open.py程序对应的界面如下图所示，功能为选择一张图片打开显示在窗口中

![image-20240208182553789](https://s2.loli.net/2024/02/08/qXWCfcv52zmMJRD.png)

![image-20240208182718876](https://s2.loli.net/2024/02/08/cDUMkuoK8v1lJSA.png)
