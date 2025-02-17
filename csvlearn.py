import pandas
data=pandas.read_csv("input.csv")
for i in data['sdsurl']:
        print(type(i))