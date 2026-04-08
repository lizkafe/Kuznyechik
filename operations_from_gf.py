from sympy import *
import sympy as sp

def mod(poly, p):
    x = Symbol('x')
    coeff = Poly(poly, x).all_coeffs()
    for i in range (len(coeff)):
        coeff[i] = coeff[i] % p
    new_poly = Poly (coeff, x)
    mult = new_poly.as_expr()
    return mult

def multiply(poly1, poly2, n, irred_poly):
    p = 2
    irred_poly = sp.sympify(irred_poly)

    result = poly1 * poly2

    if degree(result) <= (n - 1):
        ready_res = mod(result, p)
        return ready_res
    else:
        while degree(result) > (n - 1):
            result = div(result, irred_poly)[1]
        ready_res = mod(result, p)
        return ready_res
    
def add_up(poly1, poly2):
    p = 2 
    result = poly1 + poly2
    ready_res = mod(result, p)
    return ready_res
       


    

        
# x = Symbol('x')
# coeffs = [0, 0, 1, 1, 0, 0, 0, 0]
# # coeffs = [1] + [randint(0, 2-1) for _ in range(8)] 
# polyn = Poly(coeffs, x, modulus=2)
# print(polyn.as_expr())

