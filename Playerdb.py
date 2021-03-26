import os
import random
import kivy
#https://www.youtube.com/watch?v=dxXsZKmD3Kk&ab_channel=DerekBanas
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import StringProperty
from random import randrange

#to do:
#lave et bedre system til at udvælge kort, måske med en lettere måde at definere chancer på
#rykke alt in og output ind i den rigtige klasse
#lav kivy

# Declare both screens
class Cardpicker():

    def Listpicker(self,nonetype):#denne funktion modtager en nonetype der indeholder flere elementer og udvælger så et element
        self.str = str(nonetype)
        self.splitstr = self.str.split("'")
        self.punishlist = self.splitstr[1].split("!")
        self.catlist = self.splitstr[3].split("!")
        return [self.punishlist[random.randrange(1,int(self.punishlist[0])+1)],self.catlist[random.randrange(1,int(self.catlist[0])+1)]]

    def Openfile(self, str_location, str_location2):#denne funktion åbner en fil for at finde en str, som kan retuneres... funktionen kunne godt generaliseres og køres 2 gange, men det må være et fremtidigt projekt
        self.punishfile = open("punishment.txt", "r")#man kan sagtens gøre sådan så denne funktion ikke behøves at kaldes hver gang der trykkes på knappen eller ihvertfald sådan så man ikke behøver åbne en fil, fjerne trailing newline osv. hver gang
        self.catfile = open("category.txt", "r")
        self.punishlist = []
        self.catlist = []
        self.returnlist = []
        for x in self.punishfile.readlines():
            self.x = x.replace("\n", "")
            self.punishlist.append(self.x)
        if str_location == "drinks":
            self.returnlist.append(self.punishlist[0])
        elif str_location == "shots":
            self.returnlist.append(self.punishlist[1])
        elif str_location == "strips":
            self.returnlist.append(self.punishlist[2])
        elif str_location == "bottoms":
            self.returnlist.append(self.punishlist[3])
        elif str_location == "embarrassings":
            self.returnlist.append(self.punishlist[4])
        else:
            print("ERROR1 in openfile")
        for x in self.catfile.readlines():
            self.x = x.replace("\n", "")
            self.catlist.append(self.x)
        if str_location2 == "stories":
            self.returnlist.append(self.catlist[0])
        elif str_location2 == "games":
            self.returnlist.append(self.catlist[1])
        elif str_location2 == "bullyings":
            self.returnlist.append(self.catlist[2])
        elif str_location2 == "fknowledges":
            self.returnlist.append(self.catlist[3])
        elif str_location2 == "guesses":
            self.returnlist.append(self.catlist[4])
        else:
            print("ERROR2 in openfile")
        self.punishfile.close()
        self.catfile.close()
        return self.returnlist#denne skal retunereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

    def CardTagsPicker(self, dict):#Denne funktion modtager et dict med x antal elementer. det dict indeholder en key som er et ord og en val som er chancen for at den key bliver valgt
    #det er vigtigt at den totale sum val er 100 ellers er det ikke ligeligt fordelt. Funktionen vælger en tilfældig key og retunerer den
        self.picker = random.randrange(1,101)#generer et tilfældigt tal mellem 1 og 101 hvor 1 er inkluderet men 101 er ikke
        self.dval = list(dict.values())
        self.dkey = list(dict.keys())
        #self.picked = None
        self.begin = 0
        self.end = 0
        for x in range(len(self.dkey)):
            if self.begin < self.picker < self.end+self.dval[x]+1:
                return self.dkey[x]
            else:
                self.begin += self.dval[x]
                self.end += self.dval[x]


    def Cardcategory(self):#en gruppe af dicts der indeholder et tal der udgør procentchancen for at den kategori bliver valgt
        self.ppunishDict = {
        "drinks":20,#eksempelvis er der 20% chance for at en kategori vælges hvis den har 20 som tal
        "shots":20,
        "strips":20,
        "bottoms":20,
        "embarrassings":20
        }
        self.pcategoryDict = {
        "stories":20,
        "games":20,
        "bullyings":20,
        "fknowledges":20,
        "guesses":20
        }
        #self.pthemeDict = {}

class Infodb():
    def Setupdb(self):
        self.plst = []

    def Scoreboard(self, dict):#indeholder selve spillerne og deres point
        self.accesscoreboard = dict#det dict der indeholder spillere som keys og score som value

class Scoremec():#holder styr på spillernes Score

    def ScoreboardCreate(self,list_of_players):#laver et dict med spillerne og deres score
        self.playerscoredict = {}
        self.counter = len(list_of_players)-1
        for x in list_of_players:
            self.playerscoredict.update({list_of_players[self.counter] : 0})
            self.counter -= 1
        inf.Scoreboard(self.playerscoredict)
        #Scoremec.Scoreprint()
        #Gamemec.Randompick()
        #kør det næste der skal køres herefter

class MenuScreen(Screen):
    def ___init___(self):
        name_input = ObjectProperty(None)#definerer name_input som et ObjectProperty
        player_list = ObjectProperty(None)


    def submit_player(self):
        player_name = self.name_input.text #finder name_input som tekst
        if player_name not in inf.plst and player_name.strip():#hvis navnet ikke er i listen og navnet ikke er tomt/false
            self.player_list.adapter.data.extend([player_name]) #lav et nyt element med navn player_name?
            self.player_list._trigger_reset_populate()
            inf.plst.append(player_name)#append til playerlist
        else:
            pass

#jeg vil gerne have at man når man fjerner personer fra listen så behøver man ikke klikke hver gang, man kan bare klikke delete og så slettes den øverste
    def remove_player(self):#fjerner en spiller fra listen
        if self.player_list.adapter.selection:#hvis der er klikket på en listitem?
            selection = self.player_list.adapter.selection[0].text
            self.player_list.adapter.data.remove(selection) #fjern det der er inde i selection variablen
            self.player_list._trigger_reset_populate() #updater listview
            inf.plst.remove(selection)
        #else:#ellers så slet det øverste
            #selection = self.player_list.adapter.selection[1].text
            #self.player_list.adapter.data.remove(selection) #fjern det der er inde i selection variablen
            #self.player_list._trigger_reset_populate() #updater listview
            #selection = self.player_list.adapter.selection[0].text
            #self.player_list.adapter.data.remove(selection) #fjern det der er inde i selection variablen
            #self.player_list._trigger_reset_populate() #updater listview

    def start_game(self):
        noplayerspopup = Popup(title='Errorpopup', content=Label(text='Add more players'), size_hint=(None, None), size=(400, 400))
        try:
            if len(inf.plst) < 2:
                noplayerspopup.open()
            else:
                score.ScoreboardCreate(inf.plst)
                sm.current = "game"
        except AttributeError:
            noplayerspopup.open()

    def pack_pick(self):
        sm.current = "pack"

class GameScreen(Screen):
    card_text = StringProperty()

    def Nextcard(self):
        card.Cardcategory()#denne linje skal nok ikke ske her hver gang der trykkes på knappen, men den har det fint her for nu
        self.list = card.Listpicker(card.Openfile(card.CardTagsPicker(card.ppunishDict),card.CardTagsPicker(card.pcategoryDict)))
        self.needplayers = self.list[1].count("@")#hvor mange @ er der i list[1] // @ er et symbol for mennesker
        self.currentplayers = inf.plst #henter en liste over spillere
        if self.needplayers == 1:#hvis der skal bruges en spiller
                self.list[1] = self.list[1].replace("@", self.currentplayers[randrange(0,len(self.currentplayers))])
        elif self.needplayers == 2:#hvis der skal bruges 2 spillere
                self.player1 = self.currentplayers[randrange(0,len(self.currentplayers))]
                self.player2 = randrange(0,len(self.currentplayers))
                #der skal laves noget der checker med 100% sikkerhed at player1 og player2 ikke er den samme men while loops fungerer ikke

                self.list[1] = self.list[1].replace("@", self.player1)
                self.list[1] = self.list[1].replace(self.player1, self.currentplayers[self.player2], 1)
        self.woven = str(self.list[1]+" ELLER "+self.list[0])
        self.card_text = self.woven

class IntroScreen(Screen):
    pass

class PackScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class PLayerlistbtn(ListItemButton): #fungerer som en slags handler?????
    pass

kv = Builder.load_file("Playerdb.kv")

sm = WindowManager()

screens = [MenuScreen(name="menu"), GameScreen(name="game"), PackScreen(name="pack"), IntroScreen(name="intro")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "menu"

class MyMainApp(App):
    def build(self):
        return sm
inf = Infodb()
score = Scoremec()
card = Cardpicker()

if __name__ == "__main__":
    inf.Setupdb()
    MyMainApp().run()
