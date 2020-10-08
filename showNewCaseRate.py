import json
import matplotlib.pyplot as plt

date = []
num_tests = []
newCaseRate = []
deaths = []
plt2 = plt

with open("cases.json") as jsFile:
    data = json.load(jsFile)

for obj in data["tests"]:
    date.append(obj["date"])
    num_tests.append(obj["number_of_tests"])
    newCaseRate.append(obj["number_of_new_cases"] / obj["number_of_tests"] * 100)


plt.plot_date(date,newCaseRate,fmt='r-o')
plt.title("italy COVID-19 increase rate")
plt.ylabel("rate in %")
plt.show()