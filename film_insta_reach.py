# Film insta reach data
import json
import requests
import pandas as pd
import json

result = requests.get(
    'https://graph.facebook.com/v3.3/17841405702734743/media?fields=ig_id&access_token=EAACTMzReSCwBAGkD1F9ZATOPZCuKYZAojEhFR1ZBiPeDcr3pi3KZBZAeuVBiFnmbdCS336XQiNZAfQPs0mNnIUo0KLAK99bataZA2Vz011dV5JQz1Si5oW1nF4KgcEPRN9PhGAZCj4W25FI8mVn6ARZB4up84a3W3cvKiCPGz0cYBvOLjBIOpgZAZBZAm&').json()

with open('personal.json', 'w') as json_file:
    json.dump(result, json_file)

# save data into json
abs = json.load(open('personal.json'))

# save data into dataframe
df = pd.DataFrame(abs["data"])

list_of_json =[]



for x in df["id"]:
    result = requests.get(
    f'https://graph.facebook.com/v7.0/{x}/insights?access_token=EAACTMzReSCwBAGkD1F9ZATOPZCuKYZAojEhFR1ZBiPeDcr3pi3KZBZAeuVBiFnmbdCS336XQiNZAfQPs0mNnIUo0KLAK99bataZA2Vz011dV5JQz1Si5oW1nF4KgcEPRN9PhGAZCj4W25FI8mVn6ARZB4up84a3W3cvKiCPGz0cYBvOLjBIOpgZAZBZAm&metric=impressions,reach&period=day').json()
    list_of_json.append(result)
with open('personal3.json', 'w') as my_json_file:
    json.dump(list_of_json, my_json_file)

val1 = json.load(open('personal3.json'))

# save data into dataframe
df_val = pd.DataFrame(val1)

#print(df_val)
df_val.to_csv('Film_insta_reach.csv')

