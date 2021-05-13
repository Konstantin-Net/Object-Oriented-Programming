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
        average_grade = round(numpy.average([numpy.average(i) for i in self.grades.values()]), 1)
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {average_grade} \n" \
               f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)} \n" \
               f"Завершённые курсы: {', '.join(self.finished_courses)} \n"

    def __lt__(self, other):
        self_average_grade = numpy.average([numpy.average(i) for i in self.grades.values()])
        other_average_grade = numpy.average([numpy.average(i) for i in other.grades.values()])
        if not isinstance(other, Student):
            return "Не студент"
        else:
            return self_average_grade < other_average_grade

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
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
        self.grades = {}

    def __str__(self):
        average_grade = round(numpy.average([numpy.average(i) for i in self.grades.values()]), 1)
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {average_grade} \n"

    def __lt__(self, other):
        self_average_grade = numpy.average([numpy.average(i) for i in self.grades.values()])
        other_average_grade = numpy.average([numpy.average(i) for i in other.grades.values()])
        if not isinstance(other, Lecture):
            return "Не лектор"
        return self_average_grade < other_average_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


#  Создание экземпляров каждого класс
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JS']

best_student2 = Student('Amelia', 'White', 'famale')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['JS']

cool_lecture = Lecture('Sammy', 'Buddy')
cool_lecture.courses_attached += ['Python']

cool_lecture2 = Lecture('Andrew', 'Williams')
cool_lecture2.courses_attached += ['JS']

cool_reviewer = Reviewer('Arthur', 'Smith')
cool_reviewer.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Calvin', 'Jones')
cool_reviewer2.courses_attached += ['JS']

#  Вызов методов каждого класса
best_student.add_courses("C++")
best_student.rate_hw(cool_lecture, 'Python', 8)
best_student.rate_hw(cool_lecture, 'Python', 9)
best_student.rate_hw(cool_lecture, 'Python', 10)

best_student.rate_hw(cool_lecture2, 'JS', 9)
best_student.rate_hw(cool_lecture2, 'JS', 9)
best_student.rate_hw(cool_lecture2, 'JS', 10)

best_student2.add_courses("C++")
best_student2.rate_hw(cool_lecture, 'Python', 8)
best_student2.rate_hw(cool_lecture, 'Python', 8)
best_student2.rate_hw(cool_lecture, 'Python', 10)

best_student2.rate_hw(cool_lecture2, 'JS', 9)
best_student2.rate_hw(cool_lecture2, 'JS', 8)
best_student2.rate_hw(cool_lecture2, 'JS', 10)

cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 8)

cool_reviewer.rate_hw(best_student2, 'Python', 8)
cool_reviewer.rate_hw(best_student2, 'Python', 8)
cool_reviewer.rate_hw(best_student2, 'Python', 9)

cool_reviewer2.rate_hw(best_student, 'JS', 7)
cool_reviewer2.rate_hw(best_student, 'JS', 8)
cool_reviewer2.rate_hw(best_student, 'JS', 9)

cool_reviewer2.rate_hw(best_student2, 'JS', 9)
cool_reviewer2.rate_hw(best_student2, 'JS', 8)
cool_reviewer2.rate_hw(best_student2, 'JS', 10)

#  Вызов магических методов каждого класса
print(best_student)
print(best_student2)
print(cool_lecture)
print(cool_lecture2)
print(cool_reviewer)
print(cool_reviewer2)
print(best_student > best_student2)
print(cool_lecture < cool_lecture2)

print(best_student.grades)
print(cool_lecture.grades)
print(cool_lecture2.grades)


def grades_student(stud, cours):
    return round(numpy.average([numpy.average(i.grades[cours]) for i in stud]), 1)


def grades_lecture(lect, cours):
    return round(numpy.average([numpy.average(i.grades[cours]) for i in lect]), 1)


print(grades_student([best_student, best_student2], 'Python'))
print(grades_lecture([cool_lecture2], 'JS'))
