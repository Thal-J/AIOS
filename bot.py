#setup
import discord
import random
import time
client = discord.Client()

tokenFile = open("token.txt", "r")
token=str(tokenFile.read())

@client.event
async def on_message(messagename):
    examplembed = discord.Embed(
        title = 'Retrieving information',
        description = 'Dreaming—torchbugs—overturned jar',
        colour = discord.Colour.red()
    )
    examplembed.set_footer(text='AIOS functionality preparing')
    examplembed.set_image(url='https://media.discordapp.net/attachments/494443546989035520/509201412672978944/unknown.png?width=888&height=500')
    examplembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    examplembed.set_author(name='AIOS', icon_url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    
    NewEmbed = discord.Embed(
        title = 'Information Retrieved',
        description = 'Sample Information',
        colour = discord.Colour.green()
    )
    NewEmbed.set_footer(text='AIOS functionality delivered')
    NewEmbed.set_image(url='https://cdn.discordapp.com/attachments/494443546989035520/512170758848380928/unknown.png')
    NewEmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    NewEmbed.set_author(name='AIOS', icon_url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')

    if messagename.content==('Output'):
        oldmessage = await client.send_message(messagename.channel, ('speech'), embed=examplembed)
        time.sleep(15)
        await client.edit_message(oldmessage, new_content=None, embed=NewEmbed)

@client.event
async def on_ready():
    print("ready")
    await client.change_presence(game=discord.Game(name='The Engine of Expression'))
    
    
client.run(token)
