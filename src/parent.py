import random
from typing import List

from src import Student


class Parent:
    _children: List[Student]
    _name: str
    _mood: bool

    def __init__(self, name: str, children: List[Student]):
        self._name = name
        self._children = children
        for child in children:
            child.set_parent(self)
        self._mood = random.choice([True, False])

    def __say_about(self, child: Student):
        print(f"{self._name.capitalize()} говорит: ", end='')

        if self._mood:
            if child.is_excellent():
                print(f"Мой ребёнок {child.get_name()} очень прилежный. Повезло, что у меня есть "
                      "такой прекрасный ребёнок.")
            else:
                print(f"Мой ребёнок {child.get_name()} "
                      "отличается сообразительнстью и острым умом.")
        else:
            if child.is_excellent():
                print(f"У меня сегодня плохое настроение, поэтому скажу лишь несколько слов о "
                      f"{child.get_name()}. Он умный и хорошо учится.")
            else:
                print(f"У меня плохое настроение и мой {child.get_name()} плохо учится. "
                      f"Не знаю в кого он пошёл.")

    def say_about_each(self):
        for child in self._children:
            self.__say_about(child)

    def say_somebody(self):
        child = random.choice(self._children)
        self.__say_about(child)

    def say_all(self):
        excellent: bool
        marks = 0
        for child in self._children:
            marks += 1 if child.is_excellent() else -1

        if marks > 0:
            excellent = True
        else:
            excellent = False

        print(f"{self._name.capitalize()} говорит: ", end='')

        if self._mood:
            if excellent:
                print("Мои дети самые лучшие на свете! Они отличники да ещё и умницы!")
            else:
                print("Мои дети просто золото! Я их люблю и неважно, что они учатся не на отлично.")
        else:
            if excellent:
                print("Я сегодня неважно себя чувствую, но мои дети очень хороши в школе!")
            else:
                print("Дети это одна головная боль. Учатся плохо, плюс настроение утром всё испортили.")

    def say_about(self, child: Student):
        if child not in self._children:
            print(f"[ERROR]{child.get_name()} не ребёнок {self._name}")
        else:
            excellent: bool
            marks = 0
            for child1 in self._children:
                marks += 1 if child1.is_excellent() else -1

            if marks > 0:
                excellent = True
            else:
                excellent = False

            print(f"{self._name.capitalize()} говорит: ", end='')

            if self._mood:
                if excellent:
                    print(f"Мой ребёнок {child.get_name()} очень прилежный. Повезло, что у меня есть "
                          "такой прекрасный ребёнок.")
                else:
                    print(f"Мой ребёнок {child.get_name()} "
                          "отличается сообразительнстью и острым умом.")
            else:
                if excellent:
                    print(f"У меня сегодня плохое настроение, поэтому скажу лишь несколько слов о "
                          f"{child.get_name()}. Он умный и хорошо учится.")
                else:
                    print(f"У меня плохое настроение и мой {child.get_name()} плохо учится. "
                          f"Не знаю в кого он пошёл.")
