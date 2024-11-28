class dsa:
    data=10
    def __init__(self,a) -> None:
        self.val=a
        self.data=dsa.data
        dsa.data+=1
    def getvalue(self):
        return self.val