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

# Generating an average column. 
# We'll call it the song factor
