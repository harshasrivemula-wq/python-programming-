# Manufacturing Cost and Profitability Analysis

products = ["Product A", "Product B", "Product C"]

material_cost = [5000, 7000, 6000]
labour_cost = [2000, 2500, 2200]
wastage = [500, 700, 400]
machine_cost = [1500, 1800, 1600]
selling_price = [11000, 14000, 11500]

profit_target = 1500

for i in range(len(products)):
    print("\nProduct:", products[i])

    total_cost = (material_cost[i] + labour_cost[i] +
                  wastage[i] + machine_cost[i])

    profit = selling_price[i] - total_cost

    print("Material Cost:", material_cost[i])
    print("Labour Cost:", labour_cost[i])
    print("Wastage Cost:", wastage[i])
    print("Machine Cost:", machine_cost[i])
    print("Total Production Cost:", total_cost)
    print("Selling Price:", selling_price[i])
    print("Profit:", profit)

    if profit >= profit_target:
        print("Profit Target: Achieved")
    else:
        print("Profit Target: Not Achieved")

print("\nOverall Analysis")

total_material = sum(material_cost)
total_labour = sum(labour_cost)
total_wastage = sum(wastage)
total_machine = sum(machine_cost)
total_sales = sum(selling_price)

total_cost = (total_material + total_labour +
              total_wastage + total_machine)

total_profit = total_sales - total_cost

print("Total Production Cost:", total_cost)
print("Total Selling Price:", total_sales)
print("Total Profit:", total_profit)