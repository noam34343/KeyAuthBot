import discord
from discord.ext import commands
import os
import time
import requests
import random
import string

sellerkey = "keyauth sellerkey"
token = "bot token"

icon_url = "icon url"
embed_footer_text = "embed text footer "

keyauth = commands.Bot(command_prefix="!", intents=discord.Intents.all())
keyauth.remove_command("help")

# auth commands
@keyauth.event 
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title=f"**Command Not found**", description=f"*{ctx.author.mention}*, Sorry! this command doesnt exist")
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)

@keyauth.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"**Missing Required Arguments**", description=f"*{ctx.author.mention}*, Sorry! You are missing required arguments.", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)


@keyauth.command()
async def authstatus(ctx):
    req = requests.get(f"https://keyauth.win/")
    embed = discord.Embed(title="**KeyAuth authentication Status**", description=f"*KeyAuth authentication website status*: **{req.status_code}**", color=0x3498db)
    embed.set_footer(text=embed_footer_text, icon_url=icon_url)
    await ctx.send(embed=embed)


@keyauth.command()
async def ping(ctx):
    embed = discord.Embed(title="**pong!**", description=f"{round(keyauth.latency * 1000)} ms", color=0x3498db)
    embed.set_footer(text=embed_footer_text, icon_url=icon_url)
    await ctx.send(embed=embed)






@keyauth.command()
async def deletelicense(ctx, key):
    req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=del&key={key}")
    if req.json()["success"]:
        embed = discord.Embed(title="Deleted License", description=f"{ctx.author.mention} You Successfully deleted license key, License key: {key}", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Failed to delete License", description=f"{ctx.author.mention}, Failed to Delete license key, License key: {key}", color=0xe74c3c)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)


@keyauth.command()
async def banlicense(ctx, key, reason):
    req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=ban&key={key}&reason={reason}")
    if req.json()["success"]:
        embed = discord.Embed(title="Banned license", description=f"{ctx.author.mention} You Successfully Banned license key, License key: {key}", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Failed to Ban License", description=f"{ctx.author.mention}, Failed to Ban license key, License key: {key}", color=0xe74c3c)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)



@keyauth.command()
async def unbanlicense(ctx, key):
    req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=unban&key={key}")
    if req.json()["success"]:
        embed = discord.Embed(title="Unbanned license", description=f"{ctx.author.mention} You Successfully Unbanned license key, License key: {key}", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Failed to Unban License", description=f"{ctx.author.mention}, Failed to Unban license key, License key: {key}", color=0xe74c3c)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)


@keyauth.command()
async def retrievelicense(ctx, user):
    req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=getkey&user={user}")
    req.json()
    embed = discord.Embed(title="Retrieved license", description=f"{ctx.author.mention} You Successfully Retrieved license key, Check your dms!", color=0x3498db)
    embed.set_footer(text=embed_footer_text, icon_url=icon_url)
    await ctx.send(embed=embed)
    await ctx.author.send(req.json())


@keyauth.command()
async def verifylicense(ctx, key):
    req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=verify&key={key}")
    if req.json()["success"]:
        embed = discord.Embed(title="Verified License key", description=f":white_check_mark: License Exist: True\nLicense key: {key}", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Verified License key", description=f":anger: License Exist: False\nLicense key: {key}", color=0xe74c3c)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)


@keyauth.command()
async def genkey(ctx, day: int):
	license = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(40))
	req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=add&format=json&expiry={day}&mask={license}&level=3&amount=1&owner=SellerAPI")
	if req.json()["success"]:
		key = req.json()["key"]
		await ctx.send(f"Successfully generated License key!\nLicense key: ```{key}```")
        



@keyauth.command()
async def activate(ctx, license):
    username = ctx.author
    password = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(10))
    req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=activate&user={username}&key={license}&pass={password}format=text")
    if req.json()["success"]:
        embed = discord.Embed(title="*Successfully activated license key*", description=f"Details about the account", color=0x3498db)
        embed.add_field(name="username\n: ", value=f"{username}")
        embed.add_field(name="password\n: ", value=f"{password}")
        embed.add_field(name="License key\n: ", value=f"{license}")
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(f"{ctx.author.mention}, Successfully activated license key! check your dms for mroe information")
        await ctx.author.send(embed=embed)
    else:
        await ctx.send(f"{ctx.author.mention}, Failed to activate license key! check your dms for more information")
        await ctx.author.send(req.json())




@keyauth.command()
async def resethwid(ctx, user):
    req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=resetuser&user={user}")
    if req.json()["success"]:
        embed = discord.Embed(title="Resetted HWID", description=f":white_check_mark: Successfully resetted HWID for {user}", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Failed to reset HWID", description=f":anger: Failed to reset HWID for {user}", color=0xe74c3c)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)


@keyauth.command()
async def banuser(ctx, user, reason):
    req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=banuser&user={user}&reason={reason}")
    if req.json()["success"]:
        embed = discord.Embed(title="Banned user", description=f":white_check_mark: Successfully banned user {user} for {reason}", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Failed to ban user", description=f":anger: Failed to ban user {user}", color=0xe74c3c)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)

        
@keyauth.command()
async def unbanuser(ctx, user):
    req = requests.get(f"https://keyauth.win/api/seller/?sellerkey={sellerkey}&type=unbanuser&user={user}")
    if req.json()["success"]:
        embed = discord.Embed(title="Unbanned User", description=f"{ctx.author.mention} You Successfully Unbanned User, Username: {user}", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Failed to Unban User", description=f"{ctx.author.mention}, Failed to Unban User , Username: {user}", color=0xe74c3c)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)

# moderator commands

@keyauth.command()
async def ban(ctx, user: discord.Member=None, reason=None):
    if reason == None:
        await ctx.send(f"{ctx.author.mention}, You must provide a reason before ban this user!")
    elif user == None:
        await ctx.send(f"{ctx.author.mention}, You must provide a user to ban before using this command")
    else:
        await user.ban()
        embed = discord.Embed(title="Banned user", description=f"Successfully banned user: {user}\nreason: {reason}\nrequested by: {ctx.author.mention}", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)


@keyauth.command()
async def kick(ctx, user: discord.Member=None, reason=None):
    if reason == None:
        await ctx.send(f"{ctx.author.mention}, You must provide a reason before kick this user!")
    elif user == None:
        await ctx.send(f"{ctx.author.mention}, You must provide a user to kick before using this command")
    else:
        await user.kick()
        embed = discord.Embed(title="Kicked user", description=f"Successfully kicked user: {user}\nreason: {reason}\nrequested by: {ctx.author.mention}", color=0x3498db)
        embed.set_footer(text=embed_footer_text, icon_url=icon_url)
        await ctx.send(embed=embed)


@keyauth.command()
async def chnick(ctx, user: discord.Member, nick):
    await user.edit(nick=nick)
    await ctx.send(f"{ctx.author.mention}, Successfully changed nickname for {user}")


@keyauth.command()
async def slowmode(ctx, secs: int):
    await ctx.channel.edit(slowmode_delay=secs)
    await ctx.send(f"{ctx.author.mention}, Successfully setted slowmode for {ctx.channel.mention}")


@keyauth.command()
async def lock(ctx):
    await ctx.channel.edit_permissions(send_messages = False)
    await ctx.send(f"{ctx.author.mention}, Successfully Locked channel {ctx.channel.mention}")


@keyauth.command()
async def unlock(ctx):
    await ctx.channel.edit_permissions(send_messages = True)
    await ctx.send(f"{ctx.author.mention}, Successfully Locked channel {ctx.channel.mention}")





keyauth.run(token)

