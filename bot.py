import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

text = """🌍 Кароткі дайджэст

— Тэставае паведамленне. Бот працуе.
"""

url = f"https://api.telegram.org/bot8202814688:AAHqPVRKlVFIfRQV348Mdlgkk3Bj6mfyVus/sendMessage"
requests.post(url, data={"chat_id": CHAT_ID, "text": text})
