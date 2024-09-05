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
