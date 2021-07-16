import requests
import json
from tabulate import tabulate
from datetime import datetime

def printResult(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    #print("Headers: ---------------")
    #print(resData.headers)
    #print("\n")

    #print("Returned data: ---------------")
    #print(resData.content)

currentday = datetime.now()

currentdaytime = currentday.strftime("%d-%m-%Y")

pincodes = "560066"

paramsoption = {'pincode':pincodes,'date':currentdaytime}

urlhits = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

response = requests.get(urlhits,params=paramsoption)

printResult(response)

helperjson = response.json()

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

sotrjson = json.dumps(response.json(),sort_keys=True, indent=4)

#print(sotrjson)


for centerlist in helperjson["centers"]:
 #   print(centerlist)
    pname = centerlist['name']
    paddress = centerlist['address']
    pblockname = centerlist['block_name']
    pcenterid = centerlist['center_id']
    pdistrict = centerlist['district_name']
    ppincode = centerlist['pincode']
    pfee = centerlist['fee_type']
    for dos in centerlist['sessions']:
        pavailable_capacity = dos['available_capacity']
        pdate = dos['date']
        pmin_age_limit = dos['min_age_limit']
        pslot = dos['slots']
        pvaccine = dos['vaccine']
        #print(pname,paddress,pblockname,pdistrict,ppincode,pdate,pavailable_capacity,pmin_age_limit,pvaccine)
        CENTERID = 'Center ID'
        NAME = 'Name'
        ADDRESS = 'Address'
        BLOCKNAME = 'Block Name'
        DISTRICT = 'District'
        PINCODE = 'Pincode'
        Fee= 'Fee Type'
        DATE = 'date'
        AVAILABLE_CAPACITY = 'Available Capacity'
        MIMIMUM_AGE_LIMIT = 'Minimum Age Limit'
        VACCINE = 'Vaccine'

        table = [[CENTERID,NAME,ADDRESS,BLOCKNAME,DISTRICT,PINCODE,DATE,pdate,AVAILABLE_CAPACITY,MIMIMUM_AGE_LIMIT,VACCINE],[pcenterid,pname,paddress,pblockname,pdistrict,ppincode,pfee,pdate,pavailable_capacity,pmin_age_limit,pvaccine]]
        fileoutlist = (tabulate(table,headers="firstrow",tablefmt="grid"))
        fileouthtml = (tabulate(table,headers="firstrow",tablefmt="html"))
        #finaltablehtml=(tabulate(table, headers="firstrow", tablefmt="html"))
        #finaltabletext=(tabulate(table, headers="firstrow", tablefmt="grid"))
        #print(finaltabletext);

        #filelisten = [finaltablehtml,finaltabletext]
        filelisten = [fileouthtml,fileoutlist]

        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        port = 1025
        sender_email = 'localhost'
        receiver_email = ['localhost','localhost']
        reply_to_email = 'localhost'
        carbonc_copy_email = 'localhost'

        message = MIMEMultipart("alternative")

        message["Subject"] = "Test Mail"
        message["From"] = sender_email
        message["To"] = ",".join(receiver_email)
        message["Cc"] = ",".join(carbonc_copy_email)
        message["Reply-to"] = reply_to_email

        text = f"""
        Hello team,

        Please find data below.

        {filelisten[1]}

        Regards,
        Hemanth.
        """

        html = f"""
        <html>
        <head>
        <style>
        table, th, td {{ border: 1px solid black; border-collapse: collapse; }}
        th, td {{ padding: 5px; }}
        </style>
        </head>
        <body>
        <p>Hello team,</p>
        <p>Please find html data below.</p>

        {filelisten[0]}

        <p>Regards,</p>
        <p>Hemanth.</p>
        </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "plain")
        message.attach(part1)
        message.attach(part2)

        with smtplib.SMTP("0.0.0.0", port) as server:
            server.sendmail(
                sender_email,receiver_email,message.as_string()
                )

            print('\n')
            print('Mail Sent Successfully')
