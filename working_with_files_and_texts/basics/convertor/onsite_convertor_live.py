"""
GOAL
load vstupni_data.txt. Create a new file where first column (bytXXXX will be replaced with a corresponding value in
conversion_dict dictionary
"""

import os
from typing import List


conversion_dict = {
    "byt0001": "1+1",
    "byt0002": "2+1",
    "byt0003": "2+kk",
    "byt0004": "3+1",
    "byt0005": "3+kk",
    "byt0006": "4+1",
    "byt0007": "4+kk",
    "byt0008": "5+1"
}


def find_all_text_files(path: str) -> List[str]:
    """
    list comprehension
    find all text files using os.listdir(path) method (returns only name of the files in directory
    using os.path.join(path, file_name) and os.path.sep create absolute path
    function returns absolute path for every single file
    """
    # alternative without using list comprehension
    # file_path = []
    # for file_name in os.listdir():
    #     file_path_candidate = os.path.join(path, file_name)
    #     if os.path.isfile(file_path_candidate) and file_name.endswith(".txt"):
    #         file_path.append(file_path_candidate)

    file_path = [
        os.path.join(path, file_name)   # what we want to the list
        for file_name in os.listdir()
        if os.path.isfile(os.path.join(path, file_name))  and ".txt" if file_name
    ]
    return file_path


def read_text_file(fpath: str) -> List[str]:
    ...


def process_data(data_lines: List[str]) -> List[str]:
    ...


def save_processed_data(processed_data: List[str], output_path: str):
    ...


def main(input_dir: str, output_dir: str):
    ...


if __name__ == "__main__":
    main(os.path.join(os.getcwd(), "task"), os.path.join(os.getcwd(), "output"))
