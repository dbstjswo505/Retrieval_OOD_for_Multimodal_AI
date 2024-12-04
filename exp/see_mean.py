import json
import numpy as np
import pdb

with open('prediction_with_comp.json', 'r') as jfile:
    data = json.load(jfile)
new_data = dict()
for key in data.keys():
    new_data[key] = data[key][:2]
    new_data[key].append(np.mean(data[key][2:]))
with open('mean_prediction_with_comp.json', 'w') as jfile2:
    json.dump(new_data, jfile2)
pdb.set_trace()
z=1
