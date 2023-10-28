from kivy.app import App
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass
    #'dp' stands for density-independent pixels
    # It could be possible that we set size 
    # from one device, which is larger or 
    # smaller in another device. For this, dp is 
    # used so that the size adjusts to each device

    # The values in 'color' are float numbers 
    # from 0 to 1, indicating the percentage of 
    # each color red, green, blue. Last value 
    # stands for the opacity of the text
    

class TheLabApp(App):
    pass
    
TheLabApp().run()