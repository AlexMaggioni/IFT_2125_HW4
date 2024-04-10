#Alex Maggioni, 20266243
#Canelle Wagner, 20232321

import sys
from collections import deque

#Fonction pour lire le fichier d'input. Vous ne deviez pas avoir besoin de la modifier.
#Retourne la liste des noms d'étudiants (students) et la liste des paires qui ne peuvent
#doivent pas être mis dans le même groupe (pairs)
#
#Function to read the input file. You shouldn't have to modify it.
#Returns the list of student names (students) and the list of pairs of students that
#shouldn't be put in the same group (pairs)
def read(fileName):
    # lecture du fichier
    fileIn = open(fileName,"r")
    linesIn = fileIn.readlines()
    fileIn.close()

    nbStudents = int(linesIn[0])
    students = []
    if(nbStudents != 0):
        students = [s.strip() for s in linesIn[1:nbStudents+1]]
    nbPairs = int(linesIn[nbStudents+1])
    pairs = []
    if(nbPairs != 0):
        pairs = [s.strip().split() for s in linesIn[nbStudents+2:nbStudents+nbPairs+2]]

    return students, pairs


#Fonction qui écrit dans le fichier d'output. 
#le paramètre content est un string
#
#Function that writes in the output file.
#The content parameter is a string
def write(fileName, content):
    Outputfile = open(fileName, "w")
    Outputfile.write(content)
    Outputfile.close()

#Fonction principale à compléter.
#students : liste des noms des étudiants
#pairs : liste des paires d'étudiants à ne pas grouper ensemble
#        chaque paire est sous format de liste [x, y]
#Valeur de retour : string contenant la réponse. Si c'est impossible, retourner "impossible"
#                   Sinon, retourner en un string les deux lignes représentant les
#                   les deux groupes d'étudants (les étudiants sont séparés par des
#                   espaces et les deux lignes séparées par un \n)
#
#Function to complete
#students : list of student names
#pairs : list of pairs of students that shouldn't be grouped together.
#        each pair is given as a list [x, y]
#Return value : string with the output. If it is impossible, return "impossible".
#               otherwise, return in a single string both ouput lines that contain
#               two groups (students are separated by spaces and the two lines by a \n)
def createGroups(students, pairs):
    # Cas spécifique : aucun étudiant
    if not students:
        return "impossible"
    
    # Initialiser les couleurs de tous les élèves à -1
    colors = {student: -1 for student in students}
    
    # Construire le graphe
    graph = {student: [] for student in students}
    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)
    
    # Fonction pour essayer de colorer le graphe avec BFS
    def bfs(start):
        queue = deque([start])
        colors[start] = 0  # Commencer par colorier le premier noeud avec 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                # Si le voisin n'a pas encore été colorié, lui attribuer la couleur opposée
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[node]
                    queue.append(neighbor)
                # Si le voisin a déjà été colorié avec la même couleur, le graphe n'est pas biparti
                elif colors[neighbor] == colors[node]:
                    return False
        return True
    
    # Essayer de colorer le graphe avec BFS pour chaque composante non colorée
    for student in students:
        if colors[student] == -1 and not bfs(student):
            return "impossible"
    
    # Construire les deux groupes
    group1 = [student for student, color in colors.items() if color == 0]
    group2 = [student for student, color in colors.items() if color == 1]
    
    # Retourner la représentation des groupes, ou "impossible" si aucun étudiant n'a été traité
    return " ".join(group1) + "\n" + " ".join(group2) if students else "impossible"



#Normalement, vous ne devriez pas avoir à modifier
#Normaly, you shouldn't need to modify
def main(args):
    input_file = args[0]
    output_file = args[1]
    students, pairs = read(input_file)
    output = createGroups(students, pairs)
    write(output_file, output)
            

#Ne pas changer
#Don't change
if __name__ == '__main__':
    main(sys.argv[1:])