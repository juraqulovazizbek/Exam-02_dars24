def calculate_stats(numbers: list) -> dict:
 
        jami = sum(numbers)
        urtacha = round(jami / len(numbers), 2) if numbers else 0

        return {
        "sum": jami,
        "average": urtacha
    }

print(calculate_stats([3, 7, 10, -5, -8, 15, 22]))
