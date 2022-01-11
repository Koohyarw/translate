import logging, time, random
from telethon.sync import TelegramClient
from telethon import events
from googletrans import Translator





languages = """

 af :  afrikaans ,
 sq :  albanian ,
 am :  amharic ,
 ar :  arabic ,
 hy :  armenian ,
 az :  azerbaijani ,
 eu :  basque ,
 be :  belarusian ,
 bn :  bengali ,
 bs :  bosnian ,
 bg :  bulgarian ,
 ca :  catalan ,
 ceb :  cebuano ,
 ny :  chichewa ,
 zh-cn :  chinese (simplified) ,
 zh-tw :  chinese (traditional) ,
 co :  corsican ,
 hr :  croatian ,
 cs :  czech ,
 da :  danish ,
 nl :  dutch ,
 en :  english ,
 eo :  esperanto ,
 et :  estonian ,
 tl :  filipino ,
 fi :  finnish ,
 fr :  french ,
 fy :  frisian ,
 gl :  galician ,
 ka :  georgian ,
 de :  german ,
 el :  greek ,
 gu :  gujarati ,
 ht :  haitian creole ,
 ha :  hausa ,
 haw :  hawaiian ,
 iw :  hebrew ,
 hi :  hindi ,
 hmn :  hmong ,
 hu :  hungarian ,
 is :  icelandic ,
 ig :  igbo ,
 id :  indonesian ,
 ga :  irish ,
 it :  italian ,
 ja :  japanese ,
 jw :  javanese ,
 kn :  kannada ,
 kk :  kazakh ,
 km :  khmer ,
 ko :  korean ,
 ku :  kurdish (kurmanji) ,
 ky :  kyrgyz ,
 lo :  lao ,
 la :  latin ,
 lv :  latvian ,
 lt :  lithuanian ,
 lb :  luxembourgish ,
 mk :  macedonian ,
 mg :  malagasy ,
 ms :  malay ,
 ml :  malayalam ,
 mt :  maltese ,
 mi :  maori ,
 mr :  marathi ,
 mn :  mongolian ,
 my :  myanmar (burmese) ,
 ne :  nepali ,
 no :  norwegian ,
 ps :  pashto ,
 fa :  persian ,
 pl :  polish ,
 pt :  portuguese ,
 pa :  punjabi ,
 ro :  romanian ,
 ru :  russian ,
 sm :  samoan ,
 gd :  scots gaelic ,
 sr :  serbian ,
 st :  sesotho ,
 sn :  shona ,
 sd :  sindhi ,
 si :  sinhala ,
 sk :  slovak ,
 sl :  slovenian ,
 so :  somali ,
 es :  spanish ,
 su :  sundanese ,
 sw :  swahili ,
 sv :  swedish ,
 tg :  tajik ,
 ta :  tamil ,
 te :  telugu ,
 th :  thai ,
 tr :  turkish ,
 uk :  ukrainian ,
 ur :  urdu ,
 uz :  uzbek ,
 vi :  vietnamese ,
 cy :  welsh ,
 xh :  xhosa ,
 yi :  yiddish ,
 yo :  yoruba ,
 zu :  zulu ,
 fil :  Filipino ,
 he :  Hebrew 


"""
mute_pv = []
mute_group = []

class Bot:
    api_id = ##api id
    api_hash = "##api hash"    
    admin =  ##admin id
    translator =  Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
    




logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

client = TelegramClient("pro", Bot.api_id, Bot.api_hash)
@client.on(events.NewMessage)
async def main(event):
    global mute_pv, mute_group
    user_id = event.sender_id
    if(user_id == Bot.admin):
        text = event.raw_text
        if(text in ["ping","Ping"]):
            await client.edit_message(event.chat_id, event.message, "Online")
            time.sleep(1.5)
            await client.delete_messages(event.chat_id, [event.message])
            return
        text = text.split()
        if(text[0] in ["translate"]):
            if(len(text) == 1):
                if(event.is_reply):
                    replied = await event.get_reply_message()

                    lang = Bot.translator.detect(replied.raw_text).lang
                    if(lang != "fa"):
                        text = Bot.translator.translate(replied.raw_text, dest = "fa").text
                        await client.edit_message(event.chat_id, event.message, text)
                    else:
                        text = Bot.translator.translate(replied.raw_text, dest = "en").text
                        await client.edit_message(event.chat_id, event.message, text)
                return
            if(len(text) == 3 and text[1] == "to"):
                if(text[1] == "to"):
                    lang = text[2]

                    
                    if(event.is_reply):
                        replied = await event.get_reply_message()


                        try:
                            text = Bot.translator.translate(replied.raw_text, dest = lang).text
                            await client.edit_message(event.chat_id, event.message, text)
                            return
                        except:
                            await client.edit_message(event.chat_id, event.message, "‌Language Not Found‌")

                    
            if(len(text) > 3 and text[1] == "to"):
                text = event.raw_text.split("\n")
                t = text[0].split()
                lang = t[2]

                
                message = ""
                for line in text[1:]:
                    try:
                        message += Bot.translator.translate(line, dest = lang).text + "\n"
                    
                    except:
                        await client.edit_message(event.chat_id, event.message, "‌Language Not Found‌")
                        return
                await client.edit_message(event.chat_id, event.message, message)
        text = event.raw_text
        if(text == "translate help"):
            new_text = f"Available Languages:{languages}"
            await client.edit_message(event.chat_id, event.message, new_text)

client.start()
client.run_until_disconnected()

