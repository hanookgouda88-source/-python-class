battery = 100

for i in range(5):
    battery -= 10
    print("Battery:", battery)

if battery < 50:
    print("Low battery")
else:
    print("Battery is OK")