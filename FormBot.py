import requests
import discord
from discord import Embed, File
from discord.ext import commands

# Configure the bot
prefix = "&"
client = commands.Bot(command_prefix=prefix, case_insensitive=True)
client.remove_command('help')

# Start notifying in the console.
@client.event
async def on_ready():
  print(f"Bot is now online and ready! - {client.user.name}")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"&help, bot coded and hosted by FallenV4!"))

# The bot activities.
@client.command()
async def help(ctx):
	# Commands available in the bot.
    embed = Embed(title="GFormBot, an automated google form w/ discord.")
    embed.add_field(name="&help", value="Display the commands available.", inline=False)
    embed.add_field(name="&register", value="Start the form registration process.", inline=False)
    embed.add_field(name="&info", value="Show the information regarding the bot.", inline=False)
    embed.add_field(name="&version", value="Show the version of the bot.", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def register(ctx, *, arg):
	# Convert user message into string.
	print(arg)
	msginput = str(arg)
	print(msginput)
	# Split both data from the user's message.
	name,email = msginput.split("_")
	#Prepare a POST request into Google Form.
	await ctx.send("Thank you, we are now processing the registration...")
  # Change this into your Google Form Request URL with the data.
	url = """https://docs.google.com/forms/d/e/1FAIpQLScOidRE0x1ZhQcszmbqeYkD5qcG-iXDtWGFpHtwT9xu2fKG3w/formResponse?entry.857965010="""+ name +"""&entry.1202030598="""+ email +"""&
	"""

	print(url)
	# Sending the form data into the Form.
	requests.post(url)
	logs = "A form data has been sent! :\n**Email Address : **"+email+"\n**Full Name : **"+name+""
	success = Embed(title=":white_check_mark:   Successful Form Automation", description=logs, color=4564285)
	await ctx.send(embed=success)


@client.command()
async def info(ctx):

	# Information regarding the bot.
	info = Embed(title="Thank you for using the GFormBot.", description="This bot was created by **Fallen**, It was all started when I got extremely lazy to fill the attendance check.\nEh, now I have given away the source code. You may use this freely as you want.\nDon't forget to give me a credit also!.", color=4431584)

	info.add_field(name="Who coded all of those?", value="All of those was coded by Fallen, also known as TemenNsk on Github. Subscribe into my YouTube channel if you feel so. That will appreciate my work a lot!. It's TemenNsk.", inline=False)

	info.add_field(name="How did I use this?", value="Just input your data in the following format.\nAfter that, the bot will do the rest of the job.\n`&register <name>_<email>` **(Underscore are required!)**", inline=False)

	info.add_field(name="Can I invite the bot?", value="Surely, you can freely invite the bot into any server you want!.\n[**Invite Our Bot Into Your Server!**](https://github.com/TemenNsk)", inline=False)

	info.add_field(name="Contact Developer!", value="Telegram : @FallenV4\nDiscord : Fallen#0021", inline=False)
	await ctx.send(embed=info)

@client.command()
async def version(ctx):
	# Version regarding the bot
    version = Embed(title="Bot Development Version", description="Bot ver. : **v.1.0.0** (Fresh Release)\nAuthor / Creator : Fallen#0021\nConnection Form : Sample Registration Form.", color=4431584)

    await ctx.send(embed=version)

# Run the bot with the bot token.
client.run("Change this into your bot token.")
