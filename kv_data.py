import pandas
import numpy as np

data = pandas.read_csv("raw_data.csv")
yardsNextYear = []
tdsNextYear = []
fumblesNextYear = []
ygNextYear = []
gamesNextYear = []
ptsNextYear = []

for index, row in data.iterrows():
    player = row["ID"]
    year = row["Year"]
    next_year = data.loc[(data["ID"] == player) & (data["Year"] == year+1)]
    yards = "N/A"
    tds = "N/A"
    fumbles = "N/A"
    yg = "N/A"
    games = "N/A"
    points = "N/A"
    if next_year.shape[0]:
        assert(next_year.shape[0] == 1)
        yards = next_year["Yards"].to_numpy()[0]
        tds = next_year["TD"].to_numpy()[0]
        fumbles = next_year["Fumbles"].to_numpy()[0]
        yg = next_year["Y/G"].to_numpy()[0]
        games = next_year["Games"].to_numpy()[0]
        points = 0.1*yards + 6.0*tds - 2.0*fumbles
    yardsNextYear.append(yards)
    tdsNextYear.append(tds)
    fumblesNextYear.append(fumbles)
    ygNextYear.append(yg)
    gamesNextYear.append(games)
    ptsNextYear.append(points)

data["Yards Next Year"] = yardsNextYear
data["TD Next Year"] = tdsNextYear
data["Fumbles Next Year"] = fumblesNextYear
data["Y/G Next Year"] = ygNextYear
data["Games Next Year"] = gamesNextYear
data["Points Next Year"] = ptsNextYear
data.to_csv("data.csv", index=False, float_format="{:.4f}".format)
