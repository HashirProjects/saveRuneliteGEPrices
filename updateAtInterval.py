from updateLog import Updater
import threading
import asyncio
from concurrent.futures import ThreadPoolExecutor


async def ainput(prompt: str = "") -> str:# delivrance/ainput.py on github
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, input, prompt)


async def updateFunction(interval, UPDATES_DONE):
	while True:
		updater = Updater()
		updater.run()
		updater.save()
		UPDATES_DONE[0] += 1
		await asyncio.sleep(interval)

async def sendStatusMessages(UPDATES_DONE):
	end = False
	while not end:
		print(f"The Updater has updated the log file {UPDATES_DONE[0]} times ")
		r = await ainput("Press x and enter to stop Updater, or press enter to update status message")
		if r == "x":
			end = True


async def main():
	UPDATES_DONE= [0]
	end = [False]

	t1 = asyncio.create_task(updateFunction(300, UPDATES_DONE))
	t2 = asyncio.create_task(sendStatusMessages(UPDATES_DONE))

	await t2

if __name__ == "__main__":
	asyncio.run(main())