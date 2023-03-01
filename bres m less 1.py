def bres(x1,y1,x2,y2):
    
    dy = y2 - y1
    dx = x2 - x1
    p_not = (2*dy) - dx

    for i in range(10):
        if p_not>=0:
            p_not  = p_not + 2 * (dy-dx)
            ny = y1 + 1
        else:
            p_not = p_not + 2*dy

        print(p_not)
        # p_not = np_not
        nx = x1 + 1
        # print(nx, ny)


bres(1,4,11,11)