import os

class Start():
    def Game(self):
        self.playerlist = []
        self.amount = input("Indtast antallet af spillere\n")
        while self.amount.isnumeric() != True: #imens ovenstående input ikke er et nummer
            print('FEJL-"ANGIV KUN HELE TAL"') #print fejl
            self.amount = input("Indtast antallet af spillere\n") #spørg igen
        self.amount = int(self.amount)
        print('Indtast navne')
        while self.amount > 0:
            self.playername = input('')
            self.playerlist.append(self.playername)
            self.amount -= 1
        os.system('CLS')
        Playermec.Players(self.playerlist)

class In_out():
    def Score():
        pass

class Playermec():
    def Players(self,list):
        print(list)

    def Score():
        pass

class Gamemec():
    def Randompick():
        pass

class Gamecards():
    pass
#en class der udvælger fra en anden class

Start = Start()
In_out = In_out()
Playermec = Playermec()
Gamemec = Gamemec()
Gamecards = Gamecards()
Start.Game()
