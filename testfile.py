class svector:

    def __init__(self,vinp):
        if not (isinstance(vinp,list)):
            raise TypeError("Only flat vectors are accepted")
        if any(isinstance(x, list) for x in vinp):
            raise TypeError("Input must be a flat list.")
        self.vinp = vinp

    def norm(self,num):
        sum = 0
        for i in self.vinp:
            sum += (i**num)
        out = sum**(1/num)
        return(out)
    
    def vunit(self):
        unit = [i/self.norm(2) for i in self.vinp]
        return(unit)
    



x = svector([1,1,1])
print(x.norm(2))
print(x.vunit())


