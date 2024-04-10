#Nom, Matricule
#Nom, Matricule

import math
import random 
import sys

def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()

def main(args):
    n = int(args[0])
    output_file = args[1]

    # TODO : Compléter ici/Complete here...
    # Vous pouvez découper votre code en d'autres fonctions...
    # You may split your code in other functions...

    answer = 0

    # answering
    write(output_file, str(answer))

    

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])