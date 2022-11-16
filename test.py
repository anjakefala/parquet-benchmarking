import pyarrow as pa
import pyarrow.parquet as pq

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0,1000000,size=(1000000, 4)), columns=list('ABCD'))

table = pa.Table.from_pandas(df)

pq.write_table(table, 'integers.parquet')
