
import httplib2
import os
from apiclient import discovery
from oauth2client import client, file, tools
import oauth2client

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES              = ['https://www.googleapis.com/auth/drive',
                       'https://www.googleapis.com/auth/drive.file',
                       'https://www.googleapis.com/auth/drive.appdata',
                       'https://www.googleapis.com/auth/drive.apps.readonly',
                       'https://www.googleapis.com/auth/drive.metadata.readonly'
                      ]
APPLICATION_NAME    = 'GOOGLE DRIVE API TEST APP'



def get_service(account):
    credentials = get_credentials(account)
    print ("[SYSTEM] Get a crendetial - %s" % account)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v2', http=http)
    print ("[SYSTEM] Get a Service object - %s" % account)
    return service

def get_credentials(account):
    home_dir = os.path.expanduser(os.getcwd() + "/credential")
    credential_dir = os.path.join(home_dir, account)
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)

    fileName = 'google_oauth_credential.json'
    credential_path = os.path.join(credential_dir, fileName)

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:

        flow = client.flow_from_clientsecrets("credential/" + account + "/client_secret.json", SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)

    return credentials



"""
import httplib2
from apiclient import discovery
import oauth2client
import requests
import os
import sys
import googleDrive



def get_service(account):
    credentials = get_credentials_by_id(account)
    print ("[SYSTEM] Get a crendetial - %s" % account)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v2', http=http)
    print ("[SYSTEM] Get a Service object - %s" % account)
    return service


def get_credentials_by_id(id):

    url = "https://seoyujin.github.io/"
    r = requests.get(url)
    address = r.text.strip()

    server_address = address + "/credentials"
    data = {'id':id}
    r = requests.post(server_address, data)

    credential_dir = os.path.expanduser(os.getcwd() + "/credential")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_name = id + "_credential.json"
    credential_path = os.path.join(credential_dir, credential_name)

    strJSON = r.text
    indexOfSF = strJSON.find("jigsaw_folder_id")
    if indexOfSF != -1:
        strSF = strJSON[indexOfSF+20:]
        endOfSF = strSF.find('"')

        frontJSON = strJSON[:indexOfSF-3]
        endJSON = strJSON[indexOfSF+endOfSF+21:]
        jsonText = frontJSON + endJSON

    else:
        jsonText = r.text

    # Create credential.json
    f = open("./credential/"+credential_name, 'w')
    f.write(jsonText)
    f.close()

    # read credential to get store!
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    # Delete already read credential filer
    os.remove(credential_path)

    if not credentials or credentials.invalid:
        print ("[ERROR ] That credential is wrong file, Please get credential again")
        #googleDrive.donate_id(id)

    return credentials

"""






"""
def get_credentials(account):
    # Set path to write credential json
    credential_dir = os.path.expanduser(os.getcwd() + "/credential")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)

    cnt = 0

    r = requests.get("http://1.234.65.53:9991/credentials")
    jsonText = r.text

    list = r.text.split('\n')

    for idx in range(0, len(list)-1):

        if (idx % 2) == 0:
            strAccount = list[idx]
            indexOfUnder = strAccount.index('_')
            indexOfDot = strAccount.index('.')
            accountName = strAccount[indexOfUnder+1:indexOfDot]

            if accountName == account:
                credential_name = account + "_credential.json"
                strJSON = list[idx+1]

                indexOfSF = strJSON.find("jigsaw_folder_id")
                strSF = strJSON[indexOfSF+20:]
                endOfSF = strSF.find('"')

                frontJSON = strJSON[:indexOfSF-3]
                endJSON = strJSON[indexOfSF+endOfSF+21:]
                jsonText = frontJSON + endJSON
                break
            else:
                cnt += 1

    if cnt == (len(list)-1) / 2:
        print ("[ERROR ] Input the wrong account name")
        sys.exit(0)

    # Create credential.json
    f = open("./credential/"+credential_name, 'w')
    f.write(jsonText)
    f.close()

    credential_path = os.path.join(credential_dir, credential_name)

    # read credential to get store!
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    # Delete already read credential filer
    if os.path.isfile(credential_path):
        os.remove(credential_path)

    #googleDrive.revoke_credentials(account)

    if not credentials or credentials.invalid:
        print ("[ERROR ] That credential is wrong file, Please get credential again")
        googleDrive.donate_id(account)

    return credentials
"""
