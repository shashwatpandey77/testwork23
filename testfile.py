class svector:

    def __init__(self,vinp):
        if not (isinstance(vinp,list)):
            raise TypeError("Only flat vectors are accepted")
        if not any(isinstance(x, float or int) for x in vinp):
            raise TypeError("Input must be a flat list with real numbers only.")
        self.vinp = vinp
        
    def norm(self,num):
        if not(isinstance(num,int)):
            raise TypeError('Only positive integers are acceptible in the argument')
        assert num > 0, f'Only positive integers are acceptible in the argument'

        sum = 0
        for i in self.vinp:
            sum += (i**num)
        out = sum**(1/num)
        return(out)
    
    def vunit(self):
        unit = [i/self.norm(2) for i in self.vinp]
        return(unit)
    



x = svector([1,1,1.5])
print(x.norm(-2))
print(x.vunit())


