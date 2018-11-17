# setup
# This imports the random library; a library which allows random functionality
import random
# This imports time; a library allowing timing and other functions
import time
# This imports discord; a library allowing the program to access Discord
import discord

# This sets the client which the program uses to access Discord
client = discord.Client()

# This conceals the token from you, the causal reader.
tokenFile = open("token.txt", "r")
token = str(tokenFile.read())


@client.event
# This enables checking of messages
async def on_message(messagename):
    # This is a pool of random 'dreams' which the bot pulls from in later sections of the code
    dreamlist = [
        "Torchbugs",
        "Overturned jar",
        "Familiar embrace",
        "Discarded Flowers",
        "Empty Cylinder",
        "Raindrops on glass",
        "Wood Smoke",
        "Deceased bird",
        "Handkerchief",
        "Glowing embers",
        "Wool blanket",
        "Storm clouds",
        "Wind",
        "Familiar smell",
        "Wrinkled hands",
        "Burning tapestry",
        "Screaming",
        "Soiled tablecloth",
        "Washboard",
        "Pottery wheel",
        "Laughter",
        "Flower garden",
        "Bird songs",
        "Fish pond",
        "Skipping stone",
        "Moonlight",
        "Scrib jelly",
        "A rainy day",
        "One netch",
        "Two netch",

    ]

    dream1 = random.choice(dreamlist)
    dreamlist.remove(dream1)
    dream2 = random.choice(dreamlist)
    dreamoutput = ("Dreaming … " + dream1 + ". " + dream2 + ".")
    dreamlist.append(dream1)

    examplembed = discord.Embed(
        title='Retrieving information...',
        description=dreamoutput,
        colour=discord.Colour.red()
    )
    examplembed.set_footer(text='AIOS functionality preparing')
    # examplembed.set_image(
    #    url='https://media.discordapp.net/attachments/494443546989035520/509201412672978944/unknown.png?width=888'
    #         '&height=500')
    examplembed.set_thumbnail(
        url='https://www.pdfonline.com/convert-jpg-to-pdf/images/loadingAnimation.gif')
    examplembed.set_author(name='AIOS',
                           icon_url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261'
                                    '/k86qvkS.png')

    NewEmbed = discord.Embed(
        title='Information Retrieved',
        description='Sample Information',
        colour=discord.Colour.green()
    )
    NewEmbed.set_footer(text='AIOS functionality delivered')
    #NewEmbed.set_image(url='https://cdn.discordapp.com/attachments/494443546989035520/512170758848380928/unknown.png')
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
# A number of functions relating to the bot's activation
async def on_ready():
    # The bot outputs 'ready' to the pythonic output
    print("ready")
    # The bot changes its now playing status to 'The Engine of Expression'
    await client.change_presence(game=discord.Game(name='The Engine of Expression'))


# this runs the program
client.run(token)
