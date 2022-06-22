import os
import datetime
import shutil
from posixpath import abspath
from time import sleep

import parserlib
from parserlib import get_value, parse_file, load_table, load_settings

settings = ["source_folder", "source_copy_folder", "destin_folder", "destin_copy_folder" ,"parsing_table", "log_file"]

try:
    load_settings("settings.json")
except:
    print("Configuration file settings.json is missing. Please create one with the 'configure' tool and save it here.")
    input()
    quit()

try:
    load_table(get_value("parsing_table"))
except:
    print("Translation table '" + get_value("parsing_table") + "' is missing. Please provide yourself one and put it here.")
    input()
    quit()


def deliver(file_name, origin_path, target_path, copy_path, target_copy_path):
    printnl("Working on file " + file_name)

    parse_file(origin_path+"/"+file_name, target_path+"/"+file_name)
    printnl("\tParsed " + file_name + " to " + get_value("destin_folder"))

    shutil.move(origin_path + "/" + file_name, copy_path + "/" + file_name)
    printnl(f"\tCopied {file_name} to " + get_value("source_copy_folder"))

    shutil.copy(target_path + "/" + file_name, target_copy_path + "/" + file_name)
    printnl("\tCopied parsed " + file_name + " to " + get_value("destin_copy_folder"))
    return True


def get_type_files():
    extensions = []
    for i in get_all_files():
        extension = get_file_exten(i)
        if extension not in extensions:
            extensions.append(extension)
    return extensions


def get_file_exten(full_file_name):
    return full_file_name.split(".")[1]

def get_file_name(full_file_name):
    return full_file_name.split(".")[0]

def get_files_that_start_with(prefix):
    _list = []
    for i in get_all_files():
        if i.startswith(prefix):
            _list.append(i)
    return _list

def get_all_files():
    return os.listdir(get_value("source_folder"))


def get_files(type:str):
    _list = []
    for f in os.listdir(get_value("source_folder")):
        if f.endswith(type):
            _list.append(f)
    return _list



# print and log
def printnl(*arg):
    st = ""
    for s in arg:
        st = st + str(s) + " "
    print(st)

    file = open(get_value("log_file"), "at")
    file.write(f"{datetime.datetime.now()}: {st}\n")
    file.close()


def run():
    printnl("Script started.")

    printnl("Conversion table loaded.")

    printnl("Settings loaded.")

    abs_origin_path = get_value("source_folder") + "/"
    abs_target_path = get_value("destin_folder") + "/"
    abs_copy_path = get_value("source_copy_folder") + "/"
    abs_target_copy_path = get_value("destin_copy_folder") + "/"

    while True:

        if len(get_all_files()) > 0:
            # Displaying how many files are found in the source directory
            printnl("Found " + str(len(get_all_files())) + " files in source folder of which...")
            _str = ""
            for t in get_type_files():
                number = len(get_files("." + t))
                _str += str(number) + " ." + t + " files, "
            printnl("\t" + _str)

        for f in get_files("E"):
            to_remove = f
            name_lists = get_files_that_start_with(get_file_name(f))
            name_lists.remove(to_remove)
            name_lists.append(f) # Last to be sent
            for n in name_lists:
                deliver(n, abs_origin_path, abs_target_path, abs_copy_path, abs_target_copy_path)

        sleep(int(get_value("delay")))


if __name__ == '__main__':
    run()
