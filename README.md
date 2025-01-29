# Position Log Extractor

## Overview
Position Log Extractor is a Python-based GUI application that allows users to extract distinct initials from position log PDFs. The extracted initials are saved as a CSV file in the user's Downloads folder.

## Features
- **Select multiple PDF files**: Users can choose multiple PDFs for processing.
- **Extract initials**: Automatically extracts distinct initials from the logs.
- **Save to CSV**: Saves the extracted initials in a CSV file in the Downloads folder.
- **User-friendly GUI**: Simple and intuitive interface using Tkinter.
- **Automated file opening**: Opens the output file upon completion.

## Requirements
- Python 3.x
- Required Python packages:
  - `pdfplumber`
  - `pandas`
  - `tkinter`

Install dependencies using:
```sh
pip install pdfplumber pandas
```

## Usage
### Running the Application
To start the application, run:
```sh
python main.py
```

### Extracting Data
1. Click **Select PDFs** to choose one or more PDF files.
2. Click **Extract** to process the files.
3. The distinct initials will be extracted and saved as `Distinct_Initials_Combined_{DATE-HERE}.csv`, with the extracted date appended, in your **Downloads** folder.
4. A pop-up notification will appear with a link to the file.

## Creating an Executable
To create a standalone executable using `pyinstaller`, run:
```sh
pyinstaller --onefile --windowed extractor.spec
```
The executable will be found in the `dist` folder.

## License
This project is open-source and free to use under the MIT License.

## Author
Developed by Blake Bradford

