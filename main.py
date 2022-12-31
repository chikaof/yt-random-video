import requests
import random

def get_random_video():
  # Fetch popular videos
  api_key = "YOUR_API_KEY"
  url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&key={api_key}"
  response = requests.get(url)
  data = response.json()

  # Select the video from the list.
  video_index = random.randint(0, len(data["items"]) - 1)
  video = data["items"][video_index]

  # Return title and link :)
  title = video["snippet"]["title"]
  link = f"https://www.youtube.com/watch?v={video['id']}"

  return title, link

title, link = get_random_video()
print(f"t: {title}")
print(f"l: {link}")
