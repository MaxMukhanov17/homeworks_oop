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

    def setting_average(self):
        res = []
        for grade in self.grades.values():
            res += grade
        aver_grade = (sum(res)/len(res))
        return aver_grade

    def show_courses(self):
        res = ','.join(self.courses_in_progress)
        return res
    
    def show_finished_courses(self):
        for course in self.finished_courses:
            return course

    def __lt__(self, other):
        self.setting_average()
        if not isinstance(other, Student):
            print('Такого студента не существует')
            return 
        return self.setting_average() < other.setting_average()

    def __str__(self):
        self.setting_average()
        self.show_courses()
        self.show_finished_courses()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.setting_average()}\nКурсы в процессе обучения: {self.show_courses()}\nЗавершенные курсы: {self.show_finished_courses()}'
        return res
    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def setting_average(self):
        res = []
        for grade in self.grades.values():
            res += grade
        aver_grade = (sum(res)/len(res))
        return aver_grade
    
    def __lt__(self, other):
        self.setting_average()
        if not isinstance(other,Lecturer):
            print('Такого лектора не существует')
            return 
        return self.setting_average() < other.setting_average()

    def __str__(self):
        self.setting_average()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.setting_average()}'
        return res
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_in_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка!')
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def calc_average_st(students_list, course):
    list_grades = []
    for student in students_list:
        if course in student.courses_in_progress:
            for grades in student.grades.values():
                list_grades += grades
                aver_grade = (sum(list_grades)/len(list_grades))
    return aver_grade


def calc_average_lc(lecturers_list, course):
    list_grades = []
    for lecturer in lecturers_list:
        if course in lecturer.courses_in_attached:
            for grades in lecturer.grades.values():
                list_grades += grades
                aver_grade = (sum(list_grades)/len(list_grades))
    return aver_grade
                
   


some_student_1 = Student('Ruoy', 'Eman', 'male')
some_student_2 = Student('Max', 'Mukh', 'male')

some_student_1.courses_in_progress += ['Python']
some_student_2.courses_in_progress += ['Python']
some_student_1.courses_in_progress += ['Git']
some_student_1.finished_courses += ['Введение в программирование']

some_reviewer_1 = Reviewer('Some', 'Buddy')
some_reviewer_2 = Reviewer('John', 'Depp')
some_reviewer_1.courses_in_attached += ['Python']
some_reviewer_2.courses_in_attached += ['Python']

some_lecturer_1 = Lecturer('Some', 'Buddy')
some_lecturer_2 = Lecturer('David', 'Beckham')
some_lecturer_1.courses_in_attached += ['Python']
some_lecturer_2.courses_in_attached += ['Python']

some_reviewer_1.rate_hw(some_student_1, 'Python', 10)
some_reviewer_1.rate_hw(some_student_1, 'Python', 8)
some_reviewer_1.rate_hw(some_student_1, 'Python', 9)

some_reviewer_2.rate_hw(some_student_2, 'Python', 10)
some_reviewer_2.rate_hw(some_student_2, 'Python', 6)
some_reviewer_2.rate_hw(some_student_2, 'Python', 10)

some_student_1.rate_lc(some_lecturer_1, 'Python', 10)
some_student_1.rate_lc(some_lecturer_1, 'Python', 5)
some_student_1.rate_lc(some_lecturer_1, 'Python', 10)

some_student_2.rate_lc(some_lecturer_2, 'Python', 8)
some_student_2.rate_lc(some_lecturer_2, 'Python', 9)
some_student_2.rate_lc(some_lecturer_2, 'Python', 6)


print(some_reviewer_1)
print(some_lecturer_1)
print(some_student_1)
print(some_student_1 < some_student_2)
print(some_lecturer_1 > some_lecturer_2)
print(calc_average_st(students_list = [some_student_1, some_student_2], course = 'Python'))
print(calc_average_lc(lecturers_list = [some_lecturer_1, some_lecturer_2], course = 'Python'))