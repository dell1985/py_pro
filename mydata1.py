

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plta
import time
import sqlite3 as sql


df=pd.read_csv('pm2.csv')
print("打开了数据库")
n0=np.arange(5)
print(n0)
n=pd.Series(np.arange(10),index=np.arange(1,20,2))
print(n)
print(df.columns)
df=df.reindex(columns=['合约代码','期货公司名称','持买单','增减量'])
print(df.合约代码)