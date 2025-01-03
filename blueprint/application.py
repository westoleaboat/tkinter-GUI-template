"""
blueprint/application.py: root window class
"""
import tkinter as tk
from tkinter import ttk
from . import views as v
from . import models as m


class Application(tk.Tk):  # subclase from Tk instead of Frame
    """Application root window.
    It needs to contain:
        - A title label
        - An instance of MyForm class (call and place form in GUI)

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = m.myModel()
        self.myform = v.MyForm(self, self.model)

        # window title
        self.title('Blueprint Application')
        self.columnconfigure(0, weight=0)

        # header
        ttk.Label(  # parent is self. self is our Tk instance inside this class
            self, text='Header',
            font=("TkDefaultFont, 18")
        ).grid(row=0)

        # Add form with widgets
        self.myform = v.MyForm(self, self.model)

        self.myform.grid(row=1, padx=10, sticky=tk.W + tk.E)
    #     self.myform.bind('<<TranslateText>>', self._on_trans)

    # def _on_trans(self, *_):
    #     # retrieve input
    #     data = self.myform.get()
    #     # translate
    #     output = self.model.translate(data)
    #     # activate output
    #     self.myform._disable_var.set(False)
    #     # self.myform.set_output_state(tk.NORMAL)

    #     # set output
    #     self.myform._vars['Output'].set(output)

    #     # disable output
    #     self.myform._disable_var.set(True)
    #     # self.myform.set_output_state(tk.DISABLED)



        ############# EXAMPLE PLOTS #############
        def show_mychart(self, *_):
            data_nodes = self.model.nodes()
            data = data_nodes
            # popup = tk.Toplevel()
            chart = v.LineChartView(
                self.myform, data, (800,400),
                'Day','Average Height (cm)','lab_id'
            )
            # chart.pack(fill='both', expand=True)
            chart.grid(row=0, column=0)
        
        show_mychart(self)

        def show_yield_chart(self, *_):
            chart = v.YieldChartView(
            self.myform,
            'Average plot humidity', 
            'Average plot temperature',
            'Yield as a product of humidity and temperature'
            )
            chart.grid(sticky=tk.E + tk.W, row=1, column=0)

            data_seeds = self.model.seeds()
            seed_colors = {
                'AXM477': 'red', 
                'AXM478': 'yellow',
                'AXM479': 'green', 
                'AXM480': 'blue'
            }


            for seed, color in seed_colors.items():
                seed_data = [
                    (x['avg_humidity'], x['avg_temperature'], x['yield'])
                    for x in data_seeds if x['seed_sample'] == seed
                ]
                # print(f"Seed: {seed}, Data: {seed_data}")
                # Draw scatter for this seed
                if seed_data:  # Ensure there's data for the seed
                    chart.draw_scatter(seed_data, color, seed)

        show_yield_chart(self)
        ############### END EXAMPLES ############


if __name__ == "__main__":
    # create instance of our application and start its mainloop
    app = Application()
    app.mainloop()
