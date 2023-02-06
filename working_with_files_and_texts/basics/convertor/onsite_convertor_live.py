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
    with open(fpath, mode="r", encoding="utf-8") as read_file:
        return read_file.readlines()


def process_data(data_lines: List[str]) -> List[str]:
    processed_data = []
    for line in data_lines:
        first_data = line.split(",")[0]
        rest_data = line.split(",")[1:]
        converted_first_data = conversion_dict[first_data]
        converted_text = ",".join([converted_first_data] + rest_data)
        processed_data.append(converted_text)
    return processed_data


def save_processed_data(processed_data: List[str], output_path: str):
    with open(output_path, mode="w", encoding="utf-8") as f:
        output_str = "".join(processed_data)
        f.write(output_str)


def main(input_dir: str, output_dir: str):
    file_path = find_all_text_files(input_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for i, fpath in enumerate(file_path):
        data_lines = read_text_file(fpath)
        processed_data = process_data(data_lines)
        output_path = os.path.join(output_dir, f"output_{i + 1}.txt")
        save_processed_data(processed_data, output_path)


if __name__ == "__main__":
    main(os.path.join(os.getcwd(), "task"), os.path.join(os.getcwd(), "output"))
