#from functions.get_files_info import get_files_info
from functions.run_python_file import *


def test():
    
   
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)

if __name__ == "__main__":
    test()
