from os import path, walk
from time import sleep
import collections
from transformer_proxy import TransformerProxy


class Observer:

    def __init__(self, directory):
        self.directory = directory
        self.transformer = TransformerProxy("./images/original", "./images/processed")

    def observe(self):

        def sort_files():
            """Sort the files separately from the folders and sort files with extension (.jpg, .jpeg) to list(file_sort)"""
            file_sort = []
            ext = [".jpg", ".jpeg"]
            for root, dirs, files in walk(self.directory):
                for file_dir in files:
                    if file_dir.endswith(tuple(ext)):
                        file_sort.append(file_dir)
                return file_sort

        # check if path exists
        if not path.isdir(self.directory):
            print("ERROR - directory not found!!!")
            return
        else:
            print("Check for changes in your directory...")
            sort_files()

        # start watching
        last_file_list = []
        while True:
            file_list = sort_files()
            if collections.Counter(last_file_list) != collections.Counter(file_list):
                added = [f for f in file_list if not f in last_file_list]
                removed = [f for f in last_file_list if not f in file_list]

                if added:
                    for f in range(len(added)):
                        print(f"New File {added[f]} Added in folder {self.directory}")
                if removed:
                    for f in range(len(removed)):
                        print(f"File {removed[f]} Removed from folder {self.directory}")

                # Processor / Transformer ########

                for file in file_list:
                    print(file + " processed.")
                    self.transformer.transform(file)
            last_file_list = file_list
            sleep(5)
