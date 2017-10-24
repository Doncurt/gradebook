class Student(object):
'''
Hello, Mike. I just realized that I didnt submit my gradebook to you and the files on my repo arent up to date( deleted some of the ones I thought that I wouldnt need after this weekend becuase I was being taught how to best structure my projects for accessing and git). I completely understand all logic(as proven by the heard immunity project folowing this)


'''

'''
Constructor method takes a name and the student ID. the GPA is left blank for the sole reasn that it will be calculated in the _update_grade_in_class method. The assingments are stored in a dictionary as per assignment parameters
'''
 def __init__(self, name, student_ID):
         self.name = name
         self.student_ID = student_ID
         self.GPA = None
         self.assignments = {}
'''
updates the grades in class based on if they are added or dropped, the vallue of such is calculated by summing the values in the assignments dictionary( first by turning it into a lsst). The average(GPA) of such is determined by the number of assignments
'''
    def _update_grade_in_class(self):
        point_total = sum(list(self.assignments.values()))
        num_assignments = len(self.assignments)
        if num_assignments == 0:
            self.GPA = None
        else:
            self.GPA = (point_total / num_assignments)
'''
Method to change the grade on an assignment which accesses the dictionary to change these values. when thos os changed it also changes the grade in the class by invoking the _update_grade_in_class method. if the assignment name is incorrect it prints an error message
'''
    def update_grade_for_assignment(self, assignment_name, grade):
        if assignment_name in self.assignments:
            self.assignments[assignment_name] = grade
            self._update_grade_in_class()
        else:
            print("The student does not have any assignment by that name!")
'''
deletes an assingment by removing it from the dictionary of assignments. Also calls the _update_grade_in_class function to update the grade in the class. Prints an error message if the assignment name is incorrect
'''
    def delete_assignment(self, assignment_name):
        if assignment_name in self.assignments:
            self.assignments.pop(assignment_name, None)
            self._update_grade_in_class()
        else:
            print("The student does not have any assignment by that name!")
'''
adds an assingment by puttting it in thedictionary of assignments. Calls method the _update_grade_in_class to update the grade in the class . Prints an error message if the assignment name is incorrect
'''
    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        self._update_grade_in_class()
