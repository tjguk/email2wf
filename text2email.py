import os, sys
import configparser
import getpass
import xmlrpc.client

#
# Expects an ini file which looks like this:
# [setup]
# username=xxx
# password=yyy
# server=zzz
#

def create_email(username, password, wfserver, email_alias, filepath="emails.txt"):
    with open(filepath) as f:
        emails = f.read().split()
    server = xmlrpc.client.ServerProxy("https://api.webfaction.com/")
    session_id, account = server.login(username, password, wfserver, 2)
    existing_emails = dict((e['email_address'], e) for e in server.list_emails(session_id))
    if email_alias in existing_emails:
        server.delete_email(session_id, email_alias)
    server.create_email(session_id, email_alias, ", ".join(emails))

def main(ini_filepath="text2email.ini", filepath="emails.txt"):
    ini = configparser.ConfigParser()
    ini.read(ini_filepath)
    setup = ini['setup']
    username = setup['username']
    password = setup['password']
    server = setup['server']
    email_alias = setup['email_alias']
    return create_email(username, password, server, email_alias, filepath)

if __name__ == '__main__':
    main(*sys.argv[1:])
