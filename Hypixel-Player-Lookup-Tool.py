#Hypixel User Lookup Tool By LegendOfHero
#Lastest Build in 2021/01/26

import datetime as dt
import requests
import os
import time
from colorama import init,Fore,Back,Style
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Hypixel User Lookup By LegendOfHero | Build #210126")
init(autoreset=True)
os.popen('mode con cols=120 lines=30')
time.sleep (0.5)
apitrycount = 0
apisuccess = 1
print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")

def start():
    global apisuccess
    global apitrycount
    if f"{apisuccess}" > "1":
        os.system("cls")
    else:
        try:
            f = open("ApiKey.txt", "r")
            api_key = f.read()
            print("\033[0;33;40m[API-Check] 正在检测Api Key...\033[0m")
            testapi = requests.get(f"https://api.hypixel.net/player?key={api_key}&name=LegendOfHero", timeout=(3, 3)).json()
            if testapi['success']:
                f = open("ApiKey.txt", "w+")
                f.write(api_key)
                f.close()
                f = open("ApiKey.txt", "r")
                print("\033[0;32;40m[API-Check] 检测完成，调用的Api Key有效。\033[0m")
                apisuccess += 1
                time.sleep (1)
            else:
                print("\033[0;31;40m[API-Check] 检测完成，调用的Api Key无效。请尝试更换Api Key。\033[0m")
                time.sleep (1)
                return start()

        except requests.exceptions.RequestException:
            print(f"\033[0;31;40m[API-Check] 连接到服务器错误，重试中... [重试-#{apitrycount}]\033[0m")
            apitrycount += 1
            return start()
    
        except FileNotFoundError:
            print("\033[0;33;40m请使用任一正版账号登录Hypixel，然后使用[/api new]命令在游戏内获取")
            api_key = input("请输入API Key: ")
            print("\033[0;33;40m[API-Check] 正在检测Api Key...\033[0m")
            testapi = requests.get(f"https://api.hypixel.net/player?key={api_key}&name=TechMaster85").json()
            if testapi['success']:
                f = open("ApiKey.txt", "w+")
                f.write(api_key)
                f.close()
                f = open("ApiKey.txt", "r")
                os.system("cls")
                print("\033[0;32;40m[API-Check] 检测完成，调用的Api Key有效。\033[0m")
                time.sleep (1)
            else:
                print("\033[0;31;40m[API-Check] 检测完成，调用的Api Key无效。请尝试更换Api Key。\033[0m")
                time.sleep (1)
                return start()

    os.system("cls")
    print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
    f = open("ApiKey.txt", "r")
    api_key = f.read()
    player_name = input("\033[0;32;40m请输入你想要查询的玩家名称: \033[37;40m")
    if f"{player_name}" == "":
        print("\033[0;33;40m[Request-Empty] 玩家名不能为空...\033[0m")
        print("\033[0;33;40m\n[Information] 按下Enter继续...\033[0m")
        input()
        os.system("cls")
        print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
        return start()
    else:
        if f"{apisuccess}" == "2":
            apisuccess += 1
            os.system("cls")
            print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
        else:
            os.system("cls")
            print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
        print("\033[0;33;40m[Request] 请求已发送，正在等待回应...\033[0m")
    
    aa = 0
    while aa < 9999:
        try:
            data = requests.get(f"https://api.hypixel.net/player?key={api_key}&name={player_name}", timeout=(3, 3)).json()
            break
        except requests.exceptions.RequestException:
            aa += 1
            print(f"\033[0;31;40m[Request-Error#1] 连接到服务器错误，重试中... [重试-#{aa}]\033[0m")

    i = 0
    while i < 9999:
        try:
            data1 = requests.get(f"https://api.slothpixel.me/api/players/{player_name}", timeout=(3, 3)).json()
            break
        except requests.exceptions.RequestException:
            i += 1
            print(f"\033[0;31;40m[Request-Error#2] 连接到服务器错误，重试中... [重试-#{i}]\033[0m")
            
    bb = 0
    while bb < 9999:    
        try:
            data2 = requests.get(f"https://api.slothpixel.me/api/guilds/{player_name}", timeout=(3, 3)).json()
            break
        except requests.exceptions.RequestException:
            bb += 1
            print(f"\033[0;31;40m[Request-Error#3] 连接到服务器错误，重试中... [重试-#{bb}]\033[0m")
 
    
    find1 = f"{data}"
    find2 = f"{data2}"
    find = f"{data1}"
    cc = f"{data1}".find("'username': None")
    if f"{player_name}" == "Mojang" or f"{player_name}" == "mojang" or f"{player_name}" == "Hypixel" or f"{player_name}" == "hypixel" or f"{cc}" == '1':
        find1 = "{'success': True, 'player': None}"
    
    if f"{cc}" == '1':
        find = "{'error': 'Player does not exist'}"
    
    f = f"{data2}".find("'tag_formatted'")
    if f"{f}" == '-1':
        guild = "&7[无]"
    else:
        if f"{data2['tag_formatted']}" == "null" or f"{data2['tag_formatted']}" == "None":
            guild = "&7[未知]"
        else:
            guild = f"{data2['tag_formatted']}"
    guild = guild.replace('&0','\033[30;47m')
    guild = guild.replace('&1','\033[34;40m')
    guild = guild.replace('&2','\033[32;40m')
    guild = guild.replace('&3','\033[36;40m')
    guild = guild.replace('&4','\033[31;40m')
    guild = guild.replace('&5','\033[35;40m')
    guild = guild.replace('&6','\033[33;40m')
    guild = guild.replace('&7','\033[37;40m')
    guild = guild.replace('&8','\033[37;40m')
    guild = guild.replace('&9','\033[34;40m')
    guild = guild.replace('&a','\033[32;40m')
    guild = guild.replace('&b','\033[36;40m')
    guild = guild.replace('&c','\033[31;40m')
    guild = guild.replace('&d','\033[35;40m')
    guild = guild.replace('&e','\033[33;40m')
    guild = guild.replace('&f','\033[37;40m')
    guild = guild.replace('&k','')
    guild = guild.replace('&l','')
    guild = guild.replace('&m','')
    guild = guild.replace('&n','\033[4m')
    guild = guild.replace('&o','')
    guild = guild.replace('&r','')
    
    if find1 == "{'success': True, 'player': None}":
        if find == "{'error': 'Player does not exist'}"  or find == "{'error': 'Invalid username or UUID!'}":
            os.system("cls")
            print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
            print("\033[0;31;40m[Request-NotFound] 你输入的玩家名不存在，请检查后重试。\033[0m")
            print("\033[0;33;40m\n[Information] 按下Enter继续...\033[0m")
            input()
            os.system("cls")
            return start()
        else:
            os.system("cls")
            print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
            a = f"{data1}".find("'language'")
            if f"{a}" == "-1":
                lang = "\033[0;33;40m未知\033[0m"
            else:
                lang = f"{data1['language']}"
            language = f"{lang}"
            language = language.replace('ENGLISH','English (英语)')
            language = language.replace('CHINESE_SIMPLIFIED','简体中文 (中文)')
            language = language.replace('GERMAN','Deutsch (德语)')
            language = language.replace('FRENCH','简体中文 (中文)')
            language = language.replace('DUTCH','Français (法语)')
            language = language.replace('SPANISH','Español (西班牙语)')
            language = language.replace('ITALIAN','Italiano (意大利语)')
            language = language.replace('CHINESE_TRADITIONAL','繁體中文 (中文)')
            language = language.replace('PORTUGUESE_BR','Português (Brasil) [葡萄牙语 (巴西)]')
            language = language.replace('RUSSIAN','Русский (俄语)')
            language = language.replace('KOREAN','한국어 (韩语)')
            language = language.replace('POLISH','Polski (波兰语)')
            language = language.replace('JAPANESE','日本語 (日语)')
            language = language.replace('PIRATE','Pirate Speak (海盗语)')
            language = language.replace('PORTUGUESE_PT','Português (葡萄牙语)')
            language = language.replace('GREEK','Ελληνικά (希腊语)')
            a = f"{data1}".find("'rank_formatted'")
            if f"{a}" == "-1":
                rank = ""
            else:
                rank = f"{data1['rank_formatted']}"
            rank = rank.replace('&0','\033[30;47m')
            rank = rank.replace('&1','\033[34;40m')
            rank = rank.replace('&2','\033[32;40m')
            rank = rank.replace('&3','\033[36;40m')
            rank = rank.replace('&4','\033[31;40m')
            rank = rank.replace('&5','\033[35;40m')
            rank = rank.replace('&6','\033[33;40m')
            rank = rank.replace('&7','\033[37;40m')
            rank = rank.replace('&8','\033[37;40m')
            rank = rank.replace('&9','\033[34;40m')
            rank = rank.replace('&a','\033[32;40m')
            rank = rank.replace('&b','\033[36;40m')
            rank = rank.replace('&c','\033[31;40m')
            rank = rank.replace('&d','\033[35;40m')
            rank = rank.replace('&e','\033[33;40m')
            rank = rank.replace('&f','\033[37;40m')
            rank = rank.replace('&k','')
            rank = rank.replace('&l','')
            rank = rank.replace('&m','')
            rank = rank.replace('&n','\033[4m')
            rank = rank.replace('&o','')
            rank = rank.replace('&r','')
            
    
            c1 = f"{data1}".find("'first_login'")
            c2 = f"{data1}".find("'last_login'")
            c3 = f"{data1}".find("'last_logout'")
            if f"{c1}" == '-1':
                firstlogin = "\033[0;33;40m未知\033[0m"
            else:
                if f"{data1['first_login']}" == "None":
                    firstlogin = "\033[0;33;40m未知\033[0m"
                else:
                    firstlogin = dt.datetime.fromtimestamp(data1['first_login'] / 1000)
    
            if f"{c2}" == '-1':
                lastlogin = "\033[0;33;40m未知\033[0m"
            else:
                if f"{data1['last_login']}" == "None":
                    lastlogin = "\033[0;33;40m未知\033[0m"
                else:
                    lastlogin = dt.datetime.fromtimestamp(data1['last_login'] / 1000)
    
            if f"{c3}" == '-1':
                lastlogout = "\033[0;33;40m未知\033[0m"
            else:
                if f"{data1['last_logout']}" == "None":
                    lastlogout = "\033[0;33;40m未知\033[0m"
                else:
                    lastlogout = dt.datetime.fromtimestamp(data1['last_logout'] / 1000)

            online = f"{data1['online']}"
            online = online.replace('True','\033[32m在线\033[0m')
            online = online.replace('False','\033[31m离线\033[0m')
            
            d = f"{data1}".find("'karma'")
            karma = "\033[0;33;40m未知\033[0m"
            if f"{d}" == "-1":
                karma = "\033[0;33;40m未知\033[0m"
            else:
                if f"{data1['karma']}" == "None":
                    karma = "\033[0;33;40m未知\033[0m"
                else:
                    karma = f"{data1['karma']}"
                    karma = "{:,}".format(int(karma))
            
            d = f"{data1}".find("'achievement_points'")
            achievementPoints = "\033[0;33;40m未知\033[0m"
            if f"{d}" == "-1":
                achievementPoints = "\033[0;33;40m未知\033[0m"
            else:
                if f"{data1['achievement_points']}" == "None":
                    achievementPoints = "\033[0;33;40m未知\033[0m"
                else:
                    achievementPoints = f"{data1['achievement_points']}"
                    achievementPoints = "{:,}".format(int(achievementPoints))
            d = f"{data1}".find("'mc_version'")
            mcversion = "\033[0;33;40m未知\033[0m"
            if f"{d}" == "-1":
                mcversion = "\033[0;33;40m未知\033[0m"
            else:
                if f"{data1['mc_version']}" == "None":
                    mcversion = "\033[0;33;40m未知\033[0m"
                else:
                    mcversion = f"{data1['mc_version']}"
                    
            arcadecoins = "\033[0;33;40m未知\033[0m"
            d = f"{data1}".find("'Arcade'")
            if f"{d}" == "-1":
                arcadecoins = "\033[0;33;40m未知\033[0m"
            else:
                if f"{data1['stats']['Arcade']['coins']}" == "None":
                    arcadecoins = "\033[0;33;40m未知\033[0m"
                else:
                    arcadecoins = f"{data1['stats']['Arcade']['coins']}"
                    arcadecoins = "{:,}".format(int(arcadecoins))


            print(f"玩家 {rank}{data1['username']}{guild} \033[0m的信息:"
                f"\n等级: {data1['level']}"
                f"\nKarma: {karma}"
                f"\n街机硬币: {arcadecoins}"
                f"\n成就点数: {achievementPoints}"
                f"\n在线状态: {online} [{data1['last_game']}]"
                f"\n使用的语言: {language}"
                f"\n使用的Minecraft版本: Minecraft {mcversion}"
                f"\n"
                f"\n第一次登录时间: {firstlogin}"
                f"\n最近登录时间: {lastlogin}"
                f"\n最近下线时间: {lastlogout}"
                f"")

            print("\033[0;32;40m\n[Request-Done] 信息输出完成。\033[0m")
            print("\033[0;33;40m\n[Information] 退出请直接关闭窗口。按下Enter继续...\033[0m")
            input()
            os.system("cls")
            print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
            return start()


    elif not data['success']:
        os.system("cls")
        print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
        print("\033[0;31;40m[Request-APIError] 数据错误，请检查你的网络连接或尝试更换Api Key。\033[0m")
        print("\033[0;33;40m\n[Information] 按下Enter继续...\033[0m")
        input()
        os.system("cls")
        return start()

    else:
        os.system("cls")
        print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
        a = f"{data}".find("'userLanguage'")
        if f"{a}" == "-1":
            b = f"{data1}".find("'language'")
            if f"{b}" == "-1":
                lang = "\033[0;33;40m未知\033[0m"
            else:
                lang = f"{data1['language']}"
        else:
            lang = f"{data['player']['userLanguage']}"
        language = f"{lang}"
        language = language.replace('ENGLISH','English (英语)')
        language = language.replace('CHINESE_SIMPLIFIED','简体中文 (中文)')
        language = language.replace('GERMAN','Deutsch (德语)')
        language = language.replace('FRENCH','简体中文 (中文)')
        language = language.replace('DUTCH','Français (法语)')
        language = language.replace('SPANISH','Español (西班牙语)')
        language = language.replace('ITALIAN','Italiano (意大利语)')
        language = language.replace('CHINESE_TRADITIONAL','繁體中文 (中文)')
        language = language.replace('PORTUGUESE_BR','Português (Brasil) [葡萄牙语 (巴西)]')
        language = language.replace('RUSSIAN','Русский (俄语)')
        language = language.replace('KOREAN','한국어 (韩语)')
        language = language.replace('POLISH','Polski (波兰语)')
        language = language.replace('JAPANESE','日本語 (日语)')
        language = language.replace('PIRATE','Pirate Speak (海盗语)')
        language = language.replace('PORTUGUESE_PT','Português (葡萄牙语)')
        language = language.replace('GREEK','Ελληνικά (希腊语)')
        a = f"{data1}".find("'rank_formatted'")
        if f"{a}" == "-1":
            rank = ""
        else:
            rank = f"{data1['rank_formatted']}"
        rank = rank.replace('&0','\033[30;47m')
        rank = rank.replace('&1','\033[34;40m')
        rank = rank.replace('&2','\033[32;40m')
        rank = rank.replace('&3','\033[36;40m')
        rank = rank.replace('&4','\033[31;40m')
        rank = rank.replace('&5','\033[35;40m')
        rank = rank.replace('&6','\033[33;40m')
        rank = rank.replace('&7','\033[37;40m')
        rank = rank.replace('&8','\033[37;40m')
        rank = rank.replace('&9','\033[34;40m')
        rank = rank.replace('&a','\033[32;40m')
        rank = rank.replace('&b','\033[36;40m')
        rank = rank.replace('&c','\033[31;40m')
        rank = rank.replace('&d','\033[35;40m')
        rank = rank.replace('&e','\033[33;40m')
        rank = rank.replace('&f','\033[37;40m')
        rank = rank.replace('&k','')
        rank = rank.replace('&l','')
        rank = rank.replace('&m','')
        rank = rank.replace('&n','\033[4m')
        rank = rank.replace('&o','')
        rank = rank.replace('&r','')
        
        c1 = f"{data}".find("'firstLogin'")
        c2 = f"{data}".find("'lastLogin'")
        c3 = f"{data}".find("'lastLogout'")
        if f"{c1}" == "-1":
            firstlogin = "\033[0;33;40m未知\033[0m"
        else:
            if f"{data['player']['firstLogin']}" == "None":
                firstlogin = "\033[0;33;40m未知\033[0m"
            else:
                firstlogin = dt.datetime.fromtimestamp(data['player']['firstLogin'] / 1000)
    
        if f"{c2}" == '-1':
            lastlogin = "\033[0;33;40m未知\033[0m"
        else:
            if f"{data['player']['lastLogin']}" == "None":
                lastlogin = "\033[0;33;40m未知\033[0m"
            else:
                lastlogin = dt.datetime.fromtimestamp(data['player']['lastLogin'] / 1000)
    
        if f"{c3}" == '-1':
            lastlogout = "\033[0;33;40m未知\033[0m"
        else:
            if f"{data['player']['lastLogout']}" == "None":
                lastlogout = "\033[0;33;40m未知\033[0m"
            else:
                lastlogout = dt.datetime.fromtimestamp(data['player']['lastLogout'] / 1000)
    
        online = f"\033[31m离线\033[0m"
        if f"{c2}" == "-1" or f"{c3}" == "-1":
           online = f"\033[31m离线\033[0m"
        else:
            if f"{data['player']['lastLogin']}" > f"{data['player']['lastLogout']}":
                online = f"\033[32m在线\033[0m"
            else:
                online = f"\033[31m离线\033[0m" 
        
        d1 = f"{data1}".find("'karma'")
        d = f"{data}".find("'karma'")
        karma = "\033[0;33;40m未知\033[0m"
        if f"{d}" == "-1":
            if f"{d1}" == "-1":
                karma = "\033[0;33;40m未知\033[0m"
            else:
                if f"{data1['karma']}" == "None":
                    karma = "\033[0;33;40m未知\033[0m"
                else:
                    karma = f"{data1['karma']}"
                    karma = "{:,}".format(int(karma))
        else:
            if f"{data['player']['karma']}" == "None":
                karma = "\033[0;33;40m未知\033[0m"
            else:
                karma = f"{data['player']['karma']}"
                karma = "{:,}".format(int(karma))
                
        d = f"{data}".find("'achievementPoints'")
        achievementPoints = "\033[0;33;40m未知\033[0m"
        if f"{d}" == "-1":
            achievementPoints = "\033[0;33;40m未知\033[0m"
        else:
            if f"{data['player']['achievementPoints']}" == "None":
                achievementPoints = "\033[0;33;40m未知\033[0m"
            else:
                achievementPoints = f"{data['player']['achievementPoints']}"
                achievementPoints = "{:,}".format(int(achievementPoints))
                
        arcadecoins = "\033[0;33;40m未知\033[0m"
        d = f"{data1}".find("'Arcade'")
        if f"{d}" == "-1":
            arcadecoins = "\033[0;33;40m未知\033[0m"
        else:
            if f"{data1['stats']['Arcade']['coins']}" == "None":
                arcadecoins = "\033[0;33;40m未知\033[0m"
            else:
                arcadecoins = f"{data1['stats']['Arcade']['coins']}"
                arcadecoins = "{:,}".format(int(arcadecoins))
                
        d = f"{data}".find("'mcVersionRp'")
        mcversion = "\033[0;33;40m未知\033[0m"
        if f"{d}" == "-1":
            d1 = f"{data1}".find("'mc_version'")
            if f"{d1}" == "-1":
                mcversion = "\033[0;33;40m未知\033[0m"
            else:
                if f"{data1['mc_version']}" == "None":
                    mcversion = "\033[0;33;40m未知\033[0m"
                else:
                    mcversion = f"{data1['mc_version']}"
        else:
            if f"{data['player']['mcVersionRp']}" == "None":
                mcversion = "\033[0;33;40m未知\033[0m"
            else:
                mcversion = f"{data['player']['mcVersionRp']}"
                
        d = f"{data1}".find("'username'")
        playername = f"{player_name}"
        if f"{d}" == "-1":
            playername = f"{data['player']['playername']}"
        else:
            playername = f"{data1['username']}"
            
        d = f"{data1}".find("'level'")
        lobbylevel = "\033[0;33;40m未知\033[0m"
        if f"{d}" == "-1":
            lobbylevel = f"\033[0;33;40m未知\033[0m"
        else:
            lobbylevel = f"{data1['level']}"
            
        d = f"{data1}".find("'last_game'")
        lastgame = "\033[0;33;40m未知\033[0m"
        if f"{d}" == "-1":
            lastgame = f"\033[0;33;40m未知\033[0m"
        else:
            lastgame = f"{data1['last_game']}"

        print(f"玩家 {rank}{playername}{guild} \033[0m的信息:"
            f"\n等级: {lobbylevel}"
            f"\nKarma: {karma}"
            f"\n街机硬币: {arcadecoins}"
            f"\n成就点数: {achievementPoints}"
            f"\n在线状态: {online} [{lastgame}]"
            f"\n使用的语言: {language}"
            f"\n使用的Minecraft版本: Minecraft {mcversion}"
            f"\n"
            f"\n第一次登录时间: {firstlogin}"
            f"\n最近登录时间: {lastlogin}"
            f"\n最近下线时间: {lastlogout}"
            f"")

        print("\033[0;32;40m\n[Request-Done] 信息输出完成。\033[0m")
        print("\033[0;33;40m\n[Information] 退出请直接关闭窗口。按下Enter继续...\033[0m")
        input()
        os.system("cls")
        print("\033[1;37;46m==========================================Hypixel User Lookup By LegendOfHero==========================================")
        return start()
start()