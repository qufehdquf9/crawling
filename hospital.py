import csv
import requests
from bs4 import BeautifulSoup

cityNames = ['seoul', 'incheon', 'kangwon', 'Gyeonggi', 'chungbuk', 'chungnam', 'sejong', 'daejeon', 'Gyeongbuk', 
                'daegu', 'jeonbuk', 'Gyeongnam', 'ulsan', 'busan', 'gwangju', 'jeonnam', 'jeju']

url = "http://www.ksog.org/public/hospital_addr_list.php?sido={}&page={}"

f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(['지역', '병원', '주소', '전화번호'])

for name in cityNames:
    i = 1
    while True:
        rq = requests.get(url.format(name, i))
        rq.encoding = None

        soup = BeautifulSoup(rq.text, 'html.parser')
        hospitalL = soup.findAll('tr')[1:]
        if hospitalL:
            for hosp in hospitalL:
                wr.writerow([name]+[l.text for l in hosp.findAll('td')[:3]])
        else:
            break
        i += 1
f.close()