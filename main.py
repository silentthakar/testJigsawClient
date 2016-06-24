#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: utf-8 -*-

# Set global executable instruction
# chmod 744 __init__.py
# ln -s "/Users/yeonhong/Downloads/jigsaw_client/main.py" /usr/local/bin/jigsaw


import googleDrive
import file
import sys
import argparse
import credentials

def main(argv):

    parser = argparse.ArgumentParser(
        prog='jigsaw',
        description='''
commands:
         [ -h ]                          Show Usage.
         [ -ls ]                         Print shared file list.
         [ -df ]                         Print used quota of google drive.
         [ -check ]                      Check metadata is correct or not.
         [ -put <file name> ]            Upload file on google drive.
         [ -get <file name> ]            Download file on google drive.
         [ -rm <file name> ]             Delete file on google drive.
         [ -enrol <account name> ]       Get permission to get credential.
         [ -vk <account name> ]          Revoke credential''',

        formatter_class=argparse.RawDescriptionHelpFormatter)

    #parser.add_argument('-l', "--list_id", nargs="+") -> use args list
    parser.add_argument("-ls", action='store_true')
    parser.add_argument("-df", action='store_true')
    parser.add_argument("-r", action='store_true')
    parser.add_argument("-l", action='store_true')
    parser.add_argument("-check", action='store_true')
    parser.add_argument("-put", "--upload_file")
    parser.add_argument("-get", "--download_file")
    parser.add_argument("-rm", "--delete_file")
    parser.add_argument("-la", "--file_list_of_id")
    parser.add_argument("-enrol", "--enrol_id")
    parser.add_argument("-ra", "--remove_file_of_id")
    parser.add_argument("-vk", "--revoke_account")

    #parser.parse_args('-h'.split())R
    args = parser.parse_args()

    #print (args)

    if args.ls:
        file.printFileList()

    elif args.df:
        googleDrive.check_capacity_of_google_drive()

    elif args.r:
        googleDrive.delete_all_files_of_all_account()

    elif args.l:
        googleDrive.print_all_file_list_of_all_account()

    elif args.check:
        file.checkFileID()

    # Upload command
    elif args.upload_file:
        file.uploadFile(args.upload_file)

    # Download command
    elif args.download_file:

        if args.download_file.rfind('/') < 10:
            file.downloadFile(args.download_file)
        else:
            file.downloadFileByString(args.download_file)

    elif args.delete_file:
        file.deleteFile(args.delete_file)

    # List - Print file list in google drive
    elif args.file_list_of_id:
        googleDrive.print_files_in_shared_folder(args.file_list_of_id)

    elif args.remove_file_of_id:
        googleDrive.delete_all_files_of_one_account(args.remove_file_of_id)

    elif args.enrol_id:
        indexOfAt = args.enrol_id.index('@')
        id = args.enrol_id[:indexOfAt]
        googleDrive.donate_id(id)

    elif args.revoke_account:
        indexOfAt = args.revoke_account.index('@')
        id = args.revoke_account[:indexOfAt]
        googleDrive.revoke_credentials(id)

    """
    googleDrive.donate_id("silencenoeul")
    googleDrive.donate_id("silenceachim")
    googleDrive.donate_id("silencesoop")

    googleDrive.donate_id("silencebada")
    googleDrive.donate_id("silencedeul")
    googleDrive.donate_id("silencemool")

    googleDrive.donate_id("silencebyul")
    googleDrive.donate_id("silencebaram")
    googleDrive.donate_id("silencebool")

    googleDrive.donate_id("silencepado")
    googleDrive.donate_id("silencemorae")
    googleDrive.donate_id("silencebool")
    """

    #googleDrive.check_capacity_of_google_drive()

    # Print credential list
    #googleDrive.get_credentials_list()
    #credentials.get_credentials_by_id("silencedeul")

    # Upload file by name
    #file.uploadFile("Raspberrypi-Connect.m4v")
    #file.uploadFile("MGMG.mp4")
    #file.uploadFile("cafebene.png")
    #file.uploadFile("cloud.m4v")

    # Delete all
    #googleDrive.delete_all_files_of_all_account()

    # delete file by name
    #file.deleteFile("MGMG.mp4")
    #file.deleteFile("cafebene.png")
    #file.deleteFile("connect.m4v")

    # Delete one account
    #googleDrive.delete_all_files_of_one_account("silencenamu")

    # Print file list in shared folder
    #googleDrive.print_file_list_of_all_account()

    # Print all file list in google drive
    #googleDrive.print_all_file_list_of_all_account()

    # Print to download
    #file.printFileList()

    # Download by string
    #file.downloadFileByString("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")
    #file.downloadFileByString("eNpdlM2WojAQhZ9oZgJI2y5lDNCMBMkvZtOHgNNoALHlCPL0Qzubjut77v2qKlUpzm17KPqfzeL2C3jjDljeJRuuPVVg/FMKHKLGDQWEs2i9He3k4wc76yGmfC9tvNmL/g+mH7MI+GFoSbt9IUvGLLlnXYZPqJdBbDqV8CNu4eEAyw5rZjK5QP2hxpoEpU1raMbyLNJKA5eJ6I3Q1BTjZmbNOWiqcK6BGZsI6WMHLiRcsTgszIIKm0eFEzuyqW/M+ar2PUpsPkB3fZtYWPHEr+/JpkbbR5/LwlK7vXKPb5bg1YWLLiZBBRT8YgLk3yk52IGvWOtVKKy3SkSMP4bwzYnDahQB5rTtqApeTaZg/KjmbOV7EwfMjKX63BP/7CRC29y+mmLho03meHXsdHEJ2RNTw4nzCKXNMLBTajLVqZpyK7Upu7o5fzDd5V+9sGP9HiunDkijnS1DDfe/XuVV3QsCelmdlzj8mIomtZWNcvYY/MJbTPf3T51ky3ySHcmqS9qWl1K8mk6pK1HyDiRZyco2Npmplq3YVGPCV2/JY3zfYimNxszSVp51n8qCpnjg3lU10GIWHCV8aoVn5ZYyq5Z6dZEAmAWVlo8JRAFhbhA/VtM9dn178+jRJaiOfivogy1bTP+378d5Z93t/PQ6Kcy6nDpyd2isgZzWs/iyR/f12i3bESY06gVbkX3bEcGh6VQMj0Sgq9h4+d4pTCZnvrsH5UVBeVNZbMbmerWZxb9xvRr/L/U3sdzUL0rzG826++Exvm+xpZYDZ+gS06qSDJgFMeCjlFcoD8rPQmvzkIjGm3njo7xGu6J5umzu6wWZPKbovL/w6XgJjW3UoEkEPMdT+uRkw3RoZYSs+jNuCpNZhlGPbOs3thHci8KMzSxfigZXtE5HybUpUoglEeDO2ODG4Omr2WbdJFqUJeHcr3hqpcx8mYTr+/z3XYko/gFcXacK")

    #file.checkFileID()

    #googleDrive.get_log(0)

    #googleDrive.revoke_credentials("silencethakar")

    #credentials.get_credentials_by_id("silencedeul")

    #print (googleDrive.get_group_name_of_credential("silencenamu"))

    #googleDrive.get_file_id_and_name_in_shared_folder("silencebool")

    #credentials.get_credentials_by_id("silencenamu")

if __name__ == '__main__':
    main(sys.argv)

