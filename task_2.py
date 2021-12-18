class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_in_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка!')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_in_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка!')
        


this_student = Student('Max', 'Mukh', 'male')
this_student.courses_in_progress += ['Python']

this_reviewer = Reviewer('Alex', 'Bardin')
this_reviewer.courses_in_attached += ['Python']

this_lecturer = Lecturer('Oleg', 'Byl')
this_lecturer.courses_in_attached += ['Python']

this_reviewer.rate_hw(this_student, 'Python', 7)
this_student.rate_lc(this_lecturer, 'Python', 10)
print(this_student.grades)
print(this_lecturer.grades)