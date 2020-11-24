import os
import random

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
        Scoremec.ScoreboardCreate(self.playerlist)

class In_out():
    def Score():
        pass

class Scoremec():#holder styr på spillernes Score

    def ScoreboardCreate(self,list):
        self.playerlist = list
        self.playerscoredict = {}
        self.counter = len(list)-1
        for x in list:
            self.playerscoredict.update({self.playerlist[self.counter] : 0})
            self.counter -= 1
        Scoremec.Scoreboard(self.playerscoredict)
        Scoremec.Scoreprint()
        Gamemec.Randompick()
        #kør det næste der skal køres herefter

    def Scoreboard(self, dict):#indeholder selve spillerne og deres point
        self.accesscoreboard = dict#det dict der indeholder spillere som keys og score som value

    def Scoreprint(self): #skal printe spillernes score
        os.system('CLS')
        print("Scoreboardet lyder\n",Scoremec.accesscoreboard)

    def ScoreAdd(self,player, amount):#skal tilføje en værdi til spillernes Scoreboard
        self.dict = Scoremec.accesscoreboard#henter det aktuelle dict der indeholder score og players
        self.dict[player] += amount #tilføjer score til den givne player
        Scoremec.Scoreboard(self.dict)#opdaterer det dict der ligger i funktionen scoreboard
        Scoremec.Scoreprint()


class Gamemec(): #holder styr på "spillekort" og turns

    def Turn(self):#skifter turn
        try:#forsøg at gøre turncount en større
            self.turncount += 1
        except AttributeError:#hvis turncount ikke findes så lav turn til en værdi af 1
            self.turncount = 1
        Gamemec.Updateactivecards(self.turncount)


    def Randompick(self):
        while True:
            Gamemec.Turn()
            self.pick = random.randrange(1,4)
            self.turnlength = random.randrange(5,15)
            if self.pick == 1:
                Play.Nofuck(self.turnlength)
            elif self.pick == 2:
                Play.Queen()
            elif self.pick == 3:
                Play.Stereotype()

    def Updateactivecards(self, turn):#opdaterer kortene når der er gået en tur
        pass

    def Activecards(self, Cardstring, Turnint):#indeholder hvilke kort er aktive og hvor lang tid de er active i en dict
        try:
            self.activecardsdict.update({Cardstring : Turnint})
        except AttributeError:
            self.activecardsdict = {}
        print(self.activecardsdict)

    def Activecardsprint():
        pass

    def Activecardsadd(self,):
        pass

class Gamecards():

    def Nofuck(self,turnlength):
        print("x")

    def Queen(self):
        print("udvælg en dronning")
        Scoremec.ScoreAdd(input("Hvem vandt"),10)

    def Stereotype(self):
        print("z")

#en class der udvælger fra en anden class

Start = Start()
In_out = In_out()
Scoremec = Scoremec()
Gamemec = Gamemec()
Play = Gamecards()
Start.Game()
