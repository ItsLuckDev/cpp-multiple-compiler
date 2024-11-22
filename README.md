Sure! Here is a README file in both English and Italian versions.

---

**README.md (English)**

# C++ Batch Compiler Script

This Python script is designed to automate the process of compiling all `.cpp` files in the current directory using `g++`. It also cleans up the compiled `.exe` files after execution, which is useful for situations where you just want to verify if the compilation is successful, without keeping the executables.

## Features

- **Batch Compilation**: Automatically detects and compiles all `.cpp` files in the current directory.
- **Cross-Platform Colors**: Uses `colorama` to provide colored output for better readability, compatible with both Windows and Unix-like systems.
- **Automatic Cleanup**: After compiling, deletes the generated executable files.

## Requirements

- Python 3
- `g++` (GNU Compiler Collection) installed and accessible via command line
- Python library `colorama`

You can install `colorama` using the following command:

```sh
pip install colorama
```

## How to Use

1. Make sure you have Python 3 and `g++` installed on your system.
2. Place this script in the directory where your `.cpp` files are located.
3. Run the script using Python:

   ```sh
   python compile_and_cleanup.py
   ```

The script will:

- Detect all `.cpp` files in the directory.
- Attempt to compile each file using the `g++` command.
- Print colored output to indicate success or failure.
- Delete the generated `.exe` files after compilation.

## Example Output

- Files that compile successfully are shown in **green**.
- Errors during compilation are shown in **magenta**.
- File deletions are reported after successful compilation.

## Notes

- This script uses `g++` with flags `-Wall` and `-std=c++14` for compilation, which enables all warnings and enforces C++14 standard respectively.
- The script is useful for testing purposes to ensure all `.cpp` files are error-free.

---
