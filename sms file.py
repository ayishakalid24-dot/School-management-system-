import os

# =============================
# Data Storage
# =============================

data_file = "students.txt"
teachers_file = "teachers.txt"
classrooms_file = "classrooms.txt"

# Load data
students, teachers, classrooms = [], [], []

def load_data():
    global students, teachers, classrooms

    # Students
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) >= 5:
                    student = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2],
                        "classroom": parts[3],
                        "scores": eval(parts[4]) if parts[4] else {}
                    }
                    students.append(student)

    # Teachers
    if os.path.exists(teachers_file):
        with open(teachers_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    teacher = {"username": parts[0], "password": parts[1], "classroom": parts[2]}
                    teachers.append(teacher)

    # Classrooms
    if os.path.exists(classrooms_file):
        with open(classrooms_file, "r") as f:
            classrooms.extend([c.strip() for c in f.readlines()])

def save_data():
    # Save students
    with open(data_file, "w") as f:
        for s in students:
            f.write(f"{s['id']},{s['name']},{s['age']},{s['classroom']},{s['scores']}\n")

    # Save teachers
    with open(teachers_file, "w") as f:
        for t in teachers:
            f.write(f"{t['username']},{t['password']},{t['classroom']}\n")

    # Save classrooms
    with open(classrooms_file, "w") as f:
        for c in classrooms:
            f.write(c + "\n")

# =============================
# Authentication
# =============================

def login():
    print("===== Student Management System =====")
    print("1. Admin Login")
    print("2. Teacher Login")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        user = input("Username: ")
        pwd = input("Password: ")
        if user == "admin" and pwd == "123":
            admin_menu()
        else:
            print("Wrong login!")
            login()

    elif choice == "2":
        user = input("Teacher Username: ")
        pwd = input("Password: ")
        for t in teachers:
            if t["username"] == user and t["password"] == pwd:
                teacher_menu(t)
                return
        print("Wrong login!")
        login()
    else:
        exit()

# =============================
# Admin Menu
# =============================

def admin_menu():
    while True:
        print("\n===== Admin Menu =====")
        print("1. Manage Classrooms")
        print("2. Manage Teachers")
        print("3. Manage Students")
        print("4. Manage Scores")
        print("5. Generate Reports")
        print("6. View Statistics")
        print("7. Ranking & Pass/Fail")
        print("8. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            manage_classrooms()
        elif choice == "2":
            manage_teachers()
        elif choice == "3":
            manage_students()
        elif choice == "4":
            enter_scores()
        elif choice == "5":
            view_reports()
        elif choice == "6":
            statistics()
        elif choice == "7":
            ranking_and_passfail()
        elif choice == "8":
            save_data()
            login()
        else:
            print("Invalid choice!")

# =============================
# Teacher Menu
# =============================

def teacher_menu(teacher):
    while True:
        print(f"\n===== Teacher Menu (Class: {teacher['classroom']}) =====")
        print("1. View My Students")
        print("2. Enter/Update Scores")
        print("3. Generate Report Card")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            for s in students:
                if s["classroom"] == teacher["classroom"]:
                    print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Scores: {s['scores']}")
        elif choice == "2":
            enter_scores(teacher["classroom"])
        elif choice == "3":
            for s in students:
                if s["classroom"] == teacher["classroom"]:
                    print(f"\nReport for {s['name']} (ID: {s['id']})")
                    for subj, score in s["scores"].items():
                        print(f"  {subj}: {score}")
        elif choice == "4":
            save_data()
            login()
        else:
            print("Invalid choice!")

# =============================
# Classroom Management
# =============================

def manage_classrooms():
    while True:
        print("\n--- Classroom Management ---")
        print("1. Add Classroom")
        print("2. Edit Classroom")
        print("3. Delete Classroom")
        print("4. List Classrooms")
        print("5. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            cname = input("Enter classroom name: ")
            classrooms.append(cname)
            save_data()
            print("Classroom added!")
        elif ch == "2":
            old = input("Enter old classroom name: ")
            new = input("Enter new name: ")
            if old in classrooms:
                classrooms[classrooms.index(old)] = new
                for s in students:
                    if s["classroom"] == old:
                        s["classroom"] = new
                for t in teachers:
                    if t["classroom"] == old:
                        t["classroom"] = new
                save_data()
                print("Updated!")
            else:
                print("Not found!")
        elif ch == "3":
            cname = input("Enter classroom to delete: ")
            if cname in classrooms:
                classrooms.remove(cname)
                save_data()
                print("Deleted!")
            else:
                print("Not found!")
        elif ch == "4":
            print("Classrooms:", classrooms)
        elif ch == "5":
            return

# =============================
# Teacher Management
# =============================

def manage_teachers():
    while True:
        print("\n--- Teacher Management ---")
        print("1. Add Teacher")
        print("2. Edit Teacher")
        print("3. Delete Teacher")
        print("4. List Teachers")
        print("5. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            u = input("Enter username: ")
            p = input("Enter password: ")
            c = input("Assign classroom: ")
            teachers.append({"username": u, "password": p, "classroom": c})
            save_data()
            print("Teacher added!")
        elif ch == "2":
            u = input("Enter username to edit: ")
            for t in teachers:
                if t["username"] == u:
                    t["password"] = input("New password: ")
                    t["classroom"] = input("New classroom: ")
                    save_data()
                    print("Updated!")
                    return
            print("Not found!")
        elif ch == "3":
            u = input("Enter username to delete: ")
            for t in teachers:
                if t["username"] == u:
                    teachers.remove(t)
                    save_data()
                    print("Deleted!")
                    return
            print("Not found!")
        elif ch == "4":
            for t in teachers:
                print(f"Username: {t['username']} | Classroom: {t['classroom']}")
        elif ch == "5":
            return

# =============================
# Student Management
# =============================

def manage_students():
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Edit Student")
        print("5. Delete Student")
        print("6. Back")
        ch = input("Enter choice: ")

        if ch == "1":
            sid = input("Enter ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            c = input("Enter classroom: ")
            student = {"id": sid, "name": name, "age": age, "classroom": c, "scores": {}}
            students.append(student)
            save_data()
            print("Student added!")
        elif ch == "2":
            for s in students:
                print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Class: {s['classroom']}")
        elif ch == "3":
            keyword = input("Enter student ID or Name: ").lower()
            for s in students:
                if keyword == s["id"].lower() or keyword in s["name"].lower():
                    print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Class: {s['classroom']} | Scores: {s['scores']}")
        elif ch == "4":
            sid = input("Enter student ID to edit: ")
            for s in students:
                if s["id"] == sid:
                    s["name"] = input("New name: ")
                    save_data()
                    print("Updated!")
                    return
            print("Not found!")
        elif ch == "5":
            sid = input("Enter student ID to delete: ")
            for s in students:
                if s["id"] == sid:
                    students.remove(s)
                    save_data()
                    print("Deleted!")
                    return
            print("Not found!")
        elif ch == "6":
            return

# =============================
# Scores
# =============================

def enter_scores(classroom=None):
    sid = input("Enter student ID: ")
    for s in students:
        if s["id"] == sid and (classroom is None or s["classroom"] == classroom):
            subject = input("Enter subject: ")
            score = int(input("Enter score: "))
            s["scores"][subject] = score
            save_data()
            print("Score saved!")
            return
    print("Student not found")
# Load datad or not in your class!")

# =============================
# Reports
# =============================

def view_reports():
    for s in students:
        print(f"\nReport for {s['name']} (ID: {s['id']}, Class: {s['classroom']})")
        if not s["scores"]:
            print("  No scores yet.")
        else:
            for subj, score in s["scores"].items():
                print(f"  {subj}: {score}")

# =============================
# Statistics
# =============================

def statistics():
    if not students:
        print("No students available!")
        return

    total, count = 0, 0
    subject_totals, subject_counts = {}, {}

    for s in students:
        for subj, sc in s["scores"].items():
            total += sc
            count += 1
            subject_totals[subj] = subject_totals.get(subj, 0) + sc
            subject_counts[subj] = subject_counts.get(subj, 0) + 1

    if count == 0:
        print("No scores yet!")
    else:
        avg = total / count
        print(f"Overall Average Score: {avg:.2f}")

        best_subj, worst_subj = None, None
        best_avg, worst_avg = -1, 101

        for subj in subject_totals:
            subj_avg = subject_totals[subj] / subject_counts[subj]
            print(f"{subj} Average: {subj_avg:.2f}")

            if subj_avg > best_avg:
                best_avg, best_subj = subj_avg, subj
            if subj_avg < worst_avg:
                worst_avg, worst_subj = subj_avg, subj

        print(f"Best Performing Subject: {best_subj} ({best_avg:.2f})")
        print(f"Worst Performing Subject: {worst_subj} ({worst_avg:.2f})")

# =============================
# Ranking & Pass/Fail
# =============================

def ranking_and_passfail():
    if not students:
        print("No students available!")
        return

    rankings = []
    for s in students:
        if s["scores"]:
            avg = sum(s["scores"].values()) / len(s["scores"])
            rankings.append((avg, s))

    if not rankings:
        print("No scores entered yet!")
        return

    rankings.sort(reverse=True, key=lambda x: x[0])

    print("===== Student Rankings =====")
    for i, (avg, s) in enumerate(rankings, 1):
        print(f"{i}. {s['name']} (ID: {s['id']}, Class: {s['classroom']}) - Average: {avg:.2f}")

    passed = sum(1 for avg, _ in rankings if avg >= 50)
    failed = len(rankings) - passed
    total = len(rankings)

    if total > 0:
        print(f"\nPass Rate: {(passed/total)*100:.2f}% | Fail Rate: {(failed/total)*100:.2f}%")

# =============================
# Main
# =============================

load_data()
login()




