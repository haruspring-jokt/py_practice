# APIラッパと非同期I/Oモジュールの読み込み
import discord
import asyncio

# クライアント接続オブジェクト
client = discord.Client()

# 起動時の処理

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# 誰かが発言した時の処理

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    # 返事をする
    if client.user.id in message.content:
        await client.send_message(message.channel, '{} 呼んだ？'.format(message.author.mention))

    # 任意のチャンネルで発言
    channel_id = client.get_channel('455353173171765253') # test
    await client.send_message(channel_id, '勝手に喋るよ')

# botの接続と起動 （tokenはbotアカウントのアクセストークン）
client.run('NDU1MzUyODI5MzU2NTM5OTI2.Df6xJA.BIALbzMVu1PGiUWjXoa7EQgdJHU')
