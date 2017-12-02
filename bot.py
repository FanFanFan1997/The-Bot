
import discord
from discord.ext import commands
import random
import facebook

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)




@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def read():
    """Chooses between multiple choices."""
    app_id=  '306163839896677'
    app_secret= 'b46fed8fbb1539af3827de7009c750a8'
    access_token= app_id + "|" + app_secret
    page_name = 'https://www.facebook.com/mcmasterconfessions/'
    graph = facebook.GraphAPI(access_token, 2.11)#Request access

    site_info =  graph.get_object(id=page_name, field= 'message') #Get id of page
    post =  graph.get_connections(id=site_info["id"], connection_name = 'posts') #Get posts of page

    post = post['data'][0]['message'] #Get first post
    post= ''.join([i if ord(i) < 128 else ' ' for i in post]) #Take out 'unknown' characters


    post_data = open('post_data.txt','w')
    post_data.write(post) #Saves the most recent post in file
    post_data.close()
    with open ('post_data.txt') as f:
        data = f.readlines()

    for line in data:
        words = line.split()
        if words == []:
            continue
        else:
            words += "\n"
            words = " ".join(words) 
            await bot.say(words)

    f.close()

@bot.command()
async def hate(*args)
    await bot.say("brandon is ugly")

    

       
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

bot.run(TOKEN_NUMBER)
