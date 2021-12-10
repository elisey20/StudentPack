from typing import List
from src import Student, Teacher, Class, Parent, Meeting, Grandmother


def main():
    teacher1 = Teacher("OLEG")
    teacher2 = Teacher("VLADIMIR")
    students: List[Student] = []
    for i in range(30):
        students.append(Student("vasa" + str(i)))

    class_geometry = Class(teacher1, students)
    class_geometry.lesson()
    class_geometry.lesson()

    class_chemistry = Class(teacher2, students)
    class_chemistry.lesson()
    class_chemistry.lesson()

    parent1 = Parent("Misha", [students[0], students[3]])
    parent2 = Parent("Anton", [students[1], students[2]])
    parent3 = Parent("Grisha", [students[12], students[15], students[20]])
    parent4 = Parent("Pasha", [students[9]])
    grand = Grandmother("Svetlana", [students[24]])
    students[0].rate(5)
    students[0].rate(5)
    students[0].rate(5)
    students[0].rate(5)
    students[3].rate(2)
    students[3].rate(2)
    students[3].rate(2)
    students[3].rate(2)

    meeting = Meeting()
    meeting.add_parents([parent1, grand])
    meeting.add_teachers([teacher1, teacher2])
    meeting.add_classes([class_chemistry, class_geometry])
    meeting.meeting()


if __name__ == "__main__":
    main()
