import json
import matplotlib.pyplot as plt

date = []
daily_death = []

with open('datas\cases.json') as jsfile:
    data = json.load(jsfile)

for obj in data["tests"]:
    date.append(obj["date"])
    daily_death.append(obj["death"])


plt.bar(date,daily_death,width=0.5)
plt.grid()
plt.xticks(visible=False)
plt.title("Daily deaths in italy")
plt.ylabel("deaths")
plt.show()
