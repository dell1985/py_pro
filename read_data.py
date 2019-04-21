

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plta
import time
import sqlite3 as sql


df=pd.read_csv('data/pm2.csv')
print(df.columns)
df=df.reindex(columns=['合约代码','期货公司名称','持买单','增减量'])
print(df.合约代码)