import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix='!') 

blocking_message = ['bad_word', 'bad_word2'] # u can add or change bad words

@bot.event
async def on_message(message):
    if blocking_message in message.content: 
        await message.delete() # deleting bad word
        await message.channel.send(f'{message.author.mention}, blocked word!')
    await bot.process_commands(message) 

bot.run('TOKEN')
