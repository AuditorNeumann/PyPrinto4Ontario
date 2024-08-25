import os
import time
import random
from positive_affirmations import positive_affirmations

def main():
    """
    The main function that welcomes the user, explains the program, and calls the pyPrinto4Ontario.py script.
    """
    print_title()
    print("Welcome to pyPrinto4Ontario!")
    print("\nThis program allows you to list all files within a specified directory and save the results to a text file.")
    print("You can also limit the results to specific file types, and the program will provide progress updates as it scans the files.")
    print("At the end, you can choose to run the program again or exit with some positive affirmations!\n")
    print("Remember you can press CTRL+C to close this program at anytime!\n\n")
    print("Now let's begin!\n")

    
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    
    # Construct the full path to pyPrinto4Ontario.py
    script_path = os.path.join(script_dir, "pyPrinto4Ontario.py")
    
    # Ensure that the current working directory is the script's directory
    os.chdir(script_dir)
    
    # Execute the pyPrinto4Ontario.py script
    os.system(f"python \"{script_path}\"")
    try_again()

def print_title():
    """
    Prints a stylized title for the program.
    """
    title = """
    ######################################
    #                                    #
    #        pyPrinto4Ontario            #
    #                                    #
    ######################################
    """
    print(title)

def try_again():
    """
    Prompts the user to run the program again or exit. If the user chooses to exit,
    prints 5 random positive affirmations and counts down before exiting.
    """
    choice = input("Press Enter to run the program again or type 'exit' to exit: ")
    if choice.lower() == "exit":
        print("Thank you for using pyPrinto4Ontario! You're super awesome!")
        
        # Randomly select 5 positive affirmations
        selected_affirmations = random.sample(positive_affirmations, 5)
        
        for i in range(5, 0, -1):
            # Print goodbye message and affirmation on the same line
            print(f"Goodbye in {i} seconds... {selected_affirmations[5 - i]}")
            time.sleep(1)
        
        print("Goodbye!")
        exit()
    else:
        main()

if __name__ == "__main__":
    main()
