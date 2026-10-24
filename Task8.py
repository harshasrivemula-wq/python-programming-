# Attendance Recovery Computation

students = ["Harsha", "Karthik", "Anu", "Ravi"]

attended = [32, 28, 35, 25]
total_classes = [40, 40, 45, 35]

threshold = 75

for i in range(len(students)):
    percentage = (attended[i] / total_classes[i]) * 100

    print("\nStudent:", students[i])
    print("Current Attendance:", percentage, "%")

    if percentage >= threshold:
        print("Status: Eligible")
        print("Extra classes required: 0")
        continue

    required = 0
    future_attended = attended[i]
    future_total = total_classes[i]

    while (future_attended / future_total) * 100 < threshold:
        future_attended = future_attended + 1
        future_total = future_total + 1
        required = required + 1

    print("Minimum consecutive classes required:", required)

    for scenario in [1, 2, 3]:
        if scenario == 1:
            extra = 5
        elif scenario == 2:
            extra = 10
        else:
            extra = 15

        new_percentage = ((attended[i] + extra) /
                          (total_classes[i] + extra)) * 100

        print("After", extra, "classes:", new_percentage, "%")