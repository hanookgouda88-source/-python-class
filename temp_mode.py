temperature = 30

if temperature < 20:
    mode = "Cold"
elif temperature <= 30:
    mode = "Normal"
else:
    mode = "Hot"

print("Temperature:", temperature)
print("Mode:", mode)