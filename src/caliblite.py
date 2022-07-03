import PySimpleGUI as sg
from switcher import Switcher

sg.theme("DarkGrey10")  # Add a touch of color
# All the stuff inside your window.
port_list = [f"Com{i}" for i in range(1, 10)] + ["Simulator"]
layout = [
    [sg.Text(" " * 50)],
    [
        sg.Text("Port"),
        sg.Drop(
            values=port_list,
            default_value="Simulator",
            auto_size_text=True,
            key="-PORT-",
            enable_events=True,
        ),
    ],
    [sg.Canvas(size=(30, 30), key="-CANVAS-"), sg.Text("Eteint", key="-STATUS-")],
    [sg.Button("Switch")],
]

# Create the Window
window = sg.Window("CalibLite", layout, resizable=True, finalize=True)
canvas = window["-CANVAS-"]
light = canvas.TKCanvas.create_oval(2, 2, 28, 28)
canvas.TKCanvas.itemconfig(light, fill="Red")
port = window["-PORT-"]
# Event Loop to process "events" and get the "values" of the inputs
switcher = Switcher("Simulator")
while True:
    event, values = window.read()
    if (
        event == sg.WIN_CLOSED or event == "Cancel"
    ):  # if user closes window or clicks cancel
        break
    elif event == "Switch":
        switcher.toggle()
        window["-STATUS-"].update("On" if switcher.is_on else "Off")
        canvas.TKCanvas.itemconfig(light, fill="Green" if switcher.is_on else "Red")
    elif event == "-PORT-":
        switcher.close()
        switcher = Switcher(window["-PORT-"].get())
    else:
        print(f"event: {event}")
switcher.close()
window.close()
