import pandas as pd
import numpy as np

srs=pd.Series([1,3,np.nan,4,np.nan])

print(srs.dropna(axis=0))