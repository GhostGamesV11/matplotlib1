import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

##Zad1

# f=[1/x for x in range(20, 41)]
# plt.plot(range(20, 41),f,"bo--",label="1/x")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.axis([20,40,0.02,0.05])
# plt.legend()
# plt.show()

##Zad2
# f=[1/x for x in range(20, 41)]
# plt.plot(range(20, 41),f,"bo--",label="1/x")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.axis([20,40,0.02,0.05])
# plt.legend()
# plt.title("Wykres funkcji f(x) dla x[20,40]")
# plt.show()

##Zad3

# zakres=np.arange(0,45,0.1)
# sinus=np.sin(zakres)
# cosinus=np.cos(zakres)
# plt.plot(zakres,sinus,label="sin(x)")
# plt.plot(zakres,cosinus,label="cos(x)")
# plt.legend()
# plt.show()

##Zad4

# zakres=np.arange(0,45,0.1)
# sinus1=np.sin(zakres)+2
# sinus2=np.sin(zakres)*1
# plt.plot(zakres,sinus1,label="sin(x)")
# plt.plot(zakres,sinus2,label="sin(x)")
# plt.title("Wykres sin(x), sin(x)")
# plt.xlabel("x")
# plt.ylabel("sin(x)")
# plt.legend(loc="center left")
# plt.show()


##Zad6

# df=pd.read_excel("imiona.xlsx",header=0)
#
# w1= df.groupby(["Plec"]).sum("Liczba")
#
# w2k=df.where(df["Plec"]=="K").groupby(["Rok"]).agg({"Liczba": ["sum"]})
# w2m=df.where(df["Plec"]=="M").groupby(["Rok"]).agg({"Liczba": ["sum"]})
# lata=df["Rok"].unique()
# plec=df["Plec"].unique()
#
# w3=df.groupby(["Rok"]).sum("Liczba")
#
# plt.subplots(1,3,figsize=(16,9))
# plt.subplot(1,3,1)
# plt.bar(plec,w1["Liczba"],color="r")
# plt.title("Liczba urodzonych chlopcow i dziewczynek w calym okresie")
# plt.xlabel("Plec")
# plt.ylabel("Miliony")
# plt.subplot(1,3,2)
# plt.plot(lata,w2k,label="K",color="pink")
# plt.plot(lata,w2m,label="M",color="b")
# plt.title("Liczba urodzonych dzieci w danym roku i danej plci")
# plt.xlabel("Lata")
# plt.ylabel("Ilośc urodzonych")
# plt.xticks(lata,rotation=60)
# plt.legend()
# plt.subplot(1,3,3)
# plt.bar(lata,w3["Liczba"],color="g")
# plt.title("Liczba urodzonych dzieci w danym roku")
# plt.xlabel("Rok")
# plt.ylabel("Ilosc urodzonych")
# plt.xticks(lata,rotation=60)
# plt.tight_layout()
# plt.show()
