from bs4 import BeautifulSoup #html網頁 -> xml -> text
from datetime import date #直接用到日期
from datetime import timedelta 
import re

starting_date = date(2020, 7, 1)
end_date = date(2021, 6, 18)
datediff = end_date - starting_date
Q_bal = 0
Net_depart = 0
while (datediff >= timedelta(days=0)):
      url = "https://www.immd.gov.hk/hkt/stat_"+ starting_date.strftime("20%y%m%d") +".html"
      html_content = requests.get(url).text
      soup = BeautifulSoup(html_content, "lxml")
      inout_table = soup.find("table", attrs={"class": "tinymce-table1 table-passengerTrafficStat"})
      data = inout_table.tbody.find_all("tr")
      dataarry = []
      for td in data[0]:
            dataarry.append(td)
      Delta = int(re.sub(r"\D", "", dataarry[11].string))-int(re.sub(r"\D", "", dataarry[21].string))
      Q_bal = Q_bal + Delta
      Net_depart = Net_depart + int(re.sub(r"\D", "", dataarry[21].string))
      print("Date =", starting_date.strftime("20%y%m%d"),"In = " , dataarry[11].string, "Out = ",  dataarry[21].string, "Delta = ", Delta, "Cumulative = ", Q_bal, "NetDept = ", Net_depart)
      starting_date = starting_date + timedelta(days=1)
      datediff = datediff - timedelta(days=1)
