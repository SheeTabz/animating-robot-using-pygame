import decimal


def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx/steps
    y_inc = dy/steps

    x = x1
    y = y1
    maxi = max(abs(dx), abs(dy))
    print(f"The gradient is {dy/dx}")

    while maxi+1>0:
        new_x = decimal.Decimal(x).quantize(decimal.Decimal('1'), rounding = decimal.ROUND_HALF_UP)
        new_y = decimal.Decimal(y).quantize(decimal.Decimal('1'), rounding = decimal.ROUND_HALF_UP)
        print(new_x, new_y)

        x = x + x_inc
        y = y + y_inc
        maxi-=1

dda(0,0,10,8)