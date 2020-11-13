from os import path, listdir
from time import sleep
import collections


def observe(directory):
    # check if path exists
    if not path.isdir(directory):
        print("ERROR - directory not found!!!")
        return

    last_file_list = listdir(directory)

    while True:
        ext = [".jpg", ".jpeg"]
        file_list = listdir(directory)

        if collections.Counter(last_file_list) != collections.Counter(file_list):
            added = [f for f in file_list if not f in last_file_list]
            removed = [f for f in last_file_list if not f in file_list]

            if added and added[0].endswith(tuple(ext)) and path.isfile(directory + "/" + added[0]): print(
                f"New File {added} Added in folder {directory}")
            if removed and removed[0].endswith(tuple(ext)): print(f"File {removed} Removed from folder {directory}")

            last_file_list = file_list

        last_file_list = file_list
        sleep(5)


observe("./images")
