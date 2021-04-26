#pp = xlrd.open_workbook('../static/market_price.xlsx')
#datas = pd.read_excel(pp, index_col=None)
# df = pd.read_excel('static/market_price.xlsx')
import xlrd
import pandas as pd


total_price = 0

class Product:
    def __init__(self, name=None, price=None ):
        self.name=name
        self.price = price

    def printProduct(self):
        print(f'name:{self.name}')
        print(f'price:{self.price}')


def getAll():
    global total_price
    list =[]
    datas = pd.read_excel('../static/market_price.xlsx') #,index_col=None

    i = 0
    while True:
        try:
            name=datas.loc[i, '과일']
            price = datas.loc[i,'가격']
            #print(name,price)
            p = Product(name=name,price=price)
            p.printProduct()
            list.append(p)
            total_price += price

        except KeyError as k:
            print(k)
            break
        i += 1
    print(f'total_price:{total_price}')
    return list


getAll()

