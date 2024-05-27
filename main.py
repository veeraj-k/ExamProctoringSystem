import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from utils.database import upload_sql
from utils.video_capture import start_video_capture
from datetime import datetime
from utils.myquiz import *
import threading

violation_queue = queue.Queue()
stop_event = threading.Event()
class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.tests = ['Operating System', 'OOPS','DBMS','Java','Python','GoLang']  # Add your test names here
        self.test_combobox.addItems(self.tests)
        self.loginbutton.clicked.connect(self.goto_page)

    def goto_page(self):
        global name, usn, login_time,subject,logout_time
        name = self.name.text()
        usn = self.roll.text()
        now = datetime.now()
        login_time=now.strftime("%d/%m/%Y %H:%M:%S")
        subject = self.test_combobox.currentText()
        test_index = self.tests.index(subject) + 1
        
        widget.close()
        t1 = threading.Thread(target=start_video_capture,args=("abc",violation_queue,stop_event))
        t1.start()
        score = startQuiz(violation_queue=violation_queue,testid=test_index)
        stop_event.set()
        print(score)
        logout_time= datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        upload_sql(usn,name,subject,login_time,logout_time,score)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(607)
    widget.setFixedHeight(676)
    widget.show()
    app.exec_()
    
