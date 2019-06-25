import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QIcon
import requests

accesskey = "" #paste your fixer.io acces key
url = "http://data.fixer.io/api/latest?access_key=" + accesskey

response = requests.get(url)
infos = response.json()

class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)

    def init_ui(self):

        self.doviz1 = QLineEdit("")
        self.doviz2 = QLineEdit("")

        self.bilgi = QLabel("")
        self.button = QPushButton("Kısaltma bilgilerini göster/gizle")
        self.button.setCheckable(True)
        
        self.combo1 = QComboBox()
        self.combo1.setFixedWidth(50)
        self.combo1.addItem("From")
        self.combo1.addItem("TRY")
        self.combo1.addItem("USD")
        self.combo1.addItem("EUR")
        self.combo1.addItem("GBP")
        self.combo1.addItem("JPY")
        self.combo1.addItem("CHF")
        self.combo1.addItem("CAD")
        self.combo1.addItem("AUD")
        self.combo1.addItem("CNY")
        self.combo1.addItem("RUB")
        self.combo1.addItem("NZD")

        self.combo2 = QComboBox()
        self.combo2.setFixedWidth(50)
        self.combo2.addItem("To")
        self.combo2.addItem("USD")
        self.combo2.addItem("EUR")
        self.combo2.addItem("TRY")
        self.combo2.addItem("GBP")
        self.combo2.addItem("JPY")
        self.combo2.addItem("CHF")
        self.combo2.addItem("CAD")
        self.combo2.addItem("AUD")
        self.combo2.addItem("CNY")
        self.combo2.addItem("RUB")
        self.combo2.addItem("NZD")

        self.flag = QLabel()
        self.flag.setPixmap(QPixmap("images/usd.png"))

        self.flag2 = QLabel()
        self.flag2.setPixmap(QPixmap("images/eu.png"))

        self.flag3 = QLabel()
        self.flag3.setPixmap(QPixmap("images/jpy.png"))

        self.flag4 = QLabel()
        self.flag4.setPixmap(QPixmap("images/gbp.png"))

        self.flag5 = QLabel()
        self.flag5.setPixmap(QPixmap("images/chf.png"))

        self.flag6 = QLabel()
        self.flag6.setPixmap(QPixmap("images/cad.png"))

        self.flag7 = QLabel()
        self.flag7.setPixmap(QPixmap("images/aud.png"))

        self.flag8 = QLabel()
        self.flag8.setPixmap(QPixmap("images/cny.png"))

        self.flag9 = QLabel()
        self.flag9.setPixmap(QPixmap("images/rub.png"))

        self.flag10 = QLabel()
        self.flag10.setPixmap(QPixmap("images/nzd.png"))

        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(2)

        self.table.setCellWidget(0,0, self.flag)
        self.table.setItem(0, 0, QTableWidgetItem("      USD/TRY"))
        self.table.setItem(0, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["USD"])).replace(".",","))))

        self.table.setCellWidget(1, 0, self.flag2)
        self.table.setItem(1, 0, QTableWidgetItem("      EUR/TRY"))
        self.table.setItem(1, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["EUR"])).replace(".",","))))

        self.table.setCellWidget(2, 0, self.flag4,)
        self.table.setItem(2, 0, QTableWidgetItem("      GBP/TRY"))
        self.table.setItem(2, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["GBP"])).replace(".",","))))

        self.table.setCellWidget(3, 0, self.flag3)
        self.table.setItem(3, 0, QTableWidgetItem("      JPY/TRY"))
        self.table.setItem(3, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["JPY"])).replace(".",","))))

        self.table.setCellWidget(4, 0, self.flag5)
        self.table.setItem(4, 0, QTableWidgetItem("      CHF/TRY"))
        self.table.setItem(4, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["CHF"])).replace(".",","))))

        self.table.setCellWidget(5, 0, self.flag6)
        self.table.setItem(5, 0, QTableWidgetItem("      CAD/TRY"))
        self.table.setItem(5, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["CAD"])).replace(".",","))))

        self.table.setCellWidget(6, 0, self.flag7)
        self.table.setItem(6, 0, QTableWidgetItem("      AUD/TRY"))
        self.table.setItem(6, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["AUD"])).replace(".",","))))

        self.table.setCellWidget(7, 0, self.flag8)
        self.table.setItem(7, 0, QTableWidgetItem("      CNY/TRY"))
        self.table.setItem(7, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["CNY"])).replace(".",","))))

        self.table.setCellWidget(8, 0, self.flag9)
        self.table.setItem(8, 0, QTableWidgetItem("      RUB/TRY"))
        self.table.setItem(8, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["RUB"])).replace(".",","))))

        self.table.setCellWidget(9, 0, self.flag10)
        self.table.setItem(9, 0, QTableWidgetItem("      NZD/TRY"))
        self.table.setItem(9, 1, QTableWidgetItem("{}".format(('%.4f' %(infos["rates"]["TRY"]/infos["rates"]["NZD"])).replace(".",","))))

        vbox = QVBoxLayout()
        vbox.addWidget(self.table)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.combo1)
        vbox2.addWidget(self.combo2)
        vbox2.addStretch()

        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.doviz1)
        vbox3.addWidget(self.doviz2)
        vbox3.addStretch()

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox2)
        hbox2.addLayout(vbox3)

        vbox4 = QVBoxLayout()
        vbox4.addLayout(hbox2)
        vbox4.addWidget(self.button)
        vbox4.addWidget(self.bilgi)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        #hbox.addStretch()
        hbox.addLayout(vbox4)

        self.fromm = QLabel("")
        self.to = QLabel("")

        self.setLayout(hbox)
        self.combo1.activated[str].connect(self.onActivated)
        self.combo2.activated[str].connect(self.onActivated2)
        self.doviz1.textChanged[str].connect(self.islem)
        self.button.clicked[bool].connect(self.showhide)
        self.setWindowIcon(QIcon("images\icon3.png"))
        self.setWindowTitle("Döviz Uygulaması")
        self.show()

    def showhide(self, pressed):
        if pressed:
            self.bilgi.setText("  USD: Amerikan Doları\n\n  EUR: Euro\n\n  GBP: İngiliz Sterlini\n\n  JPY: Japon Yeni\n\n  CHF: İsveç Frangı\n\n  CAD: Kanada Doları\n\n  AUD: Avustralya Doları\n\n  CNY: Çin Yuanı\n\n  RUB: Rus Rublesi\n\n  NZD: Yeni Zelanda Doları")
        else:
            self.bilgi.setText("")

    def onActivated(self, text):
        self.doviz1.setText("")
        self.doviz2.setText("")

        if text != "From":
            self.fromm.setText(text)

            self.firstValue = infos["rates"][self.fromm.text()]

    def onActivated2(self, text):
        self.doviz2.setText("")
        self.doviz1.setText("")

        if text != "To":
            self.to.setText(text)

            self.secondValue = infos["rates"][self.to.text()]

    def islem(self):

        if self.doviz1.text() != "" and self.combo1.currentText() != "From" and self.combo2.currentText() != "To":

            islem = self.secondValue / self.firstValue * float(self.doviz1.text())

            self.doviz2.setText("{}".format(islem))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = Window()
    window.setGeometry(500,100,400,345)
    sys.exit(app.exec_())
