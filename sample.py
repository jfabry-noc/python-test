import json
import requests

def main():
    ip_request = requests.get("https://ip.borked.sh")
    if ip_request.status_code == 200:
        ip_dict = json.loads(ip_request.content)
        print(ip_dict.get('ip'))
    else:
        print(f"Error: Response code: {ip_request.status_code}")

if __name__ == "__main__":
    try:
        main()
    except Exception (e):
        print(e)
