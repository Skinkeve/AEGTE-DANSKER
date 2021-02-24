class Start():
    pass
    """
    this shoudl proberly be deleted as funtions are outsourced to PlayerDB
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
            self.playerlist.append(self.playername.lower())
            self.amount -= 1
        os.system('CLS')
        Scoremec.ScoreboardCreate(self.playerlist)
        """

class In_out():
    def Score():
        pass



    def Scoreprint(self): #skal printe spillernes score
        os.system('CLS')
        print("Scoreboardet lyder\n",Scoremec.accesscoreboard)

    def ScoreAdd(self,player, amount):#skal tilføje en værdi til spillernes Scoreboard
        self.dict = Scoremec.accesscoreboard#henter det aktuelle dict der indeholder score og players
        self.dict[player] += amount #tilføjer score til den givne player
        Scoremec.Scoreboard(self.dict)#opdaterer det dict der ligger i funktionen scoreboard
        #Scoremec.Scoreprint()

class Gamemec(): #holder styr på "spillekort" og turns

    def Turn(self):#skifter turn
        try:#forsøg at gøre turncount en større
            self.turncount += 1
        except AttributeError:#hvis turncount ikke findes så lav turn til en værdi af 1
            self.turncount = 1
        print("I er på tur", self.turncount)
        Gamemec.Updateactivecards()


    def Randompick(self):
        self.cooldown1 = 0
        self.cooldown2 = 0
        self.cooldown3 = 0
        self.play = None
        while True:
            self.pick = random.randrange(1,18)
            self.turnlength = random.randrange(5,15)
            if self.pick == 1 and self.cooldown1 < 0:
                self.play = Play.Nofuck
                self.cooldown1 = self.turnlength+1
            elif self.pick == 2:
                self.play = Play.Queen
            elif self.pick == 3:
                self.play = Play.Stereotype
            elif self.pick == 4 and self.cooldown2 < 0:
                self.play = Play.Drukferie
                self.cooldown2 = self.turnlength+1
            elif self.pick == 5:
                self.play = Play.Guessdf
            elif self.pick == 6:
                self.play = Play.Guessalt
            elif self.pick == 7:
                self.play = Play.Danishvalue
            elif self.pick == 8:
                self.play = Play.Kapsel
            elif self.pick > 8 and self.pick < 13:
                self.play = Play.Vote
            elif self.pick == 13:
                self.play = Play.Scenario
            elif self.pick == 14:
                self.play = Play.Guessvalues
            elif self.pick == 15:
                self.play = Play.Rasmus
            elif self.pick == 16:
                self.play = Play.Reference
            elif self.pick == 17 and self.cooldown3 < 0:
                self.play = Play.Jantelov
                self.cooldown3 = self.turnlength+1
            else:
                Gamemec.Randompick()
            self.cooldown1 -= 1
            self.cooldown2 -= 1
            self.cooldown3 -= 1
            Scoremec.Scoreprint()
            Gamemec.Turn()
            try:
                self.play()
            except TypeError:
                self.play(self.turnlength)

    def Updateactivecards(self):#opdaterer kortene når der er gået en tur
        try:
            self.dict = Gamemec.activecardsdict
            self.newdict = {}
            self.values = list(self.dict.values())
            self.keys = list(self.dict.keys())
            self.counter = len(self.values)-1
            for x in self.values:
                self.values[self.counter] -=1
                if self.values[self.counter] == 0:
                    self.values.pop(self.counter)
                    self.keys.pop(self.counter)#remove from play måske ved at rykke den tilhørende value bagerst i listen?
                self.counter -= 1
            self.counter = len(self.values)-1
            for x in self.values:
                self.newdict.update({self.keys[self.counter] : self.values[self.counter]})
                self.counter -= 1
            Gamemec.Activecards(self.newdict)
            Gamemec.Activecardsprint()
        except AttributeError:
            pass

    def Activecards(self, dict):
        self.activecardsdict = dict

    def Activecardsadd(self, Cardstring, Turnint):#indeholder hvilke kort er aktive og hvor lang tid de er active i en dict
        try:
            self.dict = Gamemec.activecardsdict
        except AttributeError:
            self.dict = {}
        self.dict.update({Cardstring : Turnint})
        Gamemec.Activecards(self.dict)
        print(self.activecardsdict)

    def Activecardsprint(self):
        print(Gamemec.activecardsdict)

    def Randomplayer(self):#udvælger en tilfældig spiller fra listen over spillere og retunerer den
        return random.choice(Start.playerlist)

    def Getplayer(self, player):
        self.player = player.lower()
        self.playerlist = Start.playerlist
        while self.player not in self.playerlist:
            self.player = input("Spilleren kunne ikke findes prøv igen:")
        return self.player



class Gamecards():

    def Nofuck(self,turnlength):
        self.cardtxt = "Jeg hader amerikanisering. INGEN MÅ SIGE FUCK! straffen er 2 tåre"
        Gamemec.Activecardsadd(self.cardtxt,turnlength)

    def Queen(self):
        print("ALLE REJSER SIG OP!\nALLE TAGER HØJRE HÅND PÅ HJERTET\nPå runde siges et ord som er en del af den danske nationalsang i rækkefølge.\nSiger man et forkert ord, sætter sig, falder eller fjerner hånden fra hjertet, har man tabt og skal drikke 2 tåre\nVinderen kåres majestæt og får æren af at slå en person til ridder, og 10 point\n")
        print(Gamemec.Randomplayer(),"starter\n")
        Scoremec.ScoreAdd(Gamemec.Getplayer(input("Majestæten er: ")),10)

    def Stereotype(self):
        print("I ægte dansk ånd skal der fornærmes og derfor skal man fornærme personen til højre for sig, ud fra en Stereotype man har om personen.\nGodtages fornærmelsen som værende grov nok skal personen der fornærmede drikke og turen går videre til den næste.\nHvis fornærmelsen ikke godtages skal personen der fornærmede drikke 2 tåre og får -2 point\n")
        print(Gamemec.Randomplayer(),"starter\n")
        Scoremec.ScoreAdd(Gamemec.Getplayer(input("Den søde person iblandt jer er:")),-2)

    def Drukferie(self, turnlength):
        self.cardtxt = "Hvis man rejser sig fra bordet skal man drikke det dobbelte af hvad personen til højre for en har drukket imens man har været væk, bunden redder ikke"
        Gamemec.Activecardsadd(self.cardtxt,turnlength)

    def Guessdf(self):
        self.cardplayer = Gamemec.Randomplayer()
        print(self.cardplayer, "du er blevet givet den helt unikke mulighed for at du kan få 5 point, det eneste du skal gøre er at gætte hvilket citat som en DF'er har sagt.\nTaber du får du -2 point")
        self.truestatements = ["Rettroende muslimer er jo til skade for folkestyret","Skyd på bådflygtninge","Alle muslimer, der bekender sig til den islamiske ideologi, er tabere eller bliver tabere","Jeg har ikke ondt af dem, der drukner på flugt","Tag sådan en som Obama – hvad er han? Vi ved godt, hvad det drejer sig om. Man taler jo om den første neger i USA’s præsidentembede","enhver der løfter hånd mod politi, ambulancer eller brandvæsen skal skydes ned","Skal vi til at være tre eller fire i et ægteskab? Skal vi til at være tre eller fire om at dele forældremyndigheden? Skal vi til at kunne gifte os med andre end mennesker, men måske også med dyr?","Vi er på mange stræk antimuslimsk, fordi vi kan se nogle dybt problematiske ting, ved den måde islam fungerer på","De tyske soldater i vore gader opførte sig bedre end de muslimske drenge. Langt bedre. Soldaterne var veldisciplinerede, unge, tyske drenge.","Forslaget er ligesom homovielserne i kirken endnu et forsøg fra regeringen på at eliminere kernefamilien"]
        self.falsestatements = ["Kernefamilien har altid været og vil altid være 2 hvide forældre", "Danmark er danskernes fødselsret lige så vel som alle danskere er kristne","Den katastrofale asyl- og udlændingepolitik fra 1983 har ødelagt trygheden i samfundet","Smid nu for pokker kriminelle udlændinge ud ved første dom.","Retten til offentlig forsørgelse skal knyttes til det danske statsborgerskab","Det offentlige bruger op mod 10 mia. kroner om året på integration af udlændinge. Det skal stoppes.","Vi betragter det danske statsborgerskab som et privilegium","Intet demokrati har nogensinde formået at integrere store mængder af muslimer, og årsagen er, at det er umuligt","Vi står over for et eksponentielt voksende antal muslimer i Danmark.","Vi ønsker muslimer alt det bedste og masser af held og lykke i hvert af deres 51 muslimske lande"]
        self.falsestatement1 = random.choice(self.falsestatements)
        self.falsestatement2 = random.choice(self.falsestatements)
        while self.falsestatement1 == self.falsestatement2:
            self.falsestatement2 = random.choice(self.falsestatements)
        self.number = random.randrange(1,4)
        if self.number == 1:
            print("1.", random.choice(self.truestatements))
            print("2.", self.falsestatement1)
            print("3.", self.falsestatement2)
        elif self.number == 2:
            print("1.", self.falsestatement1)
            print("2.", random.choice(self.truestatements))
            print("3.", self.falsestatement2)
        elif self.number == 3:
            print("1.", self.falsestatement1)
            print("2.", self.falsestatement2)
            print("3.", random.choice(self.truestatements))
        self.answer = int(input("Angiv med tal hvilket citat er fra DF\n"))
        if self.answer == self.number:
            print("KORREKT!")
            Scoremec.ScoreAdd(self.cardplayer, 5)
        else:
            print("FORKERT!")
            Scoremec.ScoreAdd(self.cardplayer, -2)

    def Guessalt(self):
        self.truestatements = ["Avavdvavdejrkdlavsjfkavahdkahahddad, hvor er det crazy, det her.","Jeg må bare sige, at jeg tager afstand fra mig selv.","Det er God damn seriøst, det her.","Please write that im gay.","Som led i legaliseringen skal det være lovligt at dyrke økologisk cannabis til eget forbrug, både rekreationelt og medicinsk."]
        self.falsestatements = ["Jeg orker altså bare ikke en debat med folk fra LA","Jeg har aldrig produceret eller købt hash","Det sker ofte at jeg går en tur gennem cristiania","Legaliseringen af hash kunne åbne mange jobmuligheder for immigranter og andre mennesker uden uddannelse"]
        self.falsestatement1 = random.choice(self.falsestatements)
        self.falsestatement2 = random.choice(self.falsestatements)
        while self.falsestatement1 == self.falsestatement2:
            self.falsestatement2 = random.choice(self.falsestatements)
        self.number = random.randrange(1,4)
        if self.number == 1:
            print("1.", random.choice(self.truestatements))
            print("2.", self.falsestatement1)
            print("3.", self.falsestatement2)
        elif self.number == 2:
            print("1.", self.falsestatement1)
            print("2.", random.choice(self.truestatements))
            print("3.", self.falsestatement2)
        elif self.number == 3:
            print("1.", self.falsestatement1)
            print("2.", self.falsestatement2)
            print("3.", random.choice(self.truestatements))
        self.answer = int(input("Angiv med tal hvilket citat er fra DF\n"))
        if self.answer == self.number:
            print("KORREKT!")
            Scoremec.ScoreAdd(self.cardplayer, 5)
        else:
            print("FORKERT!")
            Scoremec.ScoreAdd(self.cardplayer, -2)

    def Danishvalue(self):
        print("I skal på runde sige en dansk værdi, taberen er den der ikke kan sige en dansk værdi eller siger en værdi som majoriteten er uenig med.\nTaberen skal drikke så mange tåre som antallet af runder man når igennem\n")
        print(Gamemec.Randomplayer(),"starter\n")
        Scoremec.ScoreAdd(Gamemec.Getplayer(input("Taberen er:")), -1)

    def Kapsel(self):#den der sidst vandt i kapsel får lov til at uddele x antal tåre eller for hver 2 tåre der ikke uddeles kan personen vælge at få 1 point
        print("Den person der sidst vandt i kapsel får lov til at fordele mellem at få 4 point eller at udele 8 tåre.\nEn ting imellem kunne eksempelvis være at personen tager 2 point og uddeler 4 tåre.\nHar ingen vundet i kapsel endnu spilles der indtil en vinder findes.\n")
        self.point = int(input("Antallet af point der gives er:"))
        while 0 > self.point or self.point > 8:
            self.point = input("SNYDER! Der kan ikke gives point over 8 eller under 0. Prøv igen:")
        Scoremec.ScoreAdd(Gamemec.Getplayer(input("Vinderen er:")),self.point)

    def Vote(self):
        print("Dette er en simpel offentligt stemme på hvad der er mest dansk/bedst ud fra to valgmuligheder.\nStemmen sker ved en tommelfinger for den første valgmulighed og op for den anden.\nTaberne er undertallet og de skal drikke 2 tåre og får -1 point.\n\nValgmulighederne er:")
        self.pick = random.randrange(1,19)
        if self.pick == 1:
            print("Osman og Jeppe eller Anna og lotte?")
        elif self.pick == 2:
            print("Kaj og Andrea eller Bamse og Kylling?")
        elif self.pick == 3:
            print("Nationalretten burde være Smørrebrød eller Stegt flæsk?")
        elif self.pick == 4:
            print("Grøndland eller færøerne?")
        elif self.pick == 5:
            print("Stram kurs eller Nye borgerlige?")
        elif self.pick == 6:
            print("Møns eller Stevns klint?")
        elif self.pick == 7:
            print("Søren ryge eller Jørgen leth")
        elif self.pick == 8:
            print("Aqua eller Shu-Bi-Dua")
        elif self.pick == 9:
            print("Birthe kjær eller Danseorkestret")
        elif self.pick == 10:
            print("Kim larsen eller Bamses venner")
        elif self.pick == 11:
            print("Lego eller ????????????????????????????????????")
        elif self.pick == 12:
            print("Blachman eller Bubber")
        elif self.pick == 13:
            print("Linse kessler eller Gustav")
        elif self.pick == 14:
            print("Chili klaus eller Master fatmann")
        elif self.pick == 16:
            print("Mick Øgendahl eller Anders Matthesen")
        elif self.pick == 17:
            print("Olsen banden eller Dirch Passer")
        elif self.pick == 18:
            print("Matador eller Huset på christianshavn")
        elif self.pick == 19:
            print("Far til fire eller Min søsters børn")
        elif self.pick == 20:
                print("Thorvald Stauning eller Harald Blåtand")
        elif self.pick == 21:
            print("Anders Fogh eller Lars Lykke Rasmussen")
        self.amount = int(input("\nHvor mange mennesker tabte: "))
        print("Angiv taberne!")
        self.loosers = []
        while self.amount > 0:
            self.loosers.append(Gamemec.Getplayer(input('')))
            self.amount -= 1
        for x in self.loosers:
            Scoremec.ScoreAdd(self.loosers[0],-1)
            self.loosers.pop(0)

    def Scenario(self):
        self.pick = random.randrange(1,6)
        if self.pick == 1:
            print("TYSKERNE KOMMER!\nPeg en pistol i sydlig retning!")
        elif self.pick == 2:
            print("SVENSKEN KOMMER!\nPeg en pistol i nordøstlig retning!")
        elif self.pick == 3:
            print("RUSSERNE KOMMER!\nGem dig under bordet!")
        elif self.pick == 4:
            print("KAPTAJN DING DONG!\nBasicly Kaptajn Morgan!")
        elif self.pick == 5:
            print("TORDENSKJOLD!\nLign Tordenskjold!")
        Scoremec.ScoreAdd(Gamemec.Getplayer(input('Taberen er den der sidst gjorde pågældende ting: ')),-2)
        #tyskerne kommer
        #svendsken kommer
        #Janteloven
        #russerne kommer
        #kaptajn ding dong

    def Guessvalues(self): #gæt de 10 danske værdier
        self.unguessed = ["1. xxxxxxxxxxxxxxxxx - 10 point","2. xxxxxx - 9 point","3. xxxxxx - 8 point","4. xxxxxx for xxxxx - 7 point","5. xxxxxxxxxxxxxxxx - 6 point","6. Det xxxxxx xxxxx - 5 point","7. xxxxxxxxxxxx og xxxxxxxxxxxx - 4 point","8. xxxxxxx - 3 point","9. xxxxx - 2 point","10. Den xxxxxxx xxxxxxxxx - 1 point"]
        self.guessed = ["1. Velfærdssamfundet - 10 point","2. Frihed - 9 point","3. Tillid - 8 point","4. Lighed for loven - 7 point","5. Kønsligestilling - 6 point","6. Det danske sprog - 5 point","7. Foreningsliv og frivillighed - 4 point","8. Frisind - 3 point","9. Hygge - 2 point","10. Den kristne kulturarv - 1 point"]
        self.guessplayer = ["","","","","","","","","",""]
        self.playerlist = Start.playerlist
        self.playercounter = len(self.playerlist)-1
        self.printcount = 0
        while True:
            print("Dette er en form for quiz hvor i skal gætte de 10 danske værdier, holdninger, vaner, skikke og særlige forhold, der udgør den nationale identitet.\nDette er resultatet af stemmer fra 300.000 danskere\nGætter man forkert er det automatisk den næste persons tur.\n")
            self.player = self.playerlist[self.playercounter]
            self.playercounter -=1
            if self.playercounter < 0:
                self.playercounter = len(self.playerlist)-1
            print("Den der gætter er", self.player,"\n")
            for x in self.unguessed:
                print(self.unguessed[self.printcount],self.guessplayer[self.printcount])
                self.printcount += 1
            self.printcount = 0
            self.svar = input("Gæt på en af svarmulighederne!\n").lower()
            if self.svar == "velfærdssamfundet" or self.svar == "velfærd" or self.svar == "velfærdssamfund":
                self.unguessed[0] = self.guessed[0]
                self.guessplayer[0] = self.player
                Scoremec.ScoreAdd(self.player,10)
            elif self.svar == "frihed":
                self.unguessed[1] = self.guessed[1]
                self.guessplayer[1] = self.player
                Scoremec.ScoreAdd(self.player,9)
            elif self.svar == "tillid":
                self.unguessed[2] = self.guessed[2]
                self.guessplayer[2] = self.player
                Scoremec.ScoreAdd(self.player,8)
            elif self.svar == "lighed for loven":
                self.unguessed[3] = self.guessed[3]
                self.guessplayer[3] = self.player
                Scoremec.ScoreAdd(self.player,7)
            elif self.svar == "kønsligestilling" or self.svar == "ligestilling":
                self.unguessed[4] = self.guessed[4]
                self.guessplayer[4] = self.player
                Scoremec.ScoreAdd(self.player,6)
            elif self.svar == "det danske sprog":
                self.unguessed[5] = self.guessed[5]
                self.guessplayer[5] = self.player
                Scoremec.ScoreAdd(self.player,5)
            elif self.svar == "foreningsliv og frivillighed":
                self.unguessed[6] = self.guessed[6]
                self.guessplayer[6] = self.player
                Scoremec.ScoreAdd(self.player,4)
            elif self.svar == "frisind":
                self.unguessed[7] = self.guessed[7]
                self.guessplayer[7] = self.player
                Scoremec.ScoreAdd(self.player,3)
            elif self.svar == "hygge":
                self.unguessed[8] = self.guessed[8]
                self.guessplayer[8] = self.player
                Scoremec.ScoreAdd(self.player,2)
            elif self.svar == "den kristne kulturarv" or self.svar == "kristendom":
                self.unguessed[9] = self.guessed[9]
                self.guessplayer[9] = self.player
                Scoremec.ScoreAdd(self.player,1)
            os.system('CLS')
            Scoremec.Scoreprint()

    def Rasmus(self):
        print("Der der kan lave den bedste efterligning af Rasmus Paludan får 2 point alle andre drikker 1 tår")
        Scoremec.ScoreAdd(Gamemec.Getplayer(input('Vinderen er: ')),2)

    def Reference(self):
        print("På runde skal der laves referencer til danske film,",Gamemec.Randomplayer(),"starter\nFor hver runde drikker alle en tår, den der taber får -1 point")
        Scoremec.ScoreAdd(Gamemec.Getplayer(input('Taberen er: ')),-1)

    def Jantelov(self,turnlength):
        print("JANTELOVEN ER VEDTAGET! At tale positivt om sig selv medfører en bunder, at sige jeg medfører en tår")
        Gamemec.Activecardsadd(self.cardtxt,turnlength)

#en class der udvælger fra en anden class

Start = Start()
In_out = In_out()
Scoremec = Scoremec()
Gamemec = Gamemec()
Play = Gamecards()
