"""
Exercise 2
Create a program called tree.py

Given a file path (absolute or relative), the program should write to a file all of the contents of the directory and the child directories bellow it. The output file should look something like this:

./file1.py
./file2.py
./dir1/file1_in_dir1.txt
./dir1/file2_in_dir1.txt
./dir3/file1_in_dir3.txt
/Users/madhavirockandla/PythonLabs/Python8Ex/
"""

import os
path = '/Users/madhavirockandla/Python8Ex/'
for dir_path, dir_names, file_names in os.walk(path):
    for file_name in file_names:
        print(os.path.join(dir_path, file_name))
        


