#setup
import discord
import random
import time
client = discord.Client()

tokenFile = open("token.txt", "r")
token=str(tokenFile.read())

@client.event
async def exampleembedoutput():
    examplembed = discord.Embed(
        title = 'Retrieving information'
        description = 'Dreaming—torchbugs—overturned jar'
        colour = discord.Colour.yellow()
    )
    examplembed.set_footer(text='AIOS functionality delivered')
    examplembed.set_image(url='https://media.discordapp.net/attachments/494443546989035520/509201412672978944/unknown.png?width=888&height=500')
    examplembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    examplembed.set_author(name='AIOS', icon_url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    
    NewEmbed = discord.Embed(
        title = 'Information Retrieved'
        description = 'Sample Information'
        colour = discord.Colour.green()
    )
    NewEmbed.set_footer(text='AIOS functionality delivered')
    NewEmbed.set_image(url='https://media.discordapp.net/attachments/494443546989035520/509201412672978944/unknown.png?width=888&height=500')
    NewEmbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    NewEmbed.set_author(name='AIOS', icon_url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    
    await client.send_message(message.channel, embed=examplembed)
    time.sleep(120)
    edit_message(message, new_content=None, *, embed=NewEmbed)

@client.event
async def on_ready():
    print("ready")
    await client.change_presence(game=discord.Game(name='The Engine of Expression'))
    
    
client.run(token)
