from django.http import HttpResponse
from django.shortcuts import render
 


def home(request):


   
    return render(request,'polls/index.html')

def about(request):
   
    import requests
    from bs4 import BeautifulSoup
    import urllib.request
    data1= request.GET['text']
    print('===================================================')
   
    data2="https://medium.com/tag/"
    search=data2+data1
    #print(search)
    ptc=requests.get(search)
    html=ptc.content
    sp=BeautifulSoup(html,"html.parser")
    list1=[]
    list2=[]
    list3=[]
    list4=[]

    l=sp.find_all(class_='link u-baseColor--link')
    
    for ref in l:
    	#print (titles.text)
    	list4.append(ref.text)


    i=sp.find_all('h3')
    a1=1
    for titles in i:
    	#print (titles.text)
    	list1.append(titles.text)
    	
    #print(i)
    print('===================================================')
    j=sp.find_all(class_='link link--darken')
    for links in j:
    	#print (titless.get('href'))
    	list2.append(links.get('href'))
    k=sp.find_all(class_='postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis')
    for names in k:
    	#print (titless.get('href'))
    	if names.text=='':
    		list3.append('no name')
    	else :
    	    list3.append(names.text)
    
    print('===================================================')
    pk11=len(i)
    print (len(i))
    print (list4)
    
    return render(request,'polls/about.html',{'v1':list1,'v2':list2,'v3':list3,'t1':data1,'aa':a1,'len':pk11,'sugg':list4})  
   
def page(request):
    
    import requests
    from bs4 import BeautifulSoup
    import urllib.request
    data1= request.GET['text']
    data2=request.GET['tag']
    print('===================================================')
    #print(data1)
    #print(data2)
    ptc=requests.get(data1)
    html=ptc.content
    sp=BeautifulSoup(html,"html.parser")
    #print(sp)
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    i=sp.find_all('h1')
    for title in i:
    	#print (titless.get('href'))
    	list1.append(title.text)
    #print(i)
    j=sp.find_all('p')
    for cont in j:
    	#print (titless.get('href'))
    	list2.append(cont.text)
    #print(list2)
    k=sp.find_all(class_='link u-baseColor--link')
    
    for ref in k:
    	#print (titles.text)
    	list3.append(ref.text)

    p=sp.find_all(class_='graf graf--p graf--leading graf--trailing')
    for rrr in p:
    	#print (titles.text)
    	list4.append(rrr.text)
    pk11=len(k)
    print(pk11)	
    print('===================================================')
    
   
    return render(request,'polls/page.html',{'src':data1,'tit':list1,'para':list2,'tags':list3,'len':pk11})    