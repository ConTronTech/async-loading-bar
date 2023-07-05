import asyncio, time, os

bar = ["|", "/", "-", "\\", "|", "/", "-", "\\"]

async def load():
    await asyncio.sleep(0.4)
    while True:  # Run forever
        for item0 in bar:
            os.system('cls')
            print(f"< BRAIN PROCESSING '{item0}'")
            await asyncio.sleep(0.1 if item0 != bar[-1] else 0.1)

asyncio.run(load())