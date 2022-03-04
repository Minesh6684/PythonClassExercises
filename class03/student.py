class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if grade > 90:
            self.grades.append(4.0)
        elif grade > 80:
            self.grades.append(3.5)
        elif grade > 70:
            self.grades.append(3)
        elif grade > 60:
            self.grades.append(2.5)
        else:
            self.grades.append(0)

    def get_gpa(self):
        return round(sum(self.grades)/ len(self.grades), 2) if sum(self.grades)/ len(self.grades) > 0 else 0

    def __str__(self):
        return f"{self.student_id}\t{self.name}\t{self.get_gpa()}"
