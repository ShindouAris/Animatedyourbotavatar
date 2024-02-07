import disnake
from disnake.ext import commands
import asyncio
import os

intents = disnake.Intents.all()

client = commands.Bot("a?", intents=intents)

@client.event
async def on_ready():
    print(f"loggin as {client.user}")


@client.command()
async def change_avt(self):

    try: # Thay thế tệp trong ./data thành avt bạn thích (Nhớ đổi tên thành `avt`)
        with open('./data/avt.gif', 'rb') as f:
                await client.user.edit(avatar=f.read())
                print("Done")
                exit(1)
    except Exception as e:
        await asyncio.sleep(1)
        print(e)


TOKEN = os.environ.get("DISCORD_TOKEN")

client.run(TOKEN)
    