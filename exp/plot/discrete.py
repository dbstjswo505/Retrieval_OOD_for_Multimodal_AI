import json
import numpy as np
import pdb
from scipy.io import savemat

new_data = dict()

with open('mean_prediction_with_comp.json','r') as jfile:
    data = json.load(jfile)

cnt = np.zeros((5,10))
score = np.zeros((5,10))
# 5 - 10 sec
# 10 - 15 sec
# 15 - 20 sec
# 20 - 25 sec
# 25 - 30 sec
# 30 - 35 sec
# 35 - 40 sec
# 40 - 45 sec
# 45 - 50 sec
# 50 - 55 sec
for key in data.keys():
    length = int(data[key][0])
    y = int((length//5)-1)
    comp = int(data[key][1]) - 1 
    x = int(comp)
    if y < 0 or y > 9:
        continue
    if x > 4:
        continue
    scoretmp = data[key][2]
    cnt[x,y] = cnt[x,y] + 1
    score[x,y] = score[x,y] + scoretmp
cnt_mask = cnt < 0.5
cnt_mask = cnt_mask*10000
cnttmp = cnt + cnt_mask
mscore = score/cnttmp
mscore = np.round(mscore,3)
pdb.set_trace()


    
