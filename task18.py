def square_values(numbers: list) -> list:
    return list(map(lambda x: {'value': x['value'] ** 2}, numbers))


print(square_values([{'value': 2}, {'value': 3}, {'value': 4}]))

