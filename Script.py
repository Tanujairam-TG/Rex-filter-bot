class script(object):
    START_TXT = """π·π΄π»πΎ {},
πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/{}>{}</a>, πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π, πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ π΄π½πΉπΎπ π"""
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    ABOUT_TXT = """β― πΌπ π½π°πΌπ΄: {}
β― π²ππ΄π°ππΎπ: <a href=https://t.me/REX_BOTZ>ππππ πππ‘ ππππ</a>
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β― π±πΎπ ππ΄πππ΄π: π·π΄ππΎπΊπ
β― π±ππΈπ»π³ πππ°πππ: v1.0.1 [ π±π΄ππ° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- π΄πΌπΈπ»πΈπ° π²π»π°ππΊπ΄ πΈπ π½πΎπ π°π½ πΎπΏπ΄π½ ππΎπππ²π΄ πΏππΎπΉπ΄π²π. 
- π²πΎπ½ππ°π²π πΎππ π³π΄ππ πΎπ½π»π π΅πΎπ ππ΄πΏπΎπππΈπ½πΆ π±ππΆπ.

<b>DEVS:</b>
- <a href=https://t.me/REX_BOTZ>ππππ πππ‘ ππππ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. πππ πππππ ππππππ ππππ πππππ ππππππππππ..
2. ππππ’ ππππππ πππ πππ πππππππ ππ π ππππ.
3. πππππ πππππππ ππππ π πππππ ππ 64 ππππππππππ.

<b>Commands and Usage:</b>
β’ /filter - <code>π°π³π³ π° π΅πΈπ»ππ΄π πΈπ½ π²π·π°π</code>
β’ /filters - <code>π»πΈππ π°π»π» ππ·π΄ π΅πΈπ»ππ΄ππ πΎπ΅ π° π²π·π°π</code>
β’ /del - <code>π³π΄π»π΄ππ΄ π° ππΏπ΄π²πΈπ΅πΈπ² π΅πΈπ»ππ΄π πΈπ½ π²π·π°π</code>
β’ /delall - <code>π³π΄π»π΄ππ΄ ππ·π΄ ππ·πΎπ»π΄ π΅πΈπ»ππ΄ππ πΈπ½ π° π²π·π°π (π²π·π°π πΎππ½π΄π πΎπ½π»π)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- π΄πΌπΈπ»πΈπ° π²π»π°ππΊπ΄ πππΏπΏπΎπππ π±πΎππ· πππ» π°π½π³ π°π»π΄ππ πΈπ½π»πΈπ½π΄ π±ππππΎπ½π

<b>NOTE:</b>
1. ππ΄π»π΄πΆππ°πΌ ππΈπ»π» π½πΎπ π°π»π»πΎππ ππΎπ ππΎ ππ΄π½π³ π±ππππΎπ½π ππΈππ·πΎππ π°π½π π²πΎπ½ππ΄π½π, ππΎ π²πΎπ½ππ΄π½π πΈπ πΌπ°π½π³π°ππΎππ.
2. π΄πΌπΈπ»πΈπ° π²π»π°ππΊπ΄ πππΏπΏπΎπππ π±ππππΎπ½π ππΈππ· π°π½π ππ΄π»π΄πΆππ°πΌ πΌπ΄π³πΈπ° πππΏπ΄.
3. π±ππππΎπ½π ππ·πΎππ»π³ π±π΄ πΏππΎπΏπ΄ππ»π πΏπ°πππ΄π³ π°π πΌπ°ππΊπ³πΎππ½ π΅πΎππΌπ°π.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EmiliaClarkeRexBot))</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    FUN_TXT = """Help: <b>π₯ππ π¬ππ½πππΎπ</b> 
    
<b>π² Nothing But Fun Stuffs</b>
1. /dice - π±πππ πππΎ π½ππΌπΎ
2. /Throw - π³π πππππ πΊ π½πΊππ
4. /Goal - π³π πππΊπ 

@Rex_Botz"""
    TELEGRAPH_TXT = """Help: <b>Telegraph Uploader</b>
    
<b>This Feature help to Upload Media Files To Telegraph Below 5MB</b>
1.Send any Media File Below 5MB.
2.Then Reply /telegraph or /tgraph or /tgmedia to the Media File.
3.That's it now you will get link.

<b>Note :</b>
This Feature May Be slow Due to Overload. So Please Wait Until you get your Link."""
    FILTER_TXT = """Help: <b>Choose Type of Filter that you need</b>"""
    FSTORE_TXT = """Help: <b>New File Store Feature</b>
    
<b>This Feature Helps you to Store your File</b>
1.Send Me any Media File.
2.The Reply /link To get sharable Link of That File Then Share the link.

<b>Note :</b>
This is Permanent File Store Feature."""
    QRCODE_TXT = """Help: π½π΄π πππ²πΎπ³π΄ πΆπ΄π½π΄ππ°ππΎπ π΅π΄π°ππππ΄

ππ·πΈπ π΅π΄π°ππππ΄ π·π΄π»πΏπ ππΎπ ππΎ π²πΎπ½ππ΄ππ π°π½π ππ΄ππ πΎπ π»πΈπ½πΊ πΈπ½ππΎ πππ²πΎπ³π΄.
1.π²ππππ πΎπ /qrcode 

2.ππππ ππ πππ’ πππ‘π ππ ππππ πΈ π πππ πππππππ ππππ πππ²πΎπ³π΄"""
    CARBON_TXT = """Help: π²π°ππ±πΎπ½ πΆπ΄π½π΄ππ°ππΎπ
    
ππ·πΈπ π΅π΄π°ππππ΄ π·π΄π»πΏπ ππΎπ ππΎ π²πΎπ½ππ΄ππ π°π½π π²πΎπ³π΄π πΎπ ππ΄ππ πΈπ½ππΎ π²π°ππ±πΎπ½ πΈπΌπ°πΆπ΄.
1.π²ππππ ππ /carbon 

2.ππππ ππ πππ’ πππ‘π ππ πππ’ πππππππ π π πππ ππππππππ ππ ππππ ππππππ πππππ"""
    PIN_TXT = """Help: πΏπΈπ½ πΎπ ππ½πΏπΈπ½ πΌπ΄πππ°πΆπ΄
    
ππ·πΈπ π΅π΄π°ππππ΄ π·π΄π»πΏπ ππΎπ ππΎ πΏπΈπ½ πΎπ ππ½πΏπΈπ½ π°π½π πΌπ΄πππ°πΆπ΄ πΈπ½ πΆππΎππΏ.
1.ππ πΏππ π πΌππππππ πππππ’ /pin ππ πππ πππππππ π’ππ ππππ ππ πππ

2.ππ πππππ π πΌππππππ πππππ’ /unpin ππ πππ πππππππ π’ππ ππππ ππ πππππ"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. πΌπππ ππ πππ πππππ ππ π’πππ πππππππ ππ ππ'π πππππππ.
2. πΌπππ ππππ ππππ π’πππ πππππππ ππππ πππ ππππππππ πππ πππ, ππππ πππ ππππ πππππ.
3. π΅πππ πππ πππ ππππ πππππππ ππ ππ π πππ ππππππ.
   πΈ'ππ πππ πππ πππ πππππ ππ ππππ πππππππ ππ ππ’ ππ.."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. πΎπ½π»π π°π³πΌπΈπ½π π²π°π½ π°π³π³ π° π²πΎπ½π½π΄π²ππΈπΎπ½.
2. ππ΄π½π³ <code>/connect</code> π΅πΎπ π²πΎπ½π½π΄π²ππΈπ½πΆ πΌπ΄ ππΎ ππ πΏπΌ

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
ππ·π΄ππ΄ π°ππ΄ ππ·π΄ π΄ππππ° π΅π΄π°ππππ΄π πΎπ΅ π΄πΌπΈπ»πΈπ° π²π»π°ππΊπ΄

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ 
βββββββββββββββββ
βββββββββββββββββ
β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    COVID_TXT = """<b> Covid 19 Information </b>
To know the Covid info send <code> /covid india </code>"""
    
    JSON_TXT = """<b> Json imformation </b>
To know the json info of the message do reply and give command as /json
"""

    PURGE_TXT = """ <b> Purge module </b>
To delete a message. Reply /purge to a message where to start purging from 
 """
    GTRANS_TXT = """ <b> Google Translator </b>
To translate a text to your required language by replying /tr language 
 """
