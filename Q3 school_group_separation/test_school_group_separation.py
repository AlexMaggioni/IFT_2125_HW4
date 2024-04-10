# CE FICHIER NE SERT QU'A APPELER ET TESTER VOTRE CODE.
# VOUS NE DEVRIEZ PAS AVOIR BESOIN DE LE MODIFIER, SAUF POUR
# AJOUTER VOUS-MÊME D'AUTRES TESTS SI VOUS LE VOULEZ.
# NE PAS REMETTRE SUR STUDIUM. REMETTEZ SEULEMENT school_group_separation.py

# THIS FILE IS ONLY USED TO CALL AND TEST YOUR CODE.
# YOU SHOULD NOT HAVE TO MODIFY IT, EXCEPT FOR ADDING
# NEW CUSTOM TESTS IF YOU WISH TO DO SO.
# DO NOT SUBMIT ON STUDIUM. ONLY SUBMIT school_group_separation.py

import school_group_separation

def verifyAns(fileNameInput, fileNameOutput, ExpectedAnswer):
    fileOut = open(fileNameOutput,"r")
    linesOut = fileOut.readlines()
    fileOut.close()

    if(not ExpectedAnswer):
        if(linesOut[0].strip() != "impossible"):
            raise Exception("Wrong answer, should be \"impossible\"")
    else:  
        fileIn = open(fileNameInput,"r")
        linesIn = fileIn.readlines()
        fileIn.close()

        nbStudents = int(linesIn[0])
        students = []
        if(nbStudents != 0):
            students = [s.strip() for s in linesIn[1:nbStudents+1]]
        nbPairs = int(linesIn[nbStudents+1])
        pairs = []
        if(nbPairs != 0):
            pairs = linesIn[nbStudents+2:nbStudents+nbPairs+2]
        
        groupA = set(linesOut[0].strip().split())
        groupB = set(linesOut[1].strip().split())

        #each student is in the answer, and only in one group
        for s in students:
            if((s in groupA) == (s in groupB)):
                if(s in groupA):
                    raise Exception("Student " + str(s) + " has been put in both groups")
                else:
                    raise Exception("Student " + str(s) + " hasn't been put in any group")
                
        #there are no extra students or duplicate:
        if(len(groupA) + len(groupB) != nbStudents):
            raise Exception("Number of students in the output is " + str(len(groupA)+len(groupB)) + ", expected " + str(nbStudents))
        
        #for every given pair, the students are in different groups
        for p in pairs:
            student1, student2 = p.strip().split()
            if((student1 in groupA and student2 in groupA) or (student1 in groupB and student2 in groupB)):
                 raise Exception("Students " + str(student1) + " and " + str(student2) + " cannot be in the same group")
    
if __name__ == '__main__':
    expected = [True, False, True, False, False, True, True, True, False, True, False]
    for i in range(len(expected)):
        try:
            fileIn = "input" + str(i) + ".txt"
            fileOut = "output" + str(i) + ".txt"
            school_group_separation.main([fileIn, fileOut])
            verifyAns(fileIn, fileOut, expected[i])
            print("Test " + str(i) + " OK\n")
        except Exception as e: 
            print("Test " + str(i) + " Fail")
            print(e)
            print()