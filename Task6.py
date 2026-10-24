# University Hostel Room Allocation

room_no = ["R101", "R102", "R103", "R104"]
capacity = [2, 3, 2, 3]
room_type = ["Boys", "Girls", "Boys", "Girls"]

students = [
    ["S01", "Boys", "A"],
    ["S02", "Boys", "A"],
    ["S03", "Girls", "B"],
    ["S04", "Girls", "B"],
    ["S05", "Boys", "A"],
    ["S06", "Girls", "C"],
    ["S07", "Boys", "C"]
]

allocated = []
unallocated = []

for student in students:
    sid = student[0]
    gender = student[1]
    group = student[2]
    assigned = False

    for i in range(len(room_no)):
        if room_type[i] == gender:
            count = 0

            for a in allocated:
                if a[0] == room_no[i]:
                    count = count + 1

            if count < capacity[i]:
                allocated.append([room_no[i], sid, group])
                assigned = True
                break

    if assigned == False:
        unallocated.append(sid)

print("Hostel Room Allocation")

for room in room_no:
    print("\n", room)
    for a in allocated:
        if a[0] == room:
            print("Student:", a[1], "Group:", a[2])

print("\nUnallocated Students:", unallocated)
print("Unallocated Demand:", len(unallocated))