import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class FileMergerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Alerzo Excel and CSV File Merger by Data team')
        self.setGeometry(300, 300, 500, 200)
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            #mergeButton {
                background-color: #28a745;
                font-weight: bold;
            }
            #mergeButton:hover {
                background-color: #218838;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        title_label = QLabel('Excel and CSV File Merger')
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #333; margin-bottom: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Path input
        path_layout = QHBoxLayout()
        path_label = QLabel('Enter the path to merge files:')
        self.path_input = QLineEdit()
        browse_button = QPushButton('Browse')
        browse_button.clicked.connect(self.browse_folder)
        path_layout.addWidget(path_label)
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(browse_button)

        # Merge button
        merge_button = QPushButton('Merge Files')
        merge_button.setObjectName("mergeButton")
        merge_button.clicked.connect(self.merge_files)

        main_layout.addLayout(path_layout)
        main_layout.addWidget(merge_button)

        self.setLayout(main_layout)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder:
            self.path_input.setText(folder)

    def merge_files(self):
        path = self.path_input.text()
        if not path:
            QMessageBox.warning(self, 'Error', 'Please enter a valid path')
            return

        try:
            merged_df = self.append_files(path)
            if merged_df is not None:
                output_path, _ = QFileDialog.getSaveFileName(self, 'Save Merged File', '', 'Excel files (*.xlsx);;CSV files (*.csv)')
                if output_path:
                    if output_path.endswith('.xlsx'):
                        merged_df.to_excel(output_path, index=False)
                    elif output_path.endswith('.csv'):
                        merged_df.to_csv(output_path, index=False)
                    QMessageBox.information(self, 'Success', f'Files merged successfully. Output saved to {output_path}')
            else:
                QMessageBox.warning(self, 'Warning', 'No Excel or CSV files found in the specified path')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An error occurred: {str(e)}')

    def append_files(self, path):
        frames = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                _, file_extension = os.path.splitext(file_path)
                
                if file_extension.lower() == '.xlsx':
                    df = pd.read_excel(file_path)
                elif file_extension.lower() == '.csv':
                    df = pd.read_csv(file_path)
                else:
                    continue
                
                frames.append(df)
        
        if frames:
            return pd.concat(frames, axis=0, ignore_index=True)
        else:
            return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileMergerApp()
    ex.show()
    sys.exit(app.exec_())