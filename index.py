import discord
from discord.ext import commands

TOKEN='NzUwNjE5MTgyMjMxNzE1OTQw.X09Klg.9faYWXT73zBnVKhSOa6jlrJdHLE'

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot başladı')
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    if message.content.startswith('!ping'):
        await message.channel.send('Pong')
    if message.content.startswith('!naber'):
        await message.channel.send('iyidir senden');
    if message.content.startswith('sa'):
        await message.channel.send('as');
    if message.content.startswith('!echo'):
        msg = message.content.split()
        output = ' '
        for word in msg[1:]:
            output+=word
            output+=' '
    if message.content.startswith('amk'):
        
        await message.channel.purge(limit=1)
    if message.content.startswith('!clear'):
        await message.channel.purge(limit=100)
@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)

    await channel.purge(limit=100)
    await ctx.send('Messaged deleted.')


@client.event
async def on_message_delete(message):
    author=message.author
    await message.channel.send('{} mesajını sildi'.format(author))
client.run(TOKEN)
