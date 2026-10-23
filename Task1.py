students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    subject = float(input("Enter minimum subject marks: "))
    attendance = float(input("Enter attendance: "))
    income = float(input("Enter family income: "))

    # Check eligibility
    if marks >= 75 and subject >= 60 and attendance >= 75 and income <= 300000:
        students.append([name, marks, subject, attendance, income])

# Ranking students
students.sort(key=lambda x: (-x[1], -x[3], x[4]))

# Display result
print("\n----- SCHOLARSHIP RESULT -----")

if len(students) == 0:
    print("No student is eligible.")

else:
    for i in range(len(students)):
        print("\nRank:", i + 1)
        print("Name:", students[i][0])
        print("Marks:", students[i][1])
        print("Attendance:", students[i][3])
        print("Income:", students[i][4])