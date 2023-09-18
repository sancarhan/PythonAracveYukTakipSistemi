import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout

class AraçVeYükTakipSistemi(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.create_database()

    def initUI(self):
        self.setWindowTitle('Araç ve Yük Takip Sistemi')
        self.setGeometry(100, 100, 400, 400)

        self.date_label = QLabel('Tarih:')
        self.date_input = QLineEdit()

        self.plate_label = QLabel('Plaka:')
        self.plate_input = QLineEdit()

        self.geldigi_il_label = QLabel('Geldiği İl:')
        self.geldigi_il_input = QLineEdit()

        self.getirdigi_yuk_label = QLabel('Getirdiği Yük:')
        self.getirdigi_yuk_input = QLineEdit()

        self.gidecegi_il_label = QLabel('Gideceği İl:')
        self.gidecegi_il_input = QLineEdit()

        self.goturecegi_yuk_label = QLabel('Götüreceği Yük:')
        self.goturecegi_yuk_input = QLineEdit()

        self.yuk_turu_label = QLabel('Yük Türü:')
        self.yuk_turu_input = QLineEdit()

        self.yuk_agirligi_label = QLabel('Yükün Ağırlığı:')
        self.yuk_agirligi_input = QLineEdit()

        self.add_button = QPushButton('Kaydet')
        self.add_button.clicked.connect(self.kaydet)

        self.list_widget = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.plate_label)
        layout.addWidget(self.plate_input)
        layout.addWidget(self.geldigi_il_label)
        layout.addWidget(self.geldigi_il_input)
        layout.addWidget(self.getirdigi_yuk_label)
        layout.addWidget(self.getirdigi_yuk_input)
        layout.addWidget(self.gidecegi_il_label)
        layout.addWidget(self.gidecegi_il_input)
        layout.addWidget(self.goturecegi_yuk_label)
        layout.addWidget(self.goturecegi_yuk_input)
        layout.addWidget(self.yuk_turu_label)
        layout.addWidget(self.yuk_turu_input)
        layout.addWidget(self.yuk_agirligi_label)
        layout.addWidget(self.yuk_agirligi_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def create_database(self):
        self.conn = sqlite3.connect('yuk_takip.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS yuklar
             (tarih TEXT, plaka TEXT, geldigi_il TEXT, getirdigi_yuk TEXT, gidecegi_il TEXT,
             goturecegi_yuk TEXT, yuk_turu TEXT, yuk_agirligi TEXT)''')
        self.conn.commit()

    def kaydet(self):
        tarih = self.date_input.text()
        plaka = self.plate_input.text()
        geldigi_il = self.geldigi_il_input.text()
        getirdigi_yuk = self.getirdigi_yuk_input.text()
        gidecegi_il = self.gidecegi_il_input.text()
        goturecegi_yuk = self.goturecegi_yuk_input.text()
        yuk_turu = self.yuk_turu_input.text()
        yuk_agirligi = self.yuk_agirligi_input.text()

        # Veritabanına kaydet
        self.c.execute("INSERT INTO yuklar VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (tarih, plaka, geldigi_il, getirdigi_yuk, gidecegi_il, goturecegi_yuk, yuk_turu, yuk_agirligi))
        self.conn.commit()

        # Listeye ekle
        item_text = f"{tarih}, {plaka}, {geldigi_il}, {getirdigi_yuk}, {gidecegi_il}, {goturecegi_yuk}, {yuk_turu}, {yuk_agirligi}"
        self.list_widget.addItem(item_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AraçVeYükTakipSistemi()
    ex.show()
    sys.exit(app.exec_())
