# Ce fichier ne sert qu'à appeler et tester votre code. 
# Vous ne devriez pas avoir besoin de le modifier, sauf pour
# ajouter vous-même d'autres tests si vous le voulez.
# Ne pas remettre sur StudiUM. Remettez seulement prime_special_groups.py
#
# /!\ CES TESTS SONT FAIT AVEC n = 1,2,3,6. ON VOUS DEMANDE DE NE PAS 
# PARTAGER PUBLIQUEMENT VOS SOLUTIONS POUR n = 4,5,7 /!\
#
# Chaque tests ne devrait idéalement pas prendre plus que quelques minutes 
# même sur un ordinateur pas très performant

# This file is only used to call and test your code.
# You should not have to modify it, except for adding
# new custom tests if you wish to do so.
# Do not submit on Studium. Only submit prime_special_groups.py
# 
# /!\ THESE TESTS ARE FOR n = 1,2,3,6. WE ASK YOU TO PLEASE NOT PUBLICLY
# SHARE YOUR ANSWERS FOR n = 4,5,7 /!\
#
# Each test should ideally not take more than a few minutes even on a 
# not very powerful computer

import prime_special_groups

def verifyAns(fileNameOutput, ExpectedAnswer):
    fileOut = open(fileNameOutput,"r")
    linesOut = fileOut.readlines()
    fileOut.close()

    answer = int(linesOut[0].strip())
    if(answer != ExpectedAnswer):
        raise Exception("Wrong answer, got " + str(answer) + ", expected " + str(ExpectedAnswer))


if __name__ == '__main__':
    expected = [792, 2484, 3850, 6728]
    valuesOfN = [1,2,3,6] #4,5,7 are kept secret :P
    for i in range(len(expected)):
        try:
            n = valuesOfN[i]
            fileOut = "output" + str(n) + ".txt"
            prime_special_groups.main([n, fileOut])
            verifyAns(fileOut, expected[i])
            print("Test with n = " + str(n) + " OK\n")
        except Exception as e: 
            print("Test with n = " + str(n) + " Fail")
            print(e)
            print()