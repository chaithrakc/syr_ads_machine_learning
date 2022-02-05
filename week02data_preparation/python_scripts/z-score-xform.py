import numpy as np
from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable
from Orange.data.pandas_compat import table_to_frame, table_from_frame
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

df = table_to_frame(in_data)
df['Age Z-score'] = (df.Age - df.Age.mean()) / df.Age.std()
out_data = table_from_frame(df)
