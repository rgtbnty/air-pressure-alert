import os
import requests

def send_image(image_path, message="📉 Air Pressure Change"):
    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]

    with open(image_path, "rb") as f:
        files = {
            "file": ("pressure.png", f, "image")
        }
        data = {
            "content": message
        }

        res = requests.post(webhook_url, data=data, files=files)

    if not res.ok:
        raise Exception(f"Discord error: {res.text}")