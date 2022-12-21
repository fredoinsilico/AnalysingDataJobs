import pandas as pd
import numpy as np
df = pd.read_csv('./linkedin-jobs-usa.csv')
df.head(30)

localizacion = df['location']
print(len(localizacion))