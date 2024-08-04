
# pyPrinto4Ontario

## Overview

The `pyPrinto4Ontario` project is a Python-based tool designed to list files within a specified directory and output the results to a text file. Additionally, it includes a feature that provides positive affirmations to users, creating a pleasant and encouraging experience. The project consists of multiple scripts:

1. **`__init__.py`:** The main entry point of the project, which orchestrates the execution of other components and manages user interactions.
2. **`pyPrinto4Ontario.py`:** Contains the core functionality for listing files and generating the output report.
3. **`positive_affirmations.py`:** A module containing a list of positive affirmations.

## Installation and Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/pyPrinto4Ontario.git
   cd pyPrinto4Ontario
   ```

2. **Ensure you have Python installed:** The project requires Python 3.x.

3. **Run the Main Program:**
   Execute the program by running the `__init__.py` script:
   ```sh
   python -m pyPrinto4Ontario
   ```

## Components

### 1. `__init__.py`

This script serves as the main entry point for the `pyPrinto4Ontario` program. It includes:

- **Welcome Message:** Greets the user upon starting the program.
- **Execution of Core Script:** Calls `pyPrinto4Ontario.py` to perform the file listing.
- **User Interaction:** Prompts the user to either run the program again or exit.
- **Positive Affirmations:** If the user chooses to exit, the script displays a countdown alongside randomly selected positive affirmations.

### 2. `pyPrinto4Ontario.py`

This script is responsible for:

- **Directory Scanning:** Recursively scans a specified directory to list all files.
- **File Type Limitation:** Optionally limits the output to specific file types such as `.txt`, `.doc`, `.pdf`, etc.
- **Output File Generation:** Saves the list of files, along with details such as file name, creation date, modification date, and file path, to a text file.
- **Progress Display:** Shows a progress bar indicating the percentage of files processed.

### 3. `positive_affirmations.py`

A simple module that contains a list of positive affirmations. These affirmations are displayed to users when they choose to exit the program, providing an uplifting and positive experience.

## How to Use

1. **Start the Program:**
   Run the `__init__.py` script, which will welcome you and initiate the file listing process.

2. **Enter Directory and Output Information:**
   You will be prompted to provide:
   - The directory path to scan for files.
   - The output directory and filename for the results.
   - Whether to limit the file types reported.

3. **View Progress:**
   The program will display a progress bar indicating the percentage of files processed.

4. **Choose to Run Again or Exit:**
   After the initial run, you can choose to run the program again or exit. If you choose to exit, the program will display a series of positive affirmations along with a countdown.

## Example Usage

```sh
$ python -m pyPrinto4Ontario
Welcome to pyPrinto4Ontario!

Enter the directory path to list files (default is C:\): C:\ExamplePath
Enter the output directory for the text file (default is C:\path	o\pyPrinto4Ontario\outputs): 
Enter the output filename (default is file_list_YYYYMMDD_HHMM.txt): file_list.txt
Limit the file types reported to .txt, .doc, .pdf, .xls, .xlsx, .ppt, and .one? (default is Yes) [Yes/No]: Yes

Note: The report will be limited to the following file types: .txt, .doc, .pdf, .xls, .xlsx, .ppt, .one.

Note: The program will now determine the total number of files to process and provide updates on its progress as it goes.
In this context, 'processing' involves reading each file's name and directory path, then saving this information to a text file (file_list.txt) upon completion.

Press [Ctrl+C] at any time to stop the program. The program will begin shortly...

Please use this time to stand up, stretch and enjoy your humanity.

Progress: [25%] Processed 2500/10000 files.
...
Progress: [100%] Processed 10000/10000 files.

File list saved to C:\path\to\pyPrinto4Ontario\outputs\file_list.txt
Total files reviewed: 10000
Files matching criteria: 8500

Press Enter to run the program again or type 'exit' to exit: exit
Thank you for using pyPrinto4Ontario! You're super awesome!
Goodbye in 5 seconds... You have a remarkable sense of curiosity!
Goodbye in 4 seconds... You are thoughtful and considerate!
Goodbye in 3 seconds... Your passion for learning is inspiring!
Goodbye in 2 seconds... You are resilient and strong!
Goodbye in 1 second... Your determination is impressive!
Goodbye!
```

## Contribution

Contributions are welcome! Feel free to submit issues or pull requests to improve the functionality and user experience of this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
