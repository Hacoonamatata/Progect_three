
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout



print(faile)

Builder.load_string('''\
<LoginScreen>
    orientation: "horizontal"
    TextInput:
        text: "500"
        on_text: root.calc(self.text)


''')



class LoginScreen(BoxLayout):
    def __int__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)



    def calc(self, text):
        print(text)


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()

