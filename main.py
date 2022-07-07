import cv2

filename = "images/t2.png"
  
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE) #resmi renksiz olarak okuma

#görüntüyü boyutlandırma
scale_percent = 5
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

#siyah beyaza çevirme
blackWhiteImage = cv2.threshold(resized, 200, 255, cv2.THRESH_BINARY)[1]

imageMatris = blackWhiteImage.tolist() # görüntüyü python listesine çevirme

# siyah yerleri 1'e beyaz yerleri 0'a çevirme
for y, i in enumerate(imageMatris):
    for x, j in enumerate(i):
        if j==255: imageMatris[y][x] = 0
        else: imageMatris[y][x] = 1

def Hesapla(matris, minBoyut):

    def Kontrol(matris, y, x): #ilgili konum ile bağlantısı olan diğer 1 değeri taşıyan konumları bulma
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
            
    kontrol_edilenler = [] #kontrol edilip 1 değeri içerdiği tespit edilen konumlar(işlem tekrarını önlemek için)
    nesneler = [] #bulunan her nesnenin konumları
    sayi = 0
    for y, i in enumerate(matris):
        for x, j in enumerate(i):
            if j == 1 and not [y,x] in kontrol_edilenler:
                sayi += 1
                nesneler.append([])
                kontrol_edilenler.append([y,x])
                for k in Kontrol(matris,y,x):
                    nesneler[sayi-1].append(k)
                    if not k in kontrol_edilenler:kontrol_edilenler.append(k)
 
    for nesne in nesneler:
        if len(nesne) < minBoyut: #minimum nesne boyut sınırının altında olanları çıkarma
            sayi -= 1
            continue

        #sadece bir kareyle birbirine bağlanmış bitişik nesneleri ayırma
        for konum in nesne:
            if matris[konum[0]-1][konum[1]] == 0 and matris[konum[0]+1][konum[1]] == 0 and matris[konum[0]][konum[1]+1] == 1 and matris[konum[0]][konum[1]-1] == 1:
                x = konum[1]
                sol, sag = 0,0
                for i in nesne:
                    if i[1] < x:
                        sol += 1
                    elif i[1] > x:
                        sag += 1
                if sol/sag <= 2 and sol/sag >= 0.5:
                    sayi += 1
                    break

            elif matris[konum[0]][konum[1]-1] == 0 and matris[konum[0]][konum[1]+1] == 0 and matris[konum[0]-1][konum[1]] == 1 and matris[konum[0]+1][konum[1]] == 1:
                y = konum[0]
                ust, alt = 0,0
                for i in nesne:
                    if i[1] < y:
                        sol += 1
                    elif i[1] > y:
                        sag += 1
                if ust/alt <= 2 and ust/alt >= 0.5:
                    sayi += 1
                    break

    return sayi

print(f"Görseldeki nesne sayısı:{Hesapla(imageMatris, 4)}")