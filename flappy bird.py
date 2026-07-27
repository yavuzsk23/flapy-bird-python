import pygame
import random

# --- AYARLAR ---
GENISLIK = 400
YUKSEKLIK = 600
YER_CEKIMI = 0.25
ZIPLAMA_GUCU = -6.5
BORU_HIZI = 3
BORU_ARALIGI = 150 # İki boru arasındaki dikey boşluk
BORU_SIKLIGI = 1500 # Yeni boru gelme süresi (ms)

# Renkler
MAVI = (113, 197, 207)   # Gökyüzü
SARI = (255, 255, 0)     # Kuş
YESIL = (115, 191, 46)   # Boru
KAHVE = (222, 216, 149)  # Zemin

class Kus:
    def __init__(self):
        self.x = 50
        self.y = YUKSEKLIK // 2
        self.hiz = 0
        self.boyut = 30

    def hareket_et(self):
        self.hiz += YER_CEKIMI
        self.y += self.hiz

    def zipla(self):
        self.hiz = ZIPLAMA_GUCU

    def ciz(self, ekran):
        pygame.draw.rect(ekran, SARI, [self.x, self.y, self.boyut, self.boyut])
        # Göz ve gaga detayları
        pygame.draw.rect(ekran, (0, 0, 0), [self.x + 20, self.y + 5, 5, 5])
        pygame.draw.rect(ekran, (255, 165, 0), [self.x + 25, self.y + 15, 10, 5])

class Boru:
    def __init__(self, x):
        self.x = x
        self.genislik = 60
        self.ust_boy = random.randint(50, YUKSEKLIK - BORU_ARALIGI - 50)
        self.alt_y = self.ust_boy + BORU_ARALIGI
        self.gecildi = False

    def hareket_et(self):
        self.x -= BORU_HIZI

    def ciz(self, ekran):
        # Üst Boru
        pygame.draw.rect(ekran, YESIL, [self.x, 0, self.genislik, self.ust_boy])
        # Alt Boru
        pygame.draw.rect(ekran, YESIL, [self.x, self.alt_y, self.genislik, YUKSEKLIK - self.alt_y])
        # Boru Başlıkları
        pygame.draw.rect(ekran, (50, 100, 20), [self.x - 5, self.ust_boy - 20, self.genislik + 10, 20])
        pygame.draw.rect(ekran, (50, 100, 20), [self.x - 5, self.alt_y, self.genislik + 10, 20])

def ana_dongu():
    pygame.init()
    ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
    pygame.display.set_caption("Cyberia Flappy Bird")
    saat = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 32, bold=True)

    kus = Kus()
    borular = []
    
    # Zamanlayıcı (Boru üretimi için)
    BORU_OLUSTUR = pygame.USEREVENT
    pygame.time.set_timer(BORU_OLUSTUR, BORU_SIKLIGI)

    skor = 0
    oyun_aktif = True

    while True:
        ekran.fill(MAVI)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if oyun_aktif:
                        kus.zipla()
                    else:
                        # Oyunu sıfırla
                        kus = Kus()
                        borular = []
                        skor = 0
                        oyun_aktif = True
            
            if event.type == BORU_OLUSTUR and oyun_aktif:
                borular.append(Boru(GENISLIK))

        if oyun_aktif:
            kus.hareket_et()
            
            for boru in borular[:]:
                boru.hareket_et()
                
                # Çarpışma Kontrolü
                kus_rect = pygame.Rect(kus.x, kus.y, kus.boyut, kus.boyut)
                ust_boru_rect = pygame.Rect(boru.x, 0, boru.genislik, boru.ust_boy)
                alt_boru_rect = pygame.Rect(boru.x, boru.alt_y, boru.genislik, YUKSEKLIK - boru.alt_y)

                if kus_rect.colliderect(ust_boru_rect) or kus_rect.colliderect(alt_boru_rect):
                    oyun_aktif = False
                
                # Skor Artışı
                if not boru.gecildi and boru.x + boru.genislik < kus.x:
                    skor += 1
                    boru.gecildi = True
                
                # Ekrandan çıkan boruları sil
                if boru.x < -boru.genislik:
                    borular.remove(boru)

            # Zemin veya tavan kontrolü
            if kus.y <= 0 or kus.y + kus.boyut >= YUKSEKLIK:
                oyun_aktif = False

        # Çizimler
        for boru in borular:
            boru.ciz(ekran)
        
        kus.ciz(ekran)
        
        # Skor gösterimi
        skor_metni = font.render(str(skor), True, (255, 255, 255))
        ekran.blit(skor_metni, (GENISLIK // 2 - 10, 50))

        if not oyun_aktif:
            mesaj = font.render("OYUN BITTI!", True, (255, 0, 0))
            tekrar = font.render("Tekrar icin SPACE", True, (0, 0, 0))
            ekran.blit(mesaj, (GENISLIK // 2 - 80, YUKSEKLIK // 2 - 50))
            ekran.blit(tekrar, (GENISLIK // 2 - 110, YUKSEKLIK // 2 + 10))

        pygame.display.update()
        saat.tick(60)

if __name__ == "__main__":
    ana_dongu()
