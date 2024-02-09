import disnake
from disnake.ext import commands
import asyncio
import os
import dotenv
dotenv.load_dotenv()
intents = disnake.Intents.all()

client = commands.Bot("a?", intents=intents)

@client.event
async def on_ready():
    print(f"loggin as {client.user}")


@client.slash_command()
async def setup_user(self, ctx: disnake.AppCommandInteraction):
    await ctx.response.defer()

    try: # Thay thế tệp trong ./data thành avt bạn thích (Nhớ đổi tên thành `avt`)
        with open('./data/avt.gif', 'rb') as f:
                await client.user.edit(avatar=f.read())
                await ctx.edit_original_response("Đã thiết lập thành công")
                print("Done")
                exit(1)
    except Exception as e:
        await asyncio.sleep(1)
        print(e)


TOKEN = os.environ.get("DISCORD_TOKEN")

client.run(TOKEN)
    