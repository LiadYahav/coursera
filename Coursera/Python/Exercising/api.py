import pandas as pd
import requests
import json

data = requests.get("https://official-joke-api.appspot.com/jokes/ten")
results = json.loads(data.text)
df2 = pd.json_normalize(results)
df2.drop(columns=["type", "id"], inplace=True)
print(df2)
