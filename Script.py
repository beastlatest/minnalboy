class script(object):
    START_TXT = """<b>Há´Êð</b> {}

<b>Iá´á´</b><a href='https://t.me/Beast100_Bot'>à¼ºMià¸ à¸ à¸ªlÍ¥Ï»uÍ£rÍ«à¸ªlià¼»</a><b>Já´sá´ A Aá´á´ á´É´á´á´ Aá´á´á´ FÉªÊá´á´Ê Bá´á´..!ð¤© TÊÉªs Bá´á´ Is Má´á´á´ Exá´Êá´sÉªá´ á´ÊÊ Fá´Ê TÊá´ "á´á´ÊÊá´ Êá´Ê á´á´á´ Éªá´s" GÊá´á´á´.Sá´ÊÊÊ Yá´á´ Cá´É´'á´ Aá´á´ Má´ Tá´ Yá´á´Ê GÊá´á´á´..!</b>"""
    HELP_TXT = """ð·ð´ð {}
ð·ð´ðð´ ð¸ð ðð·ð´ ð·ð´ð»ð¿ ðµð¾ð ð¼ð ð²ð¾ð¼ð¼ð°ð½ð³ð."""
    ABOUT_TXT = """
â¯ <b>ð¼ð ð½ð°ð¼ð´:</b> à¼ºMià¸ à¸ à¸ªlÍ¥Ï»uÍ£rÍ«à¸ªlià¼»
â¯ <b>ð²ðð´ð°ðð¾ð: Dijil</b>
â¯ <b>ð»ð¸ð±ðð°ðð: ð¿ððð¾ð¶ðð°ð¼</b>
â¯ <b>ð»ð°ð½ð¶ðð°ð¶ð´: ð¿ððð·ð¾ð½ ð¹</b>
â¯ <b>ð³ð°ðð° ð±ð°ðð´: ð¼ð¾ð½ð¶ð¾ ð³ð±</b>
â¯ <b>ð±ð¾ð ðð´ððð´ð: ð·ð´ðð¾ðºð</b>
â¯ <b>ð±ðð¸ð»ð³ ððð°ððð: v1.0.1 [ ð±ð´ðð° ]</b>"""
    SOURCE_TXT = """<b>NOTE:</b> 
<b>DEVS:</b>
- <a href=https://t.me/vaathi_comin_g>Dijil</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and à¼ºMià¸ à¸ à¸ªlÍ¥Ï»uÍ£rÍ«à¸ªlià¼» will respond whenever a keyword is found the message

<b>NOTE:</b>
1. à¼ºMià¸ à¸ à¸ªlÍ¥Ï»uÍ£rÍ«à¸ªlià¼» should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- à¼ºMià¸ à¸ à¸ªlÍ¥Ï»uÍ£rÍ«à¸ªlià¼» Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. à¼ºMià¸ à¸ à¸ªlÍ¥Ï»uÍ£rÍ«à¸ªlià¼» supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Malluhubbmovies)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of à¼º-á´±T-à¼»

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specifed user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """
â ðð¾ðð°ð» ðµð¸ð»ð´ð: <code>{}</code>
â ðð¾ðð°ð» ððð´ðð: <code>{}</code>
â ðð¾ðð°ð» ð²ð·ð°ðð: <code>{}</code>
â ððð´ð³ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±
â ðµðð´ð´ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
