import csv

# importing pandas package
import pandas

# assign dataset
data = pandas.read_csv("testData.csv")

print("Before:\n", data)

# sort data frame
data.sort_values(["points"],
                    axis=0,
                    ascending=[False],
                    inplace=True)


data.sort_values(["division"],
                    axis=0,
                    ascending=[True],
                    inplace=True)

print("\nAfter:\n", data)

