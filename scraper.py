import requests 
from bs4 import BeautifulSoup
from datetime import date,timedelta

class cases():
  def __init__(self,data):
     self.country =data.lower()
     self.src = "https://www.worldometers.info/coronavirus/country/{}/".format(self.country)
     self.result = requests.get(self.src)
     self.src =self.result.content
     self.yesterday = date.today() - timedelta(days=1)
     self.d1 = "newsdate"+ self.yesterday.strftime("%Y-%m-%d")
     self.soup = BeautifulSoup(self.src,'lxml')
  def stats(self):
    try:
      div = self.soup.findAll("div", {"class":"maincounter-number"})
      div = str(div[0]).split("\n")[1].split(">")[1].split("<")
      li = self.soup.findAll("li", {"class":"news_li"})
      li = str(li).split(">")[2].split("new cases")
      return "Total number of cases is: "+ div[0] +"\nNew cases: " + li[0]+"\nStay safe:)"
    except:
      return "Oops it seems like the country you entered does not exist, please check your spelling and try again"

 
