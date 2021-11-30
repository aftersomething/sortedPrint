import csv
import pandas

#prompting user
filename = input("Enter name of file to be sorted (including file path if the file is in an alternate directory): ")

#importing data and storing as a dataframe
data = pandas.read_csv(filename)

# sorting the data frame and resetting indexes to allow for easy printing
data.sort_values(["points"], axis=0, ascending=[False], inplace=True)

data.sort_values(["division"], axis=0, ascending=[True], inplace=True)

data = data.reset_index(level=0, drop = True)


#printing sorted records
print("records:\n")

num_records_printed = 3

for x in range(num_records_printed):
    print ("- name: ", data.loc[x,"firstname"], " ", data.loc[x, "lastname"])
    print ("  details: In division ", data.loc[x,"division"], " from ", data.loc[x, "date"], " performing ", data.loc[x, "summary"])



