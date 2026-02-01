def calculate_discount(price, discount):
    if discount > 100:
        discount = 100
    return price - (price * discount)

def get_total(items):
    total = 0
    for item in items:
        total = total + item
    return total
