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
#to do:
#lave et bedre system til at udvælge kort, måske med en lettere måde at definere chancer på
#rykke alt in og output ind i den rigtige klasse
#lav kivy

# Declare both screens
class MenuScreen(Screen):
    name_input = ObjectProperty(None)#definerer name_input som et ObjectProperty
    player_list = ObjectProperty(None)

    def Handler(ListItemButton):
        pass

    def submit_player(self):
        player_name = self.name_input.text #finder name_input som tekst
        #if player_name not in player_list:
        try:
            if player_name not in self.playerlist:
                self.player_list.adapter.data.extend([player_name]) #lav et nyt element med navn player_name?
                self.player_list._trigger_reset_populate()
                self.playerlist.append(player_name)#append til playerlist
            else:
                pass
        except AttributeError:
            self.playerlist = []
            self.player_list.adapter.data.extend([player_name])
            self.player_list._trigger_reset_populate()
            self.playerlist.append(player_name)

#jeg vil gerne have at man når man fjerner personer fra listen så behøver man ikke klikke hver gang, man kan bare klikke delete og så slettes den øverste
    def remove_player(self):#fjerner en spiller fra listen
        if self.player_list.adapter.selection:#hvis der er klikket på en listitem?
            selection = self.player_list.adapter.selection[0].text
            self.player_list.adapter.data.remove(selection) #fjern det der er inde i selection variablen
            self.player_list._trigger_reset_populate() #updater listview
        #else if self.:#ellers hvis der er flere items, så slet det øverste
            #selection = self.player_list.adapter.selection[0].text
            #self.player_list.adapter.data.remove(selection) #fjern det der er inde i selection variablen
            #self.player_list._trigger_reset_populate() #updater listview

    def start_game(self):
        sm.current = "game"
        #self.game = GamePopup()
        #try:
        #    if len(self.playerlist) > 1:
        #        self.game.open()
                #startgame.run()
        #except AttributeError:

    def pack_pick(self):
        pass

class GameScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass
"""
class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm
"""

class PLayerlistbtn(ListItemButton): #fungerer som en slags handler?????
    pass

"""
class PlayerDB(BoxLayout):
    name_input = ObjectProperty()
    player_list = ObjectProperty()
    sm = ScreenManager()
    sm.add_widget(MenuScreen(name='menu'))
    sm.add_widget(GameScreen(name='game'))

# jeg vil gerne have at spillere ikke kan hedde " "


class Game(BoxLayout):
    pass


class PlayerdbApp(App):
    def build(self):
        return PlayerDB()


class GameApp(App):#object not callable?????? måske fordi det er en app
    def build(self):
        return Game()# returner en anden kivy logic der starter spillet?
"""

kv = Builder.load_file("Playerdb.kv")

sm = WindowManager()

screens = [MenuScreen(name="menu"), GameScreen(name="game")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "menu"

class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()

#pdb = PlayerdbApp()
#startgame = GameApp()
#pdb.run()
#Start.Game()
#if __name__ == '__main__':
#    TestApp().run()
