from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QListWidget
import os
from PyQt5.QtGui import QPixmap
from PIL import Image
app = QApplication([])
window = QWidget() #Створення вікна
window.setWindowTitle("Редактор фото")
window.resize(1000,800)

but_folder = QPushButton("Папка") 
list_img = QListWidget()
label_img = QLabel("Тут буде картинка")
but_left = QPushButton("Вліво")
but_right = QPushButton("Право")
but_mirrow = QPushButton("Дзеркально")
but_bluer = QPushButton("Різкість")
but_bw = QPushButton("Чорно-біле")

lineMain = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()
lineH1 = QHBoxLayout()

lineV1.addWidget(but_folder)
lineV1.addWidget(list_img, 80)
lineMain.addLayout(lineV1)

lineV2.addWidget(label_img)
lineH1.addWidget(but_left)
lineH1.addWidget(but_right)
lineH1.addWidget(but_mirrow)
lineH1.addWidget(but_bluer)
lineH1.addWidget(but_bw)

lineV2.addLayout(lineH1)
lineMain.addLayout(lineV2,80)
window.setLayout(lineMain)

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
        return result
def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilename():
    ex = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    chooseWorkDir()
    filenames = filter(os.listdir(workdir), ex)
    list_img.clear()
    for filename in filenames:
        list_img.addItem(filename)
but_folder.clicked.connect(showFilename)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
    
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)



window.show()
app.exec_()















