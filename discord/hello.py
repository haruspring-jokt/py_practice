import discord

# まずはdiscord.pyのパッケージをインポートします
client = discord.Client()

# Botがログインし準備が完了した時の処理を書きます
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)

# token にDiscordのデベロッパサイトで取得したトークンを入れてください
# client.run("token")
client.run("NDU1MzUyODI5MzU2NTM5OTI2.Df6xJA.BIALbzMVu1PGiUWjXoa7EQgdJHU")