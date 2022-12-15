import urllib.request
import scipy as sc
import numpy as np
import re
import matplotlib.pyplot as plt
import json

def h(n,x):
    return sc.special.spherical_jn(n, x) + 1j * sc.special.spherical_yn(n, x)

def a(n,x):
    return sc.special.spherical_jn(n, x)/h(n, k*r)

def b(n,x):
    return (x * sc.special.spherical_jn(n-1, x) - n * sc.special.spherical_jn(n, x)) / (x * h(n - 1, x) - n * h(n, x))

def sigma(povtor,x):
    sigm = 0
    for n in range(1,povtor):
        sigm = sigm + np.power(-1,n)*(n+0.5)*(b(n,x)-a(n,x))
        print('n= ',n)
    return sigm

if __name__=='__main__':
    url = 'https://jenyay.net/uploads/Student/Modelling/task_02.csv'
    urllib.request.urlretrieve(url, 'prog0211.d.csv')
    with open('prog0211.d.csv', 'r') as file:
        book = file.readlines()
    var = int(input('Введите ваш вариант: '))
    shkala = int(input('Введите приближение(число шагов): '))
    print(book[var])
    print(re.findall('\d+[.]*\d*e*[-]*\d*', book[var]))
    book1 = re.findall('\d+[.]*\d*e*[-]*\d*', book[var])
    D = float(book1[1])
    print('D= ',D)
    fmin = float(book1[2])
    print('fmin= ',fmin)
    fmax = float(book1[3])
    print('fmax= ',fmax)
    r = D/2
    print('r= ',r)
    f = np.linspace(fmin,fmax,shkala)
    print('f= ',f)
    lamda = 3*10**8/f
    print('lamda= ',lamda)
    k = 2*np.pi/lamda
    print('k= ',k)
    result = lamda**2/np.pi*abs(sigma(70,k*r))**2
    print('sigma = ',result)
    plt.plot(2*np.pi*r/lamda,result/(np.pi*r**2))
    plt.xlabel('f, Гц')
    plt.ylabel(u'\u03C3, м^2')
    plt.show()
    plt.plot(f,result)

    with open("prog0211.2.csv", "w", encoding="utf-8") as file:
        for i in range(len(f)):
            file.write('номер строки: {}, f: {}, ЭПР: {}\n'.format(i+1, f[i], result[i]))
