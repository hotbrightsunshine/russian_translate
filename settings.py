import shutil

from parserlib import *


def createFile():
    settings = ["source_folder", "source_copy_folder", "destin_folder", "destin_copy_folder", "parsing_table",
                "log_file", "delay"]
    dic = {}
    for s in settings:
        dic [s] = ""
    to_parse = json.dumps(dic)
    f = open("settings.json", "wt")
    f.write(to_parse)
    f.close()

def showValues():
    try:
        dic = get_json_dict()
    except:
        createFile()
        dic = get_json_dict()
    for k in dic:
        print(f" - {k} := {dic[k]}")

def help():
    print("- create:        to create a new configuration file.")
    print("- set KEY VALUE: to set the value VALUE bound to the key KEY.")
    print("- reset:         to set all the values from scratch.")
    print("- show:          to show all the values set in this instance. ")
    print("- save PATH:     to save current settings into PATH. (Absolute is preferred)")
    print("- quit:          to exit this script. ")

def prompt():
    ins = input(" > ")
    return ins.lower().split(" ")

def reset():
    dict = get_json_dict()
    for k in dict:
        set_value(k, input(f" ! set {k} "))

def save(path):
    if path == "":
        shutil.move('./settings.json', "..")
    else:
        try:
            shutil.copy("./settings.json", path)
            print("Saved.")
        except:
            print("Incorrect path. If it isn't, try running this program as administrator. ")

def main():
    print("Type '?' or enter a command.")

    while True:
        cmd = prompt()
        if cmd[0] == 'quit':
            print("Bye bye.")
            break
        elif cmd[0] == 'show':
            showValues()
        elif cmd[0] == 'create':
            createFile()
        elif cmd[0] == 'reset':
            reset()
        elif cmd[0] == 'set':
            if len(cmd) < 3:
                print("The command you entered is wrong, please check SET parameters.")
            try:
                set_value(cmd[0], cmd[1])
            except:
                print("File missing, wrong argments, or something else. Please try again.")
                createFile()
        elif cmd[0] == 'save':
            try:
                save(cmd[1])
                continue
            except:
                print("A error occurred, please check SAVE parameters")
                continue

        elif cmd[0] == "?":
            help()
        else:
            print(f"The command '{cmd[0]}' is not a valid one, please type '?' for a list of available commands.")


if __name__ == '__main__':
    print("Welcome to the 'Russian Translate' Configuration Tool")
    main()
