import json
f = open("./Jan/200 COVID-19.json","r")
data = json.load(f)
for i in range(len(data)):
    data[i]["mark"] = "##############################"
f = open("./Jan/200 COVID-19.json","w")
json.dump(data, f)