import numpy as np
import matplotlib.pyplot as plt
alfa = 0.1*(1)/(10)**2
s = 1 #długość
D=0.1 #wspólczynnik dyfuzji
n = s/D
M = np.zeros((35000*int(n),int(n+1)))
M[:,0] = 81 #warunki brzegowe dirichleta
M[:,-1]= 180
for i in range(1, 35000*int(n)): # czas
    for j in range(1, int(n)): # przestrzen
        M[i,j] = alfa*(M[i-1,j+1]+M[i-1,j-1]-2*M[i-1,j]) + M[i-1,j]
print(M[35000,:])

x = np.array(range(0,11))
y = np.array(M[35000,:])

print(y)

x = x.reshape(-1,1)
plt.plot(x, y)
plt.xlabel('Numer węzła') #nazwa OX
plt.ylabel('Temperatura(℃)') #nazwa OY
plt.title('Równanie przewodnictwa cieplnego') #tytuł wykresu
plt.xlim(0,10)
plt.ylim(0,200)

plt.show() #wyświtenie funkcji