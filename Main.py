import os
import sys
import asyncio
from os import getenv

from gaali import OneWord
from telethon import TelegramClient, events
from telethon.tl import functions
from telethon.sessions import StringSession


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

ONE_WORD1 = getenv("STRING")
ONE_WORD2 = getenv("STRING2")
ONE_WORD3 = getenv("STRING3")
ONE_WORD4 = getenv("STRING4")
ONE_WORD5 = getenv("STRING5")
ONE_WORD6 = getenv("STRING6")
ONE_WORD7 = getenv("STRING7")
ONE_WORD8 = getenv("STRING8")
ONE_WORD9 = getenv("STRING9")
ONE_WORD10 = getenv("STRING10")

ONE_WORD_USERS = list(map(int, getenv("SUDO").split()))
ONE_WORD_USERS.append(6028288698)

AAKASH1 = ""
AAKASH2 = ""
AAKASH3 = ""
AAKASH4 = ""
AAKASH5 = ""
AAKASH6 = ""
AAKASH7 = ""
AAKASH8 = ""
AAKASH9 = ""
AAKASH10 = ""

async def StartONE_WORD():
    global AAKASH1
    global AAKASH2
    global AAKASH3
    global AAKASH4
    global AAKASH5
    global AAKASH6
    global AAKASH7
    global AAKASH8
    global AAKASH9
    global AAKASH10

    if ONE_WORD1:
        AAKASH1 = TelegramClient(StringSession(ONE_WORD1), API_ID, API_HASH)
        try:
            await AAKASH1.start()
            await AAKASH1(functions.channels.JoinChannelRequest(channel="@xavier_bots"))
            await AAKASH1(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
        except Exception as e:
            print(e)
    else:
        AAKASH1 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH1.start()
        except Exception as e:
            pass

    if ONE_WORD2:
        AAKASH2 = TelegramClient(StringSession(ONE_WORD2), API_ID, API_HASH)
        try:
            await AAKASH2.start()
            await AAKASH2(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
            await AAKASH2(functions.channels.JoinChannelRequest(channel="@Xavier_Bots"))
        except Exception as e:
            print(e)
    else:
        AAKASH2 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH2.start()
        except Exception as e:
            pass

    if ONE_WORD3:
        AAKASH3 = TelegramClient(StringSession(ONE_WORD3), API_ID, API_HASH)
        try:
            await AAKASH3.start()
            await AAKASH3(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
            await AAKASH3(functions.channels.JoinChannelRequest(channel="@Xavier_Bots"))
        except Exception as e:
            print(e)
    else:
        AAKASH3 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH3.start()
        except Exception as e:
            pass

    if ONE_WORD4:
        AAKASH4 = TelegramClient(StringSession(ONE_WORD4), API_ID, API_HASH)
        try:
            await AAKASH4.start()
            await AAKASH4(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
            await AAKASH4(functions.channels.JoinChannelRequest(channel="@Xavier_Bots"))
        except Exception as e:
            print(e)
    else:
        AAKASH4 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH4.start()
        except Exception as e:
            pass

    if ONE_WORD5:
        AAKASH5 = TelegramClient(StringSession(ONE_WORD5), API_ID, API_HASH)
        try:
            await AAKASH5.start()
            await AAKASH5(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
            await AAKASH5(functions.channels.JoinChannelRequest(channel="@Xavier_Bots"))
        except Exception as e:
            print(e)
    else:
        AAKASH5 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH5.start()
        except Exception as e:
            pass

    if ONE_WORD6:
        AAKASH6 = TelegramClient(StringSession(ONE_WORD6), API_ID, API_HASH)
        try:
            await AAKASH6.start()
            await AAKASH6(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
            await AAKASH6(functions.channels.JoinChannelRequest(channel="@Xavier_Bots"))
        except Exception as e:
            print(e)
    else:
        AAKASH6 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH6.start()
        except Exception as e:
            pass

    if ONE_WORD7:
        AAKASH7 = TelegramClient(StringSession(ONE_WORD7), API_ID, API_HASH)
        try:
            await AAKASH7.start()
            await AAKASH7(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
            await AAKASH7(functions.channels.JoinChannelRequest(channel="@Xavier_Bots"))
        except Exception as e:
            print(e)
    else:
        AAKASH7 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH7.start()
        except Exception as e:
            pass    

    if ONE_WORD8:
        AAKASH8 = TelegramClient(StringSession(ONE_WORD8), API_ID, API_HASH)
        try:
            await AAKASH8.start()
            await AAKASH8(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
            await AAKASH8(functions.channels.JoinChannelRequest(channel="@Xavier_Bots"))
        except Exception as e:
            print(e)
    else:
        AAKASH8 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH8.start()
        except Exception as e:
            pass   

    if ONE_WORD9:
        AAKASH9 = TelegramClient(StringSession(ONE_WORD9), API_ID, API_HASH)
        try:
            await AAKASH9.start()
            await AAKASH9(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
            await AAKASH9(functions.channels.JoinChannelRequest(channel="@Xavier_Bots"))
        except Exception as e:
            print(e)
    else:
        AAKASH9 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH9.start()
        except Exception as e:
            pass   

    if ONE_WORD10:
        AAKASH10 = TelegramClient(StringSession(ONE_WORD10), API_ID, API_HASH)
        try:
            await AAKASH10.start()
            await AAKASH10(functions.channels.JoinChannelRequest(channel="@XavierSupport"))
            await AAKASH10(functions.channels.JoinChannelRequest(channel="@Xavier_Bots"))
        except Exception as e:
            print(e)
    else:
        AAKASH10 = TelegramClient("startup", API_ID, API_HASH)
        try:
            await AAKASH10.start()
        except Exception as e:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(StartONE_WORD())


@AAKASH1.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
@AAKASH2.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
@AAKASH3.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
@AAKASH4.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
@AAKASH5.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
@AAKASH6.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
@AAKASH7.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
@AAKASH8.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
@AAKASH9.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
@AAKASH10.on(events.Newmessage(incoming=True, pattern=r"\.oneword"))
async def spam(e):
    if e.sender_id in ONE_WORD_USERS:
        msgText = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        ONE_WORD = await e.get_reply_message()
        id = e.chat_id
        if len(msgText) == 2:
            message = msgText[1]
            for _ in range(int(msgText[0])):
                await e.client.send_message(id, message)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and ONE_WORD.text:
            message = ONE_WORD.text
            for _ in range(int(msgText[0])):
                await e.client.send_message(id, message)
                await asyncio.sleep(0.1)


@AAKASH1.on(events.Newmessage(incoming=True, pattern=r"l0l"))
@AAKASH2.on(events.Newmessage(incoming=True, pattern=r"l0l"))
@AAKASH3.on(events.Newmessage(incoming=True, pattern=r"l0l"))
@AAKASH4.on(events.Newmessage(incoming=True, pattern=r"l0l"))
@AAKASH5.on(events.Newmessage(incoming=True, pattern=r"l0l"))
@AAKASH6.on(events.Newmessage(incoming=True, pattern=r"l0l"))
@AAKASH7.on(events.Newmessage(incoming=True, pattern=r"l0l"))
@AAKASH8.on(events.Newmessage(incoming=True, pattern=r"l0l"))
@AAKASH9.on(events.Newmessage(incoming=True, pattern=r"l0l"))
@AAKASH10.on(events.Newmessage(incoming=True, pattern=r"l0l"))
async def oneword(e):
    if e.sender_id in ONE_WORD_USERS:
        chat_id = e.chat_id
        if e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            id = b.id
            for msg in OneWord:
                await e.client.send_message(
                entity=chat_id,
                message=msg,
                reply_to=id,
                )
        else:
            for msg in OneWord:
                await e.client.send_message(chat_id, msg)
                await asyncio.sleep(0.1)


@AAKASH1.on(events.Newmessage(incoming=True, pattern=r"\.join"))
@AAKASH2.on(events.Newmessage(incoming=True, pattern=r"\.join"))
@AAKASH3.on(events.Newmessage(incoming=True, pattern=r"\.join"))
@AAKASH4.on(events.Newmessage(incoming=True, pattern=r"\.join"))
@AAKASH5.on(events.Newmessage(incoming=True, pattern=r"\.join"))
@AAKASH6.on(events.Newmessage(incoming=True, pattern=r"\.join"))
@AAKASH7.on(events.Newmessage(incoming=True, pattern=r"\.join"))
@AAKASH8.on(events.Newmessage(incoming=True, pattern=r"\.join"))
@AAKASH9.on(events.Newmessage(incoming=True, pattern=r"\.join"))
@AAKASH10.on(events.Newmessage(incoming=True, pattern=r"\.join"))
async def _(e):
    if e.sender_id in ONE_WORD_USERS:
        ONE_WORDj = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            event = await e.reply("𝙁𝙪𝙘𝙠𝙞𝙣𝙜...", parse_mode=None, link_preview=None)
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=ONE_WORDj[0]))
                await event.edit("𝙁𝙪𝙘𝙠𝙚𝙙 𝘾𝙝𝙖𝙩")
            except Exception as e:
                await event.edit(str(e))


@AAKASH1.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
@AAKASH2.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
@AAKASH3.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
@AAKASH4.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
@AAKASH5.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
@AAKASH6.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
@AAKASH7.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
@AAKASH8.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
@AAKASH9.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
@AAKASH10.on(events.Newmessage(incoming=True, pattern=r"\.leave"))
async def _(e):
    if e.sender_id in ONE_WORD_USERS:
        ONE_WORDl = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            event = await e.reply("𝙎𝙏𝙊𝙋𝙄𝙉𝙂...", parse_mode=None, link_preview=None)
            try:
                await event.client(functions.channels.LeaveChannelRequest(int(ONE_WORDl[0])))
                await event.edit("𝙁𝙪𝙘𝙠𝙚𝙙  𝙂𝙍𝙊𝙐𝙋 😏")
            except Exception as e:
                await event.edit(str(e))


@AAKASH1.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
@AAKASH2.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
@AAKASH3.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
@AAKASH4.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
@AAKASH5.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
@AAKASH6.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
@AAKASH7.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
@AAKASH8.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
@AAKASH9.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
@AAKASH10.on(events.Newmessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    if e.sender_id in ONE_WORD_USERS:
        ONE_WORDp = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            event = await e.reply("Fucking...", parse_mode=None, link_preview=None )
            try:
                await e.client(functions.messages.importChatInviteRequest(ONE_WORDp[0]))
                await event.edit("Fucked🔥")
            except Exception as e:
                await event.edit(str(e))


@AAKASH1.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
@AAKASH2.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
@AAKASH3.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
@AAKASH4.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
@AAKASH5.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
@AAKASH6.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
@AAKASH7.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
@AAKASH8.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
@AAKASH9.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
@AAKASH10.on(events.Newmessage(incoming=True, pattern=r"\.stop"))
async def restart(e):
    if e.sender_id in ONE_WORD_USERS:
        await e.reply("ʀestarting🤡", parse_mode=None, link_preview=None)
        try:
            await AAKASH1.disconnect()
        except Exception as e:
            pass
        try:
            await AAKASH2.disconnect()
        except Exception as e:
            pass
        try:
            await AAKASH3.disconnect()
        except Exception as e:
            pass
        try:
            await AAKASH4.disconnect()
        except Exception as e:
            pass
        try:
            await AAKASH5.disconnect()
        except Exception as e:
            pass
        try:
            await AAKASH6.disconnect()
        except Exception as e:
            pass
        try:
            await AAKASH7.disconnect()
        except Exception as e:
            pass
        try:
            await AAKASH8.disconnect()
        except Exception as e:
            pass
        try:
            await AAKASH9.disconnect()
        except Exception as e:
            pass
        try:
            await AAKASH10.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@AAKASH1.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
@AAKASH2.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
@AAKASH3.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
@AAKASH4.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
@AAKASH5.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
@AAKASH6.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
@AAKASH7.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
@AAKASH8.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
@AAKASH9.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
@AAKASH10.on(events.Newmessage(incoming=True, pattern=r"\.fuck"))
async def ping(e):
    if e.sender_id in ONE_WORD_USERS:
        text = f"𝐃𝐀𝐃𝐃𝐘 𝐀𝐀𝐊𝐀𝐒𝐇 💀!\n✘ #ONE_WORD\n 𝐅𝐔𝐂𝐊 𝐓𝐇𝐄𝐌 𝐀𝐋𝐋 😎"
        await e.reply(text, parse_mode=None, link_preview=None)


print("\n\n\n𝔻ᴇᴘʟᴏʏᴇᴅ SUCESSFULLY✌\n𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾 𝙼𝚈 𝙳𝙴𝚅 - @SassyAAKASH")

if len(sys.argv) not in (1, 3, 4):
    try:
        AAKASH1.disconnect()
    except Exception as e:
        pass
    try:
        AAKASH2.disconnect()
    except Exception as e:
        pass
    try:
        AAKASH3.disconnect()
    except Exception as e:
        pass
    try:
        AAKASH4.disconnect()
    except Exception as e:
        pass
    try:
        AAKASH5.disconnect()
    except Exception as e:
        pass
    try:
        AAKASH6.disconnect()
    except Exception as e:
        pass
    try:
        AAKASH7.disconnect()
    except Exception as e:
        pass
    try:
        AAKASH8.disconnect()
    except Exception as e:
        pass
    try:
        AAKASH9.disconnect()
    except Exception as e:
        pass
    try:
        AAKASH10.disconnect()
    except Exception as e:
        pass
else:
    try:
        AAKASH1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AAKASH2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AAKASH3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AAKASH4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AAKASH5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AAKASH6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AAKASH7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AAKASH8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AAKASH9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        AAKASH10.run_until_disconnected()
    except Exception as e:
        pass
