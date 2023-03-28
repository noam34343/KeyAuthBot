import discord
from discord.ext import commands
import requests
import datetime
import os
import time
import random
import string
token = "Bot Token" # bot token
prefix = "Bot Prefix" # bot prefix 
activity = "Bot Activity" # bot activity, Playing {game}
sellerkey = "KeyAuth sellerkey" # sellerkey 
auth_role = "auth role" # only people with the role can use auth commands



bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
def menu():
	print("----------------------------------------")
	print("Welcome to $name KeyAuth Bot")
	print("----------------------------------------")
	

	print('[1] Run Bot')
	print('[2] Github ')
	print('[3] Exit')
	choice = input("> ")
	if choice == '1':
		print("Loading Bot....")
		time.sleep(2)
	elif choice == '2':
		os.system("start https://github.com/noam34343")
		os.system("pause")
		os._exit(0)
	elif choice == '3':
		os._exit(0)
	else:
		print("Not A vaild Option..\n")
		time.sleep(2)
		menu()
		
menu()
		
		


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(activity))
    print("Successfully loaded KeyAuth bot")
    print(f"{prefix}help for commands")
    print(f"Logged in as: {bot.user}")
    print(f"Bot id: {bot.user.id}")




    

# auth commands


@bot.command()
@commands.has_role(auth_role)
async def deluser(ctx, user):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=deluser&user={user}")
	if req.json()["success"]:
		await ctx.send(f"{ctx.author.mention}, You successfully deleted user {user} From KeyAuth")
	else:
		await ctx.send(f"{ctx.author.mention}, Failed to delete This user!")
		

@bot.command()
@commands.has_role(auth_role)
async def hwidreset(ctx, user):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=resetuser&user={user}")
	if req.json()["success"]:
		await ctx.send(f"{ctx.author.mention}, Successfully resetted {user}")
	else:
		await ctx.send(f"{ctx.author.mention}, Failed to hwid reset this user!")
		


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="**Missing Arguments**", description=f"*{ctx.author.mention}, Sorry! you missing Arguments please check the command and try again*", color=0xe74c3c)
		embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/969552068153061466/1090270831495610398/d7d3c693b9568f320a7505c75407cce4.png", text="Keyauth Bot")
		await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		embed = discord.Embed(title="**command not found**", description=f"Sorry! {ctx.author.mention}, This command Doesnt exist!", color=0xe74c3c)
		embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/969552068153061466/1090270831495610398/d7d3c693b9568f320a7505c75407cce4.png", text="Keyauth Bot")
		await ctx.send(embed=embed)

	    
		


@bot.command()
@commands.has_role(auth_role)
async def delkey(ctx, key):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=del&key={key}")
	if req.json()["success"]:
		await ctx.send(f"{ctx.author.mention}, Successfully deleted key {key}")
	else:
		await ctx.send(f"{ctx.author.mention}, Failed to delete this user")
		



@bot.command()
@commands.has_role(auth_role)
async def unbankey(ctx, key):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=unban&key={key}")
	if req.json()["success"]:
		await ctx.send(f"{ctx.author.mention}, Successfully Unbanned key {key}")
	else:
		await ctx.send(f"{ctx.author.mention}, Failed to unban this key!")
		

@bot.command()
@commands.has_role(auth_role)
async def bankey(ctx, key, reason):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=ban&key={key}&reason={reason}")
	if req.json()["success"]:
		await ctx.send(f"{ctx.author.mention}, Successfully banned license key {key} for reason: {reason}")
	else:
		await ctx.send(f"{ctx.author.mention}, Failed to ban this license key!")	
		

@bot.command()
async def addhwid(ctx, username, hwid):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey=${sellerkey}&type=addhwiduser&user={username}&hwid={hwid}")
	if req.json()["success"]:
		await ctx.send(f"{ctx.author.mention}, Successfully added {hwid} Hwid to user {username}")
	else:
		await ctx.send(f"{ctx.author.mention}, Failed to add HWID to this user")


@bot.command()
@commands.has_role(auth_role)
async def verifyuser(ctx, user):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=verifyuser&user={user}")
	if req.json()["success"]:
		embed = discord.Embed(title="**Verified user**", description=f"UserName: {user}\nUser Exist: True", color=0x2ecc71)
		embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/969552068153061466/1090270831495610398/d7d3c693b9568f320a7505c75407cce4.png", text="Keyauth Bot")
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title="**Verified user**", description=f"UserName: {user}\nUser Exist: False", color=0xe74c3c)
		embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/969552068153061466/1090270831495610398/d7d3c693b9568f320a7505c75407cce4.png", text="Keyauth Bot")
		await ctx.send(embed=embed)
		

@bot.command()
@commands.has_role(auth_role)
async def resetuser(ctx, user):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=resetuser&user={user}")
	if req.json()["success"]:
		await ctx.send(f"{ctx.author.mention}, Successfully resetted user {user}")
	else:
		await ctx.send(f"{ctx.author.mention}, Failed to reset this user")
		

@bot.command()
@commands.has_role(auth_role)
async def activate(ctx, username, password, license):
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=activate&user={username}&key={license}&pass={password}format=text")
	if req.json()["success"]:
		embed = discord.Embed(title="**License Successfully Activated**", description=f"License Activiated\nUsername: {username}\nPassword: {password}\nlicense key: {license}", color=0x2ecc71)
		embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/969552068153061466/1090270831495610398/d7d3c693b9568f320a7505c75407cce4.png", text="Keyauth Bot")
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title="**Failed to Activate Key!**", description=f"{ctx.author.mention}, Failed to Activate this license key!, please try again later", color=0xe74c3c)
		embed.set_footer(icon_url="https://cdn.discordapp.com/attachments/969552068153061466/1090270831495610398/d7d3c693b9568f320a7505c75407cce4.png", text="Keyauth Bot")
		await ctx.send(embed=embed)
		

@bot.command()
@commands.has_role(auth_role)
async def genkey(ctx, day: int):
	key = "".join(random.choice(string.ascii_letters+string.digits) for i in range(25))
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=add&expiry={day}&mask={key}&level=1&amount=1&format=json")
	key = req.json()["key"]
	await ctx.send(f"{ctx.author.mention}, Successfully generated license key! License: {key}")
	
    
# general commands
@commands.has_permissions(ban_members = True)
@bot.command()
async def ban(ctx, user: discord.Member, *, reason):
	if reason == None:
		await ctx.send(f"{ctx.author.mention}, Please Provide a reason to ban members.")
	elif user == None:
		await ctx.send(f"{ctx.author.mention}, Please provide a user to ban.")
	else:
		await user.ban(reason=reason)
		await ctx.send(f"{ctx.author.mention},You Successfully banned user: {user}\nuser id: {user.id}")
		

@commands.has_permissions(kick_members = True)
@bot.command()
async def kick(ctx, user: discord.Member, *, reason):
	if reason == None:
		await ctx.send(f"{ctx.author.mention}, Please Provide a reason to kick members.")
	elif user == None:
		await ctx.send(f"{ctx.author.mention}, Please provide a user to kick.")
	else:
		await user.kick(reason=reason)
		await ctx.send(f"{ctx.author.mention},You Successfully kicked user: {user}\nuser id: {user.id}")
		

@commands.has_permissions(kick_members = True)
@bot.command()
async def lock(ctx):
	await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
	await ctx.send(f"{ctx.author.mention}, Successfully locked channel {ctx.channel.mention}")
	

@commands.has_permissions(kick_members = True)
@bot.command()
async def unlock(ctx):
	await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
	await ctx.send(f"{ctx.author.mention}, Successfully unlocked channel {ctx.channel.mention}")
	


    
	  
	    

		

	



bot.run(token)
