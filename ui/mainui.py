from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFont

class MainDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)




if __name__ == "__main__":
    app = QApplication([])

    login_dialog = MainDialog()
    if login_dialog.exec() == QDialog.accepted:
        username = login_dialog.get_username()
        password = login_dialog.get_password()
        print("Username:", username)
        print("Password:", password)

    app.exec()