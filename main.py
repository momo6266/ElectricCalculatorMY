def calculate_electric_tariff(kwh_consumed, rate):
    total_cost = kwh_consumed * rate
    return total_cost

shared_meter_cost = 0.00
individual_meter_cost = 0.00
remaining_individual_meter_kwh = 0.00
individual_meter_user = {}
individual_meter_kwh = {}

rate_tiers = [(0.218, 200), (0.334, 100), (0.516, 300), (0.546, 300), (0.571, 0)]

total_meter_kwh = float(input("Enter total meter consumption (kWh): "))

num_users = int(input("Enter the number of users: "))

for user in range(1, num_users + 1):
    individual_meter_kwh[user] = float(input(f"Enter individual meter consumption for User {user} (kWh): "))
    remaining_individual_meter_kwh += individual_meter_kwh[user]

fee = float(input("Enter any other fee: RM "))
discount = float(input("Enter the discount amount: RM "))

shared_meter_kwh = total_meter_kwh - remaining_individual_meter_kwh
remaining_shared_meter_kwh = shared_meter_kwh

last_shared_meter_index = -1
for index, (rate, limit) in enumerate(rate_tiers):
    if remaining_shared_meter_kwh > 0:
        shared_meter_quota = min(remaining_shared_meter_kwh, limit)
        shared_meter_cost += calculate_electric_tariff(shared_meter_quota, rate)
        remaining_shared_meter_kwh -= shared_meter_quota
        last_shared_meter_index = index
        if shared_meter_quota == 0:
            remaining_shared_meter_kwh = shared_meter_quota
            break
for user in range(1, num_users + 1):
    individual_meter_user[user] = individual_meter_kwh[user] / remaining_individual_meter_kwh

for index in range(last_shared_meter_index, len(rate_tiers)):
    rate, limit = rate_tiers[index]
    if remaining_individual_meter_kwh > 0:
        individual_meter_quota = min(remaining_individual_meter_kwh, limit - remaining_shared_meter_kwh)
        individual_meter_cost += calculate_electric_tariff(individual_meter_quota, rate)
        remaining_individual_meter_kwh -= individual_meter_quota

total_cost = shared_meter_cost + individual_meter_cost

print(f"\nShared Meter Electricity cost: RM {shared_meter_cost:.2f}")
print(f"Total Meter Electricity cost: RM {total_cost:.2f}")
print(f"Other fee: RM {fee:.2f}")
print(f"Discount amount: RM {discount:.2f}\n")
print(f"Final amount: RM {total_cost + fee - discount:.2f}\n")

for user, cost in individual_meter_user.items():
    print(
        f"Electricity cost for User {user}: RM {(shared_meter_cost / num_users) + (cost * individual_meter_cost) + (fee /num_users) - (discount / num_users):.2f}")

input("\nPress Enter to exit...")