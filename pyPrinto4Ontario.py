# pyPrinto4Ontario.py
# Description: List all files in a directory and save the list to a text file.

import os
import sys
import datetime

def list_files_in_directory(directory_path, output_file, script_name, limit_file_types, allowed_extensions):
    """
    List all files in a directory and save the list to a text file.
    :param directory_path: str: The directory path to scan for files
    :param output_file: str: The output file path to save the list of files
    :param script_name: str: The name of the script generating the file list
    :param limit_file_types: bool: Limit the file types to specific extensions
    :param allowed_extensions: list: List of file extensions to include in the list
    :return: None
    """
    # Get the total number of files for progress calculation
    total_files = sum([len(files) for _, _, files in os.walk(directory_path)])

    # Initialize counters for processed and matched files
    processed_files = 0
    matched_files = 0
    file_number_width = len(str(total_files))  # Determine the width for file numbering

    with open(output_file, 'w', encoding='utf-8') as file:
        # Write the title and prompts at the top of the file
        file.write(f"Generated by: {script_name}\n")
        file.write(f"Directory Path: {directory_path}\n")
        file.write(f"Limit File Types: {'Yes' if limit_file_types else 'No'}\n")
        if limit_file_types:
            file.write(f"File Types Limited to: {', '.join(allowed_extensions)}\n")
        file.write(f"Total Files Reviewed: {total_files}\n")
        file.write(f"Files Matching Criteria: {matched_files}\n")
        file.write(f"Output Directory: {output_file}\n")
        file.write(f"Output Filename: {os.path.basename(output_file)}\n")
        file.write(f"\n{'File No.':<{file_number_width}} | File Name | Creation Date | Modification Date | File Path\n")
        file.write("-" * (file_number_width + 80) + "\n")
        
        # Variables to control the frequency of progress updates
        last_progress_update = -1
        update_frequency = 1  # update progress every 1% of completion

        for root, dirs, files in os.walk(directory_path):
            for name in files:
                # Increment the total processed files counter
                processed_files += 1
                full_path = os.path.join(root, name)
                # Check file extension if limiting is enabled
                if not limit_file_types or os.path.splitext(name)[1].lower() in allowed_extensions:
                    matched_files += 1
                    try:
                        creation_date = datetime.datetime.fromtimestamp(os.path.getctime(full_path)).strftime('%Y-%m-%d %H:%M:%S')
                        modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(full_path)).strftime('%Y-%m-%d %H:%M:%S')
                    except FileNotFoundError:
                        creation_date = "N/A"
                        modification_date = "N/A"
                    except Exception as e:
                        creation_date = "Error"
                        modification_date = "Error"

                    file_number = str(matched_files).zfill(file_number_width)
                    file.write(f"{file_number} | {name} | {creation_date} | {modification_date} | {full_path}\n")

                # Calculate progress based on all files processed
                progress = (processed_files / total_files) * 100

                # Update the progress bar if the percentage has increased significantly
                if int(progress) > last_progress_update:
                    last_progress_update = int(progress)
                    # Clear the line and print the progress
                    clear_length = 80
                    sys.stdout.write('\r' + ' ' * clear_length + '\r')  # Clear the line
                    output_line = f"Progress: [{int(progress)}%] Processed {processed_files}/{total_files} files."
                    sys.stdout.write(output_line)
                    sys.stdout.flush()

    # Update the file with the final count of matched files
    with open(output_file, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        lines[5] = f"Files Matching Criteria: {matched_files}\n"
        file.seek(0)
        file.writelines(lines)

    print(f"\n\nFile list saved to {output_file}")
    print(f"Total files reviewed: {total_files}")
    print(f"Files matching criteria: {matched_files}")

if __name__ == "__main__":
    # Get current date and time for the default output filename
    current_datetime = datetime.datetime.now()
    date_str = current_datetime.strftime("%Y%m%d_%H%M")

    # Script name
    script_name = "List-Files-In-Directory-using-Python.py"

    # Ask the user for the directory to scan and the output file location
    directory_path = input(f"Enter the directory path to list files (default is C:\\): ") or "C:\\"
    
    # Define the default output directory within the current working directory
    default_output_directory = os.path.join(os.getcwd(), "outputs")
    
    # Create the 'outputs' directory if it doesn't exist
    if not os.path.exists(default_output_directory):
        os.makedirs(default_output_directory)
    
    # Get the output directory from the user or use the default
    output_directory = input(f"Enter the output directory for the text file (default is {default_output_directory}): ") or default_output_directory
    
    default_filename = f"file_list_{date_str}.txt"
    output_filename = input(f"Enter the output filename (default is {default_filename}): ") or default_filename

    # Ask the user if they want to limit the file types reported
    limit_file_types_input = input("Limit the file types reported to .txt, .doc, .pdf, .xls, .xlsx, .ppt, and .one? (default is Yes) [Yes/No]: ") or "Yes"
    limit_file_types = limit_file_types_input.lower() in ['yes', 'y', '']
    allowed_extensions = ['.txt', '.doc', '.pdf', '.xls', '.xlsx', '.ppt', '.one']

    # Inform the user about the file type limitation
    if limit_file_types:
        print(f"\nNote: The report will be limited to the following file types: {', '.join(allowed_extensions)}.\n")
    else:
        print("\nNote: The report will include all file types.\n")

    # Warning message about the file counting process
    print("Note: The program will now determine the total number of files to process and provide updates on its progress as it goes.\n"
          "In this context, 'processing' involves reading each file's name and directory path, then saving this information to a text file "
          f"({output_filename}) upon completion.\n"
          "Press [Ctrl+C] at any time to stop the program. The program will begin shortly...\n\n"
          "Please use this time to stand up, stretch and enjoy your humanity.\n")

    # Define the output file path
    output_file = os.path.join(output_directory, output_filename)

    # Call the function to list files
    list_files_in_directory(directory_path, output_file, script_name, limit_file_types, allowed_extensions)
