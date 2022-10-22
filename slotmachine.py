from random import randrange

class Slot:
    lista_simb=[]
    def __init__(self, l=lista_simb):
        for i in range(0,50):
            l.append("#")
        for j in range(0,40):
            l.append("$")
        for k in range(0,30):
            l.append("%")
        for i in range(0,20):
            l.append("&")
        for j in range(0,10):
            l.append("@")
        for k in range(0,5):
            l.append("£")
        for j in range(0,1):
            l.append("€")
    def maquina(self,l=lista_simb):
        x = randrange(0,156)
        y= randrange(0,156)
        z= randrange(0,156)
        self.comb_1 = l[x]
        self.comb_2 = l[y]
        self.comb_3 = l[z]
    def premio(self, n):
        if self.comb_1==self.comb_2==self.comb_3=="#":
            premio=5*n
        elif self.comb_1==self.comb_2==self.comb_3=="$":
            premio=10*n
        elif self.comb_1==self.comb_2==self.comb_3=="%":
            premio=20*n
        elif self.comb_1==self.comb_2==self.comb_3=="&":
            premio=70*n
        elif self.comb_1==self.comb_2==self.comb_3=="@":
            premio=200*n
        elif self.comb_1==self.comb_2==self.comb_3=="£":
            premio=1000*n
        elif self.comb_1==self.comb_2==self.comb_3=="€":
            premio=100000*n
        else:
            premio=0
        return f'You won {premio} €'
    def __str__(self):
        return f"The combination is \n {self.comb_1} : {self.comb_2} : {self.comb_3}"
    def play(self):
            x=1
            while x:
                bet=float(input("How much money do you want to bet?"))
                if bet<=0:
                    print("You ran out of credits!\n")
                    break
                elif 0<bet<1:
                    print("You do not have enough credits. Retry!")
                else:
                    bet-=1
                    self.maquina()
                    print(self)
                    print(self.premio(bet))
                    x=int(input("Do you want to keep playing? Press 1 for yes, 0 for no\n"))
            print("Thank you for playing with us!")




