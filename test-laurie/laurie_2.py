
import os
import glob
import re

NB_PARAMS = 5
NB_ZERO = 4
PREFIX = "animatic" # a changer en Animatic
EXT = ".exr"
MATCH = "^" + PREFIX + "[0-9]*"

def normalize_namefile(path, namefiles):
    for f in namefiles:
        new_f = re.sub(match, PREFIX, txt)
        os.rename(path + "//" + f, path + "//" + new_f)

'''def str_zero(namefile, num): # return str(['0' for x in range(NB_ZERO - len(str(num)) + 1)])
    x = re.sub("^" + PREFIX + ".", "", namefile)
    x = re.sub(str(num) + EXT, "", x)
    return (x)
'''
def str_zero(num): 
    return str(['0' for x in range(NB_ZERO - len(str(num)) + 1)])

def max_num(namefiles):
    nums = []
    for f in namefiles:
        x = re.sub("^" + PREFIX + "[0]*", "", f)
        x = re.sub(EXT, "", x)
        nums.append(int(x))
    return max(nums)

def ft_prog(path, move_num, suiv_num, finish_num = 0):
    files = glob.glob(path + "//" + "*.exr")
    namefiles = [os.path.basename(f) for f in files]
    if (re.search(MATCH, PREFIX + namefiles[0])):
        normalize_namefile(path, namefiles)
    n = finish_num if (finish_num != 0) else max_num(namefiles)
    n -= (move_num - 1)
    while (n > 0):
        for f in namefiles: # old_filename = path + "//" + PREFIX + str_zero(f, move_num) + str(move_num) + EXT
            old_filename = path + "//" + PREFIX + str_zero(move_num) + str(move_num) + EXT
            if (f == old_filename):
                new_filename = path + "//" + PREFIX + str_zero(f, suiv_num) + suiv_num + EXT
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

main()