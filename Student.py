
'''
Student class. Contains all of the information to process all of the student information
id will be used as a security feature in v2

will use a function that uses a dictionary in order to be able to pass the information to the classroom class more easily

for the grades a 0 denotes a zero on the assingment, while a null denotes an excused assingment
'''
class Student(Classroom):
    classroomcount = 0
    grades =list("")
    def __init__(self,name, className,idNum):
        Classroom.__init__(self, className)  # no name needed since
        self.id = idNum
        classroomcount += 1

    def _setStudentGrades():
        for i in range (10):
            print "Would you like to enter a grade for 
            grades[i]= input("Please enter grade number ", i)
        return grades

    def _getAbsences():
