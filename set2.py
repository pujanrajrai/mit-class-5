natural_number = {1, 2, 3, 4, 5, 6, 6, 6, "6"}
print(natural_number)
print()
odd_no = {1, 3, 5, 7}
even_no = {2, 4, 6, 8}
whole_no = {0, 1, 2, 3, 4, 5, 6, 7, 8}

print(odd_no.union(even_no))
print(odd_no | even_no)

print(odd_no.intersection(even_no))
print(odd_no.intersection(whole_no))
print()
print(odd_no.difference(even_no))
