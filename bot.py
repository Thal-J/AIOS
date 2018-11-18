# setup
# This imports the random library; a library which allows random functionality
import random
# This imports time; a library allowing timing and other functions
import time
# This imports discord; a library allowing the program to access Discord
import discord

# This establishes the client which the program uses to access Discord
client = discord.Client()

# This conceals the token from you, the casual reader by opening it from a text file stored locally
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
        "Burning beds",
        "Collapsed roof",
        "Crushed child",
        "Boots by the fire"
        
    ]
    # This selects a random dream from the dreamlist
    dream1 = random.choice(dreamlist)
    # This removes the dream from the list so it cannot be selected twice
    dreamlist.remove(dream1)
    # This selects a second dream
    dream2 = random.choice(dreamlist)
    # This strings the dreams together
    dreamoutput = ("Dreaming… " + dream1 + ". " + dream2 + ".")
    # This restores the first dream to the list so it can be picked in future
    dreamlist.append(dream1)

    # This establishes the loading-screen embed message
    examplembed = discord.Embed(
        # The title of the embed is displayed as "Retrieving information"
        title='Retrieving information…',
        # This displays the combined dreams
        description=dreamoutput,
        # This sets the sidebar colour of the embed to red
        colour=discord.Colour.red()
    )
    #This makes the footer of the embed display as "AIOS functionality preparing"
    examplembed.set_footer(text='AIOS functionality preparing')
    # examplembed.set_image(
    #    url='')
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
    # NewEmbed.set_image(url='https://cdn.discordapp.com/attachments/494443546989035520/512170758848380928/unknown.png')
    NewEmbed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261/k86qvkS.png')
    NewEmbed.set_author(name='AIOS',
                        icon_url='https://cdn.discordapp.com/attachments/369940161796112394/512618874689290261'
                                 '/k86qvkS.png')
    #This checks if the message read "Output"
    if messagename.content == 'Output':
        #It then sends 'oldmessage', a message containing the first embed
        oldmessage = await client.send_message(messagename.channel, 'speech', embed=examplembed)
        time.sleep(15)
        #This edits 'oldmessage' to the second embed
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
