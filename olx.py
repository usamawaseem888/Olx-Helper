from bs4 import BeautifulSoup
import requests

tm=requests.get('https://www.olx.com.pk/lahore_g4060673/honda-cars_c84?page=10&filter=make_eq_cars-honda%2Cmileage_between_1_to_999999%2Cyear_between_2020_to_2022').text
#print(tm)]\

soup=BeautifulSoup(tm,'lxml')
t=soup.find_all('li',class_='c46f3bfe')
with open('text.txt','w') as f:
 for a in t:
    ad_title=a.find('div',class_='_41d2b9f3')
    site=ad_title.find('a',href=True)
    price=ad_title.span.extract().text
    model_year=a.find('span' ,class_='fef55ec1')
    mileage=model_year.span.extract().text
    location=a.find('span',class_='_424bf2a8').text
    ad_posted=a.find('span',class_='_2e28a695').text
    cite='www.olx.com.pk'+site['href']

    f.write(f'''Ad title: {ad_title.text.strip()}
    Price: {price.strip()}
    Model Year: {model_year.text.strip()}
    Mileage: {mileage.strip()}
    location: {location.strip()}
    Date of Ad posted: {ad_posted.strip()}
    Website : {cite}
    
 ''')
    #a5112ca8