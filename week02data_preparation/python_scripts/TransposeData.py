from Orange.data.pandas_compat import table_to_frame, table_from_frame
import pandas as pd

#Convert this to a pandas DataFrame
df = table_to_frame(in_data)

# The rest of this is designed to work around a pandas problem with Categorical axes
# See here: https://github.com/pandas-dev/pandas/issues/19136#issuecomment-380908428
df.set_index(df.columns[0],inplace=True)
df = df.T
index_df =df.index.to_frame(index=False)
df = df.reset_index(drop=True)
df = pd.merge(index_df, df, left_index=True, right_index=True)

# Here, we're renaming the column headings to "Headings"
df.rename(columns={0:"Headings"},inplace=True)


