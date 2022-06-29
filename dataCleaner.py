import pandas as pd

df = pd.read_csv('allStars.csv')

df.drop(['Unnamed: 0', 'Unnamed: 5', 'tempName', 'tempDistance', 'tempMass', 'tempRadius'], axis=1, inplace=True)

final_data = df.dropna()
final_data.reset_index(drop=True,inplace = True)
final_data.to_csv("starChart.csv")