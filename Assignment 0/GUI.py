import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import encrypt


class Window(QMainWindow, QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(450, 450, 800, 520)
        self.setWindowTitle('Encrypt-Decrypt-0')
        self.setWindowIcon(QIcon('./Assets/NS.png'))
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.exit_text = 'Exited Application'
        self.file_open_button = None
        self.quit_button = None
        self.textbox_input = None
        self.textbox_output = None
        self.output_label = None
        self.input_label = None
        self.file_text = None
        self.my_output = None
        self.my_text = None
        self.encrypt_button = None
        self.n = None
        self.default_font = QFont("Arial", 14)
        self.num_lines = None
        self.language = None
        self.sent_num = None
        self.warning_text_1 = 'some unexpected error'

        self.init_ui()

    # main function containing all the buttons and other elements to display
    def init_ui(self):
        # The exit button on the right bottom corner
        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.exit_application)
        self.quit_button.resize(self.quit_button.minimumSizeHint())

        # The encrypt button on the left bottom corner
        self.encrypt_button = QPushButton('Encrypt', self)
        self.encrypt_button.clicked.connect(self.translate_gui)
        self.encrypt_button.resize(self.encrypt_button.sizeHint())


        self.decrypt_button = QPushButton('Decrypt', self)
        self.decrypt_button.clicked.connect(self.decrypt_gui)
        self.decrypt_button.resize(self.decrypt_button.sizeHint())

        # Left Textbox element used to input the text to be encryptd --- Editable
        self.textbox_input = QPlainTextEdit(self)
        self.textbox_input.setFont(self.default_font)

        # Right Textbox element used to display the output of the encryptd text --- Not Editable (incomplete)
        self.textbox_output = QPlainTextEdit(self)
        self.textbox_output.setFont(self.default_font)
        # self.textbox_output.setReadOnly(True)

        # Left Textbox heading label
        self.input_label = QLabel(self, text='Input Text')
        new_font = QFont("Arial", 16, QFont.Bold)
        self.input_label.setFont(new_font)
        self.input_label.adjustSize()
        self.input_label.setAlignment(Qt.AlignCenter)

        # Right Textbox heading label
        self.output_label = QLabel(self, text='Output Text')
        new_font = QFont("Arial", 16, QFont.Bold)
        self.output_label.setFont(new_font)
        self.output_label.adjustSize()
        self.output_label.setAlignment(Qt.AlignCenter)

        # Font for the label stating the number of lines to encrypt to
        # self.num_lines = QLabel(self, text='Language:')
        # new_font = QFont("Arial", 10)
        # self.num_lines.setFont(new_font)

        # Setting the logo or picture in the middle
        pixmap = QPixmap(os.getcwd() + "./Assets/NS.png").scaled(250, 250, Qt.KeepAspectRatio)
        pic = QLabel(self)
        pic.setPixmap(pixmap)
        pic.setAlignment(Qt.AlignCenter)

        # The layout for proper padding of the button
        encrypt_pad_layout = QHBoxLayout()
        encrypt_pad_layout.addStretch()
        encrypt_pad_layout.addWidget(self.encrypt_button)
        encrypt_pad_layout.addStretch()

        # The layout for proper padding of the button
        decrypt_button_layout = QHBoxLayout()
        decrypt_button_layout.addStretch()
        decrypt_button_layout.addWidget(self.decrypt_button)
        decrypt_button_layout.addStretch()


        # Middle layout of the grid
        middle_layout = QVBoxLayout()
        middle_layout.addWidget(pic)
        middle_layout.addLayout(encrypt_pad_layout)
        middle_layout.addLayout(decrypt_button_layout)
        # middle_layout.addLayout(line_num_input_layout)

        # The main Grid Layout
        main_grid_layout = QGridLayout()
        main_grid_layout.addWidget(self.input_label, 0, 0)
        main_grid_layout.addWidget(self.output_label, 0, 2)
        main_grid_layout.addLayout(middle_layout, 1, 1)
        main_grid_layout.addWidget(self.textbox_input, 1, 0)
        main_grid_layout.addWidget(self.textbox_output, 1, 2)
        # main_grid_layout.addWidget(self.file_open_button, 2, 0, alignment=Qt.AlignLeft)
        main_grid_layout.addWidget(self.quit_button, 2, 2, alignment=Qt.AlignRight)


        # Exit menu
        menu_exit = QAction("&Exit", self)
        menu_exit.setShortcut("Ctrl+Q")
        menu_exit.setStatusTip('Exit the program')
        menu_exit.triggered.connect(self.exit_application)

        self.statusBar()

        # The File menu option
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        # file_menu.addAction(menu_open_file)
        # file_menu.addAction(menu_save_file)
        file_menu.addAction(menu_exit)

        # The Edit menu option
        main_menu = self.menuBar()
        # file_menu = main_menu.addMenu('&Edit')
        # file_menu.addAction(font_choice_input)
        # file_menu.addAction(font_choice_output)

        self.wid.setLayout(main_grid_layout)
        self.show()


    # Takes the input from the left textbox, encrypt that and display on the right text box
    def translate_gui(self):
        # noinspection PyBroadException
        try:
            # self.lang = self.language.text()
            self.my_text = self.textbox_input.toPlainText()
            self.my_output = encrypt.solution(self.my_text)
            self.textbox_output.setPlainText(self.my_output)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Error!', 'You have to input the text in the input textbox!\n'
                                                'You have to input a number in the number box!',
                                QMessageBox.Ok)
    def decrypt_gui(self):
        # noinspection PyBroadException
        try:
            # self.lang = self.language.text()
            self.my_text = self.textbox_output.toPlainText()
            self.my_output = encrypt.solution(self.my_text)
            self.textbox_input.setPlainText(self.my_output)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, 'Error!', 'You have to input the text in the input textbox!\n'
                                                'You have to input a number in the number box!',
                                QMessageBox.Ok)

    # Exit Definition. Runs when the app is Quit using the 'Quit' button
    def exit_application(self):
        print(self.exit_text)
        sys.exit()

    # Reserve function for the selection box to have option to chose number of lines (unused)
    def selection_box(self):
        print('Inside selection_box')
        combo_box = QComboBox(self)
        for i in range(self.sent_num):
            item_text = str(i + 1) + ' Lines'
            combo_box.addItem(item_text)
        combo_box.move(365, 300)
        qApp.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Window()
    # GUI.show()
    sys.exit(app.exec_())
