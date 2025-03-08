import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Student(Person):
    def __init__(self, name, email, branch):
        super().__init__(name, email)
        self.branch = branch

class Teacher(Person):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

class College:
    def __init__(self, cid, name):
        self.name = name
        self.cid = cid
        self.students = []
        self.teachers = []
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def add_student(self, student):
        self.students.append(student)
    
    def display_teachers(self):
        if not self.teachers:
            print("No Teachers Present")
        else:
            print("\nTeacher Details")
            for t in self.teachers:
                print(f"Name: {t.name} \nEmail: {t.email}  \nSubject: {t.subject}\n")
    
    def display_students(self):
        if not self.students:
            print("No Students Present")
        else:
            print("\nStudent Details")
            for s in self.students:
                print(f"Name: {s.name} \nEmail: {s.email} \nBranch: {s.branch}\n")

def send_otp(email):
    otp = random.randint(1111, 9999)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "kprathyusha799@gmail.com"  
    password = "ihqh wsve sgur tlyk"    
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = email
    msg['Subject'] = "OTP Validation"
    msg.attach(MIMEText(f"Your OTP for login is {otp}.\nThank you.", 'plain'))
    
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()
    
    return otp

def verify_otp(expected_otp):
    for _ in range(3):
        entered_otp = int(input("Enter the OTP received: "))
        if entered_otp == expected_otp:
            print("Login Successful!\n")
            return True
        else:
            print("Invalid OTP. Try again.")
    print("Login Failed. Too many incorrect attempts.\n")
    return False

colleges = []
while True:
    print("Choose an option:")
    print("1. Create College")
    print("2. Add Teacher")
    print("3. Add Student")
    print("4. Display Teachers")
    print("5. Display Students")
    print("6. Teacher Login")
    print("7. Student Login")
    print("8. Exit")
    option = int(input("Enter your option: "))
    
    if option == 1:
        clg_id = int(input("Enter College ID: "))
        if any(c.cid == clg_id for c in colleges):
            print("College with this ID already exists. Try again.")
        else:
            clg_name = input("Enter College Name: ")
            colleges.append(College(clg_id, clg_name))
            print()
            print("College created successfully!")
            print("********************************")
    
    elif option == 2:
        clg_id = int(input("Enter College ID: "))
        college_obj = next((c for c in colleges if c.cid == clg_id), None)
        if college_obj:
            name = input("Enter Teacher Name: ")
            email = input("Enter Teacher Email: ")
            subject = input("Enter Teacher Subject: ")
            college_obj.add_teacher(Teacher(name, email, subject))
            print()
            print("Teacher added successfully!")
            print("********************************")
        else:
            print("College does not exist.\n")
    
    elif option == 3:
        clg_id = int(input("Enter College ID: "))
        college_obj = next((c for c in colleges if c.cid == clg_id), None)
        if college_obj:
            name = input("Enter Student Name: ")
            email = input("Enter Student Email: ")
            branch = input("Enter Student Branch: ")
            college_obj.add_student(Student(name, email, branch))
            print("")
            print("Student added successfully!")
            print("********************************")
        else:
            print("College does not exist.\n")
    
    elif option == 4:
        clg_id = int(input("Enter College ID: "))
        college_obj = next((c for c in colleges if c.cid == clg_id), None)
        if college_obj:
            print("********************************")
            college_obj.display_teachers()
            print("********************************")
        else:
            print("College does not exist.\n")
    
    elif option == 5:
        clg_id = int(input("Enter College ID: "))
        college_obj = next((c for c in colleges if c.cid == clg_id), None)
        if college_obj:
            print("********************************")
            college_obj.display_students()
            print("********************************")
        else:
            print("College does not exist.\n")
    
    elif option == 6:
        clg_name = input("Enter College Name: ")
        college_obj = next((c for c in colleges if c.name == clg_name), None)
        if college_obj:
            email = input("Enter Teacher Email: ")
            found_teacher = next((t for t in college_obj.teachers if t.email == email), None)
            if found_teacher:
                otp = send_otp(email)
                if verify_otp(otp):
                    print(f"Welcome, {found_teacher.name}!")
                    print("********************************")
            else:
                print("Teacher not found.\n")
        else:
            print("Enter correct College Name.\n")
    
    elif option == 7:
        clg_name = input("Enter College Name: ")
        college_obj = next((c for c in colleges if c.name == clg_name), None)
        if college_obj:
            email = input("Enter Student Email: ")
            found_student = next((s for s in college_obj.students if s.email == email), None)
            if found_student:
                otp = send_otp(email)
                if verify_otp(otp):
                    print(f"Welcome, {found_student.name}!")
                    print("********************************")
            else:
                print("Student not found.\n")
        else:
            print("Enter correct College Name.\n")
    
    elif option == 8:
        break
    
    else:
        print()
        print("Invalid option. Try again.\n")
        print()
