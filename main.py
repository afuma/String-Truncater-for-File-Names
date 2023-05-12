import os
import glob
import re
from colorama import Fore, Back, Style

MATCH = "^AnyConv.com__"

def list_to_string(s):
    string = ""
    for element in s:
        string += element
    return string

def path_name(path, num):
    return (path + "/" + PREFIX + "." + EXT)

def elem_path(elem):
    return (os.path.basename(elem))

def small_path(path, elem):
    return (elem_path(path) + '/' + elem_path(elem))

def ft_prog(path):
    files = glob.glob(path + "//**//" + "*.xpm", recursive=True)
    files.sort()
    for f in files:
        path = os.path.dirname(f)
        f = os.path.basename(f)
        if (re.search(MATCH, f)):
            new_f = re.sub(MATCH, "", f)
            os.rename(path + "//" + f, path + "//" + new_f)
            print(f + " -> " + new_f)

def ft_move_offset():
    path = input("Entrez le chemin du dossier: ")
    while (not os.path.exists(path)):
        path = input("Entrez le chemin du dossier: ")
    ft_prog(path)
    print("\n" + Style.BRIGHT + Fore.GREEN + "SUCCESS DANS DOSSIER: \"" \
                + os.path.basename(path) + "\"\n")
    return (1)

ft_move_offset()
