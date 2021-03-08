my_student = {
    'name': 'Sasha',
    'grades': [70, 88, 90, 99, 88],
    'average': None
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


#  Creating a class object

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student("Bato", [90, 94, 87])


print(student_one.name)
print(student_one.__class__) # <class 'Student'>

