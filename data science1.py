import numpy as np

data_type = [('name', 'S10'), ('class', int), ('height', float)]

students_details = [('Henry', 10, 50.8), ('Alice', 9, 42.5), ('Bob', 11, 55.2), ('Diana', 12, 60.1)]


students = np.array(students_details, dtype=data_type)
print("Oringal array:")
print(students)

print("Sort by height:")
print(np.sort(students, order='height'))