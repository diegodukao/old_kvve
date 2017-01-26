from kivy.app import App
from videocontroller import VideoController
# from kivy.uix.videoplayer import VideoPlayer
#
#
# class MyVideoPlayer(VideoPlayer):
#     def __init__(self, **kwargs):
#         self.source = "2-1-diagram-beautification.mp4"
#         self.state = 'play'
#         super().__init__(**kwargs)


class Kvve(App):

    def build(self):
        return VideoController()


if __name__ == "__main__":
    Kvve().run()
