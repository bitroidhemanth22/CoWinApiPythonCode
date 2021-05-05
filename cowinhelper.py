import requests
import json
from tabulate import tabulate
from datetime import datetime

currentday = datetime.now()

currentdaytime = currentday.strftime("%d-%m-%Y")

pincodes = "560036"

paramsoption = {'pincode':pincodes,'date':currentdaytime}

urlhits = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

response = requests.get(urlhits,params=paramsoption)

helperjson = json.loads(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

sotrjson = json.dumps(response.json(),sort_keys=True, indent=4)

print(sotrjson)

for centerlist in helperjson["centers"]:
 #   print(centerlist)
    pname = centerlist['name']
    paddress = centerlist['address']
    pblockname = centerlist['block_name']
    pcenterid = centerlist['center_id']
    pdistrict = centerlist['district_name']
    ppincode = centerlist['pincode']
    for dos in centerlist['sessions']:
        pavailable_capacity = dos['available_capacity']
        pdate = dos['date']
        pmin_age_limit = dos['min_age_limit']
        pslot = dos['slots']
        pvaccine = dos['vaccine']
        
table = [(pname,'|',paddress,'|',pblockname,'|',pcenterid,'|',pdistrict,'|',ppincode,'|',pdate,'|',pavailable_capacity,'|',pmin_age_limit,'|',pvaccine)]

print(tabulate(sorted(table),tablefmt="grid"))
