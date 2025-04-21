import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

# Load the API key from the .env file
api_key = os.getenv("YOUTUBE_API_KEY")
if api_key is None:
    raise ValueError("API key not found. Please set the YOUTUBE_API_KEY environment variable.")

youtube = build("youtube",version="v3",developerKey=api_key)

#get the channel upload playlist id
channel_id = os.getenv("CHANNEL_ID")
if channel_id is None:
    raise ValueError("Channel ID not found. Please set the CHANNEL_ID environment variable.")
channel_response = youtube.channels().list(
    part="contentDetails",
    id = channel_id
).execute()

uploads_playlist_id = channel_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

#get the videos
response = youtube.playlistItems().list(
    part="snippet",
    playlistId=uploads_playlist_id,
    maxResults=50
).execute()

# Print the video titles and IDs
for item in response["items"]:
    print(item["snippet"]["title"])
    print(item["snippet"]["resourceId"]["videoId"])
    print(item["snippet"]["thumbnails"]["default"]["url"])
    link = f"https://www.youtube.com/watch?v={item["snippet"]["resourceId"]["videoId"]}"
    print(link)
    print()