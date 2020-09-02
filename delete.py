import discord

client = discord.Client()

@client.event
async def on_message(message):
    if str(message.channel) == "deneme" and message.content != "":
        await message.channel.purge(limit=1)




client.run('NzUwNjE5MTgyMjMxNzE1OTQw.X09Klg.9faYWXT73zBnVKhSOa6jlrJdHLE') 
