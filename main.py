import sys
import threading
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication, QLabel
from backend import Chatbot


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Jarvis GPT-3"
        self.setWindowTitle(title)

        self.setStyleSheet("background-color: #760C10;")

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setStyleSheet("background-color: #D7BB2B")
        self.chat_area.setGeometry(10, 10, 680, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 600, 40)
        self.input_field.returnPressed.connect(self.send_input)

        # Add button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(620, 340, 70, 40)
        self.button.clicked.connect(self.send_input)
        self.button.setStyleSheet("background-color: #DA1F28")

        # adding ironman image
        self.label = QLabel(self)
        self.label.setGeometry(300, 400, 100, 100)
        self.pixmap = QPixmap('ironman.png')
        self.label.setPixmap(self.pixmap.scaled(100, 100))

        self.show()

    def send_input(self):
        user_input = self.input_field.text().strip()
        # user input goes to chat area
        self.chat_area.append(f"<p style='color:#FFFFFF'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        # sends user input to get_response() function in backend.py
        # openai answer is returned as response
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #ADD8E6'>Jarvis: {response}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
