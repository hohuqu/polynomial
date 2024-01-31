# polynomial.py
class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
<<<<<<< HEAD
        repr_p1 = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Div)) else repr(self.p1)
        repr_p2 = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Div)) else repr(self.p2)
        return repr_p1 + " * " + repr_p2
=======

>>>>>>> 4243269310b94b2dfd62efa207ec773156cd4f8b

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return "( " + repr(self.p1) + " ) - ( " + repr(self.p2) + " )"

# Example usage
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)

division_poly = Div(poly, Add(Int(2), X()))
print(division_poly)

subtraction_poly = Sub(poly, Mul(Int(2), X()))
<<<<<<< HEAD
print(subtraction_poly)
=======

>>>>>>> 4243269310b94b2dfd62efa207ec773156cd4f8b
