"""
create a file and insert text into it
always needed to close the file after opening because it takes memory
the file can be read ONLY once => multiple read will return nothing ==> for that use method seek
seek(0) will move cursor to position 0 aka at the beginning of the file

read works with symbols
seek and tell work with bytes - chinese symbol has represented with 3 bytes in utf-8
"""

my_string = "Hello world\n"
my_string2 = "This is a second line."

# open function will rewrite the file!
# to append something into the file use open with mode="a"
my_file = open("hello_world.txt", mode="w", encoding="utf-8")
my_file.write(my_string)
print(my_file.tell())    # tells length of the file including new line etc | tell the position of the cursor
my_file.close()

my_file = open("hello_world.txt", mode="a")
my_file.write(my_string2)
print(my_file.tell())    # tells length of the file including new line etc | tell the position of the cursor
my_file.close()

my_file = open("hello_world.txt")
print(my_file.read())
my_file.close()

"""
Context manager 'with' - ensure closing open files (it is often forgotten)
os.sep -> define a separator "/" for linux and macOS and backslash for Windows
--> os.path.join -> to create a a path for proper OS 
"""
import os
import pathlib

string3 = "This is a text for context manager section\n"
with open("context_manager.txt", mode="a") as my_file:
    my_file.write(string3)

with open("context_manager.txt", mode="r") as my_file:
    print(my_file.read())
