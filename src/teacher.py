import random
from src.student import Student


class Teacher:
    # настроение
    __mood: bool
    # характер
    __is_good = 0
    # имя преподавателя
    __name: str
    # количество выставленных оценок
    __count = -1
    # количество оценок, нужное для смены настроения
    __shift_mood = 5

    def __init__(self, name: str = ""):
        self.__name = name
        if random.random() < 0.3:
            # Если -1, то преподаватель плохой, если 1, то хороший, если 0, то обычный
            self.__is_good = random.choice([-1, 1])
        self.__mood = random.choice([True, False])
        self.__shift_mood += int(random.random()*5) - 2

    # Диапазон оценок 2-5(как в РФ)
    def rate(self, student: Student, mark: int = 1) -> None:
        if self.__is_good == 1:
            student.rate(5)
        elif self.__is_good == -1:
            student.rate(2)
        elif mark == 1:
            if self.__mood:
                if student.is_excellent():
                    student.rate(5)
                else:
                    student.rate(4)
            else:
                if student.is_excellent():
                    student.rate(random.choice([4, 5]))
                else:
                    student.rate(random.choice([2, 3]))
        else:
            student.rate(mark)
        self.__count += 1
        if self.__count % self.__shift_mood == 0:
            self.__mood = random.choice([True, False])
            print(f"Настроение преподавателя {self.__name} изменилось на " + ("хорошее" if self.__mood else "плохое"))

    def get_character(self):
        return self.__is_good

    def get_mood(self):
        return self.__mood

    def get_name(self):
        return self.__name
