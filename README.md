# Flappy Bird Clone

A classic Flappy Bird clone built with **Pygame**. Guide the bird through an endless series of pipes by tapping the space bar — one tap keeps it airborne, and every gap you clear adds to your score.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🇬🇧 English

### Overview
A lightweight, single-file recreation of the classic Flappy Bird game. The bird is affected by gravity at all times; pressing **Space** gives it an upward boost. Pipes spawn at a fixed interval with a randomized vertical gap, and the score increases each time the bird successfully passes through a pair of pipes.

### Features
- Smooth gravity-based physics
- Randomly generated pipe gaps for replayability
- Real-time score tracking
- Collision detection (pipes, ceiling, and ground)
- Instant restart on Game Over — no need to relaunch the app

### Requirements
- Python 3.10 or higher
- `pygame`

### Installation
```bash
pip install pygame
```

### Usage
```bash
python flappy_bird.py
```

**Controls:**
- `Space` — jump / flap upward
- `Space` (after Game Over) — restart the game
- Close the window to quit

### How it works
The game runs on a standard game loop capped at 60 FPS. Each frame, the bird's vertical velocity increases due to a constant `GRAVITY` value, simulating a fall; pressing Space overrides this velocity with a fixed `JUMP_STRENGTH`. Pipes are spawned via a Pygame timer event (`PIPE_EVENT`) every 1500ms, each with a randomized gap position. Collision is detected using `pygame.Rect.colliderect()` between the bird's hitbox and each pipe segment.


---

## 🇩🇪 Deutsch

### Überblick
Eine schlanke Ein-Datei-Umsetzung des klassischen Flappy-Bird-Spiels. Der Vogel unterliegt permanent der Schwerkraft; ein Druck auf **Leertaste** gibt ihm einen Aufwärtsschub. Rohre erscheinen in festen Zeitabständen mit einer zufälligen vertikalen Lücke, und der Punktestand erhöht sich jedes Mal, wenn der Vogel erfolgreich ein Rohrpaar passiert.

### Funktionen
- Flüssige, schwerkraftbasierte Physik
- Zufällig generierte Rohrlücken für hohen Wiederspielwert
- Echtzeit-Punktestand
- Kollisionserkennung (Rohre, Decke und Boden)
- Sofortiger Neustart nach Game Over — kein erneutes Starten der Anwendung nötig

### Voraussetzungen
- Python 3.10 oder höher
- `pygame`

### Installation
```bash
pip install pygame
```

### Verwendung
```bash
python flappy_bird.py
```

**Steuerung:**
- `Leertaste` — springen / nach oben flattern
- `Leertaste` (nach Game Over) — Spiel neu starten
- Fenster schließen zum Beenden

### Funktionsweise
Das Spiel läuft in einer klassischen Game-Loop mit einer Begrenzung auf 60 FPS. In jedem Frame erhöht sich die vertikale Geschwindigkeit des Vogels durch einen konstanten `GRAVITY`-Wert, was einen Fall simuliert; ein Druck auf die Leertaste überschreibt diese Geschwindigkeit mit einem festen `JUMP_STRENGTH`-Wert. Rohre werden über ein Pygame-Timer-Event (`PIPE_EVENT`) alle 1500ms erzeugt, jeweils mit einer zufällig positionierten Lücke. Die Kollisionserkennung erfolgt über `pygame.Rect.colliderect()` zwischen der Trefferbox des Vogels und jedem Rohrsegment.


---

## 🇹🇷 Türkçe

### Genel Bakış
Klasik Flappy Bird oyununun sade, tek dosyalık bir versiyonu. Kuş sürekli yerçekiminin etkisi altındadır; **Boşluk tuşuna** basmak ona yukarı doğru bir itiş kazandırır. Borular sabit aralıklarla, rastgele belirlenmiş dikey bir boşlukla belirir ve kuş her bir boru çiftini başarıyla geçtiğinde skor artar.

### Özellikler
- Akıcı, yerçekimi tabanlı fizik
- Tekrar oynanabilirlik için rastgele oluşturulan boru boşlukları
- Gerçek zamanlı skor takibi
- Çarpışma tespiti (borular, tavan ve zemin)
- Game Over sonrası anında yeniden başlatma — uygulamayı tekrar açmaya gerek yok

### Gereksinimler
- Python 3.10 veya üzeri
- `pygame`

### Kurulum
```bash
pip install pygame
```

### Kullanım
```bash
python flappy_bird.py
```

**Kontroller:**
- `Boşluk` — zıpla / yukarı çırp
- `Boşluk` (Game Over sonrası) — oyunu yeniden başlat
- Pencereyi kapatarak çıkış yap

### Nasıl çalışır?
Oyun, saniyede 60 kareyle (FPS) sınırlandırılmış standart bir oyun döngüsü üzerinde çalışır. Her karede, kuşun dikey hızı sabit bir `GRAVITY` değeriyle artar ve bu düşüşü simüle eder; Boşluk tuşuna basmak bu hızı sabit bir `JUMP_STRENGTH` değeriyle geçersiz kılar. Borular, Pygame zamanlayıcı olayı (`PIPE_EVENT`) aracılığıyla her 1500ms'de bir, rastgele bir boşluk pozisyonuyla oluşturulur. Çarpışma tespiti, kuşun çarpışma kutusu ile her boru segmenti arasında `pygame.Rect.colliderect()` kullanılarak yapılır.
