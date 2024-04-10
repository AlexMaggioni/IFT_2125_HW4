# CE FICHIER NE SERT QU'A APPELER ET TESTER VOTRE CODE.
# VOUS NE DEVRIEZ PAS AVOIR BESOIN DE LE MODIFIER, SAUF POUR
# AJOUTER VOUS-MÊME D'AUTRES TESTS SI VOUS LE VOULEZ.
# NE PAS REMETTRE SUR STUDIUM. REMETTEZ SEULEMENT well_placement.py

# THIS FILE IS ONLY USED TO CALL AND TEST YOUR CODE.
# YOU SHOULD NOT HAVE TO MODIFY IT, EXCEPT FOR ADDING
# NEW CUSTOM TESTS IF YOU WISH TO DO SO.
# DO NOT SUBMIT ON STUDIUM. ONLY SUBMIT well_placement.py

import well_placement

def verifyAns(fileNameOutput, ExpectedAnswer):
    fileOut = open(fileNameOutput,"r")
    linesOut = fileOut.readlines()
    fileOut.close()

    answer = int(linesOut[0].strip())
    if(answer != ExpectedAnswer):
        raise Exception("Wrong answer, got " + str(answer) + ", expected " + str(ExpectedAnswer))


if __name__ == '__main__':
    expected = [3,0,10,200,62,85,188882,43,1002777,141]
    for i in range(len(expected)):
        try:
            fileIn = "input" + str(i) + ".txt"
            fileOut = "output" + str(i) + ".txt"
            well_placement.main([fileIn, fileOut])
            verifyAns(fileOut, expected[i])
            print("Test " + str(i) + " OK\n")
        except Exception as e: 
            print("Test " + str(i) + " Fail")
            print(e)
            print()