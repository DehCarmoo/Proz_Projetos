# numero crescente de 1 a 20 sem o 13 :while
i=0
while(i<=20):
  i=i+1
  if(i==13):
    continue
  print(i, "andar") 
  
 # numero crescente de 1 a 20 sem o 13:for
for i in range(1,22,1): 
  if i == 13:
    continue
  print(i, "andar")
  
 # numero decrescente de 1 a 20, sem o 13 :while
i = 22
while(i <=22 and i >1):
  i = i - 1
  if(i == 13):
    continue
  print(i,"andar") 
  
  #numero decrescente de 1 a 20 sem o 13: ranger
for i in range (21, 0 ,-1):
  if i==13:
    continue
  print(i,"andar")