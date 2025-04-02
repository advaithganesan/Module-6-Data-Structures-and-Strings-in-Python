
student_marks = {
    "Alice": 85,
    "Arjun": 92,
    "Preethi": 78,
    "Diana": 90
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student named {student_name} not found.")
