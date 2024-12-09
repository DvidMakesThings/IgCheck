import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from gui import Ui_Widget  # Import the generated UI class
from instaapi import InstaAPI
from imgExtract import MediaExtractor

class InstaApp(QtWidgets.QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.zip_file_path = None

        self.drop_area.mousePressEvent = self.browse_file
        self.pushButton.clicked.connect(self.process_zip)
        self.save_button.clicked.connect(self.save_as)
        self.checkBox.stateChanged.connect(self.toggle_save_button)
        self.extractmedia.clicked.connect(self.extract_media)

    def browse_file(self, event):
        self.zip_file_path = QFileDialog.getOpenFileName(self, "Select ZIP file", "", "ZIP files (*.zip)")[0]
        if self.zip_file_path:
            self.drop_area.setText(self.zip_file_path)
            self.pushButton.setEnabled(True)
            self.extractmedia.setEnabled(True)

    def process_zip(self):
        if not self.zip_file_path:
            QMessageBox.warning(self, "No file", "Please select a ZIP file first.")
            return

        insta_api = InstaAPI(self.zip_file_path)
        not_following_me_back, i_dont_follow_them_back = insta_api.run()

        self.display_results(insta_api, not_following_me_back, i_dont_follow_them_back)

    def display_results(self, insta_api, not_following_me_back, i_dont_follow_them_back):
        self.output_area.clear()
        self.output_area.addItem(f"Followers count: {len(insta_api.followers)}")
        self.output_area.addItem(f"Following count: {len(insta_api.following)}")

        self.output_area.addItem("\nUsers who don't follow me back:")
        for idx, user in enumerate(sorted(not_following_me_back), start=1):
            self.output_area.addItem(f"{idx}. {user}")

        self.output_area.addItem("\nUsers who I don't follow back:")
        for idx, user in enumerate(sorted(i_dont_follow_them_back), start=1):
            self.output_area.addItem(f"{idx}. {user}")

        if self.checkBox.isChecked():
            self.save_results(not_following_me_back, i_dont_follow_them_back)

    def save_as(self):
        file_path = QFileDialog.getSaveFileName(self, "Save As", "", "Text files (*.txt)")[0]
        if file_path:
            with open(file_path, 'w') as file:
                for i in range(self.output_area.count()):
                    file.write(self.output_area.item(i).text() + '\n')

    def save_results(self, not_following_me_back, i_dont_follow_them_back):
        current_directory = os.getcwd()
        not_following_me_back_path = os.path.join(current_directory, 'not_following_me.txt')
        i_dont_follow_them_back_path = os.path.join(current_directory, 'not_following_byme.txt')

        with open(not_following_me_back_path, 'w') as output_file:
            output_file.write("Users who don't follow me back:\n\n")
            for idx, user in enumerate(sorted(not_following_me_back), start=1):
                output_file.write(f"{idx}. {user}\n")

        with open(i_dont_follow_them_back_path, 'w') as output_file:
            output_file.write("Users who I don't follow back:\n\n")
            for idx, user in enumerate(sorted(i_dont_follow_them_back), start=1):
                output_file.write(f"{idx}. {user}\n")

    def toggle_save_button(self):
        if self.checkBox.isChecked():
            self.save_button.setEnabled(False)
        else:
            self.save_button.setEnabled(True)

    def extract_media(self):
        if not self.zip_file_path:
            QMessageBox.warning(self, "No file", "Please select a ZIP file first.")
            return

        media_extractor = MediaExtractor(self.zip_file_path, img_folder_path=os.path.join(os.getcwd(), 'media'))
        media_extractor.extract_and_rename_media()
        QMessageBox.information(self, "Extraction Complete", "All media files have been extracted and renamed.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = InstaApp()
    window.show()
    sys.exit(app.exec_())