
import sys

vehicle_number = input("Enter vehicle number: ")
vehicle_type = input("Enter vehicle type (two wheeler/four wheeler/heavy vehicle): ")
hours = float(input("Enter parking duration in hours: "))

if vehicle_type == "two wheeler":
    rate = 20
elif vehicle_type == "four wheeler":
    rate = 50
elif vehicle_type == "heavy vehicle":
    rate = 100
else:
    print("Invalid vehicle type")
    sys.exit()

fee = rate * hours

print("\n--- Parking Receipt ---")
print("Vehicle Number:", vehicle_number)
print("Vehicle Type:", vehicle_type)
print("Parking Duration:", hours, "hours")
print("Total Parking Fee: Rs.", fee)
