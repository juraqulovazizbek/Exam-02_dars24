def find_shortest_name_student(students: list) -> str:
    shortest = min(students, key=lambda x: len(x['name']))
    return {
        "name": shortest['name'],
        "age": shortest['age']
        }

students = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]

print(find_shortest_name_student(students))