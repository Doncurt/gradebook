
'''
Classroom class that is used to create a roster for a class that is able to process student data based on the information given
this class must be created first for the sole reason that every student must be assigned a class before they can have things like attendence
or assingments

all of the students objects infor wiill be passed through here for the sole purpose of this being the processing module.
my reasoning is that you cant have students without a classroom, so all of the student info will come from here and be executed via import and export
'''
class Classroom(object):
    classroomcount = 0
    roster = {}
    assingments = {}
    meetingDays = ""
    def __init__(self,className):
        self.className = className

    '''
    sets the days that the class is meeting
    '''
    def _setMeetingDays(self,meet):
        self.meetingDays = meet
        return self.meetingDays
    '''
    Sets the classroom name for a certain student
    '''
    def _setClassName(className):
        self.className = className
        return  className

    '''
    Gets all the student names and stores them in a dictionary(from when a student object is instantiated)
    '''
    def _getRosterNames(dict):

        pass

    '''
    Gets students grade from the info given in the student class and sets it into a roster
    '''
    def _getStudentGrades():
        pass
    '''
    Gets the total number of enrolled students in a certain class
    '''
    def _getNumOfStudents():
        return classroomcount
    '''
    student counter for the class
    '''
    def _studentAdd():
        pass

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
Start of program
'''


print("\n*************************** \n")
print (" Welcome to the Gradebook, Made by A. Box \n")

printDepartment()
#temporary variable for if else
class_name = ""
dept_choice = ""
class_days = ""
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
    print ("Please try again from the class choices\n")


Classroom1 = Classroom(class_name)
print ("The classroom you just created is ", Classroom1.className)

'''
Exception handling for things outside of MWF or TTH
'''
class_days = input("\nNow please enter the days that {0} meets. In MWF or TTH format \n".format(Classroom1.className))
#tesing via printingxn

Classroom1._setMeetingDays(class_days)

print (Classroom1.meetingDays)

#sentinel value for the number of classes

assingment_count = input("Now please tell me how many assingments are in the class\n")

for i in range(assingment_count):
    
