from kivy.app import App
from videocontroller import VideoController


class Kvve(App):

    def build(self):
        return VideoController()


if __name__ == "__main__":
    Kvve().run()
