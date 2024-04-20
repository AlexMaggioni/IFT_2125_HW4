#Alex Maggioni, 20266243
#Canelle Wagner, 20232321

import math
import random 
import sys
# Ajoutés par moi 
import itertools
#from functools import lru_cache
#import time

# Test de primalité de Miller-Rabin pour les nombres inférieurs à 10^24
# Memoization des résultats de miller_rabin
#@lru_cache(None)
def miller_rabin(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17,19, 23,29, 31, 37)):
        return n in (2, 3, 5, 7, 11, 13, 17,19, 23,29, 31, 37)

    # Décomposition de n-1 en r * 2^s
    r, s = n - 1, 0
    while r % 2 == 0:
        r //= 2
        s += 1

    # Fonction pour effectuer le test de Miller-Rabin sur une base a
    def check_composite(a):
        x = pow(a, r, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True  # n est composé

    # Bases à tester
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in bases:
        if a % n != 0:  # On ne teste pas les bases qui sont multiples de n
            if check_composite(a):
                return False  # Si n échoue le test pour une base, il est composé

    return True  # Si n passe le test pour toutes les bases, il est probablement premier

# Fonction pour tester si une paire de nombres est spéciale (les deux concaténations donnent des nombres premiers)
def is_special_pair(p1, p2):
    concat1 = int(f"{p1}{p2}")
    concat2 = int(f"{p2}{p1}")
    return miller_rabin(concat1) and miller_rabin(concat2)

# Fonction pour trouver des paires spéciales jusqu'à une certaine limite
def find_special_pairs(limit):
    primes = [i for i in range(2, limit) if miller_rabin(i)]
    special_pairs = []
    for prime_pair in itertools.combinations(primes, 2):
        if is_special_pair(*prime_pair):
            special_pairs.append(prime_pair)

    p = list(set([prime for pair in special_pairs for prime in pair]))
    return p

def find_special_quads(primes, n):
    # Construire un graphe où chaque sommet est un nombre premier
    # et chaque arête relie les paires spéciales
    graph = {prime: [] for prime in primes}
    
    # Utiliser un set pour vérifier rapidement si une paire est spéciale
    special_pairs_set = set()
    for p1, p2 in itertools.combinations(primes, 2):
        if is_special_pair(p1, p2):
            graph[p1].append(p2)
            graph[p2].append(p1)
            special_pairs_set.add((p1, p2))
            special_pairs_set.add((p2, p1))

    # Trouver toutes les cliques à 4 sommets dans le graphe
    quads = set()
    for prime in primes:
        if len(graph[prime]) < 3:
            continue  # Si moins de 3 connexions, impossible de former une clique de 4
        for quad in itertools.combinations(graph[prime], 3):
            if all((p2 in graph[p1] and (p1, p2) in special_pairs_set) for p1, p2 in itertools.combinations(quad + (prime,), 2)):
                quads.add(tuple(sorted((prime,) + quad)))
    
    # Trier les quads par leur somme et obtenir la n-ième
    quads = sorted(list(quads), key=lambda q: sum(q))
    return sum(quads[n-1]) if len(quads) >= n else "Pas assez d'ensembles spéciaux trouvés, augmentez la valeur de la limite"

def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()

def main(args):
    #start_time = time.time() 
    n = int(args[0])
    output_file = args[1]

    # TODO : Compléter ici/Complete here...
    # Vous pouvez découper votre code en d'autres fonctions...
    # You may split your code in other functions...

    # Nous avons limité notre recherche pour des raisons de performance
    # Trouver les paires spéciales pour les nombres premiers jusqu'à la limite
    # La formule de la limite utilisée permet de correctement trouver le résultats au moins jusqu'à n = 100
    initial_limit = 1500 
    limit = int(round((initial_limit * math.sqrt(n)),0))
    special_pairs = find_special_pairs(limit)

    answer = find_special_quads(special_pairs, n)

    # answering
    write(output_file, str(answer))

    #end_time = time.time() 
    #execution_time = end_time - start_time  
    #print(f"Execution time: {execution_time:.2f} seconds")  


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])