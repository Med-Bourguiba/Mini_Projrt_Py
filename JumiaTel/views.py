from urllib.parse import urljoin
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from .models import Smartphone



def jumiaData(request):
    data_list = []
    for page in range(1, 14):
        url = 'https://www.jumia.com.tn/mlp-telephone-tablette/smartphones/?page=' + \
            str(page)+'#catalog-listing'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        Articles = soup.find_all(
            'article', {'class': 'prd _fb col c-prd'})

        for item in Articles:
            brand = item.find('a', {'class': 'core'}).get('data-brand')
            name=  item.find('h3', {'class': 'name'}).text,
            price=  item.find('div', {'class': 'prc'}).text.strip().replace(',','').replace('TND','')
            image= item.find('img', {'class': 'img'}).get('data-src')
            print(image),
            l =  urljoin('https://www.jumia.com.tn/',item.find('a', {'class': 'core'}).get('href'))
            
            s = Smartphone(brand= brand,name =name, price= price, image= image, lien= urljoin('https://www.jumia.com.tn/',l))
            s.save()
            data_list.append(s)

    # Get filter criteria from user input
    brand = request.GET.get('brand', None)
    max_price = request.GET.get('max_price', None)

    # Filter smartphones based on brand and max price
    data_list = filter_smartphones(data_list, brand, max_price)
    
    context = {'smartphones': data_list}
    return render(request, 'jumiaData.html', context)




def detail(request, id):
    smartphone = Smartphone.objects.get(id=id)
    context = {'smartphone': smartphone}
    return render(request, 'detail.html', context)


def filter_smartphones(data_list, brand=None, max_price=None):
    # Filter based on brand if provided
    if brand:
        data_list = [s for s in data_list if s.brand == brand]

    # Filter based on max price if provided
    if max_price:
        max_price = float(max_price)
        data_list = [s for s in data_list if float(s.price) <= max_price]

    return data_list


def smartphone_detail(request, id):
    smartphone = Smartphone.objects.get(id=id)
    context = {'smartphone': smartphone}
    return render(request, 'smartphone_detail.html', context)
