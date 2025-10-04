def count_words(text: str) -> dict:
    words = text.lower().split()
    result = {}
    for w in words:
        result[w] = result.get(w, 0) + 1
    return result

print(count_words("Python python PYTHON"))
