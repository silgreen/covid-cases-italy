import json
import matplotlib.pyplot as plt

date = []
num_tests = []
newCaseRate = []

with open("cases.json") as jsFile:
    data = json.load(jsFile)

for obj in data["tests"]:
    date.append(obj["date"])
    num_tests.append(obj["number_of_tests"])
    newCaseRate.append(obj["number_of_new_cases"] / obj["number_of_tests"] * 100)

plt.plot(date,newCaseRate)
plt.title("italy COVID-19 increase rate")
plt.xlabel("date format in dd/mm/yyyy")
plt.ylabel("rate in %")
plt.show()