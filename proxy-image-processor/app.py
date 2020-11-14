from os import path, walk
from time import sleep
import collections


def observe(directory):

    def sort_files():
        """Sort the files separately from the folders and sort files with extension (.jpg, .jpeg) to list(file_sort)"""
        file_sort = []
        ext = [".jpg", ".jpeg"]
        for root, dirs, files in walk(directory):
            for file in files:
                if file.endswith(tuple(ext)):
                    file_sort.append(file)
            return file_sort

    # check if path exists
    if not path.isdir(directory):
        print("ERROR - directory not found!!!")
        return
    else:
        sort_files()

    # start watching
    last_file_list = sort_files()
    while True:
        file_list = sort_files()
        if collections.Counter(last_file_list) != collections.Counter(file_list):
            added = [f for f in file_list if not f in last_file_list]
            removed = [f for f in last_file_list if not f in file_list]

            if added: print(f"New File {added[0]} Added in folder {directory}")
            if removed: print(f"File {removed[0]} Removed from folder {directory}")

        last_file_list = file_list
        sleep(5)


observe("./images")
