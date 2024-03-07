import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PySide6.QtCore import QFile, QTextStream

from hv_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Hardware View")
        self.ui.icons_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.system_infos_btn_2.setChecked(True)

        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)

        self.ui.system_infos_btn_1.clicked.connect(self.on_system_infos_btn_1_toggled)
        self.ui.system_infos_btn_2.clicked.connect(self.on_system_infos_btn_2_toggled)

        self.ui.activity_btn_1.clicked.connect(self.on_activity_btn_1_toggled)
        self.ui.activity_btn_2.clicked.connect(self.on_activity_btn_2_toggled)

        self.ui.disks_btn_1.clicked.connect(self.on_disks_btn_1_toggled)
        self.ui.disks_btn_2.clicked.connect(self.on_disks_btn_2_toggled)

        self.ui.cpu_btn_1.clicked.connect(self.on_cpu_btn_1_toggled)
        self.ui.cpu_btn_2.clicked.connect(self.on_cpu_btn_2_toggled)
        
        self.ui.network_btn_1.clicked.connect(self.on_network_btn_1_toggled)
        self.ui.network_btn_2.clicked.connect(self.on_network_btn_2_toggled)
        
        self.ui.about_btn_1.clicked.connect(self.on_about_btn_1_toggled)
        self.ui.about_btn_2.clicked.connect(self.on_about_btn_2_toggled)



    # function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)
        


    # function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)


    # changing QPushButton clickable status when StackedWidget index changed 
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icons_only_widget.findChildren(QPushButton) + self.ui.full_menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(True)
            else:
                btn.setAutoExclusive(True)

    
    # function for changing menu page

    def on_system_infos_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    def on_system_infos_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)


    def on_activity_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)


    def on_activity_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)


    def on_disks_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)


    def on_disks_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)


    def on_cpu_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)


    def on_cpu_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)


    def on_network_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)


    def on_network_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)



    def on_about_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)


    def on_about_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(7)

     


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # loading style file
    # with open("./style.qss", "r") as style_file:
    #     style_str = style_file.read()
    # app.setStyleSheet(style_str)

    # load style 2
    style_file = QFile("style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
