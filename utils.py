def calculate_discount(price, discount):
    if discount > 100:
        discount = 100
    return price - (price * discount / 100)

def get_total(items):
    return sum(items)