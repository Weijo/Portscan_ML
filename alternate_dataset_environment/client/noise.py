import requests, random, time 
from ftplib import FTP

PROXY = False

if PROXY:
    proxies = {
        'http': 'http://localhost:8080',
        'https': 'https://localhost:8080'
    }
else:
    proxies = {}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate"
}

def browse_page(target):
    URL = f"http://{target}/"
    requests.get(URL, headers=headers, proxies=proxies)
    print("Browsing web")

def do_ftp(target):
    print("Browsing FTP")
    ftp = FTP(target)
    ftp.login()
    ftp.dir()
    time.sleep(5)
    ftp.quit()
    ftp.close()
    print("Exited FTP")

if __name__ == "__main__":
    TARGET = "server"

    while True:
        try:
            time.sleep(random.randint(3, 10))
            browse_page(TARGET)
            time.sleep(random.randint(3, 10))
            do_ftp(TARGET)
        except:
            pass