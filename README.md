# Setup Instructions for Windows Local Environment

1. Install Python:
   - Download and install Python from the official website: https://www.python.org/downloads/windows/
   - During installation, make sure to check the box that says "Add Python to PATH"

2. Install required Python packages:
   - Open Command Prompt
   - Run the following commands:
     ```
     pip install pandas openpyxl
     ```

3. Create a project folder:
   - Create a new folder for your project, e.g., `C:\FilesMerger`

4. Create the necessary files:
   - In the project folder, create two files:
     - `index.html`: Copy the HTML content provided earlier into this file
     - `server.py`: Copy the Python script provided earlier into this file

5. Run the server:
   - Open Command Prompt
   - Navigate to your project folder:
     ```
     cd C:\FilesMerger
     ```
   - Run the Python script:
     ```
     python server.py
     ```
   - You should see a message saying "Server running on http://localhost:8000"

6. Access the web interface:
   - Open a web browser
   - Go to `http://localhost:8000`
   - You should now see the file merger interface

7. Use the application:
   - Enter the full path to the directory containing your Excel and CSV files
   - Click "Merge Files"
   - The merged file will be saved in the same directory as your input files, named "merged_files.xlsx"

Note: Make sure to keep the Command Prompt window open while using the application. Closing it will stop the server.

### Desktop app
# Excel and CSV File Merger

This desktop application provides a simple and user-friendly interface for merging multiple Excel (.xlsx) and CSV files from a specified directory into a single file.

## Features

- Graphical user interface for easy interaction
- Ability to browse and select a directory containing files to merge
- Merges all Excel (.xlsx) and CSV files found in the selected directory
- Option to save the merged file as either Excel (.xlsx) or CSV
- Error handling and user feedback through message boxes

## Tech Stack

- **Python 3.7+**: The core programming language used for the application logic
- **PyQt5**: Used for creating the graphical user interface
- **pandas**: Used for reading, processing, and writing Excel and CSV files
- **openpyxl**: Required by pandas for Excel file support

## Installation

1. Ensure you have Python 3.7 or newer installed on your system.

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/excel-csv-file-merger.git
   cd excel-csv-file-merger
   ```

3. Install the required dependencies:
   ```
   pip install PyQt5 pandas openpyxl
   ```

## Usage

1. Run the application:
   ```
   python file_merger_app.py
   ```

2. The application window will appear.

3. Enter the path to the directory containing the Excel and CSV files you want to merge, or use the "Browse" button to select the directory.

4. Click the "Merge Files" button.

5. If files are found and successfully merged, you'll be prompted to choose a location and format (Excel or CSV) to save the merged file.

6. A success message will appear with the path to your merged file.

## Building a Standalone Executable

To create a standalone executable that can be run on a Windows system without Python installed:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Create the executable:
   ```
   pyinstaller --onefile --windowed --icon=icon.ico file_merger_app.py
   ```

3. The executable will be created in the `dist` folder.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

