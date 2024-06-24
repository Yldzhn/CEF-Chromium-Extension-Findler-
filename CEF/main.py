import requests
from bs4 import BeautifulSoup
import pandas as pd

def main(option):
    if option=="1":
        args=paramSet()
        req=requests.get(f"https://chromewebstore.google.com/detail/{args}")
        soup = BeautifulSoup(req.content, "html.parser")
        headParser=soup.css.select("h1.Pa2dE")
        linkParser=req.url
        data=pd.DataFrame([{"Header":headParser[0].text,"Link":linkParser}])
        print(data)
    
    elif option=="2":
        args=csvReader()
        data=[]
        for x, y in enumerate(args):
   
            req=requests.get(f"https://chromewebstore.google.com/detail/{y}")
        
            soup = BeautifulSoup(req.content, "html.parser")
            headParser=soup.css.select("h1.Pa2dE")
            linkParser=req.url
            data.append({"Header":headParser[0].text,"Link":linkParser})
        csvCreate(data)
    else:
        print("Bir hata oluştu lütfen tekrar deneyiniz!!")
    
def csvReader():
    fileName=input("(CSV)Kaynak dosya ismi? ")
    df=pd.read_csv(f"{fileName}.csv")
    data=df.to_string(index=False).split()
    
    return data

def csvCreate(x):
    fileName=input("Yeni oluşturulacak dosya ismi? ")
    df=pd.DataFrame(x)
    df.to_csv(f"{fileName}.csv")

def paramSet():
    x=input("Extension ID:")
    x.strip()
    return x

if __name__ == '__main__':
    Option=input("1:Tekli Sorgu, 2:Çoklu Sorgu\n")
    main(Option)