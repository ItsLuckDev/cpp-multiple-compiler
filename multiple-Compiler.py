import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama to support colors even on Windows
init(autoreset=True)

def compile_and_cleanup_cpp_files():
    # Get the list of files in the current directory
    files_in_directory = os.listdir('.')
    
    # List to keep track of compiled files
    compiled_files = []

    # Iterate through all files in the directory
    for file_name in files_in_directory:
        # Check if the file has a .cpp extension
        if file_name.endswith('.cpp'):
            # Construct the name of the compiled file
            compiled_file_name = 'compiled_' + os.path.splitext(file_name)[0] + '.exe'

            # g++ command to execute
            command = f"g++ -Wall -std=c++14 {file_name} -o {compiled_file_name}"
            print(f"{Fore.YELLOW}Compiling file: {file_name}")

            # Execute the command using subprocess
            try:
                subprocess.run(command, shell=True, check=True)
                print(f"{Fore.GREEN}Successfully compiled: {compiled_file_name}")
                # Add the compiled file to the list
                compiled_files.append(compiled_file_name)
            except subprocess.CalledProcessError as e:
                print(f"{Fore.MAGENTA}Error compiling file {file_name}: {e}")

    # Delete the compiled files after compilation
    for compiled_file in compiled_files:
        try:
            os.remove(compiled_file)
            print(f"Compiled file deleted: {compiled_file}")
        except OSError as e:
            print(f"{Fore.RED}Error deleting file {compiled_file}: {e}")

if __name__ == "__main__":
    compile_and_cleanup_cpp_files()