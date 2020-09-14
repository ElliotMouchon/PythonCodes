class Fraction:
    
    def GCD(num, den):
        high = max(num, den)
        low = min (num, den)
        while high % low != 0:
            mem = high
            high = low
            low = mem % low
        return low
        
    
    def __init__(self, numerator = 0, denominator = 1):
        
        gcd = Fraction.GCD(numerator, denominator)
            
        self.num = numerator / gcd
        self.den = denominator / gcd
        
    def __add__(self, otherFrac):
        numH = self.num * otherFrac.den + otherFrac.num * self.den
        denH = self.den * otherFrac.den
        gcd = Fraction.GCD(numH, denH)
        return Fraction(numH / gcd, denH / gcd)
        
    def __mul__(self, otherFrac):
        numH = self.num * otherFrac.num
        denH = self.den * otherFrac.den
        gcd = Fraction.GCD(numH, denH)
        return Fraction(numH / gcd, denH / gcd)
        
    def __truediv__(self, otherFrac):
        numH = self.num * otherFrac.den
        denH = self.den * otherFrac.num
        gcd = Fraction.GCD(numH, denH)
        return Fraction(numH / gcd, denH / gcd)    
        
    def __sub__(self, otherFrac):
        numH = self.num * otherFrac.den - otherFrac.num * self.den
        denH = self.den * otherFrac.den
        gcd = Fraction.GCD(numH, denH)
        return Fraction(numH / gcd, denH / gcd)
        
    def __pow__(self, exp):
        numH = self.num ** exp
        denH = self.den ** exp
        return Fraction(numH, denH)

        
    def __repr__(self):
        return "{}/{}".format(self.num, self.den)
        

                