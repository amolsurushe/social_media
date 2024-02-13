# Dragon_year_fb_country wise followers
import json
import requests
import pandas as pd
import json

result = requests.get(
    'https://graph.facebook.com/v3.3/538972396156055/insights?access_token=EAACTMzReSCwBAGZBNeFDagZAAyHXpKrkWCRf6ZCScZC7XOkilZC71ZCRQwPg80XHVd8hJKZBOlMZCfnZBpV7DTIrvPvZCAX91SUYZAUOULxyIfPMH1yaaDSIzVicwGSMmEffIMRIASR7VZB23ZAHUI1WT7guj6dwInfZCBJGQ2DnpoWNHSpHHkcCdoGpLK&metric=page_follows_country&period=day&date_preset').json()

with open('personal.json', 'w') as json_file:
    json.dump(result, json_file)

# save data into json
abs = json.load(open('personal.json'))

# save data into dataframe
df1 = pd.Series(abs["data"][0]["values"][0]["value"].values())
df2 = pd.Series(abs["data"][0]["values"][0]["value"].keys())
frames = [df1, df2]
result = pd.concat(frames,axis=1)


# adding column name to the respective columns
result.columns =['followers', 'country']
print(result)

# # change the position of column
new_cols = ["country", "followers"]
df1 = result[new_cols]

# # remove index
df2 = df1.set_index('country')

# # save data into csv
df2.to_csv('Dragon_year_fb_country_name.csv')
print(df2)



