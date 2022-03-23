import os
import discord
from discord import Member
from discord.utils import get
import random
import asyncio
import time
from webserver import keep_alive

token = os.environ['token']
from discord.ext import commands



client = commands.Bot(command_prefix="?", intents=discord.Intents.all())




@client.event
async def on_ready():
	print("Bot is online and ready to administrate")
	await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                  name=f" new members and promotions"))

@client.command()
@commands.has_role("Moderator [MR]")
async def status(ctx):
    await ctx.send("> RL Admin is online! 😀")



#@client.command()
#@commands.has_role("Lead Developer")
#async def gstart(ctx, mins: int, *, prize: str):
	#embed = discord.Embed(title = "Giveaway! 🎉", description = f"{prize}", color = ctx.author.color)

	#end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60) 
	#embed.add_field(name = "Ends at: ", value = f"{end} UTC")
	#embed.set_footer(text = f"Ends {mins} minute(s) from now!")
	#my_msg = await ctx.send(embed = embed)
	#await my_msg.add_reaction("🎉")
	#await asyncio.sleep(mins)
	#new_msg = await ctx.channel.fetch_message(my_message.id)
	#users = await new_msg.reactions[0].users().flatten()
	#users.pop(users.index(client.user))

	#winner = random.choice(users)
	#await ctx.send(f"The winner is {winner.mention} and they won {prize}! To claim the prize, please DM @Plastic_trojan. If not claimed within 5 minutes, a new winner will be chosen!")

@client.event
async def on_member_join(member: Member):
    channel = client.get_channel(916370579400040500)
    await channel.send(f"{member.mention} just joined the Revision Lounge Discord Server! Say hello to them!")
    user_role = member.guild.get_role(917853271857696808)
    await member.add_roles(user_role)
    channel = client.get_channel(936721461169778764)
    await member.send (f"Hey there {member.mention} , welcome to the Revision Lounge server. We hope you enjoy everything that you can do here.\nPlease don't hesitate to get support in {channel.mention} .\n\nHave a great time! 😃")

@client.command(aliases=['md'])
@commands.has_role("Board of Directors")
async def rolemod(ctx, member: discord.Member, *, reason="No additional message sent"):
	channel = client.get_channel(939927626162798672)
	mod_role = ctx.guild.get_role(926073094957850644)
	await member.add_roles(mod_role)
	await channel.send(f"Welcome {member.mention}! You're now a moderator. You will be contacted shortly with info and command prefixes. Thanks for choosing to help out!")
	await ctx.send(f"Promotion successful! {member.mention} was promoted to Moderator")
	await member.send(
        f"You're now a moderator. You will be contacted shortly with info and command prefixes. Thanks for choosing to help out!\n\nAdditional Messages:\n```{reason}```"
    )
	channel_log = client.get_channel(916991787388776508)
	member_send = ctx.author
	curr_time = time.localtime()
	curr_clock = time.strftime("%H:%M", curr_time)
	em = discord.Embed(title="Role Change **(?md)**", description=f"{member_send.mention} just promoted {member.mention} to Moderator. 🥳\n\nAdditional Messages:\n```{reason}```", colour=discord.Colour.green())
	em.set_footer(text=f"Time Occured: {curr_time}")
	await channel_log.send(embed=em)

@client.command(aliases=['wt'])
@commands.has_role("Board of Directors")
async def roleweb(ctx, member: discord.Member, *, reason="No additional message sent"):
	channel = client.get_channel(923244817197195287)
	mod_role = ctx.guild.get_role(923243197470232696)
	await member.add_roles(mod_role)
	await channel.send(f"Welcome {member.mention}! You're now a website tester. You will be contacted shortly with info. Thanks for choosing to help out!")
	await ctx.send(f"Promotion successful! {member.mention} was promoted to Website Tester")
	await member.send(
        f"You're now a website tester. You will be contacted shortly with info. Thanks for choosing to help out!\n\nAdditional Messages:\n```{reason}```"
    )
	channel_log = client.get_channel(916991787388776508)
	member_send = ctx.author
	curr_time = time.localtime()
	curr_clock = time.strftime("%H:%M", curr_time)
	em = discord.Embed(title="Role Change **(?wt)**", description=f"{member_send.mention} just promoted {member.mention} to Website Tester. 🥳\n\nAdditional Messages:\n```{reason}```", colour=discord.Colour.green())
	em.set_footer(text=f"Time Occured: {curr_time}")
	await channel_log.send(embed=em)

@client.command(aliases=['pt'])
@commands.has_role("Board of Directors")
async def rolepartner(ctx, member: discord.Member, *, reason="No additional message sent"):
	channel = client.get_channel(945349442670825522)
	partner_role = ctx.guild.get_role(945041095753084938)
	await member.add_roles(partner_role)
	await channel.send(f"Welcome {member.mention}! You're now a partner. Thanks for choosing to partner with Revision Lounge.")
	await ctx.send(f"Promotion successful! {member.mention} was given the role Partner")
	await member.send(
        f"You're now a partner. Thanks for choosing to partner with Revision Lounge. You have recieved the _Partner_ role. This gives you a hoisted position in the members list, as well as access to the {channel.mention} channel.\n\nAdditional Messages:```{reason}```"
    )
	channel_log = client.get_channel(916991787388776508)
	member_send = ctx.author
	curr_time = time.localtime()
	curr_clock = time.strftime("%H:%M", curr_time)
	em = discord.Embed(title="Role Change **(?pt)**", description=f"{member_send.mention} just gave {member.mention} the Partner role.\n\nAdditional Messages:\n```{reason}```", colour=discord.Colour.green())
	em.set_footer(text=f"Time Occured: {curr_time}")
	await channel_log.send(embed=em)









keep_alive()
client.run(token)