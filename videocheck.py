import requests, time

# init --

CHAN_ID = ''
DEV_KEY = ''

def currentTimeFormatted():
    return time.strftime("20%y-%m-%dT%H:%M:%SZ")

checkTime = currentTimeFormatted()

# main --

def checkForNew(lastChecked):
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=' +\
	CHAN_ID + '&publishedAfter=' + lastChecked + '&type=video&key=' + DEV_KEY
    # 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=
	# {YOUR_CHAN_ID}&publishedAfter={YYYY-MM-DDTHH:MM:SSZ}&type=video&key={YOUR_API_KEY}'
	
    response = requests.get(url)

    videos = [] # Format [Time, ID1, Title1, ID2, ...]
    videos.append(currentTimeFormatted())

    data = response.json()
    print(data)

    for i in range(0, len(data["items"])):
        videos.append(data["items"][i]["id"]["videoId"])
        videos.append(data["items"][i]["snippet"]["title"])

    return videos






