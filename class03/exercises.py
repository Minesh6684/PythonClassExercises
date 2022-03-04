from student import Student


class Course:
    def __init__(self, title, course_id):
        self.title = title
        self.course_id = course_id
        self.list_student = []

    def add_student(self, name, student_id):
        self.list_student.append(Student(name, student_id))

    def __str__(self):
        out = ''
        for s in self.list_student:
            out += str(s) + '\n'
        return out


