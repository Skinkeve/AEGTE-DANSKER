import random
#self.cardplayer = Gamemec.Randomplayer()
#print(self.cardplayer, "du er blevet givet den helt unikke mulighed for at du kan få 5 point, det eneste du skal gøre er at gætte hvilket citat som en DF'er har sagt.\n Taber du får du -2 point")
class x():
    def y(self):
        self.truestatements = ["Rettroende muslimer er jo til skade for folkestyret","Skyd på bådflygtninge","Alle muslimer, der bekender sig til den islamiske ideologi, er tabere eller bliver tabere","Jeg har ikke ondt af dem, der drukner på flugt","Tag sådan en som Obama – hvad er han? Vi ved godt, hvad det drejer sig om. Man taler jo om den første neger i USA’s præsidentembede","enhver der løfter hånd mod politi, ambulancer eller brandvæsen skal skydes ned","Skal vi til at være tre eller fire i et ægteskab? Skal vi til at være tre eller fire om at dele forældremyndigheden? Skal vi til at kunne gifte os med andre end mennesker, men måske også med dyr?","Vi er på mange stræk antimuslimsk, fordi vi kan se nogle dybt problematiske ting, ved den måde islam fungerer på","De tyske soldater i vore gader opførte sig bedre end de muslimske drenge. Langt bedre. Soldaterne var veldisciplinerede, unge, tyske drenge.","Forslaget er ligesom homovielserne i kirken endnu et forsøg fra regeringen på at eliminere kernefamilien"]
        self.falsestatements = ["Kernefamilien har altid været og vil altid være 2 hvide forældre", "Danmark er danskernes fødselsret lige så vel som alle danskere er kristne","Den katastrofale asyl- og udlændingepolitik fra 1983 har ødelagt trygheden i samfundet","Med mellemøstlige mennesker følger... Smid nu for pokker kriminelle udlændinge ud ved første dom.","Retten til offentlig forsørgelse skal knyttes til det danske statsborgerskab","Det offentlige bruger op mod 10 mia. kroner om året på integration af udlændinge. Det skal stoppes.","Vi betragter det danske statsborgerskab som et privilegium","Intet demokrati har nogensinde formået at integrere store mængder af muslimer, og årsagen er, at det er umuligt","Vi står over for et eksponentielt voksende antal muslimer i Danmark.","Vi ønsker muslimer alt det bedste og masser af held og lykke i hvert af deres 51 muslimske lande"]
        self.falsestatement1 = random.choice(self.falsestatements)
        self.falsestatement2 = random.choice(self.falsestatements)
        self.falsestatement3 = random.choice(self.falsestatements)
        while self.falsestatement1 == self.falsestatement2:
            self.falsestatement2 = random.choice(self.falsestatement)
        while self.falsestatement2 == self.falsestatement3:
            self.falsestatement3 == random.choice(self.falsestatement)
        self.number = random.randrange(1,5)
        #self.statementsdict = {random.choice(self.truestatements):True, self.falsestatement1:False, self.falsestatement2:False,self.falsestatement3:False}
        if self.number == 1:
            print(random.choice(self.truestatements)
            print(random.choice(self.falsestatement1)
            print(random.choice(self.falsestatement2)
            print(random.choice(self.falsestatement3)
        elif self.number == 2:
            print(random.choice(self.falsestatement1)
            print(random.choice(self.truestatements)
            print(random.choice(self.falsestatement2)
            print(random.choice(self.falsestatement3)
        elif self.number == 3:
            print(random.choice(self.falsestatement1)
            print(random.choice(self.falsestatement2)
            print(random.choice(self.truestatements)
            print(random.choice(self.falsestatement3)
        elif self.number == 4:
            print(random.choice(self.falsestatement1)
            print(random.choice(self.falsestatement2)
            print(random.choice(self.falsestatement3)
            print(random.choice(self.truestatements)

x = x()
x.y()
