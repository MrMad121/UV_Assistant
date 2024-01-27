import tkinter as tk
from tkinter import Text

def submit():
    with open("./UV_Assistant launcher.cmd", "w") as file:
        file.write(f"{input_path.get('1.0', 'end-1c')}/.VoiceAI/.venv/Scripts/python.exe {input_path.get('1.0', 'end-1c')}/.VoiceAI/UV_Assistant.py")
    with open("./UV_Assistant_Turbo launcher.cmd", "w") as file:
        file.write(f"{input_path.get('1.0', 'end-1c')}/.VoiceAI/.venv/Scripts/python.exe {input_path.get('1.0', 'end-1c')}/.VoiceAI/UV_Assistant_Turbo.py")
    with open("./path.txt", "w") as file:
        file.write(input_path.get("1.0", "end-1c"))


    button.config(text= "Successful")

window = tk.Tk()

# Creating the font
font = ("Gabriola", 14, "bold")

# Creating colors
windowColor = "#A0CA92"
buttonColor = "#D8F793"
inputColor = "#D8F793"

# Creating the objects
button = tk.Button(window, text= "apply", bg= buttonColor, width=14, height= 2, relief= "flat", command=submit, activebackground= "#C5E6A6")
label_path = tk.Label(window, text= 'Enter the path where you installed the program', font= font, pady=10, bg= windowColor)
label_key = tk.Label(window, text= 'Enter the secret key', font= font, pady=10, bg= windowColor)
input_path = Text(window, height=1, width=50, pady=6, padx=6, bg= inputColor)
input_key = Text(window, height=1, width=50, pady=6, padx=6, bg= inputColor)

# Styling the window
window.title("Activate UV_Assistant")
window.resizable(False, False)
window.config(bg= windowColor)
window.geometry("540x220")

# Placing objects
label_path.place(x=72, y=4)
label_key.place(x= 72, y=74)
input_path.place(x= 62, y= 50)
input_key.place(x= 62, y= 120)
button.place(x= 212, y= 160)

window.mainloop()