
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
    assignments = list("")
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
Student class used to hold and proccess only a singluar students information as well as pass data tp the main class
when ever student class
'''
class Student(object):
    grades = list("")
    name = ""
    idnum = ""

    def __init__(self,name,className,id):
        self.className = className
        self.name = name
        self.id = idnum

    def _setName(name):
        self.name = name
        return self.name
'''
    def _gradeAverages( grades):
        sum = 0
        lenth = len(grades)
        for i in (len(grades)):
            sum = sum+grades[i]
            if not grades[i].isdigit():
                length -= length
                continue
        average = sum/length
        return average
'''
'''

This class is mostly for processing user entered information while encapsluating the rest of the functions and such

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
#Section for filling the List that contains all of the assigments that the students have been given
#sentinel value for the number of classes

assignment_count = input("Now please tell me how many assingments are in the class\n")
# create a dictionary with a set length based on the number of assignents
print ("\nOK. lets get some assignment names\n")

for i in range(int(assignment_count)):
    print ("what is the name of assingment ",i + 1)
    temp = input("\n")
    Classroom1.assignments.extend(temp)
    print ("The assignments given so far are: \n", Classroom1.assignments)


print ("Now that we have a class, lets enroll some students")
grades = [1,2,3,4,5]
def _gradeAverages(grades):
    sum = 0
    length = 0
    lenth = len(grades)
    for i in range (len(grades)):
        sum = sum + grades[i]
        if grades[i] > 100:
            length -= length
            continue
    average = sum/length
    return average

average = _gradeAverages(grades)

print (average)
