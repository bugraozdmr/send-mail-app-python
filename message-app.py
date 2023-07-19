import sys
from smtplib import SMTP


from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QDialog,QWidget,QStackedWidget
from PyQt5.QtGui import QIcon

class ana(QDialog):
    def __init__(self):
        print("23213e12")
        super(QDialog,self).__init__()
        loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\program\message.ui",self)



        self.pushButton.clicked.connect(self.send)
        self.pushButton_2.clicked.connect(self.delete)



    def delete(self):


        self.lineEdit.setText("")
        self.textEdit.setText("")

    def send(self):
        # textedit için toPlainText()
        # line edit için text() çalışır

        # simple mail transfer protokolu
        # Basit mail göndermek için kullanılır.



        if self.lineEdit.text() == "" or self.textEdit.toPlainText() == "" or self.lineEdit_2.text() == "":
            print("1.fonk çalıştı")
            print("Boş bırakılan alanlar var.Oraları doldur.")
            self.label_4.setText("BOŞ BIRAKILAN ALANLAR VAR")


        #not in (ile) kontrol yapıldı
        elif "@" not in self.lineEdit_2.text() or ".com" not in self.lineEdit_2.text():
            print("2.fonk çalıştı")
            self.label_4.setText("GIRILEN MAIL MEVCUT DEGIL")


        else:
            print("4.fonk çalıştı")
            self.label_4.setText("")
            try:
                # mail mesaj bilgisi
                subject = self.lineEdit.text()
                message = self.textEdit.toPlainText()
                content = "Subject: {0}\n\n{1}".format(subject, message)

                # gönderici hesap bilgileri
                mymail = "mail_adress"
                password = "your google app password"  # google uygulama için şifre veriyor !!

                # kime gonderilecek
                sentto = self.lineEdit_2.text()

                mail = SMTP("smtp.gmail.com", 587)  # google smtp sunucusu
                mail.ehlo()  # maile bağlandı
                mail.starttls()  # şifreli gönderdi mesajı
                mail.login(mymail, password)
                mail.sendmail(mymail, sentto,
                              content.encode("utf-8"))  # encode türkçe karakterlerle sıkıntı çıkmaması için yazıldı.
                print("mail gonderme islemi basarılı")

            except Exception as e:
                print("hata aldınız !\n {}".format(e))




app = QApplication(sys.argv)
ana1 = ana()
widget = QStackedWidget()
widget.addWidget(ana1)
widget.setWindowTitle("SEND MAIL")
widget.setWindowIcon(QIcon(r"C:\Users\bugra\OneDrive\Masaüstü\program\mail.png"))
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()
try:
    print("working ...")
    sys.exit(app.exec_())
except:
    print("exiting ...")
