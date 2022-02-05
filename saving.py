import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import csv
import statistics
import numpy as np

df = pd.read_csv("savings_data_final.csv")

#fig = px.scatter(df, y="quant_saved", color="rem_any")
#fig.show()


with open('savings_data_final.csv', newline="") as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)

#Finding total number of people and number of people who were reminded
total_entries = len(savings_data)
total_people_given_reminder = 0
for data in savings_data:
  if int(data[3]) == 1:
    total_people_given_reminder += 1

import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))

fig.show()

all_savings = []
for data in savings_data:
    all_savings.append(float(data[0]))
    print(f"Mean of Savings-{statistics.mean(all_savings)}")
    print(f"Median of Savings-{statistics.median(all_savings)}")
    print(f"Mode of Savings-{statistics.mode(all_savings)}")

reminded_savings = []
not_reminded_savings = []

for data in savings_data:
    if int(data[3]) == 1:
        reminded_savings.append(float(data[0]))
    else:
        not_reminded_savings.append(float(data[0]))

    print("Results for people who are reminded to save" )
    print(f"Mean of savings-{statistics.mean(reminded_savings)}")
    print(f"Median of Savings-{statistics.median(reminded_savings)}")
    print(f"Mode of Savings-{statistics.mode(reminded_savings)}")
    print("\n\n")
    print("Results for people who are not reminded")
    print(f"Mean of savings-{statistics.mean(not_reminded_savings)}")
    print(f"Median of Savings-{statistics.median(not_reminded_savings)}")
    print(f"Mode of Savings-{statistics.mode(not_reminded_savings)}")

#Standard Deviation
print(f"Standard deviation of all the data -> {statistics.stdev(all_savings)}")
print(f"Standard deviation of people who were reminded -> {statistics.stdev(reminded_savings)}")
print(f"Standard deviation of people who were not reminded -> {statistics.stdev(not_reminded_savings)}")


age = []
savings = []
for data in savings_data:
  if float(data[5]) != 0:
    age.append(float(data[5]))
    savings.append(float(data[0]))

correlation = np.corrcoef(age, savings)
print(f"Correlation between the age of the person and their savings is - {correlation[0,1]}")