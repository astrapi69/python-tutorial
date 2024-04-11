# Import pandas as pd
import pandas as pd
import os

csv_path = os.path.dirname(os.path.realpath(__file__))
csv_filename = 'cars.csv'
full_path = csv_path + '/' + csv_filename
# Import the cars.csv data: cars
df = pd.read_csv(full_path)
# Print out cars
print(df)

print("#####")
# get subset from the dataframe
subset = df.loc[:3];
print(subset)
print("#####")
tsv_filename = 'subset_sample.tsv';
tsv_gz_filename = tsv_filename + '.gz';
# convert to tsv file
subset.to_csv(tsv_filename, sep="\t") 

import gzip
import shutil
with open(tsv_filename, 'rb') as f_in:
    with gzip.open(tsv_gz_filename, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
print("#####")

print("#####")
column_array = ['cars_per_cap','country']
# get subset from the dataframe
subset_cc = df.loc[:2,column_array];
print(subset_cc)
print("#####")
# clean up
if os.path.exists(tsv_filename):
    os.remove(tsv_filename)
if os.path.exists(tsv_gz_filename):
    os.remove(tsv_gz_filename)


