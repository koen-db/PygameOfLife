# Pygame of Life

## Conway's Game of Life

## Eerst en vooral

Voor we van start gaan hebben we een aantal zaken nodig. Die zul je op je computer moeten installeren.

### Python

Python zelf uiteraard: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Editor

Een programma om code te schrijven, dit kan de meegeleverde REPL zijn of een andere editor.

### Pygame installeren

Pygame is een bibliotheek aan code om eenvoudig spelletjes mee te maken, zonder veel code zelf te moeten schrijven.

Je kan dit installeren door in de _commandoprompt_ het volgende in te tikken:

`pip install pygame`

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

Om ons speelveld te maken gaan we de code inladen die `pygame` voor ons voorziet.

```python
import pygame
```

### 




Bronvermelding:

Dit spelletje is gebaseerd op https://github.com/StanislavPetrovV/Python-Game-of-life/ (MIT licentie). Dezelfde code werd gebruikt in een Youtube video: https://www.youtube.com/watch?v=lk1_h2_GLv8