
import Classroom
import Student
'''

This class is mostly for processing user entered information while encaplusating the rest of the functions and such

as such some of the functions will be declared here

The first function handles the set up for displaying what department the classes will be in
'''
'''
set up to print department names for the coming prompt
'''

def printDepartment():
 print ("Which one of these department are you looking for courses in?\n")
 print ("\nCS\t\tEng\t\tMath\n")
'''
Prints the current classes in The CS department
'''
def csClasses():
    print ("The corrent offererings for CS classes are:\n ")
'''
Prints the current classes in the English department
'''
def engClasses():
    print ("The corrent offererings for English classes are:\n ")
'''
Prints the current classes in the math department
'''
def mathsClasses():
    print ("The current offerings for Maths are: \n")

'''
Gets all the student names and stores them in a dictionary(from when a student object is instantiated)
'''
def _getRosterNames(dict):

    pass

'''
Start of program
'''


print("\n*************************** \n")
print (" Welcome to the Gradebook, Made by A. Box \n")

printDepartment()

dept_choice = ""
dept_choice= input("Please give me the name of the department\n cs for 'CS'\t eng for 'English'\t ma for Math'\n")

    if dept_choice == "cs":
        class_name = input("What CS class Number is this? : \n" )
        class_name = "CS" +class_name
        print (class_name)

    elif dept_choice == "eng":
        class_name = input("What English class Number is this? : \n" )
        class_name = "Eng" +class_name
        print (class_name)

    elif dept_choice == "ma":
        class_name = input("What Math class Number is this? : \n" )
        class_name = "Math" +class_name
        print (class_name)
    else:
        print ("Please try again from the class choices")
