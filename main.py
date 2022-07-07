def Hesapla(matris):

    def Kontrol(matris, y, x):
        if not y+1 >= len(matris) and matris[y+1][x] == 1 and not [y+1,x] in kontrol_edilenler:
            kontrol_edilenler.append([y+1,x])
            Kontrol(matris, y+1, x)    

        if not y-1 < 0 and matris[y-1][x] == 1 and not [y-1,x] in kontrol_edilenler:
            kontrol_edilenler.append([y-1,x])
            Kontrol(matris, y-1, x) 

        if not x+1 >= len(matris[y]) and matris[y][x+1] == 1 and not [y,x+1] in kontrol_edilenler:
            kontrol_edilenler.append([y,x+1])
            Kontrol(matris, y, x+1) 

        if not x < 0 and matris[y][x-1] == 1 and not [y,x-1] in kontrol_edilenler:
            kontrol_edilenler.append([y,x-1])
            Kontrol(matris, y, x-1) 

        return kontrol_edilenler
            
    kontrol_edilenler = []
    sayi = 0
    for y, i in enumerate(matris):
        for x, j in enumerate(i):
            if j == 1 and not [y,x] in kontrol_edilenler:
                sayi += 1
                kontrol_edilenler.append([y,x])
                for k in Kontrol(matris,y,x):
                    if not k in kontrol_edilenler:kontrol_edilenler.append(k)

    return sayi

matris = [ 
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0 ],
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
]

print(f"Görseldeki nesne sayısı:{Hesapla(matris)}")