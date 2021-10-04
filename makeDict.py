import pickle
import json

with open("itemList.txt", "rb") as file:
	itemList = pickle.load(file)

itemDict = {}
for name, i, limit in itemList:
	itemDict[i]  = {"name" : name, "data" : {}}

with open("priceLog.json", "w") as file:
	json.dump(itemDict, file)