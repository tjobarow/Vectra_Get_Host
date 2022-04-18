import requests, urllib.parse, os, json, urllib3
urllib3.disable_warnings()

# If you do not use linux or mac, you can just set this variable equal to the API key. This is NOT RECOMMENDED though. 
API_KEY=os.getenv('VECTRA_KEY')

###############################
# Get hostname
###############################

hostname = input("Enter hostname without domain (i.e laptop, not laptop.example.com):")
domain = input("Enter domain (i.e example.com):")

hostname_fqdn = hostname+"."+domain

################################
# MAKE REQUESTS
################################

def lookup(hostname):
    print(f"Trying to lookup via {hostname}...")
    
    hostname_encoded = urllib.parse.quote(f"host.name:\"{hostname}\"")

    VECTRA_BASE_URL=os.getenv('VECTRA_URL')

    API_ENDPOINT = "/api/v2.2/search/hosts/"

    PARAMS = f"?query_string={hostname_encoded}"

    FULL_URL = VECTRA_BASE_URL+API_ENDPOINT+PARAMS

    HEADERS = {
            'Authorization':f'Token {API_KEY}',
            'Accept':'application/json',
            'Content-Type':'application/json'
            }

    response_hostname =  requests.get(url=FULL_URL,headers=HEADERS,verify=False)

    #print(json.dumps(response_hostname.json(),indent=4))

    if response_hostname.json()['count'] == 0:
        print("No results found...")
    else:
        #print(json.dumps(response_hostname.json(),indent=4))
        for result in response_hostname.json()['results']:
            print(f"Vectra believes the probably owner for {result['name']} is {result['probable_owner']}") 

lookup(hostname)
lookup(hostname_fqdn)
