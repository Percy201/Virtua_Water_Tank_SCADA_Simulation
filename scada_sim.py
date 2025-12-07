import PySimpleGUI as sg
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

# Simulation variables
water_level = 50  # 0-100 scale
pump_on = False
water_history = []

# GUI layout
layout = [
    [sg.Text('Virtual Water Tank SCADA', font=('Any', 18))],
    [sg.Text('Water Level:'), sg.ProgressBar(100, orientation='h', size=(30, 20), key='-LEVEL-')],
    [sg.Text('Pump Status:'), sg.Text('', size=(10,1), key='-PUMP-')],
    [sg.Text('Sensors:')],
    [sg.Text('Low', size=(5,1)), sg.Text('', size=(2,1), key='-LOW-')],
    [sg.Text('Medium', size=(5,1)), sg.Text('', size=(2,1), key='-MED-')],
    [sg.Text('High', size=(5,1)), sg.Text('', size=(2,1), key='-HIGH-')],
    [sg.Canvas(key='-CANVAS-')],
    [sg.Button('Exit')]
]

window = sg.Window('Virtual SCADA', layout, finalize=True)

# Matplotlib figure for real-time graph
fig, ax = plt.subplots()
ax.set_title("Water Level Over Time")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Level")
line, = ax.plot([], [], 'b-')
ax.set_ylim(0, 100)

# Embed figure in PySimpleGUI
canvas_elem = window['-CANVAS-']
canvas = FigureCanvasTkAgg(fig, canvas_elem.Widget)
canvas.draw()
canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

# Function to update the graph
def update_graph():
    line.set_xdata(range(len(water_history)))
    line.set_ydata(water_history)
    ax.set_xlim(0, max(10, len(water_history)))
    canvas.draw()

# Simulation loop in a separate thread
def simulation():
    global water_level, pump_on, water_history
    while True:
        if pump_on:
            water_level += 1
        else:
            water_level -= 0.5  # natural drain
        water_level = max(0, min(100, water_level))
        # sensor indicators
        low = water_level < 30
        med = 30 <= water_level < 70
        high = water_level >= 70
        # pump logic
        if low:
            pump_on = True
        elif high:
            pump_on = False
        # update history
        water_history.append(water_level)
        if len(water_history) > 100:
            water_history.pop(0)
        # update GUI
        window['-LEVEL-'].update(current_count=water_level)
        window['-PUMP-'].update('ON' if pump_on else 'OFF')
        window['-LOW-'].update('●' if low else '○')
        window['-MED-'].update('●' if med else '○')
        window['-HIGH-'].update('●' if high else '○')
        update_graph()
        time.sleep(0.1)

# Start simulation thread
threading.Thread(target=simulation, daemon=True).start()

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

window.close()
