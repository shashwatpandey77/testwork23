class svector:

    def __init__(self,vinp):
        if not (isinstance(vinp,list)):
            raise TypeError("Only flat vectors are accepted")
        if any(isinstance(x, list) for x in vinp):
            raise TypeError("Input must be a flat list.")
        self.vinp = vinp
    



x = svector([1,[2,3]])

