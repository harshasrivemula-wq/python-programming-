# Examination Seating Validation

seating = [
    ["101", "102", "RESERVED", "104"],
    ["105", "", "107", "108"],
    ["109", "110", "111", "102"]
]

valid_students = ["101", "102", "104", "105", "107",
                  "108", "109", "110", "111", "112"]

seen = []

for row in seating:
    for seat in row:

        # Check empty seats
        if seat == "":
            print("Empty seat found")

        # Check reserved seats
        elif seat == "RESERVED":
            print("Reserved position found")

        # Check valid student
        elif seat not in valid_students:
            print("Invalid student:", seat)

        # Check duplicate roll number
        elif seat in seen:
            print("Duplicate roll number:", seat)

        else:
            seen.append(seat)

print("\n----- SEATING REPORT -----")
print("Valid students:", seen)
print("Total seats:", len(seating) * len(seating[0]))

empty = 0
for row in seating:
    for seat in row:
        if seat == "":
            empty = empty + 1

print("Empty seats:", empty)
print("Seating validation completed.")