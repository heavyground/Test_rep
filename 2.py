class Student:
    def __init__ (self, studentId, name, email, grades, attendance):
        self.studentId= studentId
        self.name = name
        self.email = email
        self.grade_history = {}
        self.grades = {}
        self.attendance = attendance
    
    def addGrade(self, subject, grade):
        self.grades[subject] = grade
    
    def getGrade(self, subject):
        return self.grades[subject]
    
    def calculateAverage(self):
        total = 0
        avg = 0
        for subject in self.grades:
            total += self.grades[subject]
        avg = total/len(self.grades)
        return avg
    
    def getLetterGrade(self):
        q = self.calculateAverage()
        if q <= 40:
            return "F"
        elif q <=60:
            return "D"
        elif q <= 80:
            return "C"
        elif q <= 90:
            return "B"
        else:
            return "A"
    
    def getStudentInfo(self):
        return f"name: {self.name} id: {self.studentId} grades: {self.grades} average: {self.calculateAverage()} attendance: {self.attendance}"

    def __str__(self):
        return f"name: {self.name} id: {self.studentId} grades: {self.grades} average: {self.calculateAverage()} attendance: {self.attendance}"


class GradeBook:
    def __init__ (self, className, students):
        self.className = className
        self.students = []

    def addStudent(self, student):
        self.students.append(student)
    
    def removeStudent(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                self.students.remove(student)
                return
        print("Студент не найден")
    
    def findStudent(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                return student
        return "Студент не найден"
    
    def getClassAverage(self):
        total = 0
        avg = 0
        for student in self.students:
            total += student.calculateAverage()
        avg = total/len(self.students)
        return f"Средняя оценка всех студентов {avg}"
    
    def getTopStudents(self, count):
        top = self.students.copy()
        for i in range(len(self.students)):
            for j in range(0, len(self.students)-i-1):
                atten = top[j].attendance/100
                atten2 = top[j+1].attendance/100
                if top[j].calculateAverage() * atten  < top[j+1].calculateAverage() * atten2:
                    top[j], top[j+1] = top[j+1], top[j]
        
        return top[:count]

    def displayAllStudents(self):
        for student in self.students:
            print(student.getStudentInfo())
    
    def getStudentsByLetterGrade(self, letterGrade):
        gradeSt = []
        for student in self.students:
            if student.getLetterGrade() == letterGrade:
                gradeSt.append(student)
        if gradeSt != None:
            return gradeSt
        else:
            print("Оценка не найдена")
            return
        
    def reports(self):
        with open("C:/Users/roman/Downloads/py_отчет.txt", "w", encoding="utf-8") as file:
            for student in self.students:
                file.write(student.getStudentInfo())
                file.write("\n")
            
        

gradeBook = GradeBook("Computer Science 101", [])

student1 = Student("S001", "Alice Johnson", "alice@school.com", [], 70)
student2 = Student("S002", "Bob Smith", "bob@school.com", [], 31)
student3 = Student("S003", "Charlie Brown", "charlie@school.com", [], 82)
student4 = Student("S004", "sdfsdf", "charlie@school.com", [], 41)

student1.addGrade("Math", 95.0)
student1.addGrade("English", 88.0)
student1.addGrade("Science", 1.0)

student2.addGrade("Math", 2.0)
student2.addGrade("English", 5.0)
student2.addGrade("Science", 1.0)

student3.addGrade("Math", 17.0)
student3.addGrade("English", 88.0)
student3.addGrade("Science", 40)

student4.addGrade("Science", 40)

print(student1.getGrade("Math"))

print(student1.calculateAverage())
print(student2.calculateAverage())
print(student3.calculateAverage())

print(student1.getLetterGrade())


gradeBook.addStudent(student1)
gradeBook.addStudent(student2)
gradeBook.addStudent(student3)
gradeBook.addStudent(student4)


print(gradeBook.findStudent("S002"))
print(gradeBook.findStudent("S003"))

print(gradeBook.getClassAverage())

top_st = gradeBook.getTopStudents(4)

print("top:")
for i in range(len(top_st)):
    print(top_st[i])

print("\n")
gradeBook.displayAllStudents()

print("\n")
gradeSt = gradeBook.getStudentsByLetterGrade("C")
for i in range(len(gradeSt)):
    print(gradeSt[i])

gradeBook.reports()