from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

# List of Israeli companies
israeli_companies = [
    "Waze", "Mobileye", "Check Point Software Technologies", "Teva Pharmaceutical Industries",
    "CyberArk", "Taboola", "Fiverr", "Amdocs", "ICQ", "Viber", "SolarEdge", "Wix", "OrCam", "Outbrain", 
    "McDonald's", "Coke", "Pepsi", "Colgate", "Pepsodent", "Lays", "Kinley", "Starbucks", 
    "Burger King", "Johnson's Baby", "Johnson & Johnson"
]

israeli_companies_lower = [company.lower() for company in israeli_companies]

class CompanyCheckerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text="Enter the name of the company:", font_size=20, color=(1, 1, 1, 1))
        layout.add_widget(self.label)
        
        self.entry = TextInput(font_size=18, size_hint_y=None, height=50)
        layout.add_widget(self.entry)
        
        self.button = Button(text="Check", size_hint_y=None, height=50, on_press=self.check_company)
        layout.add_widget(self.button)
        
        self.message_label = Label(text="FREE PALESTINE", font_size=20, color=(1, 0.2, 0.2, 1))
        layout.add_widget(self.message_label)
        
        self.credit_label = Label(text="by-Omar", font_size=14, color=(1, 1, 1, 1), size_hint_y=None, height=20)
        layout.add_widget(self.credit_label)
        
        self.additional_message_label = Label(text="THIS PROGRAM SHOWS COMPANIES WHICH ARE ISRAELI OR FUND ISRAEL", font_size=12, color=(0.7, 0.7, 0.7, 1), size_hint_y=None, height=20)
        layout.add_widget(self.additional_message_label)
        
        return layout

    def check_company(self, instance):
        company = self.entry.text.strip().lower()
        if company in israeli_companies_lower:
            self.show_popup("Result", "It's Israeli")
        else:
            self.show_popup("Result", "It's not Israeli")

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        message_label = Label(text=message, font_size=18)
        popup_layout.add_widget(message_label)
        close_button = Button(text="Close", size_hint_y=None, height=50)
        popup_layout.add_widget(close_button)
        
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.5))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    CompanyCheckerApp().run()
