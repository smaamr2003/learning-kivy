from kivy.app import App
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass
    # The root rule in kv file is declared by 
    # declaring the class of your root widget, 
    # without any 
    # indentation, followed by : and will be set 
    # as the root attribute of the App instance:

class TheLabApp(App):
    pass
    # In this app, we can set the widgets without 
    # needing to use the kv file (using the 'build' 
    # method), but using kv file is much easier
    
TheLabApp().run()