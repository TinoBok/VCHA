from guizero import App, Text, TextBox, PushButton, ButtonGroup, Picture, info, warn, Box







app = App(title="Ruud", width=1000, height=500, bg = "#e9e5e3")
welcome_message = Text(app, text="Welcome to our app", size=35, font="Times New Roman", color="black")



def Wifi_setting():
    wifi_setting_message = Text(app, text="WiFi setting:", size=25, font="Times New Roman", color="black")
    form = Box(app, width="fill", layout="center")
    form.border = True
    Text(form, text="Name:")
    TextBox(form )
    Text(form, text="Password:")
    TextBox(form)
    buttons = Box(app, width="fill")
    PushButton(buttons, text="Next", align="right")

Wifi_setting()

app.display()
