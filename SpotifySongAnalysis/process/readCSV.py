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
print(data.columns)
# neccesary columns obtained.
# Linear dependance, now.
# below are all vector lists:
vec1 = data["acousticness"].to_numpy()
vec2 = data["danceability"].to_numpy()
vec3 = data["energy"].to_numpy()
vec4 = data["instrumentalness"].to_numpy()
vec5 = data["key"].to_numpy()
vec6 = data["loudness"].to_numpy()
vec7 = data["mode"].to_numpy()
vec8 = data["tempo"].to_numpy()
