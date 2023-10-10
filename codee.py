import pandas as pd
import plotly.express as px

df1 = pd.read_csv('shared_articles.csv')
df2 = pd.read_csv('users_interactions.csv')

df1.columns = ['timestamp','eventType','contentId','authorPersonId', 'authorSessionId','authorUserAgent','authorRegion','authorCountry','contentType','url','title','text','lang']
df2= df2.merge(df1,on='contentId')
