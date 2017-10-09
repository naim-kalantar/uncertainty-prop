# uncertainty-prop
A python class for measurements. Allows propagation of uncertainties under arithmetic and user-defined functions

##### Basic Use:
run `python` in the same folder you've saved the file
```
import prop
mass = prop.measure(50, 1)
mass 
>>> 50 ± 1

mass2 = prop.measure(50, 3)
mass2
>>> 50 ± 3

mass + mass2
>>> 100 ± 3.16...

mass * mass2
>>> 2500 ± 158.113...

mass + 1
>>> 51 ± 1

1 + mass
>>> This doesn't work yet. I haven't found a way to fix it.
```

##### Functions:
Give `prop.fun` a function and its derivative. Applying the function to `measure(x, s)` will return `f(x) ± s * |f'(x)|`
```
mass = prop.measure(50, 1)
def f(x):
  return x * 2
def f_derivative(x)
  return 2
F = prop.fun(f, f_derivative)
F(mass)
>>> 100 ± 2
```
