import requests
from bs4 import BeautifulSoup



URL = "https://www.maseno.ac.ke/index/"
page = requests.get(URL)

if (page.status_code != 200):
    print(page.status_code)
else:
    print(page.status_code)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="ja-right")
    print(results.prettify())


    

   