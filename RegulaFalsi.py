#Eduardo Reyes Oyarzo
#python 2.7

from sympy import *
x = symbols("x")
print "write your function,example x**4+3*x**3-2"
function = raw_input('f(x)= ')
expr = sympify(function)
plot(expr,(x,-3,3))
xa = float(raw_input('xa: ')) #fixed
xb = float(raw_input('xb: '))
print "write your required error,example 0.001"
required_error = float(raw_input('required error: '))
current_error = 99
old_value = 0
fxa=expr.subs(x,xa) #fixed
fxb=expr.subs(x,xb)
solution = 0
n_iterations = 0
while(required_error<current_error):    
    mi = (xb-xa)/(fxb-fxa)
    xr = xb-(fxb*mi)
    fxr = expr.subs(x,xr)
    if(old_value!=0):
        if(xr!=0):
            current_error = abs((xr-old_value)/xr)
            solution = xr
        else:
            solution = "error by division at zero"
            break;
    old_value = xr
    xb = xr
    fxb = expr.subs(x,xb)
    n_iterations = n_iterations +1
print "The solution is: "
print solution
print "Iterations: "
print n_iterations