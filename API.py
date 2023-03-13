from googleapiclient.discovery import build
import json
import os

channel_id = "UCMCgOm8GZkHp8zJ6l7_hIuA"

api_key: str = os.getenv("YT_API_KEY")
youtube = build('youtube', 'v3', developerKey=api_key)
channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
print(channel)
