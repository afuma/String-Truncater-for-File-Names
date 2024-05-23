
import os
import glob
import re
from colorama import Fore, Back, Style

NB_PARAMS = 5
NB_ZERO = 3 #4
PREFIX = "animatic" # a changer en Animatic
EXT = ".exr"
MATCH = "^" + PREFIX + "[0-9]*"
VALID_COLOR = "GREEN"
INVALID_COLOR = "RED"

def msg_error(num_error, num1, num2):
    return ("ERREUR" + str(num_error) + ": modifier le fichier num: " + str(num1) + \
                    " plus grand que num_max: " + str(num2))

def normalize_namefile(path, namefiles):
    for f in namefiles:
        new_f = re.sub(MATCH, PREFIX, f)
        os.rename(path + "//" + f, path + "//" + new_f)

def list_to_string(s): 
    string = "" 
    for element in s:
        string += element 
    return string

def str_zero(num):
    return list_to_string(['0' for x in range(NB_ZERO - len(str(num)))])

def path_name(path, num):
    return (path + "/" + PREFIX + str_zero(num) + str(num) + EXT)

def max_num(namefiles):
    nums = []
    for f in namefiles:
        x = re.sub("^" + PREFIX + "[0]*", "", f)
        x = re.sub(EXT, "", x)
        nums.append(int(x))
    return max(nums)

'''def get_num(namefile):
    num = re.sub("^" + PREFIX + "[0]*", "", f)
    num = re.sub(EXT, "", x)
    num = int(num)
    return (num)
'''
def ft_prog(path, mod_num, suiv_num, finish_num = 0):
    files = glob.glob(path + "//" + "*.exr")
    namefiles = [os.path.basename(f) for f in files]
    # if (re.search(MATCH + EXT, namefiles[0])):
        # normalize_namefile(path, namefiles)
    n = finish_num if (finish_num != 0) else max_num(namefiles)
    n -= (mod_num - 1)
    while (n > 0):
        # print("n = " + str(n))
        old_filename = path_name(path, mod_num)
        new_filename = path_name(path, suiv_num)
        # print("suiv_num = " + str(suiv_num))
        if (not os.path.exists(new_filename)):
            # os.rename(old_filename, new_filename)
            print(old_filename + " -> " + new_filename)
        mod_num += 1
        suiv_num += 1
        n -= 1

def ft_move_offset(suiv_num, mod_num, finish_num):
    path = os.getcwd() # // le chemin absolue du fichier
    # suiv_num = int(input("Le numero du fichier source: ")) + 1 # le numero par lequelle le modifier
    # mod_num = int(input("Le numero du fichier cible: ")) # le numero a modifier
    # finish_num = int(input("Le numero du fichier de fin: "))
    # je dois calculer le max_num moi-meme pour faire les verifications car il y a le cas ou l'utilisateur entre 0
    print()
    suiv_num += 1
    if (suiv_num < 0 or mod_num < 0 or finish_num < 0):
        print("ERREUR 1: Le numero de fichier ne peut pas etre negatif !")
        return (0)

    if (mod_num <= suiv_num):
        print("ERREUR 2: On renomme les fichiers dans l'ordre croissant !")
        return (0)

    if (suiv_num > finish_num):
        print(msg_error(3, suiv_num, finish_num))
        return (0)

    if (mod_num > finish_num):
        print(msg_error(4, mod_num, finish_num))
        return (0)
    
    ft_prog(path, mod_num, suiv_num, finish_num)
    print()
    print("SUCCESS: Dans dossier -> " + os.path.basename(path))
    msg = "la fin du dossier !" if (not finish_num) else str(finish_num)
    print("Le numero " + str(mod_num) + " est modifie par " + str(suiv_num) + " puis jusqu'a " + msg)
    return (1)

def print_color(num)
    if (num): print(Style.BRIGHT + Fore.RED + "OK")
    if (not num): print(Style.BRIGHT + Fore.GREEN + "KO")

def main()
    # le fichier a modifier est le parametre numero 2
    # si les deux premiers parametres sont egaux alors ERREUR 2
    # si les deux premiers parametres sont egaux alors ERREUR 2
    # ERREUR 2                                          par le fichier numero 1
    if (ft_move_offset(0, 0, 0) == 0): print_color(1) # modifier le fichier numero 0
                                                        # jusqu'au fichier numero 0
    # ERREUR 2
    if (ft_move_offset(0, 0, 1) == 0): print_color(1) # modifier le fichier numero 0 par le fichier numero 1 jusqu'au fichier numero 0
    # ERREUR 2
    if (ft_move_offset(0, 1, 0) == 0): print_color(1) # modifier le fichier numero 1 par le fichier numero 1 jusqu'au fichier numero 0
    # ERREUR 2
    if (ft_move_offset(1, 0, 0) == 0): print_color(1) # modifier le fichier numero 0 par le fichier numero 2 jusqu'au fichier numero 0
    # ERREUR 2 -------
    if (ft_move_offset(1, 3, 0) == 0): print_color(1) # modifier le fichier numero 3 par le fichier numero 2 jusqu'au fichier numero 0
    # ERREUR 
    if (ft_move_offset(3, 0, 5) == 0): print_color(1) # modifier le fichier numero 0 par le fichier numero 4 jusqu'au fichier numero 5
    # ERREUR 2
    if (ft_move_offset(10, 10, 0) == 0): print_color(1) # modifier le fichier numero 10 par le fichier numero 11 jusqu'au fichier numero 0
    
    if (ft_move_offset(0, 14, 12) == 0): print_color(1) # modifier le fichier numero 14 par le fichier numero 1 jusqu'au fichier numero 12
    # ERREUR 1
    if (ft_move_offset(-1, 0, 4) == 0): print_color(1) # modifier le fichier numero 0 par le fichier numero 0 jusqu'au fichier numero 4
    # ERREUR 1
    if (ft_move_offset(0, -1, 0) == 0): print_color(1) # modifier le fichier numero -1 par le fichier numero 1 jusqu'au fichier numero 0
    # ERREUR 1
    if (ft_move_offset(-1, -2, 3) == 0): print_color(1) # modifier le fichier numero -2 par le fichier numero 0 jusqu'au fichier numero 3
    if (ft_move_offset(10, 0, 10) == 0): print_color(1) # modifier le fichier numero 0 par le fichier numero 11 jusqu'au fichier numero 10
    # ERREUR 1
    if (ft_move_offset(5, 5, 5) == 0): print_color(1) # modifier le fichier numero 5 par le fichier numero 6 jusqu'au fichier numero 5
    # ERREUR 1
    if (ft_move_offset(4, 3, -1) == 0): print_color(1) # modifier le fichier numero 3 par le fichier numero 5 jusqu'au fichier numero -1
    if (ft_move_offset(4, 3, 3) == 0): print_color(1) # modifier le fichier numero 3 par le fichier numero 5 jusqu'au fichier numero 3
    
# A FAIRE

# corriger le bug +1 a la fin avec les valeurs (0, 0, 0) dans le terminal
# tester le normalize_namefile