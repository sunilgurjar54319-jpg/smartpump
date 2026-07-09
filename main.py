from kivy.app import App
from kivy.uix.button import Button

class SmartPump(App):
    def build(self):
        return Button(text="Smart Pump")

SmartPump().run()
