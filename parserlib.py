import csv
import json

table = {}
settings = {}

def get_json_dict(filename):
    file = open(filename, "rt")
    content = file.read()
    file.close()
    return json.loads(content)


def set_value(key, value):
    if key in get_json_dict():
        _dict = get_json_dict()
        _dict[key] = value

        to_parse = json.dumps(_dict)
        open("settings.json", "wt").write(to_parse)

        return True
    return False


def get_value(key):
    return settings[key]


def get_parsing_dict(tablename):
    file = open(tablename, newline='')
    reader = csv.reader(file, delimiter=";")

    rows_csv = []
    parsing_dic = {}

    for row in reader:
        rows_csv.append(row)

    for elem in rows_csv:
        parsing_dic[f'{elem[0]}'] = f'{elem[1]}'

    file.close()
    return parsing_dic


def load_table(tablename):
    global table
    table = get_parsing_dict(tablename)


def load_settings(filename):
    global settings
    settings = get_json_dict(filename)


def bin_parse_c(char_code_int):
    parsing_dict = table
    if(parsing_dict[f'{char_code_int}']) == '':
        return -1
    return int(parsing_dict[f'{char_code_int}'])


def parse(content):
    str_tbp = bytearray()
    for c in content:
        parsed_c = bin_parse_c(c)
        if parsed_c >= 0:
            str_tbp.append(int(parsed_c))
    return str_tbp


def parse_file(origin, output):
    file = open(origin, "rb")
    content = file.read()

    parsed = open(output, "wb")
    content_tbp = parse(content)
    parsed.write(content_tbp)

    file.close()
    parsed.close()