from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
myurl="https://www.rottentomatoes.com/m/interstellar_2014/reviews/"
uclient = ureq(myurl)
pagehtml=uclient.read()
uclient.close()
pagesoup=soup(pagehtml,"html.parser")
containers=pagesoup.findAll("div",{"class":"row review_table_row"})

container=containers[0]

review=container.findAll('div',{"class":"the_review"})

filename="CriticsReview.csv"
f=open(filename,"a")
headers="Critics Name,Review\n"
f.write(headers)

for container in containers:
    name=container.div.a["href"]

    views = container.findAll('div',{"class":"the_review"})
    review=views[0].text

    print(name.replace(",","|")+","+review+"\n")
    f.write(name.replace(",","|")+","+review+"\n")

f.close()



