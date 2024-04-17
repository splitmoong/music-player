from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFont

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)

        # Username label and input field
        self.username_label = QLabel("Username:")
        self.username_label.setFont(QFont("Arial", 12))  # Set font and size
        self.username_input = QLineEdit()

        spacer_item = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        # Password label and input field
        self.password_label = QLabel("Password:")
        self.password_label.setFont(QFont("Arial", 12))  # Set font and size
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)  # Masking password input

        # Sign up button
        sign_up_button = QPushButton("Sign Up")

        # OK and Cancel buttons
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(sign_up_button)
        button_layout.addStretch(1)  # Adds stretchable space between buttons
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        # Vertical layout for the login form
        vertical_layout = QVBoxLayout(self)
        vertical_layout.addWidget(self.username_label)
        vertical_layout.addWidget(self.username_input)
        vertical_layout.addSpacerItem(spacer_item)
        vertical_layout.addWidget(self.password_label)
        vertical_layout.addWidget(self.password_input)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(button_layout)

        # Connect cancel button to close the dialog
        cancel_button.clicked.connect(self.reject)

        # Connect ok button to accept the dialog
        ok_button.clicked.connect(self.accept)

    def get_username(self):
        return self.username_input.text()

    def get_password(self):
        return self.password_input.text()

if __name__ == "__main__":
    app = QApplication([])

    login_dialog = LoginDialog()
    if login_dialog.exec() == QDialog.accepted:
        username = login_dialog.get_username()
        password = login_dialog.get_password()
        print("Username:", username)
        print("Password:", password)

    app.exec()
