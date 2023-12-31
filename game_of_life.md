---
title: "Pygame of Life"
author:
  - Koen De Bruyne, CoderDojo Ichtegem

# template specific settings - https://github.com/Wandmalfarbe/pandoc-latex-template#custom-template-variables
book: true
titlepage: true
titlepage-rule-color: FFFFFF
titlepage-color: 642580
titlepage-text-color: FFFFFF
logo-width: 10cm
logo: "/home/k/OneDrive/coderdojo/CoderDojo_logo.png"
heading-color: 642580
toc-title: "Inhoudstafel"
listings-no-page-break: true
footnotes-pretty: true
colorlinks: true
---

# Pygame of Life

De code is ook terug te vinden op [https://github.com/koen-db/PygameOfLife](https://github.com/koen-db/PygameOfLife)

## Info: Conway's Game of Life

_Game of Life_[^1], soms kortweg _Life_ genoemd, is een in 1970 door de Britse wiskundige John Conway bedachte cellulaire automaat, een tweedimensionaal raster met vierkante 'cellen' die 'levend' of 'dood' kunnen zijn, en die zich volgens vastgestelde regels ontwikkelen en daarbij allerlei patronen kunnen vormen.

![By Thane Plambeck - &quot;https://www.flickr.com/photos/thane/20366806/&quot;, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=13076802](../../OneDrive/coderdojo/Pygame of Life/images/576px-John_H_Conway_2005.jpg "By Thane Plambeck - &quot;https://www.flickr.com/photos/thane/20366806/&quot;, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=13076802")

Er wordt gewerkt op een raster van vierkante cellen. Het raster is onbegrensd, dus oneindig groot. Elke cel kan zich in twee toestanden bevinden: een cel is gekleurd of wit.

Nadat een aantal cellen van een raster is ingekleurd, begint het spel. Game of Life werkt met 'generaties'; om te bepalen of een cel gekleurd ('levend') is of wit ('dood') in de volgende generatie wordt er een aantal regels toegepast aan de hand van de status (levend of dood) die de buurcellen hebben. Elke cel heeft 8 buurcellen.

* Als een cel door 2 of 3 gekleurde buurcellen omgeven wordt, blijft deze cel zelf ook gekleurd, zoals in het voorbeeld hieronder.

![Blijvenleven.png](../../OneDrive/coderdojo/Pygame of Life/images/Blijvenleven.png)

In deze afbeelding blijft de middelste cel gekleurd, want de cel wordt omgeven door 2 andere gekleurde cellen.

* Als een cel door 4 of meer gekleurde buurcellen omgeven wordt, gaat deze cel dood door 'overbevolking' (dat wil zeggen, de cel wordt wit). Als een cel door minder dan twee gekleurde buurcellen omgeven wordt, gaat deze cel ook dood, maar dan door eenzaamheid. Zie voorbeeld hieronder.

![Doodgaan.png](../../OneDrive/coderdojo/Pygame of Life/images/Doodgaan.png)

In deze afbeelding gaat de middelste cel dood, want de cel wordt door meer dan 3 of minder dan 2 gekleurde cellen omgeven.

* Als een dode cel wordt omgeven door precies 3 gekleurde buurcellen, wordt deze dode cel ook gekleurd ('geboren'), zoals in het voorbeeld hieronder.

![Geborenworden.png](../../OneDrive/coderdojo/Pygame of Life/images/Geborenworden.png)

In deze afbeelding wordt de middelste cel geboren, want de cel wordt door exact 3 gekleurde cellen omgeven.
Al deze transformaties geschieden gelijktijdig voor alle cellen.

## Het spel: eerst en vooral

Voor we van start gaan hebben we een aantal zaken nodig. Die zul je op je computer moeten installeren.

### Python

Python zelf uiteraard: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Editor

Een programma om code te schrijven, dit kan de meegeleverde REPL zijn of een andere editor.

### Pygame installeren

Pygame is een bibliotheek aan code om eenvoudig spelletjes mee te maken, zonder veel code zelf te moeten schrijven.

Je kan dit installeren door in de _commandoprompt_ het volgende in te tikken:

`pip install pygame`

Je bekomt een _commandopromt_ door in Windows het `Windows`-symbool samen met de `R` toets in te duwen, en daarna `cmd` in te tikken.

```
pip install pygame
Collecting pygame
  Obtaining dependency information for pygame from https://files.pythonhosted.org/packages/5f/0d/64b84142b477c0d7041bd93a91d4dc6d7901dad4f58323f69779c86757f5/pygame-2.5.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata
  Downloading pygame-2.5.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (13 kB)
Downloading pygame-2.5.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (14.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.0/14.0 MB 18.6 MB/s eta 0:00:00
Installing collected packages: pygame
Successfully installed pygame-2.5.2

[notice] A new release of pip is available: 23.2.1 -> 23.3.1
[notice] To update, run: pip install --upgrade pip
```

## Speelveld

### Import

Om ons sptel te maken gaan we de code inladen die `pygame` voor ons voorziet.

```python
import pygame
```

### Grootte en snelheid

We maken een aantal variabelen: eentje voor de grootte van het scherm (in pixels) en eentje voor de snelheid: 10 frames per seconde.

```python
SCHERM = BREEDTE, HOOGTE = 1280,720
SNELHEID = 10
```

### pygame

We starten daarna `pygame` op, maken een speelveld met de `SCHERM` parameter en maken een klok die de tijd van het spel zal bijhouden.

```python
pygame.init()
speelveld = pygame.display.set_mode(SCHERM)
klok = pygame.time.Clock()
```

### Spellus

De spellus is een eindeloze lus, die dus de ganse tijd herhaalt. Die maken we door `while True:` op een lijn te zetten.

In Python zetten we de lijnen eronder telkens met 4 spaties ervoor, zolang die lijnen in de lus moeten uitgevoerd worden.

- `speelveld.fill` zal het kader opvullen met zwart.
- `for event...` zorgt ervoor dat we het spel kunnen afsluiten, let hier ook telkens op de 4 spaties telkens er een nieuwe lijn komt.
- `pygame.display.flip` zal het scherm tekenen
- `klok.tick()` zegt dan weer tegen het spel dat er een volgende fase mag ingegaan worden.

```python
while True:

    speelveld.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    pygame.display.flip()
    klok.tick(SNELHEID)
```

### Raster

Om het spel duidelijker te kunnen zien gaan we een _raster_ tekenen.
Deze waarde komt vlak na de `SNELHEID` en voor de `pygame.init()` te staan:

- `TEGEL` zal de grootte zijn in pixels van elk vierkantje van de raster

```python
...
SNELHEID = 10
TEGEL = 40

pygame.init()
...
```

Daarna tekenen we de raster.

! let op de insprong van deze lijnen, die moet even ver naar rechts staan als de `pygame.display.flip()`

```python
            ...
            exit()

    [pygame.draw.line(speelveld, pygame.Color('darkslategray'), (x, 0), (x, HOOGTE)) for x in range(0, BREEDTE, TEGEL)]
    [pygame.draw.line(speelveld, pygame.Color('darkslategray'), (0, y), (BREEDTE, y)) for y in range(0, HOOGTE, TEGEL)]
    
    pygame.display.flip()
    ...
```

![raster.png](./images/raster.png)

## Het leven begint

### De eerste fase tekenen

Wij gaan _leven_ voorstellen als groene vierkantjes in de raster.

We nemen het aantal kolommen (`K`) en rijen (`R`) door de `BREEDTE` en `HOOGTE` van het speelveld te delen (`//`) door het aantal pixels van een tegel.

```python
K, R = BREEDTE // TEGEL, HOOGTE // TEGEL
```

De volgende code maakt een raster zo groot als ons speelveld en vult dit op met `0` en `1`.  Let goed op met het overnemen van de formule, een klein foutje is snel gemaakt. Het is een beetje een willekeurige formule die een leuk resultaat geeft.

```python
huidig_veld = [ [(k // (r+1) ) % 2 for k in range(K)] for r in range(R)]
```

Dit maakt de volgende tekening:
```
[
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
[0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
```
Nu nul en één zegt ons niet zo veel, het wordt mooier als we dit ook kunnen tekenen op ons speelveld.

```python
	...
    [pygame.draw.line(speelveld, pygame.Color('darkslategray'), (x, 0), (x, HOOGTE)) for x in range(0, BREEDTE, TEGEL)]
    [pygame.draw.line(speelveld, pygame.Color('darkslategray'), (0, y), (BREEDTE, y)) for y in range(0, HOOGTE, TEGEL)]
    
    for x in range(1, K - 1):
        for y in range(1, R - 1):
            if huidig_veld[y][x]:
                pygame.draw.rect(speelveld, pygame.Color('forestgreen'), (x * TEGEL + 2, y * TEGEL + 2, TEGEL - 2, TEGEL - 2))
    
    pygame.display.flip()
	...
```
![patroon.png](./images/patroon.png)

### De regels van het leven in code

Een cel in ons raster kan 2 statussen hebben: "AAN" (`1`) of "AF" (`0`). De regels kijken altijd naar een cel in verhouding tot de 8 omliggende cellen. Cellen veranderen van status tussen beurten in, volgens deze 4 regeltjes:

1. Als een cel AAN is en minder dan 2 buren heeft die ook AAN zijn, gaat de cel AF
2. Als een cel AAN is en 2 of 3 buren heeft die AAN zijn, blijft de cel AAN
3. Als een cel AAN is meer dan 3 buren heeft die AAN zijn, gaat de cel AF
4. Als een cel AF is en exact 3 buren heeft die AAN zijn, gaat de cel AAN

![regels.png](./images/regels.png)

In python code wordt dit dan als volgt geschreven. Voor elke cel in `huidig_veld` wordt volgens de positie `x` en `y` gekeken naar de status van de omliggende buren. Als de status AAN ofwel `1` is, wordt de teller `aantal_buren` met 1 verhoogd. Dit geheel is wat een functie genoemd wordt.

`... + 2` ziet er vreemd uit, maar dat is omdat `range()` telt "tot" dat getal en niet "tot en met" dat getal.

Eenmaal we het aantal actieve buren hebben, kijken we naar de status van de cel zelf en hoeveel buren er actief zijn. Aan de hand daarvan passen we de status van de cel zelf aan.

```python
def regels(huidig_veld, x, y):
    aantal_buren = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if huidig_veld[j][i]:
                aantal_buren += 1

    if huidig_veld[y][x]:
        aantal_buren -= 1
        if aantal_buren == 2 or aantal_buren == 3:
            return 1
        return 0
    else:
        if aantal_buren == 3:
            return 1
        return 0
```

### De regels toepassen

We starten met een volledige leeg veld voor de volgende "beurt":
```python
volgend_veld= [[0 for k in range(K)] for r in range(R)]
```
Tijdens het tekenen van het huidige veld, passen we ook de regels toe voor het volgende veld:
```python
volgend_veld[y][x] = regels(huidig_veld, x, y)
```
Daarna kopiëren we het volgende veld naar het huidige speelveld. Dit gebeurt nadat alles getekend werd.
```python
from copy import deepcopy
# Het 'volgende' veld wordt nu het 'huidige' veld
huidig_veld = deepcopy(volgend_veld)
```

Voor de duidelijkheid het complete programma van voor naar achter:
```python
import pygame
from copy import deepcopy

SCHERM = BREEDTE, HOOGTE = 1280,720
SNELHEID = 10
TEGEL = 40
K, R = BREEDTE // TEGEL, HOOGTE // TEGEL

pygame.init()
speelveld = pygame.display.set_mode(SCHERM)
klok = pygame.time.Clock()

huidig_veld = [[(k + r) % 2 for k in range(K-1)] for r in range(R-1)]
volgend_veld= [[0 for k in range(K)] for r in range(R)]

def regels(huidig_veld, x, y):
    aantal_buren = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if huidig_veld[j][i]:
                aantal_buren += 1

    if huidig_veld[y][x]:
        aantal_buren -= 1
        if aantal_buren == 2 or aantal_buren == 3:
            return 1
        return 0
    else:
        if aantal_buren == 3:
            return 1
        return 0

while True:

    speelveld.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(speelveld, pygame.Color('darkslategray'), (x, 0), (x, HOOGTE)) for x in range(0, BREEDTE, TEGEL)]
    [pygame.draw.line(speelveld, pygame.Color('darkslategray'), (0, y), (BREEDTE, y)) for y in range(0, HOOGTE, TEGEL)]
    
    for x in range(1, K - 1):
        for y in range(1, R - 1):
            if huidig_veld[y][x]:
                pygame.draw.rect(speelveld, pygame.Color('forestgreen'), (x * TEGEL + 2, y * TEGEL + 2, TEGEL - 2, TEGEL - 2))
            volgend_veld[y][x] = regels(huidig_veld, x, y)
    
    # Het 'volgende' veld wordt nu het 'huidige' veld
    huidig_veld = deepcopy(volgend_veld)
    
    pygame.display.flip()
    klok.tick(SNELHEID)

```

### Willekeurige start

Bovenaan importeren we de keuzefunctie `choice` die ons zal toelaten een willekeurige `1` of `0` te kiezen:
```python
from random import choice
```
Daarna passen we de lijn aan die het initiële veld maakt:
```python
huidig_veld = [[choice([0, 1]) for k in range(K)] for r in range(R)]
```

### Kleinere cellen of snellere evolutie

Speel eens met de waarde van `TEGEL`, probeer bijvoorbeeld eens 20 of 10.

Speel ook eens met de waarde van `SNELHEID`, probeer dit eens hoger te zetten om snellere evolutie te krijgen.

![random.png](./images/random.png)

> Bronvermelding:
> 
> Dit spelletje is gebaseerd op https://github.com/StanislavPetrovV/Python-Game-of-life/ (MIT licentie). Dezelfde code werd gebruikt in een Youtube video: https://www.youtube.com/watch?v=lk1_h2_GLv8

[^1]: [Game of Life, Wikipedia](https://nl.wikipedia.org/wiki/Game_of_Life) 
