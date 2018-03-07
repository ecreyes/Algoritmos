#Eduardo Reyes Oyarzo
#python 2.7
from sympy import *
x = symbols("x")
print "write your function,example x**4+3*x**3-2"
function = raw_input('f(x)= ')
expr = sympify(function)
plot(expr,(x,-3,3))
xa = float(raw_input('xa: '))
xb = float(raw_input('xb: '))
solution = 0
fxa=expr.subs(x,xa)
fxb=expr.subs(x,xb)
if(fxa*fxb<0):
    while(true):
        xr = (xa+xb)/2
        fxa = expr.subs(x,xa)
        fxr = expr.subs(x,xr)
        if(fxr==0.0):
            solution = xr
            break;
        if(fxa*fxr>0):
            xa = xr
        else:
            xb = xr
    print "The solution is: "
    print solution
else:
    print "The algorithm is not compatible"