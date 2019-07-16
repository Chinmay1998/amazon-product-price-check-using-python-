import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL='https://www.amazon.in/Apple-MR972HN-15-4-inch-i7-8850H-Integrated/dp/B07G49GQ56/ref=sr_1_4?keywords=macbook+pro&qid=1562967733&s=gateway&sr=8-4'
headers ={"User agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}


def send_mail():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('emailid', 'password')
    subject='Price of ur mac fell down below 2.5 lakh!!'
    body= 'link :  https://www.amazon.in/Apple-MR972HN-15-4-inch-i7-8850H-Integrated/dp/B07G49GQ56/ref=sr_1_4?keywords=macbook+pro&qid=1562967733&s=gateway&sr=8-4'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'use your mail@gmail.com',
        'toaddress@gmail.com',
        msg
    )
    print("email sent")
    server.quit()

def check_price():
    page= requests.get(URL, headers=headers)
    
    soup= BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    print(title.strip())
    price=soup.find(id="priceblock_ourprice").get_text()
    price.strip()
    
    res = [int(i) for i in price if i.isdigit()]
    res1=res[0:6]
    # Converting integer list to string list
    s = [str(i) for i in res1]
    
    # Join list items using join()
    conv_price = int("".join(s))
    
    #conversion successful
    float(conv_price)
    print(conv_price)
    
    
    #logic starts here
    
    if(conv_price <250000):
        send_mail()
    else:
        print('price dint fall below 2.5 lakh')

while True:
    check_price()
    time.sleep(2)
