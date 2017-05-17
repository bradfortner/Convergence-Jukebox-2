import kivy
kivy.require("1.9.1") # used to alert user if this code is run on an earlier version of Kivy.
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
import pickle
import os
import os.path, time
import sys  # Used to check and switch resolutions for convergence jukebox.
from ctypes import *  # Used by playmp3.py windows based mp3 player.
# http://www.mailsend-online.com/blog/play-mp3-files-with-python-on-windows.html
from operator import itemgetter
import datetime  # Used in RSS generation.
import PyRSS2Gen  # Used n RSS generation.
import getpass  # Gets user name http://stackoverflow.com/questions/4325416/how-do-i-get-the-username-in-python.
import keyboard # Used to simulated keyboard events to call screen update functions http://bit.ly/2qwRrTh

computer_account_user_name = getpass.getuser()  # Used to write various log and RSS files to local directories.
if sys.platform == 'win32':
    winmm = windll.winmm  # Variable used in playmp3.py.
full_path = os.path.realpath('__file__')  # http://bit.ly/1RQBZYF
print full_path

song_list_recover = open('song_list.pkl', 'rb')
song_list = pickle.load(song_list_recover)
song_list_recover.close()
del song_list_recover
for i in range (0,16): # Adds blank songs to end of sont_list
    song_list.append([u'zzzzz', u'zzzzz', u' ' , u' ', u' ', u' ', u' ', u' ', 'zzzzz - zzzzz.mp3', u' '])
song_list.sort(key=itemgetter(1), reverse=False)
display_info_recover = open("output_list.txt", 'r+')
output_list_read = display_info_recover.read()
display_info_recover.close()
display_info = output_list_read.split(",")

the_bands_file_open = open("the_bands.txt", 'r+')
to_be_split = the_bands_file_open.read()
the_bands_file_open.close()
the_bands_list = to_be_split.split(",")
the_bands_list_lower_case = []
for s in the_bands_list:
    the_bands_list_lower_case.append(s.lower())

upcoming_list_recover = open('upcoming_list.pkl', 'rb')
upcoming_list = pickle.load(upcoming_list_recover)
upcoming_list_recover.close()
selections_available = len(song_list)
del upcoming_list_recover
credit_amount = 0
adder = 0
last_pressed =""
cursor_position = 0
screen_number = 0
song_selection_number = ""
x = 0
file_time_old = "Wed Dec 30 22:56:15 2015"

Window.fullscreen = True # does not force full screen
Window.size = (1280, 720) # sets 720p

Builder.load_string('''
<Label>:
    color: 0,.7,0,1 # Sets text colour to green.
    font_size: 18
    valign: 'middle'
    halign: 'left'
    text_size: self.size
<Button>:
    font_size: 16
    color: 1,1,1,1 # Sets text colour to white.
    bold: True
    background_normal: "" # Button background defalts to grey. This sets the background to plain.
    background_color: (0.0, 0.0, 0.0, 0.0)# Sets the buttons colour to black.
    halign: 'center'
    valign: 'middle'
    text_size: self.size
    size_hint: .255, .0620
<FloatLayout>:
    id: selection
    canvas.before:
        BorderImage:
            source: 'jukebox.png'
            pos: self.pos
            size: self.size
    Label:
        id: sort_mode
        text: "UPCOMING SELECTIONS"
        font_size: 28
        halign: 'center'
        size_hint: .32, 1
        pos: 1,131
    Label:
        text: "Twenty-Five Cents Per Selection"
        halign: 'center'
        size_hint: .3, 1
        pos: 12,-267
    Label:
        id: jukebox_name
        text: "Convergence Music System 2.0"
        color: 0,0,0,1 # Sets text colour to black.
        font_size: 38
        bold: True
        halign: 'center'
        size_hint: .7, 1
        pos: 390,292
''')

class JukeboxScreen(FloatLayout):

    def my_buttons_text(self):  # my_button_text event handler code
        global adder
        self.ids.song_0_title.text = str(song_list[adder][0])
        self.ids.song_0_artist.text = str(song_list[adder][1])
        self.ids.song_1_title.text = str(song_list[adder + 1][0])
        self.ids.song_1_artist.text = str(song_list[adder + 1][1])
        self.ids.song_2_title.text = str(song_list[adder + 2][0])
        self.ids.song_2_artist.text = str(song_list[adder + 2][1])
        self.ids.song_3_title.text = str(song_list[adder + 3][0])
        self.ids.song_3_artist.text = str(song_list[adder + 3][1])
        self.ids.song_4_title.text = str(song_list[adder + 4][0])
        self.ids.song_4_artist.text = str(song_list[adder + 4][1])
        self.ids.song_5_title.text = str(song_list[adder + 5][0])
        self.ids.song_5_artist.text = str(song_list[adder + 5][1])
        self.ids.song_6_title.text = str(song_list[adder + 6][0])
        self.ids.song_6_artist.text = str(song_list[adder + 6][1])
        self.ids.song_7_title.text = str(song_list[adder + 7][0])
        self.ids.song_7_artist.text = str(song_list[adder + 7][1])
        self.ids.song_8_title.text = str(song_list[adder + 8][0])
        self.ids.song_8_artist.text = str(song_list[adder + 8][1])
        self.ids.song_9_title.text = str(song_list[adder + 9][0])
        self.ids.song_9_artist.text = str(song_list[adder + 9][1])
        self.ids.song_10_title.text = str(song_list[adder + 10][0])
        self.ids.song_10_artist.text = str(song_list[adder + 10][1])
        self.ids.song_11_title.text = str(song_list[adder + 11][0])
        self.ids.song_11_artist.text = str(song_list[adder + 11][1])
        self.ids.song_12_title.text = str(song_list[adder + 12][0])
        self.ids.song_12_artist.text = str(song_list[adder + 12][1])
        self.ids.song_13_title.text = str(song_list[adder + 13][0])
        self.ids.song_13_artist.text = str(song_list[adder + 13][1])
        self.ids.song_14_title.text = str(song_list[adder + 14][0])
        self.ids.song_14_artist.text = str(song_list[adder + 14][1])
        self.ids.song_15_title.text = str(song_list[adder + 15][0])
        self.ids.song_15_artist.text = str(song_list[adder + 15][1])

class MyFinalApp(App):

    def build(self):
        final_gui = JukeboxScreen()
        Clock.schedule_interval(MyFinalApp.file_reader, 5)
        Window.bind(on_key_down=self.key_action)
        self.song_playing_name = Button(text=str(display_info[0]), pos=(580, 540), font_size=30, size_hint=(None, None),
                                        width=500)
        self.song_playing_artist = Button(text=str(display_info[1]), pos=(430, 490), font_size=30,
                                          size_hint=(None, None), width=800, halign="center", valign="middle")
        if len(display_info[0]) > 25:
            self.song_playing_name.font_size = 25
        elif len(display_info[0]) > 18:
            self.song_playing_name.font_size = 35
        else:
            self.song_playing_name.font_size = 50
        if len(display_info[1]) > 25:
            self.song_playing_artist.font_size = 25
        elif len(display_info[1]) > 18:
            self.song_playing_artist.font_size = 35
        else:
            self.song_playing_artist.font_size = 50
        self.sort_mode = Label(text="Sort Mode By Artist", pos=(42,278), font_size=38)
        self.my_first_title = Button(text=str(song_list[adder][0]), pos=(495,456))
        self.my_first_artist = Button(text=str(song_list[adder][1]), pos=(495,433))
        self.my_second_title = Button(text=str(song_list[adder+1][0]), pos=(495,403))
        self.my_second_artist = Button(text=str(song_list[adder+1][1]), pos=(495,380))
        self.my_third_title = Button(text=str(song_list[adder+2][0]), pos=(495,348))
        self.my_third_artist = Button(text=str(song_list[adder+2][1]), pos=(495,325))
        self.my_fourth_title = Button(text=str(song_list[adder+3][0]), pos=(495,293))
        self.my_fourth_artist = Button(text=str(song_list[adder+3][1]), pos=(495,270))
        self.my_fifth_title = Button(text=str(song_list[adder+4][0]), pos=(495,238))
        self.my_fifth_artist = Button(text=str(song_list[adder+4][1]), pos=(495,216))
        self.my_sixth_title = Button(text=str(song_list[adder+5][0]), pos=(495,185))
        self.my_sixth_artist = Button(text=str(song_list[adder+5][1]), pos=(495,162))
        self.my_seventh_title = Button(text=str(song_list[adder+6][0]), pos=(495,132))
        self.my_seventh_artist = Button(text=str(song_list[adder+6][1]), pos=(495,109))
        self.my_eigth_title = Button(text=str(song_list[adder+7][0]), pos=(495,77))
        self.my_eigth_artist = Button(text=str(song_list[adder+7][1]), pos=(495,54))
        self.my_ninth_title = Button(text=str(song_list[adder+8][0]), pos=(835,456))
        self.my_ninth_artist = Button(text=str(song_list[adder+8][1]), pos=(835,433))
        self.my_tenth_title = Button(text=str(song_list[adder+9][0]), pos=(835,403))
        self.my_tenth_artist = Button(text=str(song_list[adder+9][1]), pos=(835,380))
        self.my_eleventh_title = Button(text=str(song_list[adder+10][0]), pos=(835,348))
        self.my_eleventh_artist = Button(text=str(song_list[adder+10][1]), pos=(835,325))
        self.my_twelfth_title = Button(text=str(song_list[adder+11][0]), pos=(835,293))
        self.my_twelfth_artist = Button(text=str(song_list[adder+11][1]), pos=(835,270))
        self.my_thirteenth_title = Button(text=str(song_list[adder+12][0]), pos=(835,238))
        self.my_thirteenth_artist = Button(text=str(song_list[adder+12][1]), pos=(835,216))
        self.my_fourteenth_title = Button(text=str(song_list[adder+13][0]), pos=(835,185))
        self.my_fourteenth_artist = Button(text=str(song_list[adder+13][1]), pos=(835,162))
        self.my_fifteenth_title = Button(text=str(song_list[adder+14][0]), pos=(835,132))
        self.my_fifteenth_artist = Button(text=str(song_list[adder+14][1]), pos=(835,109))
        self.my_sixteenth_title = Button(text=str(song_list[adder+15][0]), pos=(835,77))
        self.my_sixteenth_artist = Button(text=str(song_list[adder+15][1]), pos=(835,54))
        self.my_play_mode = Label(text=str(display_info[5]),pos=(40,245))
        self.my_title_song = Label(text="Title: " + str(display_info[0]),pos=(40,225))
        self.my_title_artist = Label(text="Artist: " + str(display_info[1]), pos=(40, 205))
        self.my_title_year = Label(text="Year: " + str(display_info[3]), pos=(40, 185))
        self.my_title_length = Label(text="Length: " + str(display_info[4]), pos=(135, 185))
        self.my_title_album = Label(text="Album: " + str(display_info[2]), pos=(40, 165))
        selections_screen_starter(self)
        selections_screen_updater(self)
        self.my_credit_amount = Label(text="CREDITS " + str(credit_amount), pos=(117,-236),font_size=35)
        self.selections_available = Label(text="Selections Available: " + str(selections_available), pos=(97,-287))
        final_gui.add_widget(self.song_playing_name)
        final_gui.add_widget(self.song_playing_artist)
        final_gui.add_widget(self.my_selection_one)
        final_gui.add_widget(self.my_selection_two)
        final_gui.add_widget(self.my_selection_three)
        final_gui.add_widget(self.my_selection_four)
        final_gui.add_widget(self.my_selection_five)
        final_gui.add_widget(self.my_selection_six)
        final_gui.add_widget(self.my_selection_seven)
        final_gui.add_widget(self.my_selection_eight)
        final_gui.add_widget(self.my_selection_nine)
        final_gui.add_widget(self.my_selection_ten)
        final_gui.add_widget(self.my_selection_eleven)
        final_gui.add_widget(self.my_selection_twelve)
        final_gui.add_widget(self.my_selection_thirteen)
        final_gui.add_widget(self.my_selection_fourteen)
        final_gui.add_widget(self.my_selection_fifteen)
        final_gui.add_widget(self.my_selection_sixteen)
        final_gui.add_widget(self.my_selection_seventeen)
        final_gui.add_widget(self.my_credit_amount)
        final_gui.add_widget(self.selections_available)
        final_gui.add_widget(self.sort_mode)
        final_gui.add_widget(self.my_play_mode)
        final_gui.add_widget(self.my_title_song)
        final_gui.add_widget(self.my_title_artist)
        final_gui.add_widget(self.my_title_year)
        final_gui.add_widget(self.my_title_length)
        final_gui.add_widget(self.my_title_album)
        final_gui.add_widget(self.my_first_title)
        final_gui.add_widget(self.my_first_artist)
        final_gui.add_widget(self.my_second_title)
        final_gui.add_widget(self.my_second_artist)
        final_gui.add_widget(self.my_third_title)
        final_gui.add_widget(self.my_third_artist)
        final_gui.add_widget(self.my_fourth_title)
        final_gui.add_widget(self.my_fourth_artist)
        final_gui.add_widget(self.my_fifth_title)
        final_gui.add_widget(self.my_fifth_artist)
        final_gui.add_widget(self.my_sixth_title)
        final_gui.add_widget(self.my_sixth_artist)
        final_gui.add_widget(self.my_seventh_title)
        final_gui.add_widget(self.my_seventh_artist)
        final_gui.add_widget(self.my_eigth_title)
        final_gui.add_widget(self.my_eigth_artist)
        final_gui.add_widget(self.my_ninth_title)
        final_gui.add_widget(self.my_ninth_artist)
        final_gui.add_widget(self.my_tenth_title)
        final_gui.add_widget(self.my_tenth_artist)
        final_gui.add_widget(self.my_eleventh_title)
        final_gui.add_widget(self.my_eleventh_artist)
        final_gui.add_widget(self.my_twelfth_title)
        final_gui.add_widget(self.my_twelfth_artist)
        final_gui.add_widget(self.my_thirteenth_title)
        final_gui.add_widget(self.my_thirteenth_artist)
        final_gui.add_widget(self.my_fourteenth_title)
        final_gui.add_widget(self.my_fourteenth_artist)
        final_gui.add_widget(self.my_fifteenth_title)
        final_gui.add_widget(self.my_fifteenth_artist)
        final_gui.add_widget(self.my_sixteenth_title)
        final_gui.add_widget(self.my_sixteenth_artist)
        self.my_first_title.background_color = (160, 160, 160, .2)
        self.my_first_artist.background_color = (160, 160, 160, .2)
        selection_font_size(self)
        return final_gui

    def key_action(self, *args): # Keyboard Reader Code. https://gist.github.com/tshirtman/31bb4d3e482261191a1f
        global adder
        global screen_number
        global cursor_position
        global last_pressed
        global song_selection_number
        key_event = list(args)
        global display_info
        global upcoming_list
        print "Key Number Pressed Is: " + str(key_event[1])
        if str(key_event[1]) == '47': # Changes sort mode to title
            last_pressed = "forward slash"
            if self.sort_mode.text != "Sort Mode By Title":
                print "Sorting by Title"
                song_list.sort(key=itemgetter(0), reverse=False)
                self.sort_mode.text = "Sort Mode By Title"
            else:
                print "Sorting by Artist"
                song_list.sort(key=itemgetter(1), reverse=False)
                self.sort_mode.text = "Sort Mode By Artist"
            screen_number_base = .9 # This triggers a reset of the title/artist display
        try:
            if str(key_event[1]) == '97':
                print 'a'
                if self.sort_mode.text == "Sort Mode By Title":
                    if last_pressed == "aa":
                        print "I should be b"
                        last_pressed = "aaa"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "B":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "aaa":
                        print "I should be c"
                        last_pressed = "a"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][0][0] == "C":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be a"
                        last_pressed = "aa"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "A":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                else:
                    if last_pressed == "aa":
                        print "I should be b"
                        last_pressed = "aaa"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "B":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "aaa":
                        print "I should be c"
                        last_pressed = "a"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][1][0] == "C":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be the letter a"
                        print adder
                        print cursor_position
                        last_pressed = "aa"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "A":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
        except IndexError:
            return
        if str(key_event[1]) == '98': # b keyboard key updates display on song change
            print upcoming_list
            self.my_selection_one.text = " "
            self.my_selection_two.text = " "
            self.my_selection_three.text = " "
            self.my_selection_four.text = " "
            self.my_selection_five.text = " "
            self.my_selection_six.text = " "
            self.my_selection_seven.text = " "
            self.my_selection_eight.text = " "
            self.my_selection_nine.text = " "
            self.my_selection_ten.text = " "
            self.my_selection_eleven.text = " "
            self.my_selection_twelve.text = " "
            self.my_selection_thirteen.text = " "
            self.my_selection_fourteen.text = " "
            self.my_selection_fifteen.text = " "
            self.my_selection_sixteen.text = " "
            self.my_selection_seventeen.text = " "
            try:
                if upcoming_list:
                    if upcoming_list[0]:
                        self.my_selection_one.text = upcoming_list[0]
                    if upcoming_list[1]:
                        self.my_selection_two.text = upcoming_list[1]
                    if upcoming_list[2]:
                        self.my_selection_three.text = upcoming_list[2]
                    if upcoming_list[3]:
                        self.my_selection_four.text = upcoming_list[3]
                    if upcoming_list[4]:
                        self.my_selection_five.text = upcoming_list[4]
                    if upcoming_list[5]:
                        self.my_selection_six.text = upcoming_list[5]
                    if upcoming_list[6]:
                        self.my_selection_seven.text = upcoming_list[6]
                    if upcoming_list[7]:
                        self.my_selection_eight.text = upcoming_list[7]
                    if upcoming_list[8]:
                        self.my_selection_nine.text = upcoming_list[8]
                    if upcoming_list[9]:
                        self.my_selection_ten.text = upcoming_list[9]
                    if upcoming_list[10]:
                        self.my_selection_eleven.text = upcoming_list[10]
                    if upcoming_list[11]:
                        self.my_selection_twelve.text = upcoming_list[11]
                    if upcoming_list[12]:
                        self.my_selection_thirteen.text = upcoming_list[12]
                    if upcoming_list[13]:
                        self.my_selection_fourteen.text = upcoming_list[13]
                    if upcoming_list[14]:
                        self.my_selection_fifteen.text = upcoming_list[14]
                    if upcoming_list[15]:
                        self.my_selection_sixteen.text = upcoming_list[15]
                    if upcoming_list[16]:
                        self.my_selection_seventeen.text = upcoming_list[16]
            except IndexError:
                pass
            display_info_recover = open("output_list.txt", 'r+')
            output_list_read = display_info_recover.read()
            display_info_recover.close()
            display_info = output_list_read.split(",")
            print display_info
            self.song_playing_name.text = str(display_info[0])
            self.song_playing_artist.text = str(display_info[1])
            if len(display_info[0]) > 25:
                self.song_playing_name.font_size = 25
            elif len(display_info[0]) > 18:
                self.song_playing_name.font_size = 35
            else:
                self.song_playing_name.font_size = 50
            if len(display_info[1]) > 25:
                self.song_playing_artist.font_size = 25
            elif len(display_info[1]) > 18:
                self.song_playing_artist.font_size = 35
            else:
                self.song_playing_artist.font_size = 50

            x = self.song_playing_artist.text
            if x.lower() in the_bands_list_lower_case:
                x = "The " + str(x)
                self.song_playing_artist.text = str(x)

            self.my_title_song.text = "Title: " + str(display_info[0])
            self.my_title_artist.text = "Artist: " + str(display_info[1])
            self.my_title_album.text = "Release: " +str(display_info[2])
            self.my_title_year.text = "Year: " + str(display_info[3])
            self.my_title_length.text = "Length: " + str(display_info[4])
            self.my_play_mode.text = str(display_info[5])

        try:
            if str(key_event[1]) == '100':
                print 'd'
                if self.sort_mode.text == "Sort Mode By Title":
                    if last_pressed == "dd":
                        print "I should be e"
                        last_pressed = "ddd"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "E":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "ddd":
                        print "I should be f"
                        last_pressed = "d"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][0][0] == "F":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be d"
                        last_pressed = "dd"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "D":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                else:
                    if last_pressed == "dd":
                        print "I should be e"
                        last_pressed = "ddd"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "E":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "ddd":
                        print "I should be f"
                        last_pressed = "d"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][1][0] == "F":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be the letter d"
                        print adder
                        print cursor_position
                        last_pressed = "dd"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "D":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
            if str(key_event[1]) == '103':
                print 'g'
                if self.sort_mode.text == "Sort Mode By Title":
                    if last_pressed == "gg":
                        print "I should be h"
                        last_pressed = "ggg"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "H":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "ggg":
                        print "I should be i"
                        last_pressed = "g"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][0][0] == "I":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be g"
                        last_pressed = "gg"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "G":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                else:
                    if last_pressed == "gg":
                        print "I should be h"
                        last_pressed = "ggg"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "H":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "ggg":
                        print "I should be i"
                        last_pressed = "d"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][1][0] == "I":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be the letter g"
                        print adder
                        print cursor_position
                        last_pressed = "gg"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "G":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
            if str(key_event[1]) == '106':
                print 'j'
                if self.sort_mode.text == "Sort Mode By Title":
                    if last_pressed == "jj":
                        print "I should be k"
                        last_pressed = "jjj"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "K":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "jjj":
                        print "I should be l"
                        last_pressed = "j"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][0][0] == "L":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be j"
                        last_pressed = "jj"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "J":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                else:
                    if last_pressed == "jj":
                        print "I should be k"
                        last_pressed = "jjj"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "K":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "jjj":
                        print "I should be l"
                        last_pressed = "j"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][1][0] == "L":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be the letter j"
                        print adder
                        print cursor_position
                        last_pressed = "jj"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "J":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
            if str(key_event[1]) == '109':
                print 'm'
                if self.sort_mode.text == "Sort Mode By Title":
                    if last_pressed == "mm":
                        print "I should be n"
                        last_pressed = "mmm"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "N":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "mmm":
                        print "I should be o"
                        last_pressed = "m"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][0][0] == "O":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be m"
                        last_pressed = "mm"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "M":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                else:
                    if last_pressed == "mm":
                        print "I should be n"
                        last_pressed = "mmm"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "N":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "mmm":
                        print "I should be o"
                        last_pressed = "m"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][1][0] == "O":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be the letter m"
                        print adder
                        print cursor_position
                        last_pressed = "mm"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "M":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
            if str(key_event[1]) == '112':
                print 'p'
                if self.sort_mode.text == "Sort Mode By Title":
                    if last_pressed == "pp":
                        print "I should be q"
                        last_pressed = "ppp"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "Q":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "ppp":
                        print "I should be r"
                        last_pressed = "p"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][0][0] == "R":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be p"
                        last_pressed = "pp"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "P":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                else:
                    if last_pressed == "pp":
                        print "I should be q"
                        last_pressed = "ppp"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "Q":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "ppp":
                        print "I should be r"
                        last_pressed = "p"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][1][0] == "R":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be the letter p"
                        print adder
                        print cursor_position
                        last_pressed = "pp"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "P":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
            if str(key_event[1]) == '115':
                print 'p'
                if self.sort_mode.text == "Sort Mode By Title":
                    print "I should be s"
                    last_pressed = "s"
                    first_index_of_letter = []
                    for x in range(0, len(song_list)):
                        if song_list[x][0][0] == "S":
                            first_index_of_letter.append(x)
                    adder = first_index_of_letter[0]
                else:
                    print "I should be the letter s"
                    print adder
                    print cursor_position
                    last_pressed = "s"
                    first_index_of_letter = []
                    for x in range(0, len(song_list)):
                        if song_list[x][1][0] == "S":
                            first_index_of_letter.append(x)
                    adder = first_index_of_letter[0]
            if str(key_event[1]) == '116':
                print 't'
                if self.sort_mode.text == "Sort Mode By Title":
                    if last_pressed == "tt":
                        print "I should be u"
                        last_pressed = "ttt"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "U":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "ttt":
                        print "I should be v"
                        last_pressed = "t"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][0][0] == "V":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be t"
                        last_pressed = "tt"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "T":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                else:
                    if last_pressed == "tt":
                        print "I should be u"
                        last_pressed = "ttt"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "U":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "ttt":
                        print "I should be v"
                        last_pressed = "t"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][1][0] == "V":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be the letter t"
                        print adder
                        print cursor_position
                        last_pressed = "tt"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "T":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
            if str(key_event[1]) == '119':
                print 'w'
                if self.sort_mode.text == "Sort Mode By Title":
                    if last_pressed == "ww":
                        print "I should be x"
                        last_pressed = "www"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "X":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "www":
                        print "I should be y"
                        last_pressed = "wwww"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][0][0] == "Y":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "wwww":
                        print "I should be z"
                        last_pressed = "w"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][0][0] == "Z":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be w"
                        last_pressed = "ww"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][0][0] == "W":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                else:
                    if last_pressed == "ww":
                        print "I should be x"
                        last_pressed = "www"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "X":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "www":
                        print "I should be y"
                        last_pressed = "wwww"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][1][0] == "Y":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    elif last_pressed == "wwww":
                        print "I should be z"
                        last_pressed = "w"
                        first_index_of_letter =[]
                        for x in range(0,len(song_list)):
                            if song_list[x][1][0] == "Z":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
                    else:
                        print "I should be the letter w"
                        print adder
                        print cursor_position
                        last_pressed = "ww"
                        first_index_of_letter = []
                        for x in range(0, len(song_list)):
                            if song_list[x][1][0] == "W":
                                first_index_of_letter.append(x)
                        adder = first_index_of_letter[0]
        except IndexError:
            return
        if str(key_event[1]) == '120':
            print 'x'
            credit_calculator()
            last_pressed = "x"
            print credit_amount
            self.my_credit_amount.text = "CREDITS " + str(credit_amount)
        if str(key_event[1]) == '273':
            print 'up'
            adder -= 1
            if adder < 0:
                adder = 0
            last_pressed = "up"
        if str(key_event[1]) == '274':
            print 'down'
            adder +=1
            if adder >= len(song_list)-16:
                adder = len(song_list)
            last_pressed = "down"
        if str(key_event[1]) == '275':
            print 'right'
            adder +=8
            if adder > len(song_list)-16:
                adder = len(song_list)
            last_pressed = "right"
        if str(key_event[1]) == '276':
            print 'left'
            adder -=8
            if adder < 0:
                adder = 0
            last_pressed = "left"
        screen_cursor_positioner(adder) # Determines Screen Number and Cursor Position
        selection_screen(self)  # Updates selection screen.
        highlighted_selection_generator(self) # Updates cursor location on selection screen.
        clear_last_selections(self)
        if str(key_event[1]) == '13':
            print 'return'
            print "song selection number = " + str(song_selection_number)
            song_entry(song_selection_number)
            selections_screen_updater(self)
            self.my_credit_amount.text = "CREDITS " + str(credit_amount)
            '''random_generated_song_number = randint(0,len(song_list)-1)
            song_entry(random_generated_song_number)
            selections_screen_updater(self)'''
            last_pressed = "return"

    def file_reader(self, *args):
        global file_time_old
        global upcoming_list
        file_time_check = str(time.ctime(os.path.getmtime("output_list.txt")))  # http://bit.ly/22zKqLS
        if file_time_old != file_time_check:
            #screen_display()  # Updates screen based on file change.
            rss_writer()
            keyboard.press_and_release('b') # Updates Selection Screen
            file_time_old = file_time_check
        else:
            print "Same"
            upcoming_list_recover = open('upcoming_list.pkl', 'rb')
            upcoming_list = pickle.load(upcoming_list_recover)
            upcoming_list_recover.close()
            #selections_screen_updater(self)

def rss_writer():  # This function writes rss feeds to Dropbox public directory.

    global text_display_1
    global display_info
    display_info_recover = open("output_list.txt", 'r+')
    output_list_read = display_info_recover.read()
    display_info_recover.close()
    display_info = output_list_read.split(",")
    rss_song_name = display_info[0]
    rss_artist_name = display_info[1]
    rss_album_name = display_info[2]
    rss_year_info = display_info[3]
    rss_time_info = display_info[4]
    rss_mode_info = display_info[5]
    print rss_song_name
    print rss_artist_name
    rss_current_song = " . . . . . " + str(rss_song_name) + " - " + str(rss_artist_name)
    full_path = os.path.realpath('__file__')  # http://bit.ly/1RQBZYF
    if os.path.exists(str(os.path.dirname("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"))):
        time_now = datetime.datetime.now()
        rss = PyRSS2Gen.RSS2(
            title="Convergence Music System RSS Feed Current Song",
            link="http://www.convergencejukebox.com",
            description="",
            lastBuildDate=datetime.datetime.now(),
            items=[
                PyRSS2Gen.RSSItem(
                    title=str(rss_current_song),
                    link="http://www.convergencejukebox.com",
                    description="Currently Playing",
                    pubDate=datetime.datetime(int(time_now.year), int(time_now.month), int(time_now.day),
                                              int(time_now.hour), int(time_now.minute))),
            ])

        rss.write_xml(open("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"
                           + computer_account_user_name.lower() + "_current_song.xml", "w"))

        rss = PyRSS2Gen.RSS2(
            title="Convergence Music System RSS Feed Current Song",
            link="http://www.convergencejukebox.com",
            description="",
            lastBuildDate=datetime.datetime.now(),

            items=[
                PyRSS2Gen.RSSItem(
                    title=str(rss_song_name),
                    link="http://www.convergencejukebox.com",
                    description="Title Currently Playing",
                    pubDate=datetime.datetime(int(time_now.year), int(time_now.month), int(time_now.day),
                                              int(time_now.hour), int(time_now.minute))),
            ])

        rss.write_xml(open("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"
                           + computer_account_user_name.lower() + "_title_current_song.xml", "w"))

        rss = PyRSS2Gen.RSS2(
            title="Convergence Music System RSS Feed Current Song",
            link="http://www.convergencejukebox.com",
            description="",
            lastBuildDate=datetime.datetime.now(),

            items=[
                PyRSS2Gen.RSSItem(
                    title=str(rss_artist_name),
                    link="http://www.convergencejukebox.com",
                    description="ArtistCurrently Playing",
                    pubDate=datetime.datetime(int(time_now.year), int(time_now.month), int(time_now.day),
                                              int(time_now.hour), int(time_now.minute))),
            ])

        rss.write_xml(open("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"
                           + computer_account_user_name.lower() + "_artist_current_song.xml", "w"))

def selections_screen_updater(self):
    if len(upcoming_list) >= 1:
        self.my_selection_one.text = str(upcoming_list[0])
    if len(upcoming_list) >= 2:
        self.my_selection_two.text = str(upcoming_list[1])
    if len(upcoming_list) >= 3:
        self.my_selection_three.text = str(upcoming_list[2])
    if len(upcoming_list) >= 4:
        self.my_selection_four.text = str(upcoming_list[3])
    if len(upcoming_list) >= 5:
        self.my_selection_five.text = str(upcoming_list[4])
    if len(upcoming_list) >= 6:
        self.my_selection_six.text = str(upcoming_list[5])
    if len(upcoming_list) >= 7:
        self.my_selection_seven.text = str(upcoming_list[6])
    if len(upcoming_list) >= 8:
        self.my_selection_eight.text = str(upcoming_list[7])
    if len(upcoming_list) >= 9:
        self.my_selection_nine.text = str(upcoming_list[8])
    if len(upcoming_list) >= 10:
        self.my_selection_ten.text = str(upcoming_list[9])
    if len(upcoming_list) >= 11:
        self.my_selection_eleven.text = str(upcoming_list[10])
    if len(upcoming_list) >= 12:
        self.my_selection_twelve.text = str(upcoming_list[11])
    if len(upcoming_list) >= 13:
        self.my_selection_thirteen.text = str(upcoming_list[12])
    if len(upcoming_list) >= 14:
        self.my_selection_fourteen.text = str(upcoming_list[13])
    if len(upcoming_list) >= 15:
        self.my_selection_fifteen.text = str(upcoming_list[14])
    if len(upcoming_list) >= 16:
        self.my_selection_sixteen.text = str(upcoming_list[15])
    if len(upcoming_list) == 17:
        self.my_selection_seventeen.text = str(upcoming_list[16])

def screen_cursor_positioner(adder): # Determines Screen Number And Cursor Position
    global cursor_position
    global screen_number
    screen_number = adder / 16
    if screen_number > 0:
        cursor_position = (adder % (screen_number * 16))
    else:
        cursor_position = adder
    return adder

def selections_screen_starter(self):
    global upcoming_list
    if len(upcoming_list) >= 1:
        self.my_selection_one = Label(text=str(upcoming_list[0]), pos=(40, 107))
    else:
        self.my_selection_one = Label(text=' ', pos=(40, 107))
    if len(upcoming_list) >= 2:
        self.my_selection_two = Label(text=str(upcoming_list[1]), pos=(40, 88))
    else:
        self.my_selection_two = Label(text=' ', pos=(40, 88))
    if len(upcoming_list) >= 3:
        self.my_selection_three = Label(text=str(upcoming_list[2]), pos=(40, 69))
    else:
        self.my_selection_three = Label(text=' ', pos=(40, 69))
    if len(upcoming_list) >= 4:
        self.my_selection_four = Label(text=str(upcoming_list[3]), pos=(40, 50))
    else:
        self.my_selection_four = Label(text=' ', pos=(40, 50))
    if len(upcoming_list) >= 5:
        self.my_selection_five = Label(text=str(upcoming_list[4]), pos=(40, 31))
    else:
        self.my_selection_five = Label(text=' ', pos=(40, 31))
    if len(upcoming_list) >= 6:
        self.my_selection_six = Label(text=str(upcoming_list[5]), pos=(40, 12))
    else:
        self.my_selection_six = Label(text=' ', pos=(40, 12))
    if len(upcoming_list) >= 7:
        self.my_selection_seven = Label(text=str(upcoming_list[6]), pos=(40, -7))
    else:
        self.my_selection_seven = Label(text=' ', pos=(40, -7))
    if len(upcoming_list) >= 8:
        self.my_selection_eight = Label(text=str(upcoming_list[7]), pos=(40, -26))
    else:
        self.my_selection_eight = Label(text=' ', pos=(40, -26))
    if len(upcoming_list) >= 9:
        self.my_selection_nine = Label(text=str(upcoming_list[8]), pos=(40, -47))
    else:
        self.my_selection_nine = Label(text=' ', pos=(40, -47))
    if len(upcoming_list) >= 10:
        self.my_selection_ten = Label(text=str(upcoming_list[9]), pos=(40, -66))
    else:
        self.my_selection_ten = Label(text=' ', pos=(40, -66))
    if len(upcoming_list) >= 11:
        self.my_selection_eleven = Label(text=str(upcoming_list[10]), pos=(40, -85))
    else:
        self.my_selection_eleven = Label(text=' ', pos=(40, -85))
    if len(upcoming_list) >= 12:
        self.my_selection_twelve = Label(text=str(upcoming_list[11]), pos=(40, -104))
    else:
        self.my_selection_twelve = Label(text=' ', pos=(40, -104))
    if len(upcoming_list) >= 13:
        self.my_selection_thirteen = Label(text=str(upcoming_list[12]), pos=(40, -123))
    else:
        self.my_selection_thirteen = Label(text=' ', pos=(40, -123))
    if len(upcoming_list) >= 14:
        self.my_selection_fourteen = Label(text=str(upcoming_list[13]), pos=(40, -142))
    else:
        self.my_selection_fourteen = Label(text=' ', pos=(40, -142))
    if len(upcoming_list) >= 15:
        self.my_selection_fifteen = Label(text=str(upcoming_list[14]), pos=(40, -161))
    else:
        self.my_selection_fifteen = Label(text=' ', pos=(40, -161))
    if len(upcoming_list) >= 16:
        self.my_selection_sixteen = Label(text=str(upcoming_list[15]), pos=(40, -180))
    else:
        self.my_selection_sixteen = Label(text=" ", pos=(40, -180))
    if len(upcoming_list) == 17:
        self.my_selection_seventeen = Label(text=str(upcoming_list[16]), pos=(40, -199))
    else:
        self.my_selection_seventeen = Label(text=' ', pos=(40, -199))

def highlighted_selection_generator(self): # Updates cursor location on selection screen.
    global cursor_position
    global song_selection_number
    if cursor_position == 0:
        clear_button_color(self)
        self.my_first_title.background_color = (160, 160, 160, .2)
        self.my_first_artist.background_color = (160, 160, 160, .2)
        if self.my_first_artist.text[0:4] == "The ":
            self.my_first_artist.text = self.my_first_artist.text[4:]
        for i in range(0, len(song_list) - 1):  # Identifies song number from song_list
            if song_list[i][0] == self.my_first_title.text and song_list[i][1] == self.my_first_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 1:
        clear_button_color(self)
        self.my_second_title.background_color = (160, 160, 160, .2)
        self.my_second_artist.background_color = (160, 160, 160, .2)
        if self.my_second_artist.text[0:4] == "The ":
            self.my_second_artist.text = self.my_second_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_second_title.text and song_list[i][1] == self.my_second_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 2:
        clear_button_color(self)
        self.my_third_title.background_color = (160, 160, 160, .2)
        self.my_third_artist.background_color = (160, 160, 160, .2)
        if self.my_third_artist.text[0:4] == "The ":
            self.my_third_artist.text = self.my_third_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_third_title.text and song_list[i][1] == self.my_third_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 3:
        clear_button_color(self)
        self.my_fourth_title.background_color = (160, 160, 160, .2)
        self.my_fourth_artist.background_color = (160, 160, 160, .2)
        if self.my_fourth_artist.text[0:4] == "The ":
            self.my_fourth_artist.text = self.my_fourth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_fourth_title.text and song_list[i][1] == self.my_fourth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 4:
        clear_button_color(self)
        self.my_fifth_title.background_color = (160, 160, 160, .2)
        self.my_fifth_artist.background_color = (160, 160, 160, .2)
        if self.my_fifth_artist.text[0:4] == "The ":
            self.my_fifth_artist.text = self.my_fifth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_fifth_title.text and song_list[i][1] == self.my_fifth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 5:
        clear_button_color(self)
        self.my_sixth_title.background_color = (160, 160, 160, .2)
        self.my_sixth_artist.background_color = (160, 160, 160, .2)
        if self.my_sixth_artist.text[0:4] == "The ":
            self.my_sixth_artist.text = self.my_sixth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_sixth_title.text and song_list[i][1] == self.my_sixth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 6:
        clear_button_color(self)
        self.my_seventh_title.background_color = (160, 160, 160, .2)
        self.my_seventh_artist.background_color = (160, 160, 160, .2)
        if self.my_seventh_artist.text[0:4] == "The ":
            self.my_seventh_artist.text = self.my_seventh_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_seventh_title.text and song_list[i][1] == self.my_seventh_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 7:
        clear_button_color(self)
        self.my_eigth_title.background_color = (160, 160, 160, .2)
        self.my_eigth_artist.background_color = (160, 160, 160, .2)
        if self.my_eigth_artist.text[0:4] == "The ":
            self.my_eigth_artist.text = self.my_eigth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_eigth_title.text and song_list[i][1] == self.my_eigth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 8:
        clear_button_color(self)
        self.my_ninth_title.background_color = (160, 160, 160, .2)
        self.my_ninth_artist.background_color = (160, 160, 160, .2)
        if self.my_ninth_artist.text[0:4] == "The ":
            self.my_ninth_artist.text = self.my_ninth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_ninth_title.text and song_list[i][1] == self.my_ninth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 9:
        clear_button_color(self)
        self.my_tenth_title.background_color = (160, 160, 160, .2)
        self.my_tenth_artist.background_color = (160, 160, 160, .2)
        if self.my_tenth_artist.text[0:4] == "The ":
            self.my_tenth_artist.text = self.my_tenth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_tenth_title.text and song_list[i][1] == self.my_tenth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 10:
        clear_button_color(self)
        self.my_eleventh_title.background_color = (160, 160, 160, .2)
        self.my_eleventh_artist.background_color = (160, 160, 160, .2)
        if self.my_eleventh_artist.text[0:4] == "The ":
            self.my_eleventh_artist.text = self.my_eleventh_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_eleventh_title.text and song_list[i][1] == self.my_eleventh_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 11:
        clear_button_color(self)
        self.my_twelfth_title.background_color = (160, 160, 160, .2)
        self.my_twelfth_artist.background_color = (160, 160, 160, .2)
        if self.my_twelfth_artist.text[0:4] == "The ":
            self.my_twelfth_artist.text = self.my_twelfth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_twelfth_title.text and song_list[i][1] == self.my_twelfth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 12:
        clear_button_color(self)
        self.my_thirteenth_title.background_color = (160, 160, 160, .2)
        self.my_thirteenth_artist.background_color = (160, 160, 160, .2)
        if self.my_thirteenth_artist.text[0:4] == "The ":
            self.my_thirteenth_artist.text = self.my_thirteenth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_thirteenth_title.text and song_list[i][1] == self.my_thirteenth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 13:
        clear_button_color(self)
        self.my_fourteenth_title.background_color = (160, 160, 160, .2)
        self.my_fourteenth_artist.background_color = (160, 160, 160, .2)
        if self.my_fourteenth_artist.text[0:4] == "The ":
            self.my_fourteenth_artist.text = self.my_fourteenth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_fourteenth_title.text and song_list[i][1] == self.my_fourteenth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 14:
        clear_button_color(self)
        self.my_fifteenth_title.background_color = (160, 160, 160, .2)
        self.my_fifteenth_artist.background_color = (160, 160, 160, .2)
        if self.my_fifteenth_artist.text[0:4] == "The ":
            self.my_fifteenth_artist.text = self.my_fifteenth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_fifteenth_title.text and song_list[i][1] == self.my_fifteenth_artist.text:
                song_selection_number = song_list[i][9]
    if cursor_position == 15:
        clear_button_color(self)
        self.my_sixteenth_title.background_color = (160, 160, 160, .2)
        self.my_sixteenth_artist.background_color = (160, 160, 160, .2)
        if self.my_sixteenth_artist.text[0:4] == "The ":
            self.my_sixteenth_artist.text = self.my_sixteenth_artist.text[4:]
        for i in range(0, len(song_list) - 1):
            if song_list[i][0] == self.my_sixteenth_title.text and song_list[i][1] == self.my_sixteenth_artist.text:
                song_selection_number = song_list[i][9]

def selection_screen(self): # Updates selection screen.
    global cursor_position
    global screen_number
    resize_button_text(self)
    selection_start = screen_number * 16
    if selection_start + 16 > len(song_list):
        selection_start = (screen_number * 16) - 16


    if len(str(song_list[selection_start][0])) > 36:
        if len(str(song_list[selection_start][0])) >= 48:
            self.my_first_title.font_size = 12
        elif len(str(song_list[selection_start][0])) > 44:
            self.my_first_title.font_size = 13
        else:
            self.my_first_title.font_size = 14
    if len(str(song_list[selection_start][1])) > 36:
        if len(str(song_list[selection_start][0])) >= 48:
            self.my_first_artist.font_size = 12
        elif len(str(song_list[selection_start][0])) > 44:
            self.my_first_artist.font_size = 13
        else:
            self.my_first_artist.font_size = 14
    self.my_first_title.text = str(song_list[selection_start][0])
    self.my_first_artist.text = str(song_list[selection_start][1])
    if len(str(song_list[selection_start + 1][0])) > 36:
        if len(str(song_list[selection_start + 1][0])) >= 48:
            self.my_second_title.font_size = 12
        elif len(str(song_list[selection_start + 1][0])) > 44:
            self.my_second_title.font_size = 13
        else:
            self.my_second_title.font_size = 14
    if len(str(song_list[selection_start + 1][1])) > 36:
        if len(str(song_list[selection_start + 1][0])) >= 48:
            self.my_second_artist.font_size = 12
        elif len(str(song_list[selection_start + 1][0])) > 44:
            self.my_second_artist.font_size = 13
        else:
            self.my_second_artist.font_size = 14
    self.my_second_title.text = str(song_list[selection_start + 1][0])
    self.my_second_artist.text = str(song_list[selection_start + 1][1])
    if len(str(song_list[selection_start + 2][0])) > 36:
        if len(str(song_list[selection_start + 2][0])) >= 48:
            self.my_third_title.font_size = 12
        elif len(str(song_list[selection_start + 2][0])) > 44:
            self.my_third_title.font_size = 13
        else:
            self.my_third_title.font_size = 14
    if len(str(song_list[selection_start + 2][1])) > 36:
        if len(str(song_list[selection_start + 2][0])) >= 48:
            self.my_third_artist.font_size = 12
        elif len(str(song_list[selection_start + 2][0])) > 44:
            self.my_third_artist.font_size = 13
        else:
            self.my_third_artist.font_size = 14
    self.my_third_title.text = str(song_list[selection_start + 2][0])
    self.my_third_artist.text = str(song_list[selection_start + 2][1])
    if len(str(song_list[selection_start + 3][0])) > 36:
        if len(str(song_list[selection_start + 3][0])) >= 48:
            self.my_fourth_title.font_size = 12
        elif len(str(song_list[selection_start + 3][0])) > 44:
            self.my_fourth_title.font_size = 13
        else:
            self.my_fourth_title.font_size = 14
    if len(str(song_list[selection_start + 3][1])) > 36:
        if len(str(song_list[selection_start + 3][0])) >= 48:
            self.my_fourth_artist.font_size = 12
        elif len(str(song_list[selection_start + 3][0])) > 44:
            self.my_fourth_artist.font_size = 13
        else:
            self.my_fourth_artist.font_size = 14
    self.my_fourth_title.text = str(song_list[selection_start + 3][0])
    self.my_fourth_artist.text = str(song_list[selection_start + 3][1])
    if len(str(song_list[selection_start + 4][0])) > 36:
        if len(str(song_list[selection_start + 4][0])) >= 48:
            self.my_fifth_title.font_size = 12
        elif len(str(song_list[selection_start + 4][0])) > 44:
            self.my_fifth_title.font_size = 13
        else:
            self.my_fifth_title.font_size = 14
    if len(str(song_list[selection_start + 4][1])) > 36:
        if len(str(song_list[selection_start + 4][0])) >= 48:
            self.my_fifth_artist.font_size = 12
        elif len(str(song_list[selection_start + 4][0])) > 44:
            self.my_fifth_artist.font_size = 13
        else:
            self.my_fifth_artist.font_size = 14
    self.my_fifth_title.text = str(song_list[selection_start + 4][0])
    self.my_fifth_artist.text = str(song_list[selection_start + 4][1])
    if len(str(song_list[selection_start + 5][0])) > 36:
        if len(str(song_list[selection_start + 5][0])) >= 48:
            self.my_sixth_title.font_size = 12
        elif len(str(song_list[selection_start + 5][0])) > 44:
            self.my_sixth_title.font_size = 13
        else:
            self.my_sixth_title.font_size = 14
    if len(str(song_list[selection_start + 5][1])) > 36:
        if len(str(song_list[selection_start + 5][0])) >= 48:
            self.my_sixth_artist.font_size = 12
        elif len(str(song_list[selection_start + 5][0])) > 44:
            self.my_sixth_artist.font_size = 13
        else:
            self.my_sixth_artist.font_size = 14
    self.my_sixth_title.text = str(song_list[selection_start + 5][0])
    self.my_sixth_artist.text = str(song_list[selection_start + 5][1])
    if len(str(song_list[selection_start + 6][0])) > 36:
        if len(str(song_list[selection_start + 6][0])) >= 48:
            self.my_seventh_title.font_size = 12
        elif len(str(song_list[selection_start + 6][0])) > 44:
            self.my_seventh_title.font_size = 13
        else:
            self.my_seventh_title.font_size = 14
    if len(str(song_list[selection_start + 6][1])) > 36:
        if len(str(song_list[selection_start + 6][0])) >= 48:
            self.my_seventh_artist.font_size = 12
        elif len(str(song_list[selection_start + 6][0])) > 44:
            self.my_seventh_artist.font_size = 13
        else:
            self.my_seventh_artist.font_size = 14
    self.my_seventh_title.text = str(song_list[selection_start + 6][0])
    self.my_seventh_artist.text = str(song_list[selection_start + 6][1])
    if len(str(song_list[selection_start + 7][0])) > 36:
        if len(str(song_list[selection_start + 7][0])) >= 48:
            self.my_eigth_title.font_size = 12
        elif len(str(song_list[selection_start + 7][0])) > 44:
            self.my_eigth_title.font_size = 13
        else:
            self.my_eigth_title.font_size = 14
    if len(str(song_list[selection_start + 7][1])) > 36:
        if len(str(song_list[selection_start + 7][0])) >= 48:
            self.my_eigth_artist.font_size = 12
        elif len(str(song_list[selection_start + 7][0])) > 44:
            self.my_eigth_artist.font_size = 13
        else:
            self.my_eigth_artist.font_size = 14
    self.my_eigth_title.text = str(song_list[selection_start + 7][0])
    self.my_eigth_artist.text = str(song_list[selection_start + 7][1])
    if len(str(song_list[selection_start + 8][0])) > 36:
        if len(str(song_list[selection_start + 8][0])) >= 48:
            self.my_ninth_title.font_size = 12
        elif len(str(song_list[selection_start + 8][0])) > 44:
            self.my_ninth_title.font_size = 13
        else:
            self.my_ninth_title.font_size = 14
    if len(str(song_list[selection_start + 8][1])) > 36:
        if len(str(song_list[selection_start + 8][0])) >= 48:
            self.my_ninth_artist.font_size = 12
        elif len(str(song_list[selection_start + 8][0])) > 44:
            self.my_ninth_artist.font_size = 13
        else:
            self.my_ninth_artist.font_size = 14
    self.my_ninth_title.text = str(song_list[selection_start + 8][0])
    self.my_ninth_artist.text = str(song_list[selection_start + 8][1])
    if len(str(song_list[selection_start + 9][0])) > 36:
        if len(str(song_list[selection_start + 9][0])) >= 48:
            self.my_tenth_title.font_size = 12
        elif len(str(song_list[selection_start + 9][0])) > 44:
            self.my_tenth_title.font_size = 13
        else:
            self.my_tenth_title.font_size = 14
    if len(str(song_list[selection_start + 9][1])) > 36:
        if len(str(song_list[selection_start + 9][0])) >= 48:
            self.my_tenth_artist.font_size = 12
        elif len(str(song_list[selection_start + 9][0])) > 44:
            self.my_tenth_artist.font_size = 13
        else:
            self.my_tenth_artist.font_size = 14
    self.my_tenth_title.text = str(song_list[selection_start + 9][0])
    self.my_tenth_artist.text = str(song_list[selection_start + 9][1])
    if len(str(song_list[selection_start + 10][0])) > 36:
        if len(str(song_list[selection_start + 10][0])) >= 48:
            self.my_eleventh_title.font_size = 12
        elif len(str(song_list[selection_start + 10][0])) > 44:
            self.my_eleventh_title.font_size = 13
        else:
            self.my_eleventh_title.font_size = 14
    if len(str(song_list[selection_start + 10][1])) > 36:
        if len(str(song_list[selection_start + 10][0])) >= 48:
            self.my_eleventh_artist.font_size = 12
        elif len(str(song_list[selection_start + 10][0])) > 44:
            self.my_eleventh_artist.font_size = 13
        else:
            self.my_eleventh_artist.font_size = 14
    self.my_eleventh_title.text = str(song_list[selection_start + 10][0])
    self.my_eleventh_artist.text = str(song_list[selection_start + 10][1])
    if len(str(song_list[selection_start + 11][0])) > 36:
        if len(str(song_list[selection_start + 11][0])) >= 48:
            self.my_twelfth_title.font_size = 12
        elif len(str(song_list[selection_start + 11][0])) > 44:
            self.my_twelfth_title.font_size = 13
        else:
            self.my_twelfth_title.font_size = 14
    if len(str(song_list[selection_start + 11][1])) > 36:
        if len(str(song_list[selection_start + 11][0])) >= 48:
            self.my_twelfth_artist.font_size = 12
        elif len(str(song_list[selection_start + 11][0])) > 44:
            self.my_twelfth_artist.font_size = 13
        else:
            self.my_twelfth_artist.font_size = 14
    self.my_twelfth_title.text = str(song_list[selection_start + 11][0])
    self.my_twelfth_artist.text = str(song_list[selection_start + 11][1])
    if len(str(song_list[selection_start + 12][0])) > 36:
        if len(str(song_list[selection_start + 12][0])) >= 48:
            self.my_thirteenth_title.font_size = 12
        elif len(str(song_list[selection_start + 12][0])) > 44:
            self.my_thirteenth_title.font_size = 13
        else:
            self.my_thirteenth_title.font_size = 14
    if len(str(song_list[selection_start + 12][1])) > 36:
        if len(str(song_list[selection_start + 12][0])) >= 48:
            self.my_thirteenth_artist.font_size = 12
        elif len(str(song_list[selection_start + 12][0])) > 44:
            self.my_thirteenth_artist.font_size = 13
        else:
            self.my_thirteenth_artist.font_size = 14
    self.my_thirteenth_title.text = str(song_list[selection_start + 12][0])
    self.my_thirteenth_artist.text = str(song_list[selection_start + 12][1])
    if len(str(song_list[selection_start + 13][0])) > 36:
        if len(str(song_list[selection_start + 13][0])) >= 48:
            self.my_fourteenth_title.font_size = 12
        elif len(str(song_list[selection_start + 13][0])) > 44:
            self.my_fourteenth_title.font_size = 13
        else:
            self.my_fourteenth_title.font_size = 14
    if len(str(song_list[selection_start + 13][1])) > 36:
        if len(str(song_list[selection_start + 13][0])) >= 48:
            self.my_fourteenth_artist.font_size = 12
        elif len(str(song_list[selection_start + 13][0])) > 44:
            self.my_fourteenth_artist.font_size = 13
        else:
            self.my_fourteenth_artist.font_size = 14
    self.my_fourteenth_title.text = str(song_list[selection_start + 13][0])
    self.my_fourteenth_artist.text = str(song_list[selection_start + 13][1])
    if len(str(song_list[selection_start + 14][0])) > 36:
        if len(str(song_list[selection_start + 14][0])) >= 48:
            self.my_fifteenth_title.font_size = 12
        elif len(str(song_list[selection_start + 14][0])) > 44:
            self.my_fifteenth_title.font_size = 13
        else:
            self.my_fifteenth_title.font_size = 14
    if len(str(song_list[selection_start + 14][1])) > 36:
        if len(str(song_list[selection_start + 14][0])) >= 48:
            self.my_fifteenth_artist.font_size = 12
        elif len(str(song_list[selection_start + 14][0])) > 44:
            self.my_fifteenth_artist.font_size = 13
        else:
            self.my_fifteenth_artist.font_size = 14
    self.my_fifteenth_title.text = str(song_list[selection_start + 14][0])
    self.my_fifteenth_artist.text = str(song_list[selection_start + 14][1])
    if len(str(song_list[selection_start + 15][0])) > 36:
        if len(str(song_list[selection_start + 15][0])) >= 48:
            self.my_sixteenth_title.font_size = 12
        elif len(str(song_list[selection_start + 15][0])) > 44:
            self.my_sixteenth_title.font_size = 13
        else:
            self.my_sixteenth_title.font_size = 14
    if len(str(song_list[selection_start + 15][1])) > 36:
        if len(str(song_list[selection_start + 15][0])) >= 48:
            self.my_sixteenth_artist.font_size = 12
        elif len(str(song_list[selection_start + 15][0])) > 44:
            self.my_sixteenth_artist.font_size = 13
        else:
            self.my_sixteenth_artist.font_size = 14
    self.my_sixteenth_title.text = str(song_list[selection_start + 15][0])
    self.my_sixteenth_artist.text = str(song_list[selection_start + 15][1])

    x = self.my_first_artist.text    
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_first_artist.text = str(x)
        
    x = self.my_second_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_second_artist.text = str(x)

    x = self.my_third_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_third_artist.text = str(x)

    x = self.my_fourth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_fourth_artist.text = str(x)

    x = self.my_fifth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_fifth_artist.text = str(x)

    x = self.my_sixth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_sixth_artist.text = str(x)

    x = self.my_seventh_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_seventh_artist.text = str(x)

    x = self.my_eigth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_eigth_artist.text = str(x)

    x = self.my_ninth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_ninth_artist.text = str(x)

    x = self.my_tenth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_tenth_artist.text = str(x)

    x = self.my_eleventh_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_eleventh_artist.text = str(x)

    x = self.my_twelfth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_twelfth_artist.text = str(x)

    x = self.my_thirteenth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_thirteenth_artist.text = str(x)

    x = self.my_fourteenth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_fourteenth_artist.text = str(x)

    x = self.my_fifteenth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_fifteenth_artist.text = str(x)

    x = self.my_sixteenth_artist.text
    if x.lower() in the_bands_list_lower_case:
        x = "The " + str(x)
        self.my_sixteenth_artist.text = str(x)

    
        
    clear_button_color(self)

def credit_calculator(event=None):
    global credit_amount
    credit_amount += 1
    print credit_amount

def selection_font_size(self):
    self.my_selection_one.font_size = 16
    self.my_selection_two.font_size = 16
    self.my_selection_three.font_size = 16
    self.my_selection_four.font_size = 16
    self.my_selection_five.font_size = 16
    self.my_selection_six.font_size = 16
    self.my_selection_seven.font_size = 16
    self.my_selection_eight.font_size = 16
    self.my_selection_nine.font_size = 16
    self.my_selection_ten.font_size = 16
    self.my_selection_eleven.font_size = 16
    self.my_selection_twelve.font_size = 16
    self.my_selection_thirteen.font_size = 16
    self.my_selection_fourteen.font_size = 16
    self.my_selection_fifteen.font_size = 16
    self.my_selection_sixteen.font_size = 16
    self.my_selection_seventeen.font_size = 16

def resize_button_text(self):
    self.my_first_title.font_size = 16
    self.my_first_artist.font_size = 16
    self.my_second_title.font_size = 16
    self.my_second_artist.font_size = 16
    self.my_third_title.font_size = 16
    self.my_third_artist.font_size = 16
    self.my_fourth_title.font_size = 16
    self.my_fourth_artist.font_size = 16
    self.my_fifth_title.font_size = 16
    self.my_fifth_artist.font_size = 16
    self.my_sixth_title.font_size = 16
    self.my_sixth_artist.font_size = 16
    self.my_seventh_title.font_size = 16
    self.my_seventh_artist.font_size = 16
    self.my_eigth_title.font_size = 16
    self.my_eigth_artist.font_size = 16
    self.my_ninth_title.font_size = 16
    self.my_ninth_artist.font_size = 16
    self.my_tenth_title.font_size = 16
    self.my_tenth_artist.font_size = 16
    self.my_eleventh_title.font_size = 16
    self.my_eleventh_artist.font_size = 16
    self.my_twelfth_title.font_size = 16
    self.my_twelfth_artist.font_size = 16
    self.my_thirteenth_title.font_size = 16
    self.my_thirteenth_artist.font_size = 16
    self.my_fourteenth_title.font_size = 16
    self.my_fourteenth_artist.font_size = 16
    self.my_fifteenth_title.font_size = 16
    self.my_fifteenth_artist.font_size = 16
    self.my_sixteenth_title.font_size = 16
    self.my_sixteenth_artist.font_size = 16

def clear_button_color(self):

    self.my_first_title.background_color = (0, 0, 0, 0)
    self.my_first_artist.background_color = (0, 0, 0, 0)
    self.my_second_title.background_color = (0, 0, 0, 0)
    self.my_second_artist.background_color = (0, 0, 0, 0)
    self.my_third_title.background_color = (0, 0, 0, 0)
    self.my_third_artist.background_color = (0, 0, 0, 0)
    self.my_fourth_title.background_color = (0, 0, 0, 0)
    self.my_fourth_artist.background_color = (0, 0, 0, 0)
    self.my_fifth_title.background_color = (0, 0, 0, 0)
    self.my_fifth_artist.background_color = (0, 0, 0, 0)
    self.my_sixth_title.background_color = (0, 0, 0, 0)
    self.my_sixth_artist.background_color = (0, 0, 0, 0)
    self.my_seventh_title.background_color = (0, 0, 0, 0)
    self.my_seventh_artist.background_color = (0, 0, 0, 0)
    self.my_eigth_title.background_color = (0, 0, 0, 0)
    self.my_eigth_artist.background_color = (0, 0, 0, 0)
    self.my_ninth_title.background_color = (0, 0, 0, 0)
    self.my_ninth_artist.background_color = (0, 0, 0, 0)
    self.my_tenth_title.background_color = (0, 0, 0, 0)
    self.my_tenth_artist.background_color = (0, 0, 0, 0)
    self.my_eleventh_title.background_color = (0, 0, 0, 0)
    self.my_eleventh_artist.background_color = (0, 0, 0, 0)
    self.my_twelfth_title.background_color = (0, 0, 0, 0)
    self.my_twelfth_artist.background_color = (0, 0, 0, 0)
    self.my_thirteenth_title.background_color = (0, 0, 0, 0)
    self.my_thirteenth_artist.background_color = (0, 0, 0, 0)
    self.my_fourteenth_title.background_color = (0, 0, 0, 0)
    self.my_fourteenth_artist.background_color = (0, 0, 0, 0)
    self.my_fifteenth_title.background_color = (0, 0, 0, 0)
    self.my_fifteenth_artist.background_color = (0, 0, 0, 0)
    self.my_sixteenth_title.background_color = (0, 0, 0, 0)
    self.my_sixteenth_artist.background_color = (0, 0, 0, 0)

def clear_last_selections(self):
    if self.my_first_title.text == "zzzzz":
        self.my_first_title.font_size = 0
        self.my_first_artist.font_size = 0
    if self.my_second_title.text == "zzzzz":
        self.my_second_title.font_size = 0
        self.my_second_artist.font_size = 0
    if self.my_third_title.text == "zzzzz":
        self.my_third_title.font_size = 0
        self.my_third_artist.font_size = 0
    if self.my_fourth_title.text == "zzzzz":
        self.my_fourth_title.font_size = 0
        self.my_fourth_artist.font_size = 0
    if self.my_fifth_title.text == "zzzzz":
        self.my_fifth_title.font_size = 0
        self.my_fifth_artist.font_size = 0
    if self.my_sixth_title.text == "zzzzz":
        self.my_sixth_title.font_size = 0
        self.my_sixth_artist.font_size = 0
    if self.my_seventh_title.text == "zzzzz":
        self.my_seventh_title.font_size = 0
        self.my_seventh_artist.font_size = 0
    if self.my_eigth_title.text == "zzzzz":
        self.my_eigth_title.font_size = 0
        self.my_eigth_artist.font_size = 0
    if self.my_ninth_title.text == "zzzzz":
        self.my_ninth_title.font_size = 0
        self.my_ninth_artist.font_size = 0
    if self.my_tenth_title.text == "zzzzz":
        self.my_tenth_title.font_size = 0
        self.my_tenth_artist.font_size = 0
    if self.my_eleventh_title.text == "zzzzz":
        self.my_eleventh_title.font_size = 0
        self.my_eleventh_artist.font_size = 0
    if self.my_twelfth_title.text == "zzzzz":
        self.my_twelfth_title.font_size = 0
        self.my_twelfth_artist.font_size = 0
    if self.my_thirteenth_title.text == "zzzzz":
        self.my_thirteenth_title.font_size = 0
        self.my_thirteenth_artist.font_size = 0
    if self.my_fourteenth_title.text == "zzzzz":
        self.my_fourteenth_title.font_size = 0
        self.my_fourteenth_artist.font_size = 0
    if self.my_fifteenth_title.text == "zzzzz":
        self.my_fifteenth_title.font_size = 0
        self.my_fifteenth_artist.font_size = 0
    if self.my_sixteenth_title.text == "zzzzz":
        self.my_sixteenth_title.font_size = 0
        self.my_sixteenth_artist.font_size = 0

def song_entry(song_number):  # Writes selected song to playlist.
    global credit_amount
    global upcoming_list
    if credit_amount == 0:
        playMP3('buzz.mp3')
        return
    play_list_recover = open('play_list.pkl', 'rb')
    play_list = pickle.load(play_list_recover)
    play_list_recover.close()
    new_entry = song_number
    print new_entry
    if new_entry in play_list:  # Checks if song number is in play_list to avoid duplicates. http://bit.ly/2pTlkLS
        a = play_list.index(song_number)  # Locates song number in play_list. Index number assigned to variable.
        b = play_list[a]  # b variable assigned song number at play_list index provided in above line.
        if song_number == b:
            return
    x = 0
    while x < len(song_list):  # Saves all upcoming song titles and artist to upcoming_list for side display.
        if song_list[x][9] == new_entry:
            print song_list[x][0]
            upcoming_song = str(song_list[x][0]) + " - " + str(song_list[x][1])
            upcoming_list_recover = open('upcoming_list.pkl', 'rb')
            upcoming_list = pickle.load(upcoming_list_recover)
            upcoming_list_recover.close()
            upcoming_list.append(upcoming_song)
            upcoming_list_save = open('upcoming_list.pkl', 'wb')
            pickle.dump(upcoming_list, upcoming_list_save)
            upcoming_list_save.close()
        x += 1
    play_list.append(new_entry)
    play_list_save = open('play_list.pkl', 'wb')
    pickle.dump(play_list, play_list_save)
    play_list_save.close()
    credit_amount -= 1
    playMP3('success.mp3')

def mciSend(s):  # Function of playmp3.py
    if sys.platform == 'win32':
        winmm = windll.winmm  # Variable used in playmp3.py.
        i = winmm.mciSendStringA(s, 0, 0, 0)
        if i != 0:
            print "Error %d in mciSendString %s" % (i, s)

def playMP3(mp3Name):  # Function of playmp3.py
    mciSend("Close All")
    mciSend("Open \"%s\" Type MPEGVideo Alias theMP3" % mp3Name)
    mciSend("Play theMP3 Wait")
    mciSend("Close theMP3")

def clear_alpha_keys(event=None):
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    a_key_press = 0  # Resets other multikeys to base letter..
    d_key_press = 0
    g_key_press = 0
    j_key_press = 0
    m_key_press = 0
    p_key_press = 0
    w_key_press = 0
    t_key_press = 0

def so_long(event=None): # Used to terminate program.

    if sys.platform == 'win32':
        set_default_screen_resolution()
        if os.path.exists(str(os.path.dirname(full_path)) + "\convergenceplayer.py"):
            os.system("player_quit_py.exe")  # Launches Convergence Jukebox Player
            jukebox_display.destroy()
        else:
            os.system("taskkill /im convergenceplayer.exe")
            jukebox_display.destroy()

    if sys.platform.startswith('linux'):
        sys.exit()

def set_default_screen_resolution(): # Used by so_long()

    class ScreenRes(object):  # http://bit.ly/1R6CXjF
        @classmethod
        def set(cls, width=None, height=None, depth=32):
            '''
            Set the primary display to the specified mode
            '''
            if width and height:
                print('Setting resolution to {}x{}'.format(width, height, depth))
            else:
                print('Setting resolution to defaults')

            if sys.platform == 'win32':
                cls._win32_set(width, height, depth)
            elif sys.platform.startswith('linux'):
                cls._linux_set(width, height, depth)
            elif sys.platform.startswith('darwin'):
                cls._osx_set(width, height, depth)

        @classmethod
        def get(cls):
            if sys.platform == 'win32':
                return cls._win32_get()
            elif sys.platform.startswith('linux'):
                return cls._linux_get()
            elif sys.platform.startswith('darwin'):
                return cls._osx_get()

        @classmethod
        def get_modes(cls):
            if sys.platform == 'win32':
                return cls._win32_get_modes()
            elif sys.platform.startswith('linux'):
                return cls._linux_get_modes()
            elif sys.platform.startswith('darwin'):
                return cls._osx_get_modes()

        @staticmethod
        def _win32_get_modes():
            '''
            Get the primary windows display width and height
            '''
            import win32api
            from pywintypes import DEVMODEType, error
            modes = []
            i = 0
            try:
                while True:
                    mode = win32api.EnumDisplaySettings(None, i)
                    modes.append((
                        int(mode.PelsWidth),
                        int(mode.PelsHeight),
                        int(mode.BitsPerPel),
                        ))
                    i += 1
            except error:
                pass

            return modes

        @staticmethod
        def _win32_get():
            '''
            Get the primary windows display width and height
            '''
            import ctypes
            user32 = ctypes.windll.user32
            screensize = (
                user32.GetSystemMetrics(0),
                user32.GetSystemMetrics(1),
                )
            return screensize

        @staticmethod
        def _win32_set(width=None, height=None, depth=32):
            '''
            Set the primary windows display to the specified mode
            '''
            # Gave up on ctypes, the struct is really complicated
            #user32.ChangeDisplaySettingsW(None, 0)
            import win32api
            from pywintypes import DEVMODEType
            if width and height:

                if not depth:
                    depth = 32

                mode = win32api.EnumDisplaySettings()
                mode.PelsWidth = width
                mode.PelsHeight = height
                mode.BitsPerPel = depth

                win32api.ChangeDisplaySettings(mode, 0)
            else:
                win32api.ChangeDisplaySettings(None, 0)


        @staticmethod
        def _win32_set_default():
            '''
            Reset the primary windows display to the default mode
            '''
            # Interesting since it doesn't depend on pywin32
            import ctypes
            user32 = ctypes.windll.user32
            # set screen size
            user32.ChangeDisplaySettingsW(None, 0)

        @staticmethod
        def _linux_set(width=None, height=None, depth=32):
            raise NotImplementedError()

        @staticmethod
        def _linux_get():
            raise NotImplementedError()

        @staticmethod
        def _linux_get_modes():
            raise NotImplementedError()

        @staticmethod
        def _osx_set(width=None, height=None, depth=32):
            raise NotImplementedError()

        @staticmethod
        def _osx_get():
            raise NotImplementedError()

        @staticmethod
        def _osx_get_modes():
            raise NotImplementedError()


    if __name__ == '__main__':
        print('Primary screen resolution: {}x{}'.format(
            *ScreenRes.get()
            ))
        print(ScreenRes.get_modes())
        # ScreenRes.set(1280, 720)
        # ScreenRes.set(1920, 1080)
        if sys.platform.startswith('linux'):
            print "music directory exists at " + str(os.path.dirname(full_path)) + "Removing underscores to MP3 Files."
            current_path = os.getcwd()
            print current_path
            path = str(current_path) + "/music"
            os.chdir( path )# sets path for mpg321
            [os.rename(f, f.replace('_', ' ')) for f in os.listdir('.') if not f.startswith('.')]
        ScreenRes.set() # Set defaults

if __name__=="__main__":
   MyFinalApp().run()
