import requests
import json
import numpy as np

class Updater():
	headers = {
		'User-Agent': 'GE price forcasting project',
	}
	URL = "https://prices.runescape.wiki/api/v1/osrs/6h"

	def __init__(self):
		with open("priceLog.json" , "r") as f:
			self.log = json.load(f)

	def run(self):

		r = requests.get(self.URL, headers=self.headers)
		itemID = ""
		timestamp = r.json()["timestamp"]

		finished = False
		i = 0
		while not finished:
			try:
				for i in self.log:
					try:

						price = (r.json()["data"][i]["avgHighPrice"] * r.json()["data"][i]["highPriceVolume"] + r.json()["data"][i]["avgLowPrice"] * r.json()["data"][i]["lowPriceVolume"])/(r.json()["data"][i]["highPriceVolume"] + r.json()["data"][i]["lowPriceVolume"])
						#calculates average price
						if list(self.log[i]["data"].values())[-1] != price:
							self.log[i]["data"][timestamp] = price

					except KeyError as e:
						pass

					except TypeError as e:
						pass

					except IndexError as e:
						pass

				finished = True
			except KeyError:
				self.log[i]  = {"name" : name, "data" : {}}


	def save(self):

		with open("priceLog.json" , "w") as f:
			json.dump(self.log,f)

if __name__ == "__main__":
	update=Updater()
	update.run()
	#update.save()