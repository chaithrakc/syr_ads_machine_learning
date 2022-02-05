import numpy as np
from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable
from Orange.data.pandas_compat import table_to_frame, table_from_frame
import pandas as pd
import matplotlib.pyplot as plt

# This line converts an Orange3 table into a Pandas DataFrame
df = table_to_frame(in_data)

def find_iqr(x):
  return np.subtract(*np.percentile(x, [75, 25]))

summary = pd.concat({"IQR":df[["Age","SibSp","Fare"]].apply(find_iqr),
"Mean":df[["Age","SibSp","Fare"]].mean(),"StdDev":df[["Age","SibSp","Fare"]].std()},axis=1)

print(summary)

