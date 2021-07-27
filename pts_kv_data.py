import pandas
import numpy as np

data = pandas.read_csv("raw_data.csv")
ptsNextYear = []

for index, row in data.iterrows():
    player = row["ID"]
    year = row["Year"]
    next_year = data.loc[(data["ID"] == player) & (data["Year"] == year+1)]
    points = "N/A"
    if next_year.shape[0]:
        assert(next_year.shape[0] == 1)
        yards = next_year["Yards"].to_numpy()[0]
        tds = next_year["TD"].to_numpy()[0]
        fumbles = next_year["Fumbles"].to_numpy()[0]
        points = 0.1*yards + 6.0*tds - 2.0*fumbles
    ptsNextYear.append(points)

data["Points Next Year"] = ptsNextYear
data.to_csv("data.csv", index=False, float_format="{:.4f}".format)
