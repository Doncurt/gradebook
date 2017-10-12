
'''
Classroom class that is used to create a roster for a class that is able to process student data based on the information given
this class must be created first for the sole reason that every student must be assigned a class before they can have things like attendence
or assingments

all of the students objects infor wiill be passed through here for the sole purpose of this being the processing module.
my reasoning is that you cant have students without a classroom, so all of the student info will come from here and be executed via import and export
'''
class Classroom(object):
    classroomcount = 0
    roster ={}
    def __init__(self,className):
        self.className = className


'''
Sets the classroom name for a certin student
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
