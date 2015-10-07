from kivy.app import App
from kivy.lang import Builder


class GuessingGame(App):
    def build(self):
        self.title = "Guessing Game 0.0.1"
        self.root = Builder.load_file('gui.kv')
        self.root.size = (300, 500)
        return self.root


# create and start the App running
GuessingGame().run()
