from typing import List, Union
from src import Parent, Teacher, Class


class Meeting:
    __parents: List[Parent]
    __teachers: List[Teacher]
    __classes: List[Class]

    def __init__(self):
        self.__parents = []
        self.__teachers = []
        self.__classes = []

    def add_parents(self, parents: Union[List[Parent], Parent]):
        if isinstance(parents, Parent):
            if parents not in self.__parents:
                self.__parents.append(parents)
            else:
                print(f"[ERROR] Родитель {parents} уже на собрании.")
        else:
            for parent in parents:
                if parent not in self.__parents:
                    self.__parents.append(parent)
                else:
                    print(f"[ERROR] Родитель {parent} уже на собрании.")

    def delete_parents(self, parents: Union[List[Parent], Parent]):
        if isinstance(parents, Parent):
            if parents in self.__parents:
                self.__parents.remove(parents)
        else:
            for parent in parents:
                if parent in self.__parents:
                    self.__parents.remove(parent)

    def add_teachers(self, teachers: Union[List[Teacher], Teacher]):
        if isinstance(teachers, Teacher):
            if teachers not in self.__teachers:
                self.__teachers.append(teachers)
            else:
                print(f"[ERROR] Преподаватель {teachers.get_name()} уже на собрании.")
        else:
            for teacher in teachers:
                if teacher not in self.__teachers:
                    self.__teachers.append(teacher)
                else:
                    print(f"[ERROR] Преподаватель {teacher.get_name()} уже на собрании.")

    def delete_teachers(self, teachers: Union[List[Teacher], Teacher]):
        if isinstance(teachers, Teacher):
            if teachers in self.__teachers:
                self.__teachers.remove(teachers)
        else:
            for teacher in teachers:
                if teacher in self.__teachers:
                    self.__teachers.remove(teacher)

    def add_classes(self, classes: Union[List[Class], Class]):
        if isinstance(classes, Class):
            if classes not in self.__classes:
                self.__classes.append(classes)
        else:
            for classs in classes:
                if classs not in self.__classes:
                    self.__classes.append(classs)

    def delete_classes(self, classes: Union[List[Class], Class]):
        if isinstance(classes, Class):
            if classes in self.__classes:
                self.__classes.remove(classes)
        else:
            for classs in classes:
                if classs in self.__classes:
                    self.__classes.remove(classs)

    def meeting(self):
        print("--------Собрание началось--------")
        child_without_parent = []
        child_who_parent_said = []
        for clas in self.__classes:
            if clas.get_teacher() not in self.__teachers:
                continue

            for lesson in clas.get_students_marks():
                for child in lesson:
                    if child in child_without_parent:
                        continue
                    if child.get_parent() not in self.__parents:
                        child_without_parent.append(child)
                    elif child not in child_who_parent_said:
                        child.get_parent().say_about(child)
                        child_who_parent_said.append(child)

        print(f"Родители следующих детей сегодня не явились на собрание: ", end='')
        for child in child_without_parent[:-1]:
            print(child.get_name() + ", ", end='')
        print(child_without_parent[-1].get_name())
        print("--------Собрание окончено--------")
