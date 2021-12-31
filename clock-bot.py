import discord
import asyncio
from datetime import datetime, timezone, tzinfo
import pytz

client = discord.Client()

distoken = '[BOT_TOKEN_HERE]'
timechannel = [CHANNEL_ID_HERE]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
        pacific_tz = pytz.timezone("US/Pacific")
        now = datetime.now().astimezone(pacific_tz)
        
        # With a max edit time of twice in 10 minutes, align to updating on multiples of 5 with a 5 minute interval
        if now.minute % 5 == 0:
            nameStr = f"🕒 {now.strftime('%I:%M %p %Z')}"

            print('Setting new channel Name to: {0}'.format(nameStr))

            await client.get_channel(timechannel).edit(name="{0}".format(nameStr))
            await asyncio.sleep(300)
        else:
            print('Waiting for minute multiple of 5')
            await asyncio.sleep(60)

client.run(distoken)