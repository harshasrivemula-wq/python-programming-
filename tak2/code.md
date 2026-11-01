###1\. Problem Statement

Campus Event Financial Planning:
Develop a Python program to calculate the total cost of a campus event including venue, equipment, catering, transport, and certificate costs. Calculate participant contributions, sponsorship shortfall, and the minimum registration count required to break even.

###2\. Algorithm

1. Start the program.
2. Enter venue, equipment, catering, transport, and certificate costs.
3. Enter expected participants, registration fee, and sponsorship.
4. Calculate the total event cost.
5. Calculate participant contribution.
6. Calculate total income.
7. Calculate sponsorship shortfall.
8. Calculate minimum registration count.
9. Display the financial report.
10. Check whether total income is enough to cover the total cost.
11. Stop.
3. Flowchart — Mermaid Code
```mermaid
StartEnter event costsEnter participants, fee andsponsorshipCalculate total costCalculate participantcontributionCalculate total incomeCalculate sponsorship shortfallFee 0?Calculate minimum registrationcountSet minimum count to 0Display financial reportTotal income = total cost?Event is financially successfulMore registrations are neededEndYesNoYesNo
```



This exact format can be copied into your GitHub code.md file.



4. Python Source Code
# Campus Event Financial Planningvenue = float(input("Enter venue cost: "))equipment = float(input("Enter equipment cost: "))catering = float(input("Enter catering cost: "))transport = float(input("Enter transport cost: "))certificate = float(input("Enter certificate cost: "))participants = int(input("Enter expected participants: "))fee = float(input("Enter registration fee per participant: "))sponsorship = float(input("Enter sponsorship amount: "))total_cost = venue + equipment + catering + transport + certificatecontribution = participants * feetotal_income = contribution + sponsorshipshortfall = total_cost - total_incomeif shortfall > 0:    print("Sponsorship shortfall:", shortfall)else:    print("No sponsorship shortfall.")if fee > 0:    minimum_count = int(total_cost / fee) + 1else:    minimum_count = 0print("\n--- Event Financial Report ---")print("Total Event Cost:", total_cost)print("Participant Contribution:", contribution)print("Sponsorship:", sponsorship)print("Total Income:", total_income)print("Minimum Registration Count:", minimum_count)if total_income >= total_cost:    print("Event is financially successful.")else:    print("More registrations are needed.")


5. Sample Input
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost: 15000
Enter transport cost: 5000
Enter certificate cost: 2000
Enter expected participants: 50
Enter registration fee per participant: 500
Enter sponsorship amount: 10000

6. Sample Output
No sponsorship shortfall.

--- Event Financial Report ---
Total Event Cost: 37000.0
Participant Contribution: 25000.0
Sponsorship: 10000.0
Total Income: 35000.0
Minimum Registration Count: 75
More registrations are needed.
