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
print "write your required error,example 0.001"
required_error = float(raw_input('required error: '))
current_error = 99
old_value = 0
solution = 0

while(required_error<current_error):
    xr = (xa+xb)/2
    fxa = expr.subs(x,xa)
    fxr = expr.subs(x,xr)
    if(fxa*fxr>0):
        xa = xr
    else:
        xb = xr
    if(old_value!=0):
        if(xr!=0):
            current_error = abs((xr-old_value)/xr)
            solution = xr
        else:
            solution = 0
            current_error=0
    old_value = xr
print "The solution is: "
print solution
