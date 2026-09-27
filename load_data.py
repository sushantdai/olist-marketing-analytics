import duckdb
import glob
import os

con = duckdb.connect("olist.duckdb")

for path in sorted(glob.glob("data/*.csv")):
    path = path.replace("\\", "/")
    table = (os.path.basename(path)
             .replace("olist_", "")
             .replace("_dataset.csv", "")
             .replace(".csv", ""))
    con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM read_csv_auto('{path}')")
    rows = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    print(f"{table:40} {rows:>10,}")

con.close()