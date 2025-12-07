# Virtual_Water_Tank_SCADA_Simulation
This project is a software-based SCADA simulation of a water tank system. It demonstrates real-time monitoring, sensor indicators, and automated control logic.
**Objective:** Simulate a SCADA system to monitor water levels and control a pump, showcasing real-time automation and data visualization.
## Demo Video

![Watch Virtual SCADA Demo](demo.mp4)](demo.mp4)

---

## Features
- **Real-time Water Level Display:** Shows current tank level as a progress bar (0-100%).
- **Pump Control:** Automatically turns on/off based on water levels.
- **Sensor Indicators:** Low, Medium, High sensors shown with LED-style indicators.
- **Historical Graph:** Plots water level over time to visualize trends.
- **GUI-Based Simulation:** Fully interactive dashboard using PySimpleGUI and matplotlib.
- **Cross-platform:** Runs on Windows, Mac, or Linux with Python installed.

---

## How It Works
1. **Simulation Logic:**  
   - Water level increases if the pump is on, decreases over time to simulate drainage.  
   - Sensors detect low (<30%), medium (30%-70%), and high (>70%) levels.  
2. **Automation Loop:**  
   - Pump automatically activates when the water level is low.  
   - Pump turns off when the water level reaches high.  
3. **Visualization:**  
   - PySimpleGUI displays progress bar, pump status, and LED-style sensor indicators.  
   - Matplotlib embedded graph shows historical water levels in real-time.

---

## Installation
1. **Clone the repo:**
2. **Install dependencies:**

python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI
python -m pip install matplotlib


3. **Run the simulation:**

python scada_sim.py
   ```bash
   git clone https://github.com/yourusername/virtual-water-tank-scada.git
   cd virtual-water-tank-scada
