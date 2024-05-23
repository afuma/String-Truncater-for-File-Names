
import os
import glob
import re
from colorama import Fore, Back, Style

NB_ZERO = 4
PREFIX = "Animatic"
EXT = ".exr"
MATCH = "^" + PREFIX + "[0-9]*"

def list_to_string(s):
    string = ""
    for element in s:
        string += element
    return string

def str_zero(num):
    return list_to_string(['0' for x in range(NB_ZERO - len(str(num)))])

def path_name(path, num):
    return (path + "/" + PREFIX + "." + str_zero(num) + str(num) + EXT)

def elem_path(elem):
    return (os.path.basename(elem))

def small_path(path, elem):
    return (elem_path(path) + '/' + elem_path(elem))

def ft_prog(path, num_deb):
    files = glob.glob(path + "//" + "*.exr")
    files.sort()
    num = num_deb
    for f in files:
        new_f = path_name(path, num)
        if (not os.path.exists(new_f) and f != new_f):
            if (re.search(MATCH, f)):
                f = re.sub(MATCH, PREFIX, f)
            os.rename(f, new_f)
            print(small_path(path, f) + " -> " + small_path(path, new_f))
        num += 1

def ft_move_offset():
    path = input("Entrez le chemin du dossier: ")
    while (not os.path.exists(path)):
        path = input("Entrez le chemin du dossier: ")
    num_deb = input("Entrez le numero de depart: ")
    while (not num_deb.isdigit()):
        num_deb = input("Entrez le numero de depart: ")
    num_deb = int(num_deb)
    print()
    ft_prog(path, num_deb)
    print("\n" + Style.BRIGHT + Fore.GREEN + "SUCCESS DANS DOSSIER: \"" \
                + os.path.basename(path) + "\"\n")
    return (1)

ft_move_offset()

