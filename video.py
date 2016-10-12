from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.video import Video as KivyVideo

Builder.load_file('video.kv')


class Video(KivyVideo):
    image = ObjectProperty()

    def on_state(self, instance, value):
        if self.state == 'play':
            self.cover.opacity = 0
        elif self.state == 'stop':
            self.seek(0)
            self.cover.opacity = 1
        return super(self.__class__, self).on_state(instance, value)

    def on_image(self, instance, value):
        self.cover.opacity = 1

    def on_eos(self, instance, value):
        if value:
            self.state = 'stop'

    def _on_load(self, *args):
        super(self.__class__, self)._on_load(args)
        self.color = (1, 1, 1, 1)

    def on_source(self, instance, value):
        self.color = (0, 0, 0, 0)


Factory.unregister('Video')
Factory.register('Video', cls=Video)
