import random
from typing import List

from src import Teacher
from src import Student


class Class:
    __teacher: Teacher
    __students: List[Student]
    __students_marks: List[List[Student]]

    def __init__(self, teacher: Teacher, students: List[Student]):
        self.__teacher = teacher
        self.__students = students
        self.__students_marks = []

    def get_teacher(self) -> Teacher:
        return self.__teacher

    def get_students_marks(self) -> List[List[Student]]:
        return self.__students_marks

    def lesson(self):
        print("--------Занятие началось--------")
        self.__students_marks.append([])
        ch: str
        if self.__teacher.get_character() == -1:
            ch = "Плохой"
        elif self.__teacher.get_character() == 0:
            ch = "Обычный"
        else:
            ch = "Хороший"
        print(ch + f" преподаватель {self.__teacher.get_name()} с " +
              ("хорошим" if self.__teacher.get_mood() else "плохим") +
              " настроением выставил следующие оценки:")
        for stud in self.__students:
            if random.choice([True, False]):
                self.__teacher.rate(stud)
                self.__students_marks[-1].append(stud)
                print(stud.get_name() + " получил " + str(stud.get_last_mark()))
        print("--------Занятие окончено--------")
