import pyautogui as pg
from time import sleep

# opening chrome
pg.click(954, 1059)
sleep(3)

# opening dino game
pg.click(1329,530)
pg.typewrite(r"chrome://dino/")
sleep(1)
pg.press("enter")
sleep(1)

# starting the game
pg.press("space")
sleep(1)

# running continuously
while True:
    pg.keyDown("space")
    def run():
        pg.press("space", interval = 0.05,  presses=20)

        if pg.keyUp == True:
            pg.press("space",interval = 0.10, presses=20)
              
    run()
