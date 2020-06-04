from tkinter import *
import os
import tkinter.ttk as ttk
import random
import time

tombala=["el","le","ele","elle",
         "al","la","ala","alla","Ela","ela","Lale","lale",
         "ek","ke","ak","ka","kek","kal","kalk","kel","kale","elek","keke","kelle","kelek","elekle","ekle","leke","kekle","akla",
         "il","li","ik","ki","elli","iki","ile","ilke","İlke","Ali","eki","keki","eli","laleli","ekli","kil","killi","lila","ilk","ilik","ilikle",
         "keklik","lekeli","kekik","ikili","elekli","kekikli","ikilik","ilkel","ilkeli","Akile",
         "en","ne","an","na","in","ni","ana","Nil","anne","nane","ninni","İnan","Nalan","elin","kan","eken","kanal","kalan","kene","Alkan",
         "anla","inle","nine","inek","nal","Kenan","İnal","ilan","ekin","neli","alan","inan","lakin","kanka","enli","kalkan","enik","nakil"]

uzun=0
def hecele():
    
    uzunluk=len(tombala)

    label1=Label(text="Kalan\n"+str(uzunluk),fg='red',font=("TTKB DikTemel Abece" ,30))
   
    label1.place(relx = 0.81, rely = 0.6)

    label1=Label(text="                                                                                                                 ",fg='blue',font=("TTKB DikTemel Abece" ,80))
    
    label1.place(relx = 0.35, rely = 0.3)
    
    hecele = []
    kelime=""
    heceToplam=""
    if len(tombala) >0:
        for i in random.sample((tombala),1):
          
            kelime+=i
            bits = ''.join(['1' if l in 'AEIİOÖUÜaeıioöuü' else '0' for l in i])
            tombala.remove(i)
           
        seperators = (('101', 1),('1001', 2),('10001', 3))

        index, cut_start_pos = 0, 0

        while index < len(bits):
            for seperator_pattern, seperator_cut_pos in seperators:
                if bits[index:].startswith(seperator_pattern):
                    hecele.append(i[cut_start_pos:index + seperator_cut_pos])

                    index += seperator_cut_pos
                    cut_start_pos = index
                    break

            index += 1

        hecele.append(i[cut_start_pos:])

        for hece in hecele:
            heceToplam+=hece+" "
            
        label1=Label(text=heceToplam+" -----> "+kelime,fg='blue',font=("TTKB DikTemel Abece" ,60))
        label1.place(relx = 0.1, rely = 0.3)     

    else:
        label1=Label(text="                                                                                        ",fg='blue',font=("TTKB DikTemel Abece" ,80))
        label1.place(relx = 0.1, rely = 0.3)
        uyari=Toplevel()
        Label(uyari,text="BİTTİ. YENİLENMESİ İÇİN BAŞTAN AL BUTONUNA BASINIZ.").pack()
        uyari.mainloop()
        
def al():
        pencere.destroy()
        os.startfile("hecekelimetombala.exe")
             
pencere=Tk()
pencere.tk_setPalette("light blue")
pencere.attributes("-fullscreen", 1)

mainframe = ttk.Frame(pencere,padding='3 3 12 12')
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight =1)
                    
label=Label(text="1. GRUP (ELAKİN) HECE/KELİME TOMBALASI PROGRAMI",fg="red",font=("TTKB DikTemel Abece" ,30))
label.place(relx = 0.17, rely = 0.0)

label1=Label(text="",font=("TTKB DikTemel Abece" ,60))
label1.place(relx = 0.1, rely = 0.3)

buton1=Button()
buton1.config(text="SEÇ", command=hecele,width='25',bg="red",fg="white",font=("TTKB DikTemel Abece" ,16))
buton1.place(relx = 0.08, rely = 0.85)

buton2=Button()
buton2.config(text="BAŞTAN AL", command=al,width='25',bg="red",fg="white",font=("TTKB DikTemel Abece" ,16))
buton2.place(relx = 0.40, rely = 0.85)

buton=Button()
buton.config(text="ÇIKIŞ",command=pencere.destroy,width='25',bg="red",fg="white",font=('TTKB DikTemel Abece',16))
buton.place(relx = 0.74, rely = 0.85)

pencere.mainloop()

