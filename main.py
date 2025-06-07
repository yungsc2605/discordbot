from flask import Flask
from threading import Thread
import discord
from discord.ext import commands
import asyncio
import os

# Setup bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Role/password/channel settings
TOKEN = os.environ["DISCORD_TOKEN"]
ROLE_NAME = "naughty"
CHANNEL_NAME = "vungoimora"
TARGET_CHANNEL = "hehe"
PASSWORD = "emyeucacanh"

active_users = set()

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    guild = message.guild
    member = message.author
    role = discord.utils.get(guild.roles, name=ROLE_NAME)

    if message.channel.name == CHANNEL_NAME and message.content.strip() == f"!pass {PASSWORD}":
        if role is None:
            await message.channel.send("❌ Role 'hehe' không tồn tại.")
            return

        try:
            await member.add_roles(role)
            await message.delete()
        except discord.Forbidden:
            await message.channel.send("❌ Bot không có quyền gán role.")
            return

        active_users.add(member.id)
        await message.channel.send(f"🔓 {member.mention} đã được cấp quyền truy cập kênh 'hehe'.")
        return

    if member.id in active_users and message.channel.name != TARGET_CHANNEL:
        if role in member.roles:
            try:
                await member.remove_roles(role)
                await message.channel.send(f"🔒 {member.mention} đã bị gỡ quyền vì rời khỏi kênh 'hehe'.")
            except:
                pass
        active_users.remove(member.id)

    await bot.process_commands(message)

# ---- Keep-alive server ----
app = Flask('')

@app.route('/')
def home():
    return "Bot đang hoạt động!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
bot.run(TOKEN)
