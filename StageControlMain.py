'''
Application example using build() + return
==========================================

An application can be build if you return a widget on build(), or if you set
self.root.
'''

import kivy
kivy.require('1.0.7')

import ConfigParser
import string

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

class StageControl(App):

    def build(self):
    	
        def button_press(x):
			print x.text;
        def sayHi(x):
            pass

        self.control = Control()

        Clock.schedule_interval(self.control.loop,0)


    	layout = FloatLayout(size=(300, 300))

    	l_title = Label(text="Bellarmine College Prep",pos=(0,250), font_size='50sp')
    	layout.add_widget(l_title)

        p_title = Label(text="Noises Off",pos=(0,175), font_size='30sp')
        layout.add_widget(p_title)

    	b_scenePlus = Button(text='Scene +',size_hint=(.15, .1),pos=(550, 300))
    	layout.add_widget(b_scenePlus)

    	b_sceneMinus = Button(text='Scene -',size_hint=(.15, .1),pos=(550, 200))
    	layout.add_widget(b_sceneMinus)

    	glayout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		#Make sure the height is such that there is something to scroll.
        glayout.bind(minimum_height=glayout.setter('height'))
        for i in range(30):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            btn.bind(on_release=button_press)
            glayout.add_widget(btn)
            
        root = ScrollView(size_hint=(None, None), size=(400, 450))
        root.add_widget(glayout)

        

    	layout.add_widget(root)

    	return layout

class Control:
    config = ConfigParser.ConfigParser()
    def __init__(self):
       self.config.read("scenes.txt")
       for section in self.config.sections():
            print section
            for option in self.config.options(section):
                print " ", option, "=", self.config.get(section, option)
    def loop(self,dt):
        pass
        


        

if __name__ == '__main__':
    StageControl().run()
