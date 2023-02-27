import decimal #library for rounding up numbers

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    m = dy/dx
    x = x1
    y = y1
    maxi = max(abs(dx), abs(dy))
    print(f"The gradient is {m}\n")

    while maxi>0:
        new_x = decimal.Decimal(x).quantize(decimal.Decimal('1'), rounding = decimal.ROUND_HALF_UP)
        new_y = decimal.Decimal(y).quantize(decimal.Decimal('1'), rounding = decimal.ROUND_HALF_UP)
        print(new_x, new_y)

        x = x + 1/m
        y = y + 1
        maxi-=1

dda(7,0,2,10)