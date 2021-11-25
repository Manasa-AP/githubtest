class Theorycie:
    def setcie(self,cie1,cie2):
        self.cie1_marks=cie1
        self.cie2_marks=cie2
class Labcie:
    def setlab(self,lab):
        self.lab_marks=lab
class SEE:
    def setsee(self,see):
        self.see_marks=see
class Result(Theorycie,Labcie,SEE):
    def getResult(self):
        cie=(self.cie1_marks+self.cie2_marks)/2
        se=self.see_marks/2
        res=cie+self.lab_marks+se
        return res
s=Result()
try:
    c1=eval(input("Enter CIE 1 marks (out of 40):"))
    c2=eval(input("Enter CIE 2 marks (out of 40):"))
    lab=eval(input("Enter LAB CIE marks (out of 30):"))
    see=eval(input("Enter SEE marks (out of 100):"))
    s.setcie(c1,c2)
    s.setlab(lab)
    s.setsee(see)
    print("The final result is :",s.getResult())

except:
    print("Error!!: Please Enter either float or integer value:")
