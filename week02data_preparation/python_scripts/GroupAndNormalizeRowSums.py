import numpy as np
from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable
from Orange.data.pandas_compat import table_to_frame, table_from_frame
import pandas as pd

# This line converts an Orange3 table into a Pandas DataFrame
df = table_to_frame(in_data)

# Use this to groupby whatever you want
grouped = df.groupby('Region')

# There are a variety of commands you can run in Pandas to aggregate by a grouping expression
collapsed = grouped.sum()

# Here, we're going to get row sums
row_sums = collapsed.sum(axis=1)

# Here we have normalized
normalized = collapsed.div(row_sums,axis=0)

# And this converts the data back to a table
out_data = table_from_frame(normalized) 