capital_city = {
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "Bangaladesh": "Dhaka"
}

print(capital_city.keys())
print()

print(capital_city.values())
print()

print(capital_city.items())
print()

for values in capital_city.values():
    print(values)
print()

for values in capital_city.keys():
    print(values)
print()

for key, values in capital_city.items():
    print(f"{key}:{values}")
print()
