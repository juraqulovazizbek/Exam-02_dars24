def atm_operation(balance: int, action: str, amount: int) -> dict:
 

    action = action.lower()

    
    if amount <= 0:
        return {"error": "Xato: summa musbat bo‘lishi kerak"}

    if action == "deposit":
        balance += amount
    elif action == "withdraw":
        if amount > balance:
            return {"error": "Xato: balans yetarli emas"}
        balance -= amount
    else:
        return {"error": "Xato: noto‘g‘ri amal kiritildi"}

    return {"balance": balance}

print(atm_operation(100000, "withdraw", 150000))