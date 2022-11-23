import pyarrow as pa
import pyarrow.parquet as pq

import numpy as np
import pandas as pd
from pandas.util.testing import rands

def generate_strings(nrows, nunique, string_length=10):
    unique_values = [rands(string_length) for i in range(nunique)]
    values = unique_values * (nrows // nunique)
    return values

def test_integers():
    df = pd.DataFrame(np.random.randint(0,1000000000,size=(100000000, 4)), columns=list('ABCD'))

    table = pa.Table.from_pandas(df)

    pq.write_table(table, 'integers.parquet')

def test_many_short_strings():
    # 1000000000 rows of strings length 1000, the process dies
    df = pd.DataFrame(generate_strings(100000000, 1000), columns=['str'])
    table = pa.Table.from_pandas(df)
    pq.write_table(table, 'strings.parquet')

test_many_short_strings()
