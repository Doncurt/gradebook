from student import Student

class Classroom(object):
'''
takes input for the class' name, the teacher's name as well as the day and time. It also initiallizes the roster as an empty dictionary and has a counter for the number of students in a classroom
'''

  def __init__(self, class_name, teacher_name, class_day_and_time):
        self.class_name = class_name
        self.teacher_name = teacher_name
        self.class_day_and_time = class_day_and_time
        self.next_available_student_number = 1
        self.roster = {}
'''
Takes a parameter for the students name, which is then used as in input for the constructor method. The number of students is increased by one, the roster is updated with a student ID value, and the student is displayed on the console
'''
    def enroll_student(self, student_name):
        new_student = Student(student_name, self.next_available_student_number)
        self.next_available_student_number += 1
        self.roster[new_student.student_ID] = new_student
        print(new_student.name + ' enrolled successfully!')
'''
This method is self explained
'''
    def add_assignment_for_student(self, student_name, assignment_name, grade):
        '''Adds an assignment and corresponding grade for an individual student.'''
        for student in self.roster.values():
            if student.name == student_name:
                student.add_assignment(assignment_name, grade)
'''
Validation method that check to see if the grade assigned is an acceptable value( ints turned into floats). If not a value exception is thrown
'''
    def _is_valid_grade(self, grade):
        try:
            valid_grade = float(grade)
            if valid_grade >= 0:
                return true
        except ValueError:
            return false
'''
take the parameter for an assingment name. The crade of the student is then prompted for and checked for validity using a loop. If the input is valid, grade is added to the dictionary using the add_assignment method
'''
    def add_assignment_for_class(self, assignment_name):
        for student in self.roster.values():
            grade = ""
            while not _is_valid_grade(grade):
                grade = float(input("Enter {}'s grade for {}: ".format(student.name,
                                                                       assignment_name)))
            student.add_assignment(assignment_name, grade)
'''
drops the assingment from the dictionary whenthe student name and assignment name are entered. If the student name is correct the assingment is dropped based in its name
'''

    def drop_assignment_for_student(self, student_name, assignment_name):
        for student in self.roster.values():
            if student.name == student_name:
                student.delete_assignment(assignment_name)
'''
drops the assingment from the entire roster of students by interating over the student objects then using the method delete_assignment based on name
'''
    def drop_assignment_for_class(self, assignment_name):
        for student in self.roster.values():
            student.delete_assignment(assignment_name)
'''
getter method for the students GPA . It matches based on the student name after interating over the students roster
'''
    def get_student_GPA(self, student_name):
        for student in self.roster.values():
            if student.name == student_name:
                return student.GPA
'''
Gets the entire rosters average GPA. it fitsrs totals up the enitre classes GPA points by interating over the roster . after this the average is gained by taking the number of students in the roster, then using that to divide the summed GPA
'''
    def get_class_average(self):
        if len(self.roster) == 0:
            print("There are no students enrolled in this class!")
            return None
        else:
            point_total = sum([i.GPA for i in self.roster.values()])
            class_average = point_total / len(self.roster)
            return class_average
