from pyarrow import Table
import pyarrow.parquet as pq

from pandas import DataFrame
from pandas.util.testing import rands

def generate_strings(nrows, nunique, string_length=10):
    unique_values = [rands(string_length) for i in range(nunique)]
    values = unique_values * (nrows // nunique)
    return values

def test_many_short_strings():
    # 1000000000 rows of strings length 1000, the process dies
    df = DataFrame(generate_strings(100000000, 1000), columns=['str'])
    table = Table.from_pandas(df)
    pq.write_table(table, 'strings.parquet')

test_many_short_strings()
