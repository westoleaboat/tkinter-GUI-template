# Tkinter GUI Boilerplate

### Overview

This Tkinter application demonstrates the use of the **Model-View-Controller (MVC)** design pattern. It features two sample plots integrated into the GUI: a scatter plot and a line chart. The application is designed to be modular, making it easy to extend and maintain.

### Features

- Scatter Plot: Visualizes relationships between three variables (e.g., humidity, temperature, and yield).

- Line Chart: Displays trends over time (e.g., daily average heights).

- MVC Architecture: Separates concerns into Model, View, and Controller layers for better organization.

### File Structure
```
project/
|-- application.py              # Main application entry point; root window class (Controller)
|-- constants.py                # Stores some named integer values
|-- models.py                   # Data handling and logic (Model); your functions go here
|-- views.py                    # GUI components (View); define your application widgets.
|-- widgets.py                  # Reusable GUI components, as labels and more widgets; 
README.md                       # This File
project.py                      # Launches Application entry point
```

### Usage
1. Clone this repo
```
git clone https://github.com/westoleaboat/tkinter-GUI-template.git
cd tkinter-GUI-template
```

2. Install dependencies if necessary:

```
# create virtual environment
python -m venv .venv

# activate it 
source .venv/bin/activate

# install with pip 
(.venv) pip install matplotlib
```
3. Run the application:
```
python blueprint.py
```

### Highlights
#### Model (models.py)
Manage the storage, retrieval, and processing
of our application's data. 
```
class Model:
    def seeds(self):
        return [
            {"Day": 0, "lab_id": "A", "Average Height (cm)": 1.42},
            {"Day": 1, "lab_id": "B", "Average Height (cm)": 1.85},
            # Additional data...
        ]

    def nodes(self):
        return [
            {"seed_sample": "AXM480", "yield": 15, "avg_humidity": 27.2, "avg_temperature": 23.8},
            # Additional data...
        ]
```
#### View (views.py)
Larger GUI components
```
class MyForm():
    ...
    w.LabelInput(
        self, 
        'Default Label',
        input_class=w.BoundText, 
        var=self._vars['Notes'],
        input_args={
            "width": 55, 
            "height": 50}
    ).grid(sticky=tk.W + tk.E, row=0, column=1, rowspan=2)
    ...

class ScatterPlotView:
    def __init__(self, parent, title, xlabel, ylabel):
        # Initialize plot

    def draw_scatter(self, data, color, label):
        # Draw data points

class LineChartView:
    def __init__(self, parent, data, size, xlabel, ylabel):
        # Initialize chart
```
#### Controller (application.py)
Connect the model and view, manage user interactions
```
from . import views as v
from . import models as m

class Application(tk.Tk):  # subclase from Tk instead of Frame
    def __init__(self, root):
        self.model = m.Model()
        self.view = v.LineChartView()

        def show_mychart(self, *_):
            data_nodes = self.model.nodes()
            data = data_nodes
            chart = v.LineChartView(...)
            chart.grid(row=0, column=0)
        
        show_mychart(self)

        def show_yield_chart(self, *_):
            chart = v.YieldChartView(...)
            # ...

        show_yield_chart(self)
```
#### Examples
Check sample implementation of the following apps:
- [particle collision](https://github.com/westoleaboat/particle-simulation-gui)
- [Shortest Node Path](https://github.com/westoleaboat/shortest-path-node-gui)
- [Text-to-binary translator](https://github.com/westoleaboat/binary-translator-gui)
- [Password Generator](https://github.com/westoleaboat/password-generator-gui)
- [Check a PyQt GUI Template](https://github.com/westoleaboat/Qt-GUI-template)
