import pandas as pd
import plotly.graph_objects as go

file = 'data.csv'

df = pd.read_csv(file)

fig = go.Figure(go.Scatter(
                    x=df.groupby('level')['attempt'].mean(),
                    y=['Level 1', 'Level 2', 'Level 3', 'Level 4']
                ))

print(df.groupby('level')['attempt'].mean())

fig.show()