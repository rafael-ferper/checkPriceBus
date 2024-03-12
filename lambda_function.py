import os
import requests
from bs4 import BeautifulSoup
import smtplib

def lambda_handler(event, context):
    check_price()

def check_price():
    URL = 'https://www.clickbus.com.br/onibus/itajuba-mg/campinas-sp-todos?departureDate=2024-03-17'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(URL, headers=headers)
    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    price = soup.find('span', {'class': 'c-bPzyLQ price-value'}).get('content')
    print(price)
    converted_price = float(price)

    if converted_price < 125.1:
        send_mail()

    print(converted_price)

    if converted_price > 125.1:
        send_mail()

def send_mail():
    user = os.getenv('USER')
    password = os.getenv('PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(user, password)

    subject = 'O preço caiu!'
    body = 'Confira o link https://www.clickbus.com.br/onibus/itajuba-mg/campinas-sp-todos?departureDate=2024-03-17'

    msg = f"Subject: {subject}\n\n{body}"
    msg = msg.encode('utf-8')

    server.sendmail(
        user,
        user,
        msg
    )
    print('E-mail enviado!')

    server.quit()
