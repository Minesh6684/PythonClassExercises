from student import Student
from random import randint
from exercises import Course

student1 = Student("Lakshman", "215345")
student2 = Student("Minesh", "683685")

def main():
    OOP = Course('OOP 2', '0112')
    OOP.add_student('Jack', '2110050')
    OOP.add_student('Mendel', '2030407')
    OOP.add_student('Hector', '2010512')


if __name__ == '__main__':
    main()

