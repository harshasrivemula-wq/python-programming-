seats = [
    ["A1", "A2", "A3", "A4"],
    ["B1", "B2", "B3", "B4"],
    ["C1", "C2", "C3", "C4"]
]

registered = ["ST101", "ST102", "ST103", "ST104"]
entered = []

print("----- EVENT ENTRY -----")

for i in range(len(registered)):
    ticket = input("Enter ticket ID: ")

    if ticket not in registered:
        print("Invalid ticket!")
        
    elif ticket in entered:
        print("Duplicate entry!")
        
    else:
        entered.append(ticket)
      
        row = (len(entered) - 1) // 4
        col = (len(entered) - 1) % 4

        if row < len(seats):
            print("Entry allowed - Seat:", seats[row][col])
        else:
            print("No seat available!")

total = 0
for row in seats:
    total = total + len(row)

available = total - len(entered)

print("\n----- SUMMARY -----")
print("Total seats:", total)
print("Entries:", len(entered))
print("Available seats:", available)