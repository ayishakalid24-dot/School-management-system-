# 📚 Student Management System (SMS)

A **Python-based Student Management System** designed to manage students, teachers, and classroom activities.  
This project helps **organize educational records, track attendance, and streamline communication** between students and teachers.

---

## 🚀 Features

### 🎓 Classroom Management (Super Admin only)
- ➕ Add Classroom (set class name + subjects)  
- ✏️ Edit Classroom (rename class, update subjects)  
- ❌ Delete Classroom  
- 📋 List All Classrooms (show subjects + student count)  

### 👨‍🏫 Teacher Management (Super Admin only)
- 🆕 Create Teacher Account (username, password, assign to classroom)  
- 🔄 Edit Teacher Account (reset password, reassign classroom)  
- 🗑️ Delete Teacher Account  
- 📌 List All Teachers (with assigned classroom)  

### 🧑‍🎓 Student Management (Admin & Teacher – Teacher restricted to their class)
- ➕ Add Student (ID, name, age → stored in assigned classroom)  
- ✏️ Edit Student Info (name, age)  
- ❌ Delete Student  
- 👀 View Students in Classroom (list of all students in that class)  
- 🔍 Search Student (by ID or name)  
- 🔄 Move Student between Classrooms (Admin only)  

### 📘 Subject & Score Management
- 📝 Assign Subjects to Classrooms (admin sets subject list per class)  
- ✍️ Enter Student Scores (teacher assigns scores subject-wise)  
- 🔄 Update Scores (modify previous scores)  
- ✅ Validate Scores (only subjects from that classroom allowed)  

### 📊 Report Cards & Rankings
- 📑 Generate Individual Report Card (per student)  
- 📂 Generate Classroom Report Card (all students, averages, grades, ranks)  
- 🏆 Rank Students in Classroom (based on average scores)  
- 🌟 Highlight Top & Lowest Performer in each class  

### 📈 Statistics
- 📊 Calculate Class Average per Subject  
- 📉 Calculate Overall Class Average  
- ✅ Pass/Fail Rate per Subject & per Class  
- 🥇 Best/Worst Performing Subject in Class  

### 🔐 Authentication & Access Control
- 🔑 Login System (username & password)  
- 👥 Role-based Access:
  - **Admin →** Full system menu  
  - **Teacher →** Only assigned classroom menu  

---

## 🛠️ Tech Stack
- **Language:** Python  

---

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ayishakalid24-dot/School-management-system-.git 
