import disnake
from disnake.ext import commands
import asyncio
import os
import dotenv
import requests
import base64
dotenv.load_dotenv()
intents = disnake.Intents.all()

client = commands.Bot("a?", intents=intents)

@client.event
async def on_ready():
    print(f"loggin as {client.user}")
    print(f"Số máy chủ hiện đang ở: {len(client.guilds)}")



@client.command(name="change_av")
async def change_avt(ctx: disnake.ApplicationCommandInteraction):
    await ctx.send("Đang tiến hành thay đổi...")

    try: # Thay thế tệp trong ./data thành avt bạn thích (Nhớ đổi tên thành `avt`)
        with open('./data/avt.gif', 'rb') as f:
                await client.user.edit(avatar=f.read())
                await ctx.send("Đã thiết lập thành công")
    except Exception as e:
        if "File cannot be larger than" in str(e):
            await ctx.send("File bạn sử dụng không thể lớn hơn 10mb!")
        else:
            await ctx.send("Đã xảy ra lỗi")
            print(e)


TOKEN = os.environ.get("DISCORD_TOKEN")
BANNER = os.environ.get("BANNER_URL")

@client.command(name="bnr")
async def bnr(ctx: disnake.ApplicationCommandInteraction):

    if BANNER: 
        banner_img_res = requests.get(BANNER)
    else:
        await ctx.send("Thiết lập ảnh banner trong tệp `.env` !!")

    if banner_img_res.status_code == 200:
        bas64_bnr = base64.b64encode(banner_img_res.content).decode("utf-8")

        payload = {
            "banner": f"data:image/gif;base64,{bas64_bnr}"
        }

        headers = {
            'Authorization': f'Bot {TOKEN}',
            'Content-Type': 'application/json'
        }

        response = requests.patch('https://discord.com/api/v10/users/@me', headers=headers, json=payload)

        if response.status_code == 200:
            await ctx.send("OK")
        else:
            await ctx.send("Not OK")
    else:
        await ctx.send(f"Ảnh lỗi rồi lmao {banner_img_res.status_code}")
         
     
client.run(TOKEN)
    