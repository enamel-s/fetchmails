import requests
import pandas as pd
from io import StringIO

url = "https://docs.google.com/spreadsheets/d/10O4IwokK1rNG3AAsWRiGzGq8Ge1gpt5sNsRuRKOSGcQ/export?format=csv&gid=0"
response = requests.get(url)
response.raise_for_status()

df = pd.read_csv(StringIO(response.text))
df.to_csv("sheet_data.csv", index=False)
print("CSV updated successfully!")
