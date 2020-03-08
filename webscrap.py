import requests
from bs4 import BeautifulSoup
filename="chemist.csv"
f=open(filename,"w")
headers="Store_Name, Store_Address, Phone_Number\n"
f.write(headers)
i=0
while i<50:
	i=i+1
	#change url according to your need
	url='https://www.justdial.com/Bangalore/Chemists-in-Koramangala/nct-10096237/page-'+str(i)
	agent={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
	page=requests.get(url, headers=agent)
	soup=BeautifulSoup(page.content,'html.parser')
	containers=soup.findAll("li",{"class":"cntanr"})

	for container in containers:
		store_name=container.find("span",{"class":"lng_cont_name"}).text
		store_address=container.find("span",{"class":"cont_fl_addr"}).text
		number=""
		try:
			contain=container.find("p",{"class":"contact-info"})
			spans=contain.find_all('span')
			for x in range(1,len(spans)):
				digit=spans[x].get('class')
				string=digit[-1].split("-")[-1]
				if string=='dc':
					number+='+'
				elif string=='fe':
					number+='('
				elif string=='hg':
					number+=')'
				elif string=='ba':
					number+='-'
				elif string=='abc':
					number+='0'
				elif string=='yz':
					number+='1'
				elif string=='wx':
					number+='2'
				elif string=='vu':
					number+='3'
				elif string=='ts':
					number+='4'
				elif string=='rq':
					number+='5'
				elif string=='po':
					number+='6'
				elif string=='nm':
					number+='7'
				elif string=='lk':
					number+='8'
				elif string=='ji':
					number+='9'
				else:
					number+='0'
		except:
			number='Not Provided'
		print(store_name)
		print(store_address)
		print(number)
		f.write(store_name+","+store_address.replace(","," ")+","+number.replace("-","")+"\n")
f.close()
