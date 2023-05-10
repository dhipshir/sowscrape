import getpass, imaplib
import email, os, sys, re
import streamlit as st
#import BeautifulSoup
  
#<instant-updates@mail.zillow.com>

#was required to generate this app specific password to use with gmail IMAP
#Gmail 2-step verification -> bottom of page: App passwords
with imaplib.IMAP4_SSL(host="imap.gmail.com", port=993) as imap_ssl:
    print("Connection Object : {}".format(imap_ssl))

    ############### Login to Mailbox ######################
    print("Logging into mailbox...")
    resp_code, response = imap_ssl.login(st.secrets["log"], st.secrets["pw"])
  
    print("Response Code : {}".format(resp_code))
    print("Response      : {}\n".format(response[0].decode()))

    ############### Set Mailbox #############
    resp_code, mail_count = imap_ssl.select(mailbox="INBOX", readonly=True)

    ############### Search mails in a given Directory #############   
    resp_code, mails = imap_ssl.search(None, '(FROM "zillow")')

    mail_ids = mails[0].decode().split()

    print("Total Mail IDs : {}\n".format(len(mail_ids)))

    for mail_id in mail_ids[-2:]:
        print("================== Start of Mail [{}] ====================".format(mail_id))

        resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)') ## Fetch mail data.

        
        message = email.message_from_bytes(mail_data[0][1]) ## Construct Message from mail data
        print("Subject    : {}".format(message.get("Subject")))
        for part in message.walk():
            print("CONTENT TYPE: " + part.get_content_type())
        #message.get_body()



        print("================== End of Mail [{}] ====================\n".format(mail_id))

        '''
        print("From       : {}".format(message.get("From")))
        print("To         : {}".format(message.get("To")))
        print("Bcc        : {}".format(message.get("Bcc")))
        print("Date       : {}".format(message.get("Date")))
        print("Subject    : {}".format(message.get("Subject")))

        print("Body : ")
        for part in message.walk():
            print("Content type: " + part.get_content_type())
            if part.get_content_type() == "text/plain": ## Only Printing Text of mail. It can have attachements
                body_lines = part.as_string().split("\n")
                print("\n".join(body_lines[:len(body_lines)])) ### Print full message
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #print("================== End of Mail [{}] ====================\n".format(mail_id))
        '''
#imap_ssl.close()
#imap_ssl.logout()
#function stubs
#getzlink()
#   from scrapy.linkextractors import LinkExtractor
#getdetails()
#   3br 2ba 1000 sqft 123 address st
#getagentcontact()
#   <p data-testid="attribution-LISTING_AGENT" class="Text-c11n-8-84-0__sc-aiai24-0 qxgaF"><span class="Text-c11n-8-84-0__sc-aiai24-0 qxgaF">MISSY KAMPMEYER</span> <span class="Text-c11n-8-84-0__sc-aiai24-0 qxgaF">904-610-9217</span></p>
#   <p data-testid="attribution-BROKER" class="Text-c11n-8-84-0__sc-aiai24-0 qxgaF"><span class="Text-c11n-8-84-0__sc-aiai24-0 qxgaF">COMPASS FLORIDA LLC</span></p>




