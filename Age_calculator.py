import datetime
da=datetime.date.today().year


class AgeCalci:
    def __init__(self,byear):
        global da 
        age=da-byear
        print("MAx Age is ",age)
AgeCalci(int(input("Enter your Born Year ")))
    

        