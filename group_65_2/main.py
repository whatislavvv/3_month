import flet as ft
from datetime import datetime 
import random

def main_page(page: ft.Page):
    page.title = "my first app"
    page.theme_mode = ft.ThemeMode.DARK
    hello_text = ft.Text(value='Hello world')
    greeting_history = []
    history_text = ft.Text("История приветствий:")
    random_names = ["Алексей", "Мария", "Иван", "Ольга", "Дмитрий", "Елена", "Павел", "Анна"]
    
    def on_button_click(_):
        # print(name_input.value)
        # pass
        name = name_input.value.strip()

        if name:
             # print(name)
            # hello_text = 'sdfsdfsdf'
            now = datetime.now()
            time_string = now.strftime("%Y:%m:%d - %H:%M:%S")
            hello_text.value = f"{time_string} - Привет, {name}!"
            hello_text.color = None
            name_input.value = None
            greeting_history.append(name) 
            print(greeting_history)
            history_text.value = f'ИСТОРИЯ ПРИВЕСТВИЙ \n' + ' \n - '.join(greeting_history)
        else:
            # print('Errorr')
            hello_text.value = 'ОШИБКА: Введите имя'
            hello_text.color = ft.Colors.RED
        page.update()

    def theme_switch(e):
        if page.theme_mode == ft.ThemeMode.DARK:
              page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.update()
    def set_random_name(_):
        name_input.value = random.choice(random_names)
        page.update()

    def toggle_history(_):
        history_text.visible = not history_text.visible
        if history_text.visible:
            toggle_history_btn.text = "Скрыть историю"
            toggle_history_btn.icon = ft.Icons.VISIBILITY_OFF
        else:
            toggle_history_btn.text = "Показать историю"
            toggle_history_btn.icon = ft.Icons.VISIBILITY
        page.update()

    def clear_history():
        greeting_history.clear()
        history_text.value = " ИСТОРИЯ ПРИВЕТСТВИЙ"
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    eleveated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND,on_click=on_button_click)
    icon_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6,on_click=theme_switch)
    random_names_button = ft.ElevatedButton('Случайное имя', icon=ft.Icons.SHUFFLE, on_click=set_random_name)
    toggle_history_btn = ft.ElevatedButton('Скрыть историю', icon=ft.Icons.VISIBILITY_OFF, on_click=toggle_history)
    clear_button = ft.IconButton(icon=ft.Icons.CLEAR,on_click=clear_history)
    page.add( hello_text,name_input,eleveated_button, icon_button,history_text,clear_button,random_names_button,toggle_history_btn)

ft.app(target=main_page)
