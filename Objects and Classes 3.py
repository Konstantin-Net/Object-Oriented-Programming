import numpy


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        average_grade = numpy.average([numpy.average(i) for i in self.grades.values()])
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {average_grade} \n" \
               f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)} \n" \
               f"Завершённые курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        self_average_grade = numpy.average([numpy.average(i) for i in self.grades.values()])
        other_average_grade = numpy.average([numpy.average(i) for i in other.grades.values()])
        if not isinstance(other, Student):  # Проверить на работоспособность
            print("Не студент")
            return
        return self_average_grade < other_average_grade

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            lecture.grades.append(grade)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        average_grade = round(numpy.average(self.grades), 1)
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {average_grade}"

    def __lt__(self, other):
        self_average_grade = numpy.average([numpy.average(i) for i in self.grades])
        other_average_grade = numpy.average([numpy.average(i) for i in other.grades])
        if not isinstance(other, Student):  # Проверить на работоспособность
            print("Не студент")
            return
        return self_average_grade < other_average_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']

best_student2 = Student('Ruoy', 'Eman', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['C++']


cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 10)
cool_mentor.rate_hw(best_student2, 'Python', 10)

print(best_student2)
print(best_student.grades)
print(best_student2.grades)
print(best_student2 < best_student)


