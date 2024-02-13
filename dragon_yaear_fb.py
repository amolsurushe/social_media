# Daily Unique Follows for dragon year gallery FB
import json
import requests
import pandas as pd
import json

result = requests.get(
    'https://graph.facebook.com/538972396156055/insights?access_token=EAACTMzReSCwBAGZBNeFDagZAAyHXpKrkWCRf6ZCScZC7XOkilZC71ZCRQwPg80XHVd8hJKZBOlMZCfnZBpV7DTIrvPvZCAX91SUYZAUOULxyIfPMH1yaaDSIzVicwGSMmEffIMRIASR7VZB23ZAHUI1WT7guj6dwInfZCBJGQ2DnpoWNHSpHHkcCdoGpLK&metric=page_daily_follows_unique&period=day&date_preset=last_28d').json()

with open('personal.json', 'w') as json_file:
    json.dump(result, json_file)

# save data into json
abs = json.load(open('personal.json'))

# save data into dataframe
df = pd.DataFrame(abs["data"][0]["values"])

# rename the column
df.rename(columns={'value': 'Actual_Follower', 'end_time': 'Date'}, inplace=True)

# change the position of column
new_cols = ["Date", "Actual_Follower"]
df1 = df[new_cols]

# remove index
df2 = df1.set_index('Date')

# save data into csv
df2.to_csv('dragon_year_fb.csv')


data = pd.read_csv("dragon_year_fb.csv")
data.dropna(inplace=True)

# new data frame with split value columns
new = data["Date"].str.split("T", n = 1, expand = True)
data["Date"] = new[0]

# making separate last name column from new data frame
data["Time"] = new[1]

# Dropping old Name columns
data.drop(columns=["Time"], inplace=True)


data.to_csv('dragon_year_fb.csv')
print(data)
