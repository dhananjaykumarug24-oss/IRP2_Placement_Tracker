

# ==========================================
# IRP-II: Placement Readiness Tracker
# Tasks 1 and 2
# ==========================================

# Student records using a list of dictionaries

students = [
    {
        "name": "Dhananjay Kumar",
        "roll": 2481026,
        "aptitude": 95,
        "verbal": 88,
        "coding": 99
    },
    {
        "name": "Akash Sivanandan",
        "roll": 2481022,
        "aptitude": 82,
        "verbal": 72,
        "coding": 90
    },
    {
        "name": "Girish Khanna",
        "roll": 2481150,
        "aptitude": 85,
        "verbal": 80,
        "coding": 87
    },
    {
        "name": "Soumen Kumar Dutta",
        "roll": 2481248,
        "aptitude": 91,
        "verbal": 85,
        "coding": 87
    },
    {
        "name": "Pulkit",
        "roll": 2481135,
        "aptitude": 77,
        "verbal": 92,
        "coding": 88
    }
]


# Function 1: Calculate average

def average(student):
    total = (
        student["aptitude"]
        + student["verbal"]
        + student["coding"]
    )

    return total / 3


# Function 2: Calculate grade

def grade(avg):

    if avg >= 80:
        return "A"

    elif avg >= 60:
        return "B"

    elif avg >= 40:
        return "C"

    else:
        return "Needs practice"


# Function 3: Find top scorer

def top_scorer(students):

    return max(students, key=average)


# Function 4: Find students needing practice

def needs_practice(students, limit=40):

    result = []

    for student in students:

        if average(student) < limit:
            result.append(student)

    return result


# Function 5: Take additional student input

def add_student():

    print("\nEnter New Student Details")

    name = input("Enter student name: ")

    roll = int(input("Enter roll number: "))

    scores = {}

    subjects = ["aptitude", "verbal", "coding"]

    for subject in subjects:

        while True:

            try:
                score = int(
                    input(f"Enter {subject} score (0-100): ")
                )

                if 0 <= score <= 100:
                    scores[subject] = score
                    break

                else:
                    print("Score must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid integer.")

    new_student = {
        "name": name,
        "roll": roll,
        "aptitude": scores["aptitude"],
        "verbal": scores["verbal"],
        "coding": scores["coding"]
    }

    return new_student


# Add one student through input()

new_student = add_student()

students.append(new_student)


# Display all student records

print("\n========== STUDENT REPORT ==========")

for student in students:

    avg = average(student)

    student_grade = grade(avg)

    print("\nName:", student["name"])
    print("Roll No:", student["roll"])
    print("Aptitude:", student["aptitude"])
    print("Verbal:", student["verbal"])
    print("Coding:", student["coding"])
    print("Average:", round(avg, 2))
    print("Grade:", student_grade)


# Display top scorer

top = top_scorer(students)

print("\n========== TOP SCORER ==========")

print("Name:", top["name"])
print("Average:", round(average(top), 2))


# Display students needing practice

practice_students = needs_practice(students)

print("\n========== NEEDS PRACTICE ==========")

print("Number of students needing practice:",
      len(practice_students))

for student in practice_students:
    print(student["name"])
