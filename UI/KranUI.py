'''
Created on 29.05.2019

@author: 10MSX933
'''
import gc
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

#class Screen(RelativeLayout):
    #def __init__(self, **kwargs):
        #super(Screen, self).__init__(**kwargs)         
        #Window.fullscreen = True
        #Window.allow_screensave = False
        #Window.minimum_width = 1920
        #Window.minimum_height = 1080
        #Window.clearcolor = (.5, .5, .5, .5)
        #layout1 = AnchorLayout(anchor_x='right', anchor_y='bottom')
        #layout2 = RelativeLayout(width = 50,size_hint = (0.5 ,1))
        #self.add_widget(layout1)     
        #layout1.add_widget(layout2)   
        #btn1 = Button(text='Links',width = 200,size_hint = (0.25 ,.25), pos_hint={'left': 0.5, 'center_y': .50})
        #layout2.add_widget(btn1)
        #btn2 = Button(text='Rechts',width = 200,size_hint = (0.25 ,.25), pos_hint={'right': .0, 'top': 0.5})
        #layout2.add_widget(btn2)
        #btn3 = Button(text='Oben',width = 200,size_hint = (0.25 ,.25), pos_hint={'center_x': .50, 'bottom': .50})
        #layout2.add_widget(btn3)
        #btn4 = Button(text='Unten',width = 200,size_hint = (0.25 ,.25), pos_hint={'left': .50, 'center_y': .50})
        #layout2.add_widget(btn4)
#screen = Screen()    
#gc.collect()
#runTouchApp(screen)

class KranUI(Widget):    
    Window.minimum_width = 1000
    Window.minimum_height = 650
    Window.size = (1000, 650)
    pass


class KranApp(App):
    def build(self):

        return KranUI()


if __name__ == '__main__':
    KranApp().run()