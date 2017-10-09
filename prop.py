def addsub(uncert, other_uncert):
    a = (uncert ** 2)
    b = (other_uncert ** 2)
    return (a + b) ** 0.5
def divmult(value, uncert, other_value, other_uncert):
    a = (uncert / value) ** 2
    b = (other_value / other_uncert) ** 2
    return (a + b) ** 0.5


class fun:
    def __init__(self, f, f_prime):
        self.func = f
        self.deriv = f_prime
    def __call__(self, num):
        if not isinstance(num, measure):
            return self.func(other)
        result = measure()
        result.value = self.func(num.value)
        result.delt = num.delt * deriv(num.value)
        return result

class measure:
    value = 0
    delt = 0
    def __init__(self, val=0, uncertanty=0):
        self.value = val
        self.delt = uncertanty
    def __add__(self, other):
        if not isinstance(other, measure):
            other = measure(other, 0)
        result = measure()
        result.value = self.value + other.value
        result.delt = addsub(self.delt, other.delt)
        return result
    def __sub__(self, other):
        if not isinstance(other, measure):
            other = measure(other, 0)
        result = measure()
        result.value = self.value - other.value
        result.delt = addsub(self.delt, other.delt)
        return result
    def __mul__(self, other):
        if not isinstance(other, measure):
            other = measure(other, 0)
        result = measure()
        result.value = self.value * other.value
        result.delt = result.value * divmult(self.value, self.delt, other.value, other.delt)
        return result
    def __truediv__(self, other):
        if not isinstance(other, measure):
            other = measure(other, 0)
        result = measure()
        result.value = self.value / other.value
        result.delt = result.value * divmult(self.value, self.delt, other.value, other.delt)
        return result
    def __repr__(self):
        return str(self.value) + " ± " + str(self.delt)

pipe = {1:measure(1,.006), 5:measure(5,.01), 10:measure(10,.02), 20:measure(20,.03), 25:measure(25,.03), 50:measure(50,.05)}
flask = {25:measure(25,.03), 50:measure(50, .05), 100:measure(100, .08), 250:measure(250,.12), 500:measure(500,.15)}
