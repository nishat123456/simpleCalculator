from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

class CalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.num1 = TextInput(hint_text='Number 1', multiline=False)
        self.num2 = TextInput(hint_text='Number 2', multiline=False)
        self.result = Label(text='Result will appear here')

        self.add_btn = Button(text='+')
        self.add_btn.bind(on_press=self.add_numbers)

        self.sub_btn = Button(text='-')
        self.sub_btn.bind(on_press=self.sub_numbers)

        self.mul_btn = Button(text='×')
        self.mul_btn.bind(on_press=self.mul_numbers)

        self.div_btn = Button(text='÷')
        self.div_btn.bind(on_press=self.div_numbers)

        self.format_spinner = Spinner(text='Standard', values=('Standard', 'Scientific'))

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)
        layout.add_widget(self.add_btn)
        layout.add_widget(self.sub_btn)
        layout.add_widget(self.mul_btn)
        layout.add_widget(self.div_btn)
        layout.add_widget(self.format_spinner)
        layout.add_widget(self.result)

        return layout

    def add_numbers(self, instance):
        self.calculate(lambda a, b: a + b)

    def sub_numbers(self, instance):
        self.calculate(lambda a, b: a - b)

    def mul_numbers(self, instance):
        self.calculate(lambda a, b: a * b)

    def div_numbers(self, instance):
        self.calculate(lambda a, b: a / b if b != 0 else 'Error: Division by 0')

    def calculate(self, operation):
        try:
            a = float(self.num1.text)
            b = float(self.num2.text)
            result = operation(a, b)
            if self.format_spinner.text == 'Scientific':
                result = f'{result:.2e}'
            self.result.text = f'Result: {result}'
        except ValueError:
            self.result.text = 'Error: Invalid input'

if __name__ == '__main__':
    CalculatorApp().run()
