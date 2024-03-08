
# This Python file uses the following encoding: utf-8
import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QSpacerItem, QSizePolicy, QButtonGroup

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


def populate_json_file(json_name, json_data):
    new_dict = {}

    with open('lists.json') as json_file:
        data = json.load(json_file)
        data.update({json_name: json_data})
        new_dict.update(data)
    with open('lists.json', 'w') as json_file:
        json.dump(new_dict, json_file)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.params = ["Id", "Type", "Name", "Regular price", "Parent"]
        self.header_row = []
        self.first_row = []
        self.json_list = {}
        self.display_json_list = {}
        self.button_group = QButtonGroup()
        self.button_group.buttonClicked.connect(self.add_json_list)

        self.ui.customer_review.clicked.connect(self.toggle_review)
        self.ui.in_stock.clicked.connect(self.toggle_stock)
        self.ui.visible.clicked.connect(self.toggle_visible)
        self.ui.published.clicked.connect(self.toggle_published)
        self.ui.create_list.clicked.connect(self.create_new_list)

        self.populate_json_list()

    def populate_json_list(self):
        try:
            with open('lists.json') as json_file:
                if json_file:
                    self.json_list = json.load(json_file)
                    self.create_list_checkboxes(self.json_list.keys())
        except Exception as ex:
            print(ex)

    def update_showm_json_list(self, display_list):
        self.ui.json_list.clear()
        for key, value in zip(display_list.keys(), display_list.values()):
            self.ui.json_list.append(f"{key}: {value}")

    def add_json_list(self, btn):
        if btn.text() in self.display_json_list.keys():
            self.display_json_list.pop(btn.text())
        else:
            self.display_json_list.update({btn.text(): self.json_list[btn.text()]})

        self.update_showm_json_list(self.display_json_list)

    def create_list_checkboxes(self, values):
        for value in values:
            button = QPushButton(value)
            self.ui.scrollAreaWidgetContents.layout().addWidget(button)
            self.button_group.addButton(button)

        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.scrollAreaWidgetContents.layout().addItem(vertical_spacer)

    def create_new_list(self):
        # ToDo: Look at the text box, grab each line and put it into a dict
        # Check if the user forgot to enter values into the the title bar or the text box
        if not self.ui.list_name.text():
            msg_box = QMessageBox.critical(self, "Missing Information", "You forgot to give the list a name")
            return
        if not self.ui.list_box.toPlainText():
            msg_box = QMessageBox.critical(self, "Missing Information", "You left the text box empty")
            return

        new_list = {}
        # Take each line in the text box and split it on the ":". Then add it to the dictinary
        for line in self.ui.list_box.toPlainText().splitlines():
            values = line.split(":")
            new_list.update({values[0]: values[1]})

        populate_json_file(self.ui.list_name.text(), new_list)



    def convert_list_to_tuple(self):
        # ToDO: When the user presses create list turn the three lists into tuples
        pass

    def toggle_published(self):
        if self.ui.published.isChecked():
            self.params.append('Published')
        if not self.ui.published.isChecked():
            self.params.remove('Published')
        print(self.params)

    def toggle_visible(self):
        if self.ui.visible.isChecked():
            self.params.append('Visible')
        if not self.ui.visible.isChecked():
            self.params.remove('Visible')

        print(self.params)

    def toggle_stock(self):
        if self.ui.in_stock.isChecked():
            self.params.append('In Stock?')
        if not self.ui.in_stock.isChecked():
            self.params.remove('In Stock?')
        print(self.params)

    def toggle_review(self):
        if self.ui.customer_review.isChecked():
            self.params.append("Allow customer review")
        if not self.ui.customer_review.isChecked():
            self.params.remove("Allow customer review")

        print(self.params)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
