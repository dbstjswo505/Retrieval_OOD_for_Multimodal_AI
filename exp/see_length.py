import json
import pdb
import numpy as np

with open("mean_prediction_with_comp.json", 'r') as jf:
    data = json.load(jf)
lengths = []

for key in data.keys():
    lengths.append(data[key][0])
sort_len = sorted(lengths)
pdb.set_trace()
