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
from kivy.graphics import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

class StageControl(App):

    config = ConfigParser.ConfigParser()
    scenes = list()

    currentIndex = 0;
    go = False

    def build(self):
    	
        
        self.config.read("scenes.txt")
        for section in self.config.sections():
            self.scenes.append(section)
        for scene in self.scenes:
            print scene



        def button_press(x):
            self.currentIndex = int(x.text.split(".")[0]) - 1;
            l_current.text = "Current Selection: " + self.scenes[self.currentIndex]


        def sayHi(x):
            pass
        def scenePlus(x):
            self.currentIndex += 1 
            if self.currentIndex > len(self.scenes) - 1:
                self.currentIndex = len(self.scenes) - 1
            l_current.text = "Current Selection: " + self.scenes[self.currentIndex]
        
        def sceneMinus(x):
            self.currentIndex -= 1
            if self.currentIndex < 0:
                self.currentIndex = 0
            l_current.text = "Current Selection: " + self.scenes[self.currentIndex]

        def go(x):
            self.go = True

        def stop(x):
            self.go = False

        def loop(x):
            if self.go:
                print self.scenes[self.currentIndex]

        #self.control = Control()

        Clock.schedule_interval(loop,0)


    	layout = FloatLayout(size=(300, 300))

    	l_title = Label(text="Bellarmine College Prep",pos=(0,250), font_size='50sp')
    	layout.add_widget(l_title)

        p_title = Label(text="Noises Off",pos=(0,200), font_size='30sp')
        layout.add_widget(p_title)

        with p_title.canvas:
            Line(points=[0, 460, 800, 460], width= 5)

    	b_go = Button(text='Start',size_hint=(.15, .05),pos=(50, 400))
        b_go.bind(on_release = go)
        layout.add_widget(b_go)

        b_stop = Button(text='Stop',size_hint=(.15, .05),pos=(200, 400))
        b_stop.bind(on_release = stop)
        layout.add_widget(b_stop)


        b_sceneUp = Button(text='Scene Up',size_hint=(.15, .1),pos=(550, 300))
        b_sceneUp.bind(on_release = sceneMinus)
    	layout.add_widget(b_sceneUp)

    	b_sceneDown = Button(text='Scene Down',size_hint=(.15, .1),pos=(550, 200))
    	b_sceneDown.bind(on_release=scenePlus)
        layout.add_widget(b_sceneDown)

        l_current = Label(text = "Current Selection: " + self.scenes[self.currentIndex], pos=(-250,-270))
        layout.add_widget(l_current)

    	glayout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		#Make sure the height is such that there is something to scroll.
        glayout.bind(minimum_height=glayout.setter('height'))
        num = 0;
        for i in self.scenes:
            btn = Button(text=str(num + 1) + ". " + str(i), size_hint_y=None, height=40)
            btn.bind(on_release=button_press)
            glayout.add_widget(btn)
            num +=1;
            
        root = ScrollView(size_hint=(None, None), size=(300, 300), pos = (50,60))
        root.do_scroll_x = False
        root.add_widget(glayout)

        

    	layout.add_widget(root)

    	return layout

class Control:
    config = ConfigParser.ConfigParser()
    scenes = list()
    def __init__(self):
        self.config.read("scenes.txt")
        for section in self.config.sections():
            self.scenes.append(section)
        for scene in self.scenes:
            print scene
    def loop(self,dt):
        pass
        


        

if __name__ == '__main__':
    StageControl().run()
