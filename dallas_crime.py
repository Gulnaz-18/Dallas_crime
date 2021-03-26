import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import os

%matplotlib inline

plt.style.use('bmh')

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('/kaggle/input/dallas-crimes/Police_Incidents.csv', low_memory=False)
df.head()

df.info()
