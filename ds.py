# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import random
from github import Github
import time
import pyperclip

g = Github("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")
user = g.get_user("ErtyHubCheats")

config = {
    'token': 'MTI1MjE1NjMyMjU2OTM5MjEyOQ.G8GGus.tqCj5tWVWTmO-fqm3msnY5-5V7FgpwA86BtXHg',
    'prefix': '-',
}

list_player = [

]
list_message = [

]
list_pus = [

]
list_player_role = {
    "𝕱𝖚𝖈𝖐 𝖞𝖔𝖚 𝖇𝖎𝖙𝖈𝖍" : "sigma_2008__77980",
    "White_Негр (Я черни)" : "faryraf",
    "𝗘б𝗮н𝗸𝗼" : "ponmegga666"
}
MsGs = ""
admins = [
    "terter08276"
]
def load_dan():
    global list_player,list_message,list_pus,MsGs
    list_player = [

    ]
    list_message = [

    ]
    list_pus = [

    ]

    load_save = open("Fds/SaveMsg", "r").read()
    load_save = load_save.split(",")
    if load_save:
        for v in load_save:
            if v != "":
                v1,v2 = v.split("/")
                if v1 != "":
                    list_player.append(v1)
                    list_message.append(int(v2))
    load_save2 = open("Fds/SaveUser", "r").read()
    load_save2 = load_save2.split(",")
    for v in load_save2:
        if v != "":
            list_pus.append(v)
    MsGs = open("Fds/ListMessages.txt", "r", encoding="utf-8").read()
load_dan()
bot = commands.Bot(command_prefix=config['prefix'],intents=discord.Intents.all())


def save_all_dd():
    global list_player,list_message,list_pus,MsGs
    save_save = ""
    for v in list_player:
        save_save = save_save + v + "/" + str(list_message[list_player.index(v)]) + ","
        open("Fds/SaveMsg", "w").write(save_save)
    save_save2 = ""
    for v in list_pus:
        save_save2 = save_save2 + v + ","
        open("Fds/SaveUser", "w").write(save_save2)
    with open('Fds/ListMessages.txt', 'r+', encoding="utf-8") as f:
        f.write(MsGs)


@bot.command()
async def give_role(ctx, member: discord.Member = None):
    if member != None:
        if [key for key, value in list_player_role.items() if value == ctx.author.name]:
            role = [key for key, value in list_player_role.items() if value == ctx.author.name]
            await member.add_roles(discord.utils.get(ctx.guild.roles, name=role[0]))
            await ctx.send(
                embed=discord.Embed(
                description=f"{ctx.author.nick or ctx.author.global_name} выдал ''' {member.nick or member.global_name} '''  роль {role[0]}",
                color=discord.Color.purple(),
                )
            )

@bot.command()
@commands.has_role("📝Scripter📝")
async def delrole(ctx, member: discord.Member = None, role: discord.Role = None):
    if member != None:
        await member.remove_roles(role)
        await ctx.send(
            embed=discord.Embed(
            description=f"**{ctx.author.nick or ctx.author.global_name} забрал у ''' {member.nick or member.global_name} ''' роль {role.name}",
            color=discord.Color.orange(),
            )
        )
@bot.command()
@commands.has_role("📝Scripter📝")
async def delrole(ctx, member: discord.Member = None, role: discord.Role = None):
    if member != None:
        await member.add_roles(role)
        await ctx.send(
            embed=discord.Embed(
            description=f"**{ctx.author.nick or ctx.author.global_name} выдал ''' {member.nick or member.global_name} ''' роль {role.name}",
            color=discord.Color.orange(),
            )
        )

@bot.event
async def on_message(ctx):
    global MsGs
    if ctx.author != bot.user:
        current_time = time.time()
        lt = time.localtime(current_time)
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        MsGs = MsGs + f"[{formatted_time}][{ctx.author.name}]---{str(ctx.content)}\n"
        if ctx.author.name in list_player:
            list_message[list_player.index(ctx.author.name)] += 1
        else:
            list_player.append(ctx.author.name)
            list_message.append(1)
        if ctx.content.startswith(config["prefix"]+'msgs'):
            if ctx.author.name in list_player:
                nmm = ""
                if ctx.author.nick:
                    nmm = ctx.author.nick
                else:
                    nmm = ctx.author.global_name
                await ctx.reply(f'{nmm} у вас {list_message[list_player.index(ctx.author.name)]} сообщений')
            else:
                nmm = ""
                if ctx.author.nick:
                    nmm = ctx.author.nick
                else:
                    nmm = ctx.author.global_name
                await ctx.reply(f'{nmm} у вас 0 сообщений')
            await ctx.delete()
        if ctx.author.name in admins and ctx.content.startswith(config["prefix"] + 'save'):
            save_all_dd()
            await ctx.add_reaction('✅')
            await ctx.reply(f'Данные сохранены')
        elif ctx.content.startswith(config["prefix"] + 'save'):
            await ctx.add_reaction('❌')
        if ctx.author.name == "terter08276" and ctx.content.startswith(config["prefix"] + 'reload'):
            load_dan()
            await ctx.add_reaction('✅')
        elif ctx.content.startswith(config["prefix"] + 'reload'):
            await ctx.add_reaction('❌')
        if ctx.author.name == "terter08276" and ctx.content.startswith(config["prefix"] + 'shutdown'):
            await ctx.reply("🔴Бот Был Выключен🔴")
            await ctx.delete()
            exit()
        if ctx.author.name in admins and ctx.content.startswith(config["prefix"] + 'say'):
            await ctx.add_reaction('✅')
            await ctx.reply(f"{str(ctx.content)[5:]}")
        elif ctx.content.startswith(config["prefix"] + 'say'):
            await ctx.add_reaction('❌')
        if ctx.author.name == "terter08276" and ctx.content.startswith(config["prefix"] + 'time_admin'):
            admins.append(str(ctx.content).split(" ")[1])
            await ctx.reply(f"Админ выдал временую админку пользователю {str(ctx.content).split(" ")[1]}")
            await ctx.add_reaction('✅')
        elif ctx.content.startswith(config["prefix"] + 'time_admin'):
            await ctx.add_reaction('❌')
        if ctx.author.name == "terter08276" and ctx.content.startswith(config["prefix"] + 'del_admin'):
            if str(ctx.content).split(" ")[1] in admins:
                admins.pop(admins.index(str(ctx.content).split(" ")[1]))
                await ctx.reply(f"Админ убрал права администратора у пользователя {str(ctx.content).split(" ")[1]}")
                await ctx.add_reaction('✅')
        elif ctx.content.startswith(config["prefix"] + 'del_admin'):
            await ctx.add_reaction('❌')
        if ctx.author.name in admins and ctx.content.startswith(config["prefix"] + 'ld'):
            sp_l = """Top 5 Messages"""
            sp_l2 = []
            for v in list_player:
                sp_l2.append((v,list_message[list_player.index(v)]))
            sp_l2.sort(key=lambda a: a[1])
            if len(sp_l2) > 4:
                for v in range(5):
                    i = len(sp_l2) - 1 - v
                    sp_l = sp_l + "\n" + str(v+1) + ". " + sp_l2[i][0] + "   " + str(sp_l2[i][1])
            else:
                for v in range(len(sp_l2)):
                    i = len(sp_l2) - 1 - v
                    sp_l = sp_l + "\n" + str(v+1) + ". " + sp_l2[i][0] + "   " + str(sp_l2[i][1])
            await ctx.reply(sp_l)
            await ctx.add_reaction('✅')
        elif ctx.content.startswith(config["prefix"] + 'ld'):
            await ctx.add_reaction('❌')
        if ctx.author.name in admins and ctx.content.startswith(config["prefix"] + 'rn_mm'):
            guild = bot.get_guild(1234538083420999770)
            members = guild.members
            await ctx.reply(f"<@{members[random.randint(1,len(members)-1)].id}>")
            await ctx.add_reaction('✅')
        elif ctx.content.startswith(config["prefix"] + 'rn_mm'):
            await ctx.add_reaction('❌')
        if ctx.author.name in admins and ctx.content.startswith(config["prefix"] + 'get_roles'):
            if str(ctx.content).split(" ")[1] == "all":
                sss = ""
                guild = bot.get_guild(1234538083420999770)

                for v in guild.roles:
                    sss = sss + f"{v},  "
                await ctx.reply(f"{sss[10:]}")
            elif str(ctx.content).split(" ")[1] == "my":
                sss = ""
                for v in ctx.author.roles:
                    sss = sss + f"{v},  "
                await ctx.reply(f"{sss[10:]}")
            await ctx.add_reaction('✅')
        elif ctx.content.startswith(config["prefix"] + 'get_roles'):
            await ctx.add_reaction('❌')
        if ctx.author.name == "terter08276" and ctx.content.startswith(config["prefix"] + 'set_msgs'):
            await ctx.add_reaction('✅')
            if str(ctx.content).split(" ")[1].isdigit():
                list_message[list_player.index(ctx.author.name)] = int(str(ctx.content).split(" ")[1])
                await ctx.reply(f"{ctx.author.name} выдал себе {str(ctx.content).split(" ")[1]} сообщений. Помните что нельзя этим пользоваться!")
            elif str(ctx.content).split(" ")[1] in list_player:
                list_message[list_player.index(str(ctx.content).split(" ")[1])] = int(str(ctx.content).split(" ")[2])
                await ctx.reply(f"{ctx.author.name} выдал пользователю {str(ctx.content).split(" ")[1]} {str(ctx.content).split(" ")[2]} сообщений. Помните что нельзя этим пользоваться!")
        elif ctx.content.startswith(config["prefix"] + 'set_msgs'):
            await ctx.add_reaction('❌')
        if ctx.content.startswith(config["prefix"] + 'get_perm'):
            await ctx.reply("На данный момент получить ключ не возможно по причине фикса дюпа. Пожалуйста подождите хотя бы до 10 июля")
            # if not ctx.author.name in list_pus and str(ctx.content).split(" ")[1] != None:
            #     if list_message[list_player.index(ctx.author.name)] >= 100:
            #         list_pus.append(ctx.author.name)
            #         await ctx.reply(f"{ctx.author.nick} получил доступ к беспл дюпу на аккаунт {str(ctx.content).split(" ")[1]}")
            #         save_all_dd()
            #         load_save3 = open("Fds/NickNames", "r").read()
            #         load_save3 = load_save3.split(",")
            #         save2 = ""
            #         for v in load_save3:
            #             save2 = save2 + v + ","
            #         save2 = save2 + str(ctx.content).split(" ")[1]
            #         open("Fds/NickNames", "w").write(save2)
            #         save = """local wl = {\np_list = {\n"""
            #         for v in save2.split(","):
            #             save = save + '"' + v + '",\n'
            #         save = save + "}\n}\nreturn wl"
            #         repo = user.get_repo("Cheats")
            #         content = repo.get_contents("wl.lua")
            #         repo.update_file(path=content.path, message="update", content=save, sha=content.sha, branch="main")
            #     else:
            #         await ctx.reply(f"У вас не хватает {100 - list_message[list_player.index(ctx.author.name)]} для получения доступа к дюпу")
            # else:
            #     await ctx.reply("Вы уже получали доступ для аккаунта сегодня")
        await bot.process_commands(ctx)





bot.run(config['token'])
