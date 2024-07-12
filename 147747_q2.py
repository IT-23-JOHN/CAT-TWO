#student class with attributes name and grades.
class Student:
    def __init__(self, name, grades):
        
    # Initialize a Student object.

        self.name = name
        self.grades = grades

    def get_average_grade(self):
    
    # Calculate the average grade of the student.

        #return: Average grade as a float.
        
        return sum(self.grades.values()) / len(self.grades)
#Classroom class with methods to add a student,display all students, get the average grade of a student and get the average for a subject.
class Classroom:
    def __init__(self):
        
    #Initialize a Classroom object.
       
        self.students = []

    def add_student(self, student):
    
        #Add a student to the classroom.
        
        self.students.append(student)

    def display_all_students(self):
        
        #Display the details of all students in the classroom.
        
        for student in self.students:
            print(f"Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, name):
        
        for student in self.students:
            if student.name == name:
                return student.get_average_grade()
        return None

    def get_subject_average(self, subject):
        
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        return total / count if count > 0 else None

# Classroom class with methods to add a student, display all student,display all students,get the average grade of a student, and get the class average for a subject
classroom = Classroom()

# Creating student instances
student1 = Student("Alice", {"Math": 90, "Science": 85})
student2 = Student("Bob", {"Math": 75, "Science": 95})
student3 = Student("Charlie", {"Math": 80, "Science": 70})

# Adding students to the classroom
classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)

# Displaying all students
classroom.display_all_students()

# Displaying the average grade of a specific student
print(f"Alice's average grade: {classroom.get_student_average('Alice')}")

# Displaying the class average for a specific subject
print(f"Class average for Math: {classroom.get_subject_average('Math')}")
