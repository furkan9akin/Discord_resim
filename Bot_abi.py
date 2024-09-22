import discord
from discord.ext import commands
import oyun
import keraspy

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, size tercihlerinize dayalı bir oyun bulabilirim.')

@bot.command()
async def oyunlar(ctx):
    kategoriler = ", ".join(oyun.oyunlar.keys())
    await ctx.send(f"Lütfen bir kategori seçin: {kategoriler}")

@bot.command()
async def kategori(ctx, kategori):
    if kategori in oyun.oyunlar:
        oyun_listesi = "\n".join([f"{tur}: {', '.join(oyunlar)}" for tur, oyunlar in oyun.oyunlar[kategori].items()])
        await ctx.send(f"İşte {kategori} oyunları:\n{oyun_listesi}")
    else:
        await ctx.send("Belirtilen kategori bulunamadı.")

@bot.command()
async def resim(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            await i.save(f"./images/{i.filename}")
            await ctx.send(f"{i.filename} resmini kaydettim.")
            sinif,skor = keraspy.x(f"./images/{i.filename}")
            if sinif=="Guvercin\n":
                await ctx.send("Güvercinler bulgur ve pirinç yerler.")
            elif sinif=="Serce\n":
                await ctx.send("Serçeler meyve, tohum, böcek ve larva yerler.")
            elif sinif=="Karga\n":
                await ctx.send("Hemen hemen her şeyi yerler.")
            elif sinif=="Diger\n":
                await ctx.send("Yer ya da yemezler.")
            else:
                await ctx.send("Hata oldu.")
    else:
        await ctx.send("Resim bulunamadı.")

@bot.command() #6 #4
async def ekok(ctx, x:int, y:int):
    for i in range(1,x*y + 1):
        if i%x==0 and i%y==0:
            await ctx.send(f"EKOK: {i}")
            return

@bot.command() #6 #4
async def ebob(ctx, x:int, y:int):
    for i in range(max(x,y) + 1,1,-1):
        if x%i==0 and y%i==0:
            await ctx.send(f"EBOB: {i}")
            return

            

    





bot.run("")
