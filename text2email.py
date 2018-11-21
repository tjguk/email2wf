import os, sys
import getpass
import xmlrpc.client

password = None
def main(password, filepath="emails.txt", email_alias="parents@kelston.org.uk"):
    with open(filepath) as f:
        emails = f.read().split()
    server = xmlrpc.client.ServerProxy("https://api.webfaction.com/")
    session_id, account = server.login('tgolden', password, 'Web630', 2)
    server.delete_email(session_id, email_alias)
    server.create_email(session_id, email_alias, ", ".join(emails))

if __name__ == '__main__':
    password = password or input("Password: ")
    main(password, *sys.argv[1:])
