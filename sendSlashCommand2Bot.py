import requests
from dotenv import load_dotenv
import os

load_dotenv()

DCCID = os.getenv("DCCID")
DCT = os.getenv("DCT")
DI = os.getenv("DI")

headers = {
    'accept': '*/*',
    'accept-language': 'cs-CZ,cs;q=0.9',
    'authorization': DCT,
    'cache-control': 'no-cache',
    'origin': 'https://discord.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': f'https://discord.com/channels/@me/{DCCID}',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'cs',
    'x-discord-timezone': 'Europe/Prague',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImNzLUNaIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vY2hhbm5lbHMvQG1lLzEyMzU5MjM1MTEyMTA0MTQwOTAiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJkaXNjb3JkLmNvbSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI5MDk5OCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
}

files = {
    'payload_json': (None, '{"type":2,"application_id":"832509655459561482","channel_id":"' + DCCID +'","session_id":"41ff30eb8ece2c0b464c5003ca6fcecf","data":{"version":"1226892554084286475","id":"1226892554084286474","name":"renew","type":1,"options":[{"type":4,"name":"id","value": '+ DI +'}],"application_command":{"id":"1226892554084286474","type":1,"application_id":"832509655459561482","version":"1226892554084286475","name":"renew","description":"Renew vps","options":[{"type":4,"name":"id","description":"VPS your ID","required":true,"description_localized":"VPS your ID","name_localized":"id"}],"dm_permission":true,"integration_types":[0],"global_popularity_rank":4,"description_localized":"Renew vps","name_localized":"renew"},"attachments":[]},"nonce":"","analytics_location":"slash_ui"}'),
}

response = requests.post('https://discord.com/api/v9/interactions', headers=headers, files=files)

print(response.text)
print(response.status_code)
