class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_attached = []

class Lecturer(Mentor):
    pass

class Reviewer(Mentor):
    pass
        
best_student = Lecturer('Ruoy', 'Eman')
best_student.courses_in_attached += ['Python']

print(best_student.name)
print(best_student.surname)
print(best_student.courses_in_attached)
print(Lecturer.mro())
print(Reviewer.mro())