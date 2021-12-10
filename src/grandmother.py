from src import Parent, Student


class Grandmother(Parent):
    def say_about(self, child: Student):
        print(f"Бабушка {self._name.capitalize()} говорит: ", end='')

        if child not in self._children:
            if self._mood:
                print(f"{child.get_name()} очень хороший, мне он нравится.")
            else:
                print(f"{child.get_name()} не нравится мне, очень шкодливый и непослушный.")
        else:
            print(f"Мой внук {child.get_name()} всегда старается на занятиях, "
                  f"в жизни он добрый и послушный мальчик!")
