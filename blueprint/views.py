"""
  blueprint/views.py: form containing widgets
"""

import tkinter as tk
from tkinter import ttk

from . import widgets as w
from .constants import FieldTypes as FT
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
  FigureCanvasTkAgg,
  NavigationToolbar2Tk
)
import matplotlib
matplotlib.use('TkAgg')


class MyForm(tk.Frame):
    """Input Form for widgets

    - self._vars = Create a dictionary to hold all out variable objects 
    - _add_frame = instance method that add a new label frame. Pass in 
                   label text and optionally a number of columns.

    """

    var_types = {
        FT.string: tk.StringVar,
        FT.string_list: tk.StringVar,
        FT.short_string_list: tk.StringVar,
        FT.iso_date_string: tk.StringVar,
        FT.long_string: tk.StringVar,
        FT.decimal: tk.DoubleVar,
        FT.integer: tk.IntVar,
        FT.boolean: tk.BooleanVar
    }

    def _add_frame(self, label, cols=3):
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame

    def __init__(self, parent, model, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.model = model
        fields = self.model.fields

        self._vars = {  # hold all variable objects
            key: self.var_types[spec['type']]()
            for key, spec in fields.items()
        }

        # disable var for Output field
        self._disable_var = tk.BooleanVar()

        # build the form
        self.columnconfigure(0, weight=1)

        # w.LabelInput(
        #     self, 
        #     'Default Label',
        #     input_class=w.BoundText, 
        #     var=self._vars['Notes'],
        #     input_args={
        #         "width": 55, 
        #         "height": 50}
        # ).grid(sticky=tk.W + tk.E, row=0, column=1, rowspan=2)


        # self._disable_var.set(True)
        self._disable_var.set(False)

        # text to display data from form
        self.output_var = tk.StringVar()

        ###########
        # buttons #
        ###########
        # improving inter-object communication was added to bug tracker

        buttons = ttk.Frame(self)  # add on a frame
        buttons.grid(sticky=tk.W + tk.E, row=4)
        # pass instance methods as callback commands
        self.transbutton = ttk.Button(
            buttons, text="Text to Binary", command=self._on_trans)
        # self.transbutton.pack(side=tk.RIGHT)

        self.transbutton = ttk.Button(
            buttons, text="Binary to Text", command=self._on_trans, state='disabled')
        # self.transbutton.pack(side=tk.RIGHT)

        # self.savebutton = ttk.Button(
        #     buttons, text="Save", command=self.master._on_save)  # on parent
        # self.savebutton.pack(side=tk.RIGHT)
        self.resetbutton = ttk.Button(
            buttons, text="Reset", command=self.reset)  # on this class
        # self.resetbutton.pack(side=tk.RIGHT)

    def reset(self):
        """Reset entries. Set all variables to empty string"""
        # activate widget
        self._disable_var.set(False)
        # self.set_output_state(tk.NORMAL)

        # reset data
        for var in self._vars.values():
            if isinstance(var, tk.BooleanVar):
                # uncheck checkbox
                var.set(False)
            else:
                # set inputs to empty string
                var.set('')
                # set data label to empty string
                # self.output_var.set('')
        # disable widget
        self._disable_var.set(True)
        # self.set_output_state(tk.DISABLED)

    def get(self):
        """Retrieve data from the form so it can be saved or used"""
        data = {}
        for key, variable in self._vars.items():
            try:
                # retrieve from ._vars
                data[key] = variable.get()
            except tk.TclError as e:
                # create error message
                message = f'Error in field: {key}. Data not saved!'
                raise ValueError(message) from e
        # return the data
        return data

    #########################################
    # Disable widget if disable_var not used:
    #
    # def set_output_state(self, state):
    #     output_widget = self._get_widget_by_var(self._vars['Output'])
    #     if output_widget:
    #         output_widget.input.configure(state=state)

    # def _get_widget_by_var(self, var):
    #     """Return the widget associated with a given variable."""
    #     for widget in self.winfo_children():
    #         if isinstance(widget, w.LabelInput) and widget.variable == var:
    #             return widget
    #     return None
    #########################################

    def _on_trans(self):
        self.event_generate('<<TranslateText>>')
        # self._disable_var.set(False)


class LineChartView(tk.Canvas):
  """A generic view for plotting a line chart"""

  margin = 2
  colors = [
    'red', 'orange', 'yellow', 'green',
    'blue', 'purple', 'violet',
    # add more for more complex plots
  ]

  def __init__(
    self, parent, data, plot_size,
    x_field, y_field, plot_by_field
  ):
    self.data = data
    self.x_field = x_field
    self.y_field = y_field
    self.plot_by_field = plot_by_field

    # calculate view size
    self.plot_width, self.plot_height = plot_size
    view_width = self.plot_width + (2 * self.margin)
    view_height = self.plot_height + (2 * self.margin)

    super().__init__(
      parent, width=view_width,
      height=view_height, background='lightgrey'
    )
    # Draw chart
    self.origin = (self.margin, view_height - self.margin)
    # X axis
    self.create_line(
      self.origin,
      (view_width - self.margin, view_height - self.margin)
    )
    # Y axis
    self.create_line(
      self.origin, (self.margin, self.margin), width=2
    )
    # X axis label
    self.create_text(
      (view_width // 2, view_height - self.margin),
      text=x_field, anchor='n'
    )
    # Y axis label
    self.create_text(
      (self.margin, view_height // 2),
      text=y_field, angle=90, anchor='s'
    )
    self.plot_area = tk.Canvas(
      self, background='#555',
      width=self.plot_width, height=self.plot_height
    )
    self.create_window(
      self.origin, window=self.plot_area, anchor='sw'
    )

    # Draw legend and lines
    plot_names = sorted(set([
      row[self.plot_by_field]
      for row in self.data
    ]))

    color_map = list(zip(plot_names, self.colors))

    for plot_name, color in color_map:
      dataxy = [
        (row[x_field], row[y_field])
        for row in data
        if row[plot_by_field] == plot_name
      ]
      self._plot_line(dataxy, color)

    self._draw_legend(color_map)


  def _plot_line(self, data, color):
    """Plot a line described by data in the given color"""

    max_x = max([row[0] for row in data])
    max_y = max([row[1] for row in data])
    x_scale = self.plot_width / max_x
    y_scale = self.plot_height / max_y
    coords = [
      (round(x * x_scale), self.plot_height - round(y * y_scale))
      for x, y in data
    ]
    self.plot_area.create_line(
      *coords, width=4, fill=color, smooth=True
    )

  def _draw_legend(self, color_map):
    # determine legend
    for i, (label, color) in enumerate(color_map):
      self.plot_area.create_text(
        (10, 10 + (i * 20)),
        text=label, fill=color, anchor='w'
      )


class YieldChartView(tk.Frame):

  def __init__(self, parent, x_axis, y_axis, title):
    super().__init__(parent)
    self.figure = Figure(figsize=(6, 4), dpi=100)
    self.canvas_tkagg = FigureCanvasTkAgg(self.figure, master=self)
    canvas = self.canvas_tkagg.get_tk_widget()
    canvas.pack(fill='both', expand=True)
    self.toolbar = NavigationToolbar2Tk(self.canvas_tkagg, self)
    self.axes = self.figure.add_subplot(1, 1, 1)
    self.axes.set_xlabel(x_axis)
    self.axes.set_ylabel(y_axis)
    self.axes.set_title(title)
    self.scatters = list()
    self.scatter_labels = list()

  def draw_scatter(self, data, color, label):
    x, y, size = zip(*data)
    scaled_size = [(s ** 2)//2 for s in size]
    scatter = self.axes.scatter(
      x, y, scaled_size,
      c=color, label=label, alpha=0.5
    )
    self.scatters.append(scatter)
    self.scatter_labels.append(label)
    self.axes.legend(self.scatters, self.scatter_labels)