def apply_discount(price, discount_pct):
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    return price * (1 + tax_pct / 100)

def final_price(price, quantity, discount_pct, tax_pct):
    subtotal = price * quantity
    descuento = apply_discount(subtotal, discount_pct)
    impuesto = apply_tax(descuento, tax_pct)
    return round(impuesto, 2)

def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    A = final_price(price_a, qty_a, disc_a, tax_pct)
    B = final_price(price_b, qty_b, disc_b, tax_pct)
    # Si B es menor, gana B. En cualquier otro caso (incluyendo empate), gana A.
    if B < A:
        return "B"
    else:
        return "A"
    elif A>B:
        return "B"
    elif A==B:
        return "A"
