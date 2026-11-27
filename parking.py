vehicle_type = input("Enter vehicle type (Two wheeler/Fourwheeler/Heavy vehicle): ")
parking_hours = float(input("Enter parking duration in hours: "))

if vehicle_type.lower() == "two wheeler":
    rate = 20
elif vehicle_type.lower() == "four wheeler":
    rate = 50
elif vehicle_type.lower() == "heavy vehicle":
    rate = 100
else:
    print("Invalid vehicle type")
    exit()

parking_fee = rate * parking_hours

print("\n--- Parking Receipt ---")
print("Vehicle Type:", vehicle_type)
print("Parking Duration:", parking_hours, "hours")
print("Total Parking Fee: Rs.", parking_fee)