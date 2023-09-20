from rectpack import newPacker
import rectpack.packer as packer
import plotly.graph_objects as go

packer = newPacker()

def yirmi_dc():
    #konteyner bilgileri
    genişlik = 2.35
    uzunluk = 5.90
    yükseklik = 2.37
    yük_kapasite = 21770
    hacim = 33
    kont_boyutları = [genişlik, yükseklik, uzunluk]

    #köşeler
    kont_köşe = [
                [0, 0, 0],
                [kont_boyutları[0], 0, 0],
                [kont_boyutları[0], kont_boyutları[2], 0],
                 [0, kont_boyutları[2], 0],
                [0, 0, kont_boyutları[1]],
                [kont_boyutları[0], 0, kont_boyutları[1]],
                [kont_boyutları[0], kont_boyutları[2], kont_boyutları[1]],
                [0, kont_boyutları[2], kont_boyutları[1]]
                ]

    #yüzler
    yüzler = [
        [kont_köşe[0], kont_köşe[1], kont_köşe[2], kont_köşe[3]],
        [kont_köşe[0], kont_köşe[1], kont_köşe[5], kont_köşe[4]],
        [kont_köşe[3], kont_köşe[0], kont_köşe[4], kont_köşe[7]]
        ]

    # 3D çizim alanını oluşturun
    fig = go.Figure()

    for yüz in yüzler:
        fig.add_trace(go.Mesh3d(
        x=[nokta[0] for nokta in yüz],
        y=[nokta[1] for nokta in yüz],
        z=[nokta[2] for nokta in yüz],
        i=[0, 1, 2, 0],
        j=[1, 2, 3, 1],
        k=[2, 3, 0, 2],
        opacity=0.9,
        color='blue'
    ))

    # Sahneyi düzenle
    fig.update_layout(scene=dict(
    xaxis=dict(range=[0, genişlik], showbackground = False, showticklabels=False),
    yaxis=dict(range=[0, uzunluk], showbackground = False, showticklabels=False),
    zaxis=dict(range=[0, yükseklik], showbackground = False, showticklabels=False)
    ))
    fig.update_scenes(aspectmode='data')
    #cisimi packer ile oluştur
    packer.add_bin(genişlik, uzunluk)

    return fig, hacim, yük_kapasite

def kırk_dc():
    # Konteyner bilgileri
    genişlik = 2.35
    uzunluk = 11.98
    yükseklik = 2.35
    yük_kapasite = 26780
    hacim = 66
    kont_boyutları = [genişlik, yükseklik, uzunluk]

      #köşeler
    kont_köşe = [
                [0, 0, 0],
                [kont_boyutları[0], 0, 0],
                [kont_boyutları[0], kont_boyutları[2], 0],
                 [0, kont_boyutları[2], 0],
                [0, 0, kont_boyutları[1]],
                [kont_boyutları[0], 0, kont_boyutları[1]],
                [kont_boyutları[0], kont_boyutları[2], kont_boyutları[1]],
                [0, kont_boyutları[2], kont_boyutları[1]]
                ]
    #yüzler
    yüzler = [
        [kont_köşe[0], kont_köşe[1], kont_köşe[2], kont_köşe[3]],
        [kont_köşe[0], kont_köşe[1], kont_köşe[5], kont_köşe[4]],
        [kont_köşe[3], kont_köşe[0], kont_köşe[4], kont_köşe[7]]
       ]

    # 3D çizim alanını oluşturun
    fig = go.Figure()

    for yüz in yüzler:
        fig.add_trace(go.Mesh3d(
        x=[nokta[0] for nokta in yüz],
        y=[nokta[1] for nokta in yüz],
        z=[nokta[2] for nokta in yüz],
        i=[0, 1, 2, 0],
        j=[1, 2, 3, 1],
        k=[2, 3, 0, 2],
        opacity=0.9,
        color='blue'
    ))

    # Sahneyi düzenle
    fig.update_layout(scene=dict(
    xaxis=dict(range=[0, genişlik]),
    yaxis=dict(range=[0, uzunluk]),
    zaxis=dict(range=[0, yükseklik])
    ))
    fig.update_scenes(aspectmode='data')
    #cisimi packer ile oluştur
    packer.add_bin(genişlik, uzunluk)

    return fig, hacim, yük_kapasite

def kırk_hc():
    #konteyner bilgileri
    genişlik = 2.35
    uzunluk = 11.98
    yükseklik = 2.69
    yük_kapasite = 26780
    hacim = 76
    kont_boyutları = [genişlik, yükseklik, uzunluk]

     #köşeler
    kont_köşe = [
                [0, 0, 0],
                [kont_boyutları[0], 0, 0],
                [kont_boyutları[0], kont_boyutları[2], 0],
                 [0, kont_boyutları[2], 0],
                [0, 0, kont_boyutları[1]],
                [kont_boyutları[0], 0, kont_boyutları[1]],
                [kont_boyutları[0], kont_boyutları[2], kont_boyutları[1]],
                [0, kont_boyutları[2], kont_boyutları[1]]
                ]

    #yüzler
    yüzler = [
        [kont_köşe[0], kont_köşe[1], kont_köşe[2], kont_köşe[3]],
        [kont_köşe[0], kont_köşe[1], kont_köşe[5], kont_köşe[4]],
        [kont_köşe[3], kont_köşe[0], kont_köşe[4], kont_köşe[7]]
       ]

    # 3D çizim alanını oluşturun
    fig = go.Figure()

    for yüz in yüzler:
        fig.add_trace(go.Mesh3d(
        x=[nokta[0] for nokta in yüz],
        y=[nokta[1] for nokta in yüz],
        z=[nokta[2] for nokta in yüz],
        i=[0, 1, 2, 0],
        j=[1, 2, 3, 1],
        k=[2, 3, 0, 2],
        opacity=0.9,
        color='blue'
    ))

    # Sahneyi düzenle
    fig.update_layout(scene=dict(
    xaxis=dict(range=[0, genişlik], showbackground = False, showticklabels=False),
    yaxis=dict(range=[0, uzunluk], showbackground = False, showticklabels=False),
    zaxis=dict(range=[0, yükseklik], showbackground = False, showticklabels=False)
    ))


    fig.update_scenes(aspectmode='data')


    #cisimi packer ile oluştur
    packer.add_bin(genişlik, uzunluk)

    return fig, hacim, yük_kapasite

def kırkbeş_hc():
    #konteyner bilgileri
    genişlik = 2.35
    uzunluk = 13.50
    yükseklik = 2.69
    yük_kapasite = 26780
    hacim = 76
    kont_boyutları = [genişlik, yükseklik, uzunluk]

     #köşeler
    kont_köşe = [
                [0, 0, 0],
                [kont_boyutları[0], 0, 0],
                [kont_boyutları[0], kont_boyutları[2], 0],
                 [0, kont_boyutları[2], 0],
                [0, 0, kont_boyutları[1]],
                [kont_boyutları[0], 0, kont_boyutları[1]],
                [kont_boyutları[0], kont_boyutları[2], kont_boyutları[1]],
                [0, kont_boyutları[2], kont_boyutları[1]]
                ]

    #yüzler
    yüzler = [
        [kont_köşe[0], kont_köşe[1], kont_köşe[2], kont_köşe[3]],
        [kont_köşe[0], kont_köşe[1], kont_köşe[5], kont_köşe[4]],
        [kont_köşe[3], kont_köşe[0], kont_köşe[4], kont_köşe[7]]
       ]

    # 3D çizim alanını oluşturun
    fig = go.Figure()

    for yüz in yüzler:
        fig.add_trace(go.Mesh3d(
        x=[nokta[0] for nokta in yüz],
        y=[nokta[1] for nokta in yüz],
        z=[nokta[2] for nokta in yüz],
        i=[0, 1, 2, 0],
        j=[1, 2, 3, 1],
        k=[2, 3, 0, 2],
        opacity=0.9,
        color='blue'
    ))

    # Sahneyi düzenle
    fig.update_layout(scene=dict(
    xaxis=dict(range=[0, genişlik], showbackground = False, showticklabels=False),
    yaxis=dict(range=[0, uzunluk], showbackground = False, showticklabels=False),
    zaxis=dict(range=[0, yükseklik], showbackground = False, showticklabels=False)
    ))

    fig.update_scenes(aspectmode='data')

    #cisimi packer ile oluştur
    packer.add_bin(genişlik, uzunluk)

    return fig, hacim, yük_kapasite


def tır():
    #tır bilgileri
    genişlik = float(input("Tır genişliğini giriniz:"))
    uzunluk = float(input("Tır uzunluğunu giriniz:"))
    yükseklik = float(input("Tır yüksekliğini giriniz:"))
    yük_kapasite = float(input("Tırınızın yük kapasitesini giriniz:"))
    hacim = genişlik * uzunluk * yükseklik
    tır_boyutları = [genişlik, yükseklik, uzunluk]

    #köşeler
    tır_köşe = [
                [0, 0, 0],
                [tır_boyutları[0], 0, 0],
                [tır_boyutları[0], tır_boyutları[2], 0],
                 [0, tır_boyutları[2], 0],
                [0, 0, tır_boyutları[1]],
                [tır_boyutları[0], 0, tır_boyutları[1]],
                [tır_boyutları[0], tır_boyutları[2], tır_boyutları[1]],
                [0, tır_boyutları[2], tır_boyutları[1]]
                ]

    #yüzler
    yüzler = [
        [tır[0], tır[1], tır[2], tır[3]],
        [tır[0], tır[1], tır[5], tır[4]],
        [tır[3], tır[0], tır[4], tır[7]]
       ]

 # 3D çizim alanını oluşturun
    fig = go.Figure()

    for yüz in yüzler:
        fig.add_trace(go.Mesh3d(
        x=[nokta[0] for nokta in yüz],
        y=[nokta[1] for nokta in yüz],
        z=[nokta[2] for nokta in yüz],
        i=[0, 1, 2, 0],
        j=[1, 2, 3, 1],
        k=[2, 3, 0, 2],
        opacity=0.9,
        color='blue'
    ))

    # Sahneyi düzenle
    fig.update_layout(scene=dict(
    xaxis=dict(range=[0, genişlik], showbackground = False, showticklabels=False),
    yaxis=dict(range=[0, uzunluk], showbackground = False, showticklabels=False),
    zaxis=dict(range=[0, yükseklik], showbackground = False, showticklabels=False)
    ))

    fig.update_scenes(aspectmode='data')

    #cisimi packer ile oluştur
    packer.add_bin(genişlik, uzunluk)

    return fig, hacim, yük_kapasite


# tır mı? konteyner mı?
kont_tır = input("Yüklerinizi konteyner ile mi yoksa tır ile mi taşımak istersiniz? konteyner/tır")

if kont_tır.lower() == "konteyner":

    hangi_kont = input("Hangi tip konteyner ile yüklerinizi taşımak istersiniz? 20 DC/40 DC/40 HC/45 HC ")

    if hangi_kont.lower() == "20 dc":
        fig, hacim, yük_kapasite = yirmi_dc()

    elif hangi_kont.lower() == "40 dc":
        fig, hacim, yük_kapasite = kırk_dc()

    elif hangi_kont.lower() == "40 hc":
        fig, hacim, yük_kapasite = kırk_hc()

    else:
        fig, hacim, yük_kapasite = kırkbeş_hc()
else:
    fig, hacim, yük_kapasite = tır()



#Dizilecek cisimler
tip_sayı = int(input("kaç farklı yük tipi yerleştirmek istiyorsunuz?"))
toplam_ağırlık = 0
toplam_hacim = 0


for tip in range(1, tip_sayı + 1):

    genişlik = float(input(f"{tip}. tip cismin genişliğini giriniz:"))
    uzunluk = float(input(f"{tip}. tip cismin uzunluğunu giriniz:"))
    yükseklik = float(input(f"{tip}. tip cismin yüksekliğini giriniz:"))
    ağırlık = float(input(f"{tip}. tip cismin ağırlığını giriniz:"))
    cisim_hacim = genişlik * uzunluk * yükseklik
    tane = int(input(f"{tip}. yük tipinden kaç tane yerleştirmek istiyorsunuz: "))



    for tane in range(1, tane+1):

        if ağırlık < yük_kapasite or cisim_hacim < hacim:

            toplam_ağırlık += ağırlık
            toplam_hacim += cisim_hacim

            if toplam_ağırlık < yük_kapasite and toplam_hacim < hacim:

                packer.add_rect(genişlik, uzunluk, yükseklik)


            elif toplam_ağırlık == yük_kapasite or toplam_hacim == hacim:

                print("Toplam ağırlık ve/veya kaplanan hacim maksimum seviyeye ulaşmıştır.")
                packer.add_rect(genişlik, uzunluk, yükseklik)

            else:
                print(f"Üzgünüm,{tip}. tip {tane}, cisim yük ve/veya hacim kapasitesini aşıyor. Eklenmedi.  ")



        else:
            print(f"Üzgünüm,{tip}. tip {tane}, cisim yük ve/veya hacim kapasitesini aşıyor. Eklenmedi.  ")


#cisimleri diz
packer.pack()

#cisim çizimi
placements = packer.rect_list()
previous_values = {}
renkler = ["red", "cyan", "magenta", "green", "yellow", "white"]
a = 0
is_previous_values_initialized = False
for placement in placements:

    x = placement[1]
    y = placement[2]
    w = placement[3]
    d = placement[4]
    h = placement[5]
    renk = renkler[a]

    def check_multiple_changes(new_values):
        global previous_values, a, is_previous_values_initialized, renk,  renkler

        if is_previous_values_initialized == False:
            # ilk cisim için previous_values sözlüğünü oluştur
            previous_values = {"w": w, "d": d, "h": h}
            is_previous_values_initialized = True

        if all(new_value == previous_values.get(variable_name) for variable_name, new_value in new_values.items()) or \
             (new_values.get("w") == previous_values.get("d") and new_values.get("d") == previous_values.get("w")):
         
            fig.add_trace(go.Mesh3d(
                x=[x, x + w, x + w, x, x, x + w, x + w, x],
                y=[y, y, y + d, y + d, y, y, y + d, y + d],
                z=[0, 0, 0, 0, h, h, h, h],
                i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
                opacity=0.5,
                color= renk
                ))

        else:

            previous_values.update(new_values)
            a += 1
            renk = renkler[a]
            fig.add_trace(go.Mesh3d(
                x=[x, x + w, x + w, x, x, x + w, x + w, x],
                y=[y, y, y + d, y + d, y, y, y + d, y + d],
                z=[0, 0, 0, 0, h, h, h, h],
                i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
                k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
                opacity=0.5,
                color= renk
                ))



    check_multiple_changes({"w": w, "d": d, "h": h})

fig.show()

