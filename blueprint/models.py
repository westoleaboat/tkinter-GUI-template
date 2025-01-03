""" blueprint/models.py: example data"""

from .constants import FieldTypes as FT
import tkinter as tk


from . import views as v


class myModel:
    # pass
    fields = {
        "Notes": {'req': True, 'type': FT.long_string}
    }

    ############### EXAMPLE DATA #####################
    # views.py LineChart Example Data

    def nodes(self):
        num_nodes = {'A', 'B', 'C'}
        data = [
    {"Day": 0, "lab_id": "A", "Average Height (cm)": 1.4198750000000000},
    {"Day": 0, "lab_id": "B", "Average Height (cm)": 1.3320000000000000},
    {"Day": 0, "lab_id": "C", "Average Height (cm)": 1.5377500000000000},
    {"Day": 1, "lab_id": "A", "Average Height (cm)": 1.7266250000000000},
    {"Day": 1, "lab_id": "B", "Average Height (cm)": 1.8503750000000000},
    {"Day": 1, "lab_id": "C", "Average Height (cm)": 1.4633750000000000},
    {"Day": 2, "lab_id": "A", "Average Height (cm)": 1.9},
    {"Day": 2, "lab_id": "B", "Average Height (cm)": 2.1},
    {"Day": 2, "lab_id": "C", "Average Height (cm)": 1.8},
    {"Day": 3, "lab_id": "A", "Average Height (cm)": 2.2},
    {"Day": 3, "lab_id": "B", "Average Height (cm)": 2.3},
    {"Day": 3, "lab_id": "C", "Average Height (cm)": 2.0},
    {"Day": 4, "lab_id": "A", "Average Height (cm)": 2.4},
    {"Day": 4, "lab_id": "B", "Average Height (cm)": 2.5},
    {"Day": 4, "lab_id": "C", "Average Height (cm)": 2.2},
]
        return data

# views.py YieldChartView Example Data

    def seeds(self):
        data2 = [
    {"seed_sample": "AXM480", "yield": 11, "avg_humidity": 27.7582142857142857, "avg_temperature": 23.7485714285714286},
    {"seed_sample": "AXM480", "yield": 20, "avg_humidity": 27.2146428571428571, "avg_temperature": 23.8032142857142857},
    {"seed_sample": "AXM480", "yield": 15, "avg_humidity": 26.2896428571428571, "avg_temperature": 23.6750000000000000},
    {"seed_sample": "AXM478", "yield": 31, "avg_humidity": 27.2928571428571429, "avg_temperature": 23.8317857142857143},
    {"seed_sample": "AXM477", "yield": 39, "avg_humidity": 27.1003571428571429, "avg_temperature": 23.7360714285714286},
    {"seed_sample": "AXM478", "yield": 29, "avg_humidity": 26.8550000000000000, "avg_temperature": 23.7632142857142857},
    {"seed_sample": "AXM479", "yield": 49, "avg_humidity": 25.8550000000000000, "avg_temperature": 23.7632142857142857},
    {"seed_sample": "AXM478", "yield": 9, "avg_humidity": 26.1550000000000000, "avg_temperature": 23.7632142857142857},
    {"seed_sample": "AXM477", "yield": 22, "avg_humidity": 27.5003571428571429, "avg_temperature": 23.7360714285714286},
    {"seed_sample": "AXM479", "yield": 19, "avg_humidity": 26.5550000000000000, "avg_temperature": 23.7632142857142857}
]
        return data2
#####################################


# class TextToBinary:
    #     """
#     Translate Texto into Binary.

#     fields dictionary is a class member variable that 
#     contains all the fields in our model

#     """

#     fields = {
#         "Input": {'req': True, 'type': FT.long_string},
#         "Output": {'req': True, 'type': FT.long_string}
#     }

#     # def __init__(self):

#     def translate(self, data):
#         """Translate text into binary"""
#         trad = ''.join(format(ord(i), '08b') for i in data['Input'])
#         # if no text to convert
#         if data == '':
#             pass  # do nothing

#         return trad
