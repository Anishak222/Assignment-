d1 = {'Anisha' : "okk", "Ana" : "ok" }
c = d1 ['Anisha']
print (c)
c= d1 ["Ana"]
print (c)
d2 = {"Anisha" : "o" , 'Anisha' : "okk" , "Anisha" : "ok" , 'Anisha' : "PPP" }
p = d2 ['Anisha'] 
print (p) 
d3 = {'number' : [2,3,4,5,6 ,7] , 'assignment' : (1,23,23,3,4,23) , "launch_date" :{12, 24 , 26 } , "class_time" : {"web" : 7 , "data_science": 8 , 'java with DSA' : 9}}
print (d3)
d3['oooo'] = ['anisha' , 'rohit' , 'payal'] 
print (d3)
e=d3['class_time'] ['java with DSA']
print (e)
del d3 ['assignment']
print (d3)
k= list (d3.items())
print (k)
y= list (d3.values ())
print (y) 
t= list (d3.keys())
print (t)
u= list (d3.fromkeys())
print (u)
h=list (d3.pop())
print (h)

marks =input ("enter marks") 
marks = 10
if marks >= 80:
    print ("ok")
elif marks <=40 and marks >=50:
    print ("okk")
elif marks <=65 and marks <=70:
    print ("okkk")
else :
    print ("okkkk")

price =int ( input ("enter price") )
if  price > 10000 :
    print ("yes i will purchase")
elif price < 900  :
    print ("i will not purchase")
else : ("thanks for inquiry") 


price = float (input("enter price"))
if  price < 9000 :
    print ("okk got it ")
    if price >9000 :
     print ("ok purchase it please")
elif price >800 :
    print ("i will purchase it")
elif  price <700 :
      print ("received it please")
else : 
    print ("thanks for inquiry")

price = int  ( input ("enter price") )
if price > 41 :
    print ("yes i will purchase")
else :
    price < 41 
    print ("no i will not purchase")
    


  
    
















