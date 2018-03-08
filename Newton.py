#Eduardo Reyes Oyarzo
#python 2.7

from sympy import *
x = symbols("x")
print "write your function,example x**4+3*x**3-2"
function = raw_input('f(x)= ')
expr = sympify(function)
expr_d = diff(expr,x)
plot(expr,(x,-3,3))
xa = float(raw_input('xa: '))
fxa=expr.subs(x,xa)
fpxa = expr_d.subs(x,xa)
n_iteration = 0
while(True):
    xr = xa - (fxa/fpxa)
    if(expr.subs(x,xr)==0.0):
        solution = xr
        break
    else:
        xa = xr
        fxa = expr.subs(x,xr)
        fpxa = expr_d.subs(x,xr)
    n_iteration = n_iteration +1
print solution
print n_iteration
    

