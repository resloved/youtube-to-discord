import discord, asyncio
from videocheck import checkForNew, currentTimeFormatted

# init --

BOT_EMAIL = ''
BOT_PASS = ''

CHAN_ID = ''

WAIT = 60    # Seconds

client = discord.Client()

# main --

def videoPostMessage(id, title):
    return "Theres a new video! " +\
           "http://www.youtube.com/watch?v=" + id


@asyncio.coroutine
def my_background_task():
    print("-- Task started --")
    yield from client.wait_until_ready()
    channel = discord.Object(id=CHAN_ID)
    cur = currentTimeFormatted()
    while not client.is_closed:
        videos = checkForNew(cur)
        cur = videos[0]
        if(len(videos) > 1):    # If there are new videos...
            for i in range(0, len(videos) - 1 / 2):     # Post each new video
                yield from client.send_message(channel, videoPostMessage(videos[i * 2], videos[i * 2 + 1]))
        yield from asyncio.sleep(WAIT)

client.loop.create_task(my_background_task())
client.run(BOT_EMAIL, BOT_PASS)
