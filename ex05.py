name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = str(height * 2.54) # height in cm
weight = 180 # lbs
weight_kg = str(weight * 2.2) # weight in kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches, or {height_cm} centimeters tall.")
print(f"He weighs {weight} pounds, or {weight_kg} kilograms.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")

print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
