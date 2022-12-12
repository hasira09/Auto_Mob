from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (310, 580)


class HomeScreen(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file('home.kv')


HomeScreen().run()
