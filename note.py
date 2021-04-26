import torch
import numpy as np
import os
a = ''
b = ['a','b','a','d','e']
import pandas as pd
c ={"apple": [1,2]}
list = pd.read_excel('static/market_price.xlsx')
print(int(list[list["과일"] == "apple"]["가격"].values[0])*2)
