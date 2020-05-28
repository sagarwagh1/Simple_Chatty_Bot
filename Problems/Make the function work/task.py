"""
The function closest_mod_5 takes exactly one integer argument x and returns the smallest integer y such that:
y is greater than or equal to x,
y is divisible by 5.
"""
# put your python code here

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return x + (5 - (x % 5))
