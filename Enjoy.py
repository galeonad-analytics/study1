# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio


async def f(l1, l2):
    async with l1:
        await asyncio.sleep(1)
    async with l2:
        await asyncio.sleep(1)
    print('Наслаждайтесь бесконечностью...')



if __name__ == '__main__':
    l1 = asyncio.Lock()
    l2 = asyncio.Lock()
    await asyncio.gather(f(l1, l2), f(l2, l1))


