
# Film fb post data
import json
import requests
import pandas as pd
import json

result = requests.get(
    'https://graph.facebook.com/1478038602226629/feed?fields&access_token=EAACTMzReSCwBAO0VwUOeAXhXT9f2fYCPyN42aoacfD7DMTBClfWCVb6kF8U1R2cJGn8k4kAV9pe1vb2ocrpVjF9bJsG3ssDZBpCZCZBJ9Y8HdbZC4ZCDPQrQHxE2A0qaZApJOZAMXZAAdH88WNwrwK5CRgV2MSvqHDQgOZA2lfr3UJ30Cdkkc3zYpzfhgDQGlCLvjLS6mJtfwCAZDZD
&').json()

with open('personal.json', 'w') as json_file:
    json.dump(result, json_file)

# save data into json
abs = json.load(open('personal.json'))

# save data into dataframe
df = pd.DataFrame(abs["data"])

list_of_json =[]



for x in df["id"]:
    result = requests.get(
    f'https://graph.facebook.com/{x}?fields=message,full_picture,shares,likes.limit(1).summary(true),comments.limit(1).summary(true),insights.metric(post_impressions_unique,post_impressions)&access_token=EAACTMzReSCwBAO0VwUOeAXhXT9f2fYCPyN42aoacfD7DMTBClfWCVb6kF8U1R2cJGn8k4kAV9pe1vb2ocrpVjF9bJsG3ssDZBpCZCZBJ9Y8HdbZC4ZCDPQrQHxE2A0qaZApJOZAMXZAAdH88WNwrwK5CRgV2MSvqHDQgOZA2lfr3UJ30Cdkkc3zYpzfhgDQGlCLvjLS6mJtfwCAZDZD
').json()
    list_of_json.append(result)

with open('personal3.json', 'w') as my_json_file:
    json.dump(list_of_json, my_json_file)

val1 = json.load(open('personal3.json'))

# save data into dataframe
df_val = pd.DataFrame(val1)

df_val["message"]

d1 = df_val["message"]
d2 = df_val["full_picture"]
# d3 = df_val["likes"][0]["summary"]["total_count"]
# d4 = df_val["comments"][0]["summary"]["total_count"]
# d5 = df_val["insights"][0]["data"][0]["name"]#df_val["insights"][0]["data"][0]["name"]
# d6 = df_val["insights"][0]["data"][0]["values"][0]["value"]
# d7 = df_val["insights"][0]["data"][1]["values"][0]["value"]
# d8 = df["created_time"]

list_of_total_like_count = []

for f in range(len(df_val["message"])):
    d11 = df_val["likes"][f]["summary"]["total_count"]
    list_of_total_like_count.append(d11)

df11 = pd.DataFrame(list_of_total_like_count, columns =['total_like_count'])

df_val["insights"][0]["data"][0]["name"]

list_of_total_insights_count = []

for n in range(len(df_val["message"])):
    d12 = df_val["insights"][n]["data"][0]["values"][0]["value"]
    list_of_total_insights_count.append(d12)

df12 = pd.DataFrame(list_of_total_insights_count, columns =['reach'])

list_of_total_reach_count = []

for m in range(len(df_val["message"])):
    d13 = df_val["insights"][m]["data"][1]["values"][0]["value"]
    list_of_total_reach_count.append(d13)

df13 = pd.DataFrame(list_of_total_reach_count, columns =['impressions'])

df14 =df["created_time"]

list_of_total_comment_count = []

for t in range(len(df_val["message"])):
    d15 = df_val["comments"][t]["summary"]["total_count"]
    list_of_total_comment_count.append(d15)

df15 = pd.DataFrame(list_of_total_comment_count, columns =['comment_count'])

df_final = pd.concat([d1,d2,df15,df11,df12,df13, df14], axis=1)

df_final.to_csv('Film_fb_post.csv')









