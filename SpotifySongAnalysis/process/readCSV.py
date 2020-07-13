###
# Author: Sriram Vadlamani
# Date: 12th February 2020
###
import os
import sys
import pandas as pd
import numpy as np

path = "/home/sriram/Documents/repo/datarecon/SpotifySongAnalysis/SpotifySongAttribs.csv"
data = pd.read_csv(path)
# for some reason. df.drop() doesn't seem to work.
del data['duration_ms']
del data['target']
# neccesary columns obtained.
# Linear dependance, now.
data = np.genfromtxt(path, dtype=float, delimiter=',', names=True)
print(data[1])
print("load successful!")
