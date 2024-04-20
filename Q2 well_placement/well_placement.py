#Alex Maggioni, 20266243
#Canelle Wagner, 20232321

import sys
from collections import deque

class UnionFind:
    # Initialisation des structures de données
    def __init__(self, size):
        self.parent = list(range(size))  
        self.rank = [0] * size  # hauteur de l'arbre
        self.size = [1] * size  # taille de l'ensemble

    # Trouver la racine de l'ensemble de 'x', avec compression de chemin
    def find(self, x):
        if self.parent[x] != x:
            # Compresser le chemin en remontant l'arbre
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    # Faire l'union des ensembles de 'x' et 'y'
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:  # Si 'x' et 'y' ne sont pas déjà dans le même ensemble
            # Attacher l'arbre plus petit sous la racine de l'arbre plus grand
            if self.rank[rootX] > self.rank[rootY]:  
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:  # Si les rangs sont égaux, choisir un comme parent et augmenter son rang
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                self.size[rootX] += self.size[rootY]

    # Renvoyer la taille de l'ensemble contenant 'x'
    def getSize(self, x):
        return self.size[self.find(x)]  

def read_problem(input_file="input.txt"):
    """Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
    faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
    d'autres librairies.
    Functions to read/write in files. you can modify them, do some parsing,
    add a return value, but don't use other librairies"""

    # Lecture du fichier
    file = open(input_file, "r")
    lines = file.readlines()
    
    # Obtenir les dimensions et la grille
    n, m = map(int, lines[0].split())
    grid = [[int(cell) for cell in line.strip()] for line in lines[1:]]

    # Fermeture du fichier
    file.close()

    return grid, n, m

def find_largest_aquifer(grid, n, m):
    # Initialiser une structure Union-Find pour la grille
    uf = UnionFind(n * m)  
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:  # Vérifier si la cellule contient un aquifère
                # Examiner les cellules adjacentes à droite et en bas pour éviter les doubles comptages
                for di, dj in [(0, 1), (1, 0)]:
                    # Calculer les coordonnées de la cellule voisine
                    ni, nj = i + di, j + dj  
                    # Vérifier si la cellule voisine est dans la grille et contient un aquifère
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        # Fusionner les deux aquifères dans l'Union-Find
                        uf.union(i * m + j, ni * m + nj)  
    largest = 0 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:  # Si la cellule contient un aquifère
                # Mettre à jour la plus grande taille si nécessaire
                largest = max(largest, uf.getSize(i * m + j))

    return largest  

    
def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    grid, n, m = read_problem(input_file)
    largest_aquifer = find_largest_aquifer(grid, n, m)
    write(output_file, str(largest_aquifer))

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])