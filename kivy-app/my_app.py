from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.exp = ''
        main_layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput(readonly = True)
        main_layout.add_widget(self.text_input)
        h_layout = None
        self.operators = ['+', '-', '*', '/', '=', 'C']
        temp = BoxLayout(orientation='horizontal')
        for operator in self.operators:
            temp.add_widget(Button(text=operator, on_press=self.on_button_press))
        main_layout.add_widget(temp)
        for i in range(0, 10):
            if i % 3 == 0:
                if h_layout:
                    main_layout.add_widget(h_layout)
                h_layout = BoxLayout(orientation='horizontal')
            h_layout.add_widget(Button(text=str(i + 1), on_press = self.on_button_press))
        return main_layout
    def on_button_press(self, instance):
        if instance.text == 'C':
            self.exp = ''
            self.text_input.text = ''
        elif instance.text == '=':
            self.text_input.text = str(eval(self.exp))
            self.exp = ''
        else:
            self.text_input.text = instance.text
            self.exp += instance.text
        # return main_layout

if __name__ == '__main__':
    app = MainApp()
    app.run()