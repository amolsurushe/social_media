
# Film insta post data
import json
import requests
import pandas as pd
import json

result = requests.get(
    'https://graph.facebook.com/v3.3/17841405702734743/media?fields=ig_id&access_token=EAACTMzReSCwBAO0VwUOeAXhXT9f2fYCPyN42aoacfD7DMTBClfWCVb6kF8U1R2cJGn8k4kAV9pe1vb2ocrpVjF9bJsG3ssDZBpCZCZBJ9Y8HdbZC4ZCDPQrQHxE2A0qaZApJOZAMXZAAdH88WNwrwK5CRgV2MSvqHDQgOZA2lfr3UJ30Cdkkc3zYpzfhgDQGlCLvjLS6mJtfwCAZDZD').json()

with open('personal.json', 'w') as json_file:
    json.dump(result, json_file)

# save data into json
abs = json.load(open('personal.json'))

# save data into dataframe
df = pd.DataFrame(abs["data"])

list_of_json =[]



for x in df["id"]:
    result = requests.get(
    f'https://graph.facebook.com/v7.0/{x}?fields=caption,comments_count,like_count,media_url,timestamp&access_token=EAACTMzReSCwBAO0VwUOeAXhXT9f2fYCPyN42aoacfD7DMTBClfWCVb6kF8U1R2cJGn8k4kAV9pe1vb2ocrpVjF9bJsG3ssDZBpCZCZBJ9Y8HdbZC4ZCDPQrQHxE2A0qaZApJOZAMXZAAdH88WNwrwK5CRgV2MSvqHDQgOZA2lfr3UJ30Cdkkc3zYpzfhgDQGlCLvjLS6mJtfwCAZDZD&period=day').json()
    list_of_json.append(result)
with open('personal3.json', 'w') as my_json_file:
    json.dump(list_of_json, my_json_file)

val1 = json.load(open('personal3.json'))

# save data into dataframe
df_val = pd.DataFrame(val1)

d1 = df_val["caption"]
d2 = df_val["comments_count"]
d3 = df_val["like_count"]
d4 = df_val["media_url"]
d5 = df_val["timestamp"]

df_final = pd.concat([d1,d2,d3,d4,d5], axis=1)
print(df_final)

df_final.to_csv('Film_insta_post.csv')

