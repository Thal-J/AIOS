# setup
#This imports the random library; a library which allows random functionality
import random
#This imports time; a library allowing timing and other functions
import time
#This imports discord; a library allowing the program to access Discord
import discord

#This sets the client which the program uses to access Discord
client = discord.Client()

#This conceals the token from you, the causal reader.
tokenFile = open("token.txt", "r")
token = str(tokenFile.read())

@client.event
#This enables checking of messages
async def on_message(messagename):

    #This is a pool of random 'dreams' which the bot pulls from in later sections of the code
    dreams = [
     "Dreaming...",
     "Torchbugs...",
     "Overturned jar..."
    ]

    examplembed = discord.Embed(
        title='Retrieving information',
        description=random.choice(dreams),
        colour=discord.Colour.red()
    )
    examplembed.set_footer(text='AIOS functionality preparing')
    examplembed.set_image(
        url='https://media.discordapp.net/attachments/494443546989035520/509201412672978944/unknown.png?width=888'
            '&height=500')
    examplembed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    examplembed.set_author(name='AIOS',
                           icon_url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261'
                                    '/k86qvkS.png')

    NewEmbed = discord.Embed(
        title='Information Retrieved',
        description='Sample Information',
        colour=discord.Colour.green()
    )
    NewEmbed.set_footer(text='AIOS functionality delivered')
    NewEmbed.set_image(url='https://cdn.discordapp.com/attachments/494443546989035520/512170758848380928/unknown.png')
    NewEmbed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    NewEmbed.set_author(name='AIOS',
                        icon_url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261'
                                 '/k86qvkS.png')

    if messagename.content == 'Output':
        oldmessage = await client.send_message(messagename.channel, 'speech', embed=examplembed)
        time.sleep(15)
        await client.edit_message(oldmessage, new_content=None, embed=NewEmbed)


@client.event
#A number of functions relating to the bot's activation
async def on_ready():
    #The bot outputs 'ready' to the pythonic output
    print("ready")
    #The bot changes its now playing status to 'The Engine of Expression'
    await client.change_presence(game=discord.Game(name='The Engine of Expression'))

#this runs the program
client.run(token)
