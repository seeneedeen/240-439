# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    diffy = abs(z-y)
    diffx = abs(z-x)
    if diffx >diffy:
        return "Cat B"
    elif diffx<diffy:
        return "Cat A"
    else:
        return "Mouse C"