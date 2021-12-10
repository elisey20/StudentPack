from typing import List
#from src import Parent


class Student:
    __marks: List[int]
    __name: str

    def __init__(self, name: str = ""):
        self.__marks = []
        self.__name = name
        self.__parent = None

    def get_name(self) -> str:
        return self.__name

    def get_last_mark(self):
        return self.__marks[-1]

    def rate(self, mark: int) -> None:
        self.__marks.append(mark)

    def is_excellent(self) -> bool:
        if len(self.__marks) == 0:
            return False

        sum = 0.0
        for mark in self.__marks:
            sum += mark
        if len(self.__marks) != 0:
            sum = sum / len(self.__marks)
        if sum > 4.5:
            return True
        else:
            return False

    def set_parent(self, parent):
        self.__parent = parent

    def get_parent(self):
        return self.__parent
