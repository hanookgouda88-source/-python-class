packet = "TEMP:25"

parts = packet.split(":")

name = parts[0]
value = parts[1]

print("Name:", name)
print("Value:", value)