import credentials
from apiclient.http import MediaFileUpload
from apiclient import errors
import urllib.request
import webbrowser
import requests
import os
import json
import ast


folderID = {}

def donate_id(id):


    url = "https://seoyujin.github.io/"
    getr = requests.get(url)
    address = getr.text.strip()
    server_address = address + "/donations"

    post_data = {'id':id}
    r = requests.post(server_address, post_data)

    url = r.url

    # MacOS
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'

    webbrowser.get(chrome_path).open_new(url)


    if os.path.isfile("config.json"):
        f = open("config.json", "r")
        readJSON = json.load(f)
        f.close()

        if not id in readJSON[0]['donation']:
            readJSON[0]['donation'].append(id)
            print ("[SYSTEM] Store google account on configuration file - %s" % id)

        # Create metadata.json
        f = open('config.json', 'w')
        json.dump(readJSON, f, indent=4)
        f.close()

    else:
        configList = []
        dict = {}
        dict['donation'] = []
        dict['donation'].append(id)
        configList.append(dict)

        serialized_dict = json.dumps(configList)
        dictJSON = ast.literal_eval(serialized_dict)

        # Create metadata.json
        f = open('config.json', 'w')
        json.dump(dictJSON, f, indent=4)
        f.close()

    log = "donate_" + id
    write_log(log)

    print ("[SYSTEM] Donate google account - %s" % id)


def create_public_folder(account):

    service = credentials.get_service(account)

    body = {
    'title': "jigsaw",
    'mimeType': 'application/vnd.google-apps.folder'
    }

    folder = service.files().insert(body=body).execute()

    permission = {
    'value': '',
    'type': 'anyone',
    'role': 'reader'
    } # https://developers.google.com/drive/web/manage-sharing

    service.permissions().insert(fileId=folder['id'], body=permission).execute()
    print ("[CREATE] Create shared folder in google drive")

    return folder


def revoke_credentials(id):

    url = "https://seoyujin.github.io/"
    getr = requests.get(url)
    address = getr.text.strip()
    server_address = address + "/credentials"

    data = {'id':id}
    r = requests.delete(server_address, params=data)

    #log = "revoke_" + id
    #write_log(log)


def get_credentials_list():
    """
    global folderID
    credentials = []
    current_credential_list = []
    credentials_list = []
    credentials_dict = {}

    url = "https://seoyujin.github.io/"
    r = requests.get(url)
    address = r.text.strip()

    server_address = address + "/credentials"
    #data = {'id':id}
    #r = requests.post(server_address, data)

    r = requests.get(server_address)
    #r = requests.get("http://jigsaw-puzzle.com:9991/credentials")
    #print (r.text)

    list = r.text.split('\n')

    group = list[0][0]

    for idx in range(0, len(list)-1):

        if (idx % 2) == 0:
            strAccount = list[idx]
            indexOfUnder = strAccount.index('_')
            indexOfDot = strAccount.index('.')
            accountName = strAccount[indexOfUnder+1:indexOfDot]
            if (group == strAccount[0]):
                credentials_list.append(accountName)
                current_credential_list.append(accountName)
                credentials_dict[group] = credentials_list
            else:
                group = strAccount[0]
                credentials_list = []
                credentials_list.append(accountName)
                current_credential_list.append(accountName)
                credentials_dict[group] = credentials_list
            credentials.append(accountName)
        else:
            strJSON = list[idx]

            indexOfSF = strJSON.find("jigsaw_folder_id")
            if indexOfSF != -1:
                strSF = strJSON[indexOfSF+20:]
                endOfSF = strSF.find('"')

                folderID[accountName] = strSF[:endOfSF]


            #dict = ast.literal_eval(strJSON)
            #print (dict)
    """


    credentials_dict = {}

    credentials_dict['a'] = ["silencenamu", "silencedeul", "silencesoop"]
    credentials_dict['b'] = ["silencebada", "silencettang", "silencemool"]
    credentials_dict['c'] = ["silencebyul", "silencebaram", "silencebool"]
    credentials_dict['d'] = ["silencepado"]

    current_credential_list = ["silencenamu", "silencedeul", "silencesoop", "silencebada", "silencettang", "silencemool", "silencebyul", "silencebaram", "silencebool", "silencepado"]


    """
    print ("[SYSTEM] Get credentials group list from github :")
    print ("         {0}".format(credentials_dict))
    print ("[SYSTEM] Get credentials list from github :")
    print ("         {0}".format(current_credential_list))
    """

    return credentials_dict, current_credential_list



def get_group_name_of_credential(user_id):

    #r = requests.get("http://silencebyul.cafe24.com:9991/group/"+user_id)
    #print(r.text)      #r.text = 'a'

    #group = r.text


    credentials_dict = {}

    credentials_dict['a'] = ["silencenamu", "silencedeul", "silencesoop"]
    credentials_dict['b'] = ["silencebada", "silencettang", "silencemool"]
    credentials_dict['c'] = ["silencebyul", "silencebaram", "silencebool"]
    credentials_dict['d'] = ["silencepado"]


    for group in credentials_dict:
        if user_id in credentials_dict[group]:
            break

    return group



def write_log(log):

    url = "https://seoyujin.github.io/"
    r = requests.get(url)
    address = r.text.strip()

    server_address = address + "/log"

    #server_address = "http://silencedeul.cafe24.com:9991/log"

    post_data = {'log':log}
    r = requests.post(server_address, post_data)
    print("[SYSTEM] {0}".format(r.text))



def write_garbage_log(log):
    """
    url = "https://seoyujin.github.io/"
    r = requests.get(url)
    address = r.text.strip()

    server_address = address + "/garbage_log"

    post_data = {'log':log}
    r = requests.post(server_address, post_data)


    #post_data = {'log':log}
    #r = requests.post("http://silencedeul.cafe24.com:9991/garbage_log", post_data)

    print("[SYSTEM] Write garbage log - '{0}'".format(r.text))
    """

def get_log(start_idx):
    """
    log_start = {'start': str(start_idx)}
    r = requests.get("http://silencenamu.cafe24.com:9991/log", params=log_start)
    print(r.text)
    """

def create_daily_folder(service, folder_name, parent_id= None):

    body = {
    'title': folder_name,
    'mimeType': 'application/vnd.google-apps.folder'
    }

    # Set the parent folder.
    if parent_id:
        body['parents'] = [{
            "kind": "drive#fileLink",
            'id': parent_id }]

    folder = service.files().insert(body=body).execute()

    permission = {
    'value': '',
    'type': 'anyone',
    'role': 'reader'
    }

    service.permissions().insert(fileId=folder['id'], body=permission).execute()
    print ("[CREATE] Create daily folder in google drive")

    return folder


def check_daily_folder_and_get_id(service, account, date, folder_id):

    global folderID
    key = "daily_" + account
    if key in folderID:
        print ("[SYSTEM] Success to get Daily folder ID -> '%s'" % key[6:])
        return folderID[key]
    else:

        results = service.files().list(orderBy='folder,title', maxResults=40).execute()
        items = results.get('items', [])

        strFolderID = ""

        for item in items:
            emailAddress = item['owners'][0]['emailAddress']
            indexOfAt = emailAddress.index('@')
            accountName = emailAddress[:indexOfAt]

            if accountName == account:
                if item['title'] == date:
                    strFolderID = item['id']
                    key = "daily_" + account
                    folderID[key] = strFolderID
                    print ("[SYSTEM] Success to get Daily folder ID -> '%s'" % account)
                    break

        if len(strFolderID) == 0:
            print ("[SYSTEM] Doesn't exist daily folder. Create daily folder - '%s'" % account)
            folder = create_daily_folder(service, date, folder_id)

            key = "daily_" + account
            folderID[key] = folder['id']

            strFolderID = folder['id']

        return strFolderID


def retrieve_all_files(service):

    result = []
    page_token = None
    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token

            files = service.files().list(orderBy='folder', **param).execute()

            result.extend(files['items'])
            page_token = files.get('nextPageToken')

            if not page_token:
                break

        except Exception as error:
            print('An error occurred: %s' % error)
            break

    return result



def get_shared_folder_id(service, account):

    global folderID

    if account in folderID:
        print ("[SYSTEM] Success to get shared folder ID - '%s'" % account)
        strFolderID = folderID[account]
    else:

        results = retrieve_all_files(service)

        strFolderID = ""

        for item in results:
            emailAddress = item['owners'][0]['emailAddress']
            indexOfAt = emailAddress.index('@')
            accountName = emailAddress[:indexOfAt]

            if accountName == account:
                if item['title'] == 'jigsaw':
                    strFolderID = item['id']
                    print ("[SYSTEM] Success to get shared folder ID - '%s'" % account)
                    break

        folderID[account] = strFolderID

    return strFolderID



def get_file_id_and_name_in_shared_folder(account):

    service = credentials.get_service(account)
    results = retrieve_all_files(service)
    folderID = get_shared_folder_id(service, account)
    cnt = 0
    daily_folder_id_list = []
    dict = {}
    returnList = []

    print ("[SYSTEM] Start to get file id and name for UPDATE")
    if not results:
        print("[SYSTEM] ------------ Shared folder is empty ------------")
    else:
        for item in results:
            if len(item['parents']) != 0:
                if item['parents'][0]['id'] == folderID:
                    orignItemType = item['mimeType']
                    itemType = orignItemType[len(orignItemType)-6:]
                    if itemType == "folder":
                        daily_folder_id_list.append(item['id'])
                    else:
                        dict = {}
                        chunkName = item['title'][12:]
                        dict[chunkName] = item['id']
                        returnList.append(dict)

                for i in range(0, len(daily_folder_id_list)):
                    if item['parents'][0]['id'] == daily_folder_id_list[i]:
                        dict = {}
                        chunkName = item['title'][11:]
                        dict[chunkName] = item['id']
                        returnList.append(dict)
                cnt += 1
        if cnt == 0:
            print("[SYSTEM] ------------ Shared folder is empty ------------")

    print ("[SYSTEM] Finished get file id and name for UPDATE - '{0}".format(account))
    return returnList


def upload_file(service, folderID, title, description, mime_type, filepath):
    #service = credentials.get_service(account)
    #folderID = get_shared_folder_id(service, account)
    fileIndexOfSlash = filepath.rfind('/')
    fileName = filepath[fileIndexOfSlash+1:]
    #"""

    media_body = MediaFileUpload(filepath, mimetype=mime_type, resumable=True)
    body = {
        'title': title,
        'description': description,
        'mimeType': mime_type,
        "parents": [{
            "kind": "drive#fileLink",
            "id": folderID,        # <<<!!!!이 부분은 public으로 설정한 폴더의 ID를 써줘야한다!!!!>>>
        }]
    }

    try:
        file = service.files().insert( body=body,media_body=media_body).execute()
        #print ("\n[UPLOAD] < {0} > on google drive - '{1}'".format(fileName, account))
        print ("\n[UPLOAD] < {0} > on google drive".format(fileName))
        return file

    except Exception as e:
        print ('[ERROR ] An error occurred: %s' % e)
        print ("         Failed upload file - '{0}'".format(filepath))
        return None
    #"""

    file = {}
    file['id'] = "111"
    file['title'] = fileName
    return file


"""
def print_files_in_account(account):

    service = credentials.get_service(account)
    result = retrieve_all_files(service)

    cnt = 0

    print("\n[SYSTEM] Print all file list - '%s'" % account)
    print ("                File Name             (File ID)")
    print ('         ------------------------------------------------')
    if not result:
        print("[SYSTEM] ------------ Shared folder is empty ------------")
    else:
        for item in result:
            print ('         {0} ({1})'.format(item['title'], item['id']))
            cnt += 1
        if cnt == 0:
            print("[SYSTEM] ------------ Shared folder is empty ------------")
    print ('         ------------------------------------------------\n')

    return result
"""


def print_files_in_shared_folder(account):

    service = credentials.get_service(account)
    results = retrieve_all_files(service)
    folderID = get_shared_folder_id(service, account)
    cnt = 0
    daily_folder_id_list = []

    print("\n[SYSTEM] Print file list - '%s'" % account)
    print ("                File Name             (File ID)")
    print ('         ------------------------------------------------')
    if not results:
        print("[SYSTEM] ------------ Shared folder is empty ------------")
    else:
        for item in results:
            if len(item['parents']) != 0:
                if item['parents'][0]['id'] == folderID:
                    orignItemType = item['mimeType']
                    itemType = orignItemType[len(orignItemType)-6:]
                    if itemType == "folder":
                        daily_folder_id_list.append(item['id'])
                    else:
                        print ('         {0} ({1})'.format(item['title'], item['id']))

                for i in range(0, len(daily_folder_id_list)):
                    if item['parents'][0]['id'] == daily_folder_id_list[i]:
                        print ('         {0} ({1})'.format(item['title'], item['id']))
                cnt += 1
        if cnt == 0:
            print("[SYSTEM] ------------ Shared folder is empty ------------")
    print ('         ------------------------------------------------\n')



def print_files_in_account(account):

    service = credentials.get_service(account)
    results = service.files().list(maxResults=50).execute()
    items = results.get('items', [])
    cnt = 0

    print("\n[SYSTEM] Print all file list - '%s'" % account)
    print ("                File Name             (File ID)")
    print ('         ------------------------------------------------')
    if not items:
        print("[SYSTEM] ------------ Shared folder is empty ------------")
    else:
        for item in items:
            print ('         {0} ({1})'.format(item['title'], item['id']))
            cnt += 1
        if cnt == 0:
            print("[SYSTEM] ------------ Shared folder is empty ------------")
    print ('         ------------------------------------------------\n')
    return items


def print_file_list_of_all_account():
    receivedCredential, accountList = get_credentials_list()
    for i in range(0, len(accountList)):
        print_files_in_shared_folder(accountList[i])



def print_all_file_list_of_all_account():
    receivedCredential, accountList = get_credentials_list()
    for i in range(0, len(accountList)):
        print_files_in_account(accountList[i])



def delete_file(service, file_id):
    try:
        service.files().delete(fileId=file_id).execute()
        print ("[DELETE] Deleted file - {0}".format(file_id))
    except errors.HttpError as error:
        print('[ERROR ] An error occurred: %s' % error)




def delete_all_files_of_all_account():
    receivedCredential, accountList = get_credentials_list()

    for i in range(0, len(accountList)):
        service = credentials.get_service(accountList[i])
        items = get_file_id_in_shared_folder_for_delete(service, accountList[i])
        for item in items:
            delete_file(service, item['id'])
        print("[DELETE] Deleted files in google drive - '%s'\n" % accountList[i])

    if os.path.isfile("metadata.json"):
        os.remove("metadata.json")
        print("[DELETE] Deleted metadata.json")
    else:
        print ("[ERROR ] Doesn't exist metadata.json")


def delete_all_files_of_one_account(account):
    service = credentials.get_service(account)
    items = get_file_id_in_shared_folder_for_delete(service, account)
    for item in items:
        delete_file(service, item['id'])
    print("[DELETE] Deleted files in google drive - '%s'\n" % account)



def downlaod_file(fileName, id1, id2, id3, chunkName):

    url = "https://drive.google.com/uc?export=download&id=" + id1
    indexOfDot = fileName.index('.')
    name = fileName[:indexOfDot]

    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)

        CHUNK = 16 * 1024
        downloadPath = os.getcwd() + "/cache/"
        with open(downloadPath + chunkName, 'wb') as f:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    break
                f.write(chunk)
        log = "download_" + name + '_' + chunkName[5:] + "_origin"
        write_log(log)

        print ("[ DOWN ] Downloaded %s" % chunkName)

    except Exception as e:

        url2 = "https://drive.google.com/uc?export=download&id=" + id2

        try:
            request = urllib.request.Request(url2)
            response = urllib.request.urlopen(request)

            CHUNK = 16 * 1024
            downloadPath = os.getcwd() + "/cache/"
            with open(downloadPath + chunkName, 'wb') as f:
                while True:
                    chunk = response.read(CHUNK)
                    if not chunk:
                        break
                    f.write(chunk)
            log = "download_" + name + '_' + chunkName[5:] + "_replication"
            write_log(log)

            print ("[ DOWN ] Downloaded(replication) %s" % fileName)

        except Exception as e:
            url3 = "https://drive.google.com/uc?export=download&id=" + id3

            try:
                request = urllib.request.Request(url3)
                response = urllib.request.urlopen(request)

                CHUNK = 16 * 1024
                downloadPath = os.getcwd() + "/cache/"
                with open(downloadPath + chunkName, 'wb') as f:
                    while True:
                        chunk = response.read(CHUNK)
                        if not chunk:
                            break
                        f.write(chunk)

                log = "download_" + name + '_' + chunkName[5:] + "_replication"
                write_log(log)

                print ("[ DOWN ] Downloaded(replication) %s" % fileName)

            except Exception as e:
                print ('[ERROR ] An error occurred: %s' % e)


def downlaod_one_file(id, fileName):
    url = "https://drive.google.com/uc?export=download&id=" + id

    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)

        CHUNK = 16 * 1024
        downloadPath = os.getcwd() + "/cache/"
        with open(downloadPath + fileName, 'wb') as f:
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    break
                f.write(chunk)

        print ("[ DOWN ] Downloaded %s" % fileName)

    except Exception as e:
                print ('[ERROR ] An error occurred: %s' % e)





# To delete all file in google drive -> Using children() method
def get_file_id_in_shared_folder_for_delete(service, account):
    #service = credentials.get_service(account)
    folderID = get_shared_folder_id(service, account)

    page_token = None
    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token

            children = service.children().list(folderId=folderID, **param).execute()
            items = children.get('items', [])

            page_token = children.get('nextPageToken')
            if not page_token:
                return items
                break


        except errors.HttpError as error:
            print ('[ERROR ] An error occurred: %s' % error)
            return None
            break



def check_file_id(fileID):

    url = "https://drive.google.com/uc?export=view&id=" + fileID

    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return True

    except Exception as e:
        #print ('[ERROR ] An error occurred: %s' % e)
        return False


def check_capacity_of_google_drive():

    if os.path.isfile("config.json"):
        f = open("config.json", "r")
        readJSON = json.load(f)
        f.close()

        accountList = readJSON[0]['donation']
        total_remain_quota = 0
        total_quota = 0

        while len(accountList) != 0:
            service = credentials.get_service(accountList.pop(0))

            about = service.about().get().execute()
            total_quota_in_drive = int(about['quotaBytesTotal'])
            used_quota  = int(about['quotaBytesUsed'])
            remain_quota = total_quota_in_drive - used_quota
            total_remain_quota += remain_quota
            total_quota += 15

        human_byte = bytes2human(total_remain_quota)

        print("\n[SYSTEM] Total remain quota is {0} / {1}.0 GB)".format(human_byte, total_quota))

    else:
        print ("[ERROR ] Doesn't exist config.json")



"""
Bytes-to-human / human-to-bytes converter.
Based on: http://goo.gl/kTQMs
Working with Python 2.x and 3.x.

Author: Giampaolo Rodola' <g.rodola [AT] gmail [DOT] com>
License: MIT
"""

# see: http://goo.gl/kTQMs
SYMBOLS = {
    'customary'     : ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'),
    'customary_ext' : ('byte', 'kilo', 'mega', 'giga', 'tera', 'peta', 'exa',
                       'zetta', 'iotta'),
    'iec'           : ('Bi', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi'),
    'iec_ext'       : ('byte', 'kibi', 'mebi', 'gibi', 'tebi', 'pebi', 'exbi',
                       'zebi', 'yobi'),
}

def bytes2human(n, format='%(value).1f %(symbol)s', symbols='customary'):
    """
    Convert n bytes into a human readable string based on format.
    symbols can be either "customary", "customary_ext", "iec" or "iec_ext",
    see: http://goo.gl/kTQMs

      >>> bytes2human(0)
      '0.0 B'
      >>> bytes2human(0.9)
      '0.0 B'
      >>> bytes2human(1)
      '1.0 B'
      >>> bytes2human(1.9)
      '1.0 B'
      >>> bytes2human(1024)
      '1.0 K'
      >>> bytes2human(1048576)
      '1.0 M'
      >>> bytes2human(1099511627776127398123789121)
      '909.5 Y'

      >>> bytes2human(9856, symbols="customary")
      '9.6 K'
      >>> bytes2human(9856, symbols="customary_ext")
      '9.6 kilo'
      >>> bytes2human(9856, symbols="iec")
      '9.6 Ki'
      >>> bytes2human(9856, symbols="iec_ext")
      '9.6 kibi'

      >>> bytes2human(10000, "%(value).1f %(symbol)s/sec")
      '9.8 K/sec'

      >>> # precision can be adjusted by playing with %f operator
      >>> bytes2human(10000, format="%(value).5f %(symbol)s")
      '9.76562 K'
    """
    n = int(n)
    if n < 0:
        raise ValueError("n < 0")
    symbols = SYMBOLS[symbols]
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i+1)*10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return format % locals()
    return format % dict(symbol=symbols[0], value=n)

def human2bytes(s):
    """
    Attempts to guess the string format based on default symbols
    set and return the corresponding bytes as an integer.
    When unable to recognize the format ValueError is raised.

      >>> human2bytes('0 B')
      0
      >>> human2bytes('1 K')
      1024
      >>> human2bytes('1 M')
      1048576
      >>> human2bytes('1 Gi')
      1073741824
      >>> human2bytes('1 tera')
      1099511627776

      >>> human2bytes('0.5kilo')
      512
      >>> human2bytes('0.1  byte')
      0
      >>> human2bytes('1 k')  # k is an alias for K
      1024
      >>> human2bytes('12 foo')
      Traceback (most recent call last):
          ...
      ValueError: can't interpret '12 foo'
    """
    init = s
    num = ""
    while s and s[0:1].isdigit() or s[0:1] == '.':
        num += s[0]
        s = s[1:]
    num = float(num)
    letter = s.strip()
    for name, sset in SYMBOLS.items():
        if letter in sset:
            break
    else:
        if letter == 'k':
            # treat 'k' as an alias for 'K' as per: http://goo.gl/kTQMs
            sset = SYMBOLS['customary']
            letter = letter.upper()
        else:
            raise ValueError("can't interpret %r" % init)
    prefix = {sset[0]:1}
    for i, s in enumerate(sset[1:]):
        prefix[s] = 1 << (i+1)*10
    return int(num * prefix[letter])



"""
# Using list() method
def get_file_id_in_shared_folder(service, account):

    results = service.files().list(maxResults=15).execute()
    items = results.get('items', [])
    folderID = get_shared_folder_id(service, account)
    cnt = 0
    idList = []

    if not items:
        print("[SYSTEM] ------------ Shared folder is empty ------------")
    else:
        for item in items:
            if len(item['parents']) != 0:
                if item['parents'][0]['id'] == folderID:
                    idList.append(item['id'])
                    cnt += 1
        if cnt == 0:
            print("[SYSTEM] ------------ Shared folder is empty ------------")
    return idList
"""



"""
def print_files_in_shared_folder_older_version(account):
    service = credentials.get_service(account)
    folderID = get_shared_folder_id(service, account)

    page_token = None
    while True:
        try:
            param = {}
            if page_token:
                param['pageToken'] = page_token

            children = service.children().list(folderId=folderID, **param).execute()

            print ("\n[SYSTEM] Print file list - '%s'" % account)
            print ("                File Name             (File ID)")
            print ('         ------------------------------------------------')
            for child in children.get('items', []):
                file_id = child['id']
                try:
                    file = service.files().get(fileId=file_id).execute()
                    print ('         {0} ({1})'.format(file['title'], file_id))
                    #print ('File Id: %s' % child['id'])
                except errors.HttpError as error:
                    print ('[ERROR ] An error occurred: %s' % error)

            if len(children['items']) == 0:
                print("[SYSTEM] ------------ Shared folder is empty ------------")
            print ('         ------------------------------------------------\n')

            page_token = children.get('nextPageToken')
            if not page_token:
                break

        except errors.HttpError as error:
            print ('[ERROR ] An error occurred: %s' % error)
            return None
            break

"""

"""
def delete_all_files(account, max=10):

    service = credentials.get_service(account)
    results = service.files().list(maxResults=max).execute()
    items = results.get('items', [])

    if not items:
        print('[ERROR ] No files found.')
    else:
        for item in items:
            try:
                service.files().delete(fileId=item['id']).execute()
                print("[DELETE] Deleted all of file in google drive - '%s'" % account)
            except errors.HttpError as error:
                print('[ERROR ] An error occurred: %s' % error)
"""