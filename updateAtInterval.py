from updateLog import Updater
import threading

def main():
	def targetfunc():
		updater = Updater()
		updater.run()
		updater.save()
		print("updated")
		time.sleep(3600)

	updateThread = threading.Thread(target= targetfunc)
	updateThread.start()

if __name__ == "__main__":
	main()