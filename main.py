from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class RainbowApp(App):
    def build(self):
        self.colors = [
            ("Красный", "#ff0000"),
            ("Оранжевый", "#ff8800"),
            ("Желтый", "#ffff00"),
            ("Зеленый", "#00ff00"),
            ("Голубой", "#00ffff"),
            ("Синий", "#0000ff"),
            ("Фиолетовый", "#ff00ff")
        ]

        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Создаем текстовое поле и метку
        self.color_code_input = TextInput(hint_text='Код цвета', multiline=False)
        self.color_name_label = Label(text='Выберите цвет')

        # Создаем кнопки для каждого цвета
        self.buttons = []
        for color_name, color_code in self.colors:
            button = Button(text=color_name, on_press=lambda instance, code=color_code, name=color_name: self.update_colors(code, name))
            button.background_color = self.hex_to_rgba(color_code)
            self.buttons.append(button)

        # Располагаем элементы в макете
        self.layout.add_widget(self.color_code_input)
        self.layout.add_widget(self.color_name_label)

        for button in self.buttons:
            self.layout.add_widget(button)

        return self.layout

    def update_colors(self, color_code, color_name):
        # Обновляем метку и текстовое поле при выборе цвета
        self.color_code_input.text = color_code
        self.color_name_label.text = color_name

    def hex_to_rgba(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return [int(hex_color[i:i + 2], 16) / 255.0 for i in (0, 2, 4)]

if __name__ == '__main__':
    RainbowApp().run()
