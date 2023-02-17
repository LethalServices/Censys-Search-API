import requests, base64, os, json
from datetime import datetime
from colorama import Fore

def SendLog(text):
    print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] {text}')  

def get_config_data():
    if os.path.isfile('Authorization.json'):
        with open('Authorization.json', 'r') as f:
            Config = json.load(f)
            SendLog(f'Config Loaded!')
            return Config
    else:
        SendLog("Missing Config, Please Make Sure A Config Is With-in The Directory!")
        exit()

def search(): 
    Config = get_config_data()
    if Config["API_ID"] == "0" or Config["API_KEY"] == "0":
        SendLog("Missing Config Parameter.")
    else:
        domain = input("URL: ")
        #Censys Auth Headers
        Auth_Data = f'{Config["API_ID"]}:{Config["API_KEY"]}'
        AuthToken = {"Authorization": f"Basic {base64.b64encode(Auth_Data.encode('ascii')).decode('ascii')}"}

        with requests.get(f'https://search.censys.io/api/v2/hosts/search?q={domain}', headers=AuthToken) as r:
            if r.status_code == 200:
                with open(f"{domain}.json", "wb") as report:
                    report.write(r.content)
                    SendLog(f"Report Saved To {os.getcwd()}\\{domain}.json.")
            elif r.status_code == 400:
                SendLog("Bad Request: The request you made is invalid.")
            elif r.status_code == 401:
                SendLog("Unauthorized: You must authenticate with a valid API ID and API KEY.")           
            elif r.status_code == 422:
                SendLog("Invalid cursor: Remove The https://.")
            elif r.status_code == 429:  
                SendLog("Too many requests: Please wait abit before resending the request.")
                              
def main():
    search()

if __name__ == "__main__":
	main()
        
