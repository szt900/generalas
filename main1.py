import random

#0
print("Osztályzatok generálása")

#1
db=int(input("Kérem az osztályzatok számát: "))

osztalyzatok=[]
#mivel tudjuk a darabszamot ezert elore meghatarozott lepesszamu ciklus
for i in range(db): 
    oszt = random.randint(1, 5)     # Az osztalyzatok 1-tol 5-ig terjednek.
    osztalyzatok.append(oszt)

#2-3
print (osztalyzatok)