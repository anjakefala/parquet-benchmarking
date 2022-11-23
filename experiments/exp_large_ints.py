from pandas import DataFrame
from numpy import random
from pyarrow import Table
import pyarrow.parquet as pq

def test_integers():
    df = DataFrame(random.randint(0,1000000000,size=(100000000, 4)), columns=list('ABCD'))

    table = Table.from_pandas(df)

    pq.write_table(table, 'integers.parquet')

test_integers()
