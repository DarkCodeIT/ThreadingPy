import threading, requests, asyncio, aiohttp, time
from concurrent.futures import ThreadPoolExecutor


def req(url: str) -> None:
	with requests.get(url=url) as response:
		print(response.status_code)

# async def rew(url: str) -> None:
# 	async with aiohttp.ClientSession() as session:
# 		async with session.get(url) as response:
# 			print(response.status)

# def main() -> None:
# 	url = "https://www.google.com/"
# 	threads = [threading.Thread(target=lambda: req(url=url), daemon=True) for _ in range(100)]

# 	for t in threads:
# 		t.start()

# 	for t in threads:
# 		t.join()

# async def mai() -> None:
# 	url = "https://www.google.com/"
# 	coro = [rew(url=url) for _ in range(100)]
# 	await asyncio.gather(*coro)
	
def main_pool():
	url = "https://www.google.com/"
	executor = ThreadPoolExecutor()
	for _ in range(10):
		executor.submit(req, url)
	
	# Отключение Executor с ожиданием окончания работы всех потоков
	executor.shutdown(wait=True)

if __name__ == "__main__":
	t = time.time()
	# main()
	# asyncio.run(mai())
	main_pool()
	print(time.time() - t)