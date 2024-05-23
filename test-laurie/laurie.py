
import os
import glob

NB_PARAMS = 5
NB_ZERO = 4
TRUE = 1
FALSE = 0

PREFIX = "animatic"
EXT = ".exr"

def str_zero(num):
    return str(['0' for x in range(NB_ZERO - len(str(num)) + 1)])

def max_num(namefile):
    for f in namefile:
        # decouper f et recuperer le nombre maximum du dossier

def ft_prog(path, move_num, suiv_num, finish_num = 0):
    files = glob.glob(path + "//" + "*.exr")
    namefile = [os.path.basename(f) for f in files]
    if (finish_num != 0):
        n = finish_num - move_num + 1
    else:
        n = max_num(namefile) - move_num + 1
    print(len(namefile))
    print(move_num)
    for f in namefile:
        old_filename = path + "//" + PREFIX + str_zero(move_num) + str(move_num) + EXT
        if (n > 0 and f == old_filename):
            print("oui")
            new_filename = path + "//" + PREFIX + str_zero(suiv_num) + suiv_num + EXT
            os.rename(old_filename, new_filename)
            move_num += 1
            suiv_num += 1
            n -= 1

def main():
    path = os.getcwd() # // le chemin absolue du fichier
    suiv_num = int(input("Le numero du fichier source: ")) + 1 # le numero par lequelle le modifier
    move_num = int(input("Le numero du fichier cible: ")) # le numero a modifier
    finish_num = int(input("Le numero du fichier de fin: "))

    ft_prog(path, move_num, suiv_num, finish_num)

    print("Renommage dans dossier -> " + os.path.basename(path) + "\n")
    msg = "la fin du dossier !" if (not finish_num) else str(finish_num)
    print("Le numero " + str(move_num) + " est modifie par " + str(suiv_num) + " puis jusqu'a " + msg)

    return (TRUE)

main()