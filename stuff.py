import pandas  
x=pandas.read_json("./51628766/message.json")
x.columns
x['text']
x['created_at']
x['text'].str.len().max()
print(f'{x.iloc[716]}')

c=x['updated_at'] == None
r=x[x['name']=="Jim Hagelin"]
r


x['attachments'].str.decode(encoding='base64').value_counts()
r['attachments'].apply(type)
