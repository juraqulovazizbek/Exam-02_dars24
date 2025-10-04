def analyze_grades(students: dict) -> dict:
    
 
    average = sum(students.values()) / len(students)

   
    avg = []
    for name, grade in students.items():
        if grade > average:
            avg.append(name)

    return {
        "average": round(average, 2),   
        "above_average": avg
    }

print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))