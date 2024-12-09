# IgExtractor

IgExtractor is a Python tool that helps you analyze your Instagram connections by extracting and processing data from a ZIP file containing your Instagram data. It identifies users who don't follow you back and users you don't follow back. Additionally, it can extract and rename media files from your Instagram data.

## Features

- Extract JSON files from the Instagram data ZIP file.
- Process the JSON files to identify followers and following.
- Generate lists of users who don't follow you back and users you don't follow back.
- Save the results to text files.
- Extract and rename media files (pictures, videos) from the Instagram data ZIP file.

## Requirements

- Python 3.x (for building the executable)
- `PyQt5` module (for building the executable)
- `zipfile` module
- `os` module
- `json` module
- `shutil` module

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/DvidMakesThings/IgExtractor.git
    cd IgExtractor
    ```

## Usage

## How to Request and Download Your Instagram Data ZIP File

To use IgExtractor, you need to obtain a ZIP file containing your Instagram data. Follow these steps to request and download your data from Instagram:

1. **Log in to Instagram**:
    - Open your web browser and go to [Instagram](https://www.instagram.com/).
    - Log in to your Instagram account.

2. **Go to Your Account Settings**:
    - Click on your profile picture in the top right corner to go to your profile.
    - Click on the gear icon (⚙️) or the three horizontal lines (☰) to open the settings menu.
    - Select "Settings" from the dropdown menu.

3. **Request Your Data**:
    - In the settings menu, click on "Privacy and Security".
    - Scroll down to the "Data Download" section.
    - Click on "Request Download".

4. **Choose Your Data Format**:
    - Instagram will ask you to choose the format in which you want to receive your data. Select "JSON" as the format.
    - Enter your email address if it is not already filled in.
    - Click "Next".

5. **Enter Your Password**:
    - Instagram will prompt you to enter your account password for security reasons.
    - Enter your password and click "Request Download".

6. **Wait for the Email**:
    - Instagram will process your request and send you an email with a link to download your data. This may take some time, depending on the size of your data and Instagram's processing time.

7. **Download Your Data**:
    - Once you receive the email from Instagram, open it and click on the "Download Data" button.
    - You will be redirected to Instagram and prompted to log in again.
    - After logging in, you will be able to download the ZIP file containing your Instagram data.

8. **Save the ZIP File**:
    - Save the downloaded ZIP file to a convenient location on your computer.


### Running the Application

1. Place your Instagram data ZIP file in a convenient location on your system.

2. Run the `IgExtractor.exe` file to start the IgExtractor application:
    - On Windows, you can double-click the `IgExtractor.exe` file to run it.
    - Alternatively, you can run it from the command prompt:
    ```sh
    ./dist/IgExtractor.exe
    ```
3. Or alternatively run the `main.py` script to start the IgExtractor application:
    ```sh
    python main.py
    ```

### Using the Application

1. **Select ZIP File**:
    - Drag and drop your Instagram data ZIP file into the designated area in the application window, or click on the area to browse and select the file.

2. **Process ZIP File**:
    - Click the "Process ZIP" button to analyze your Instagram connections.
    - The application will extract and process the JSON files from the ZIP file to identify followers and following.
    - The results will be displayed in the application window, showing the count of followers and following, as well as lists of users who don't follow you back and users you don't follow back.

3. **Save Results**:
    - If the "Autosave results" checkbox is checked, the results will be automatically saved to text files in the directory where the application is running.
    - If the checkbox is unchecked, you can manually save the results by clicking the "Save As..." button and choosing a location to save the text files.

4. **Extract Media**:
    - Click the "Extract media" button to extract and rename media files (pictures, videos) from the Instagram data ZIP file.
    - The media files will be extracted to a new "media" folder in the directory where the application is running.
    - A message box will inform you when the extraction is complete.


## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- **Email:** s.dvid@hotmail.com
- **GitHub:** [DvidMakesThings](https://github.com/DvidMakesThings)