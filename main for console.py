# Importing Modules
from itertools import cycle
import pygame
from pygame.locals import *
import random
import sys
import webbrowser
import time


# Declaring Variables
FPS = 30
SCREENWIDTH = 350
SCREENHEIGHT = 660
PIPEGAPSIZE = 100
BASEY = SCREENHEIGHT * 0.83
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
FPSCLOCK = pygame.time.Clock()
SPRITES, SOUNDS, HTMSKS = {}, {}, {}


# Version control for range
try:
    xrange
except NameError:
    xrange = range


# Declaring Button Class
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        return action


# Initializing Pygame
pygame.init()


# Setting up Caption
pygame.display.set_caption("Redex-K19")


# Loading Sprites Contents
SPRITES["background"] = pygame.image.load(
    "gallery/sprites/background.png"
).convert_alpha()
SPRITES["start"] = pygame.image.load("gallery/sprites/start.png").convert_alpha()
SPRITES["exit"] = pygame.image.load("gallery/sprites/exit.png").convert_alpha()
SPRITES["dev"] = pygame.image.load("gallery/sprites/dev.png").convert_alpha()
SPRITES["title"] = pygame.image.load("gallery/sprites/title.png").convert_alpha()
SPRITES["instructions"] = pygame.image.load(
    "gallery/sprites/instructions.png"
).convert_alpha()
SPRITES["credits"] = pygame.image.load("gallery/sprites/credits.png").convert_alpha()
SPRITES["next"] = pygame.image.load("gallery/sprites/next.png").convert_alpha()
SPRITES["back"] = pygame.image.load("gallery/sprites/back.png").convert_alpha()
SPRITES["mainmenu"] = pygame.image.load("gallery/sprites/mainmenu.png").convert_alpha()
SPRITES["replay"] = pygame.image.load("gallery/sprites/Replay.png").convert_alpha()
SPRITES["icon"] = pygame.image.load("gallery/sprites/icon256.ico").convert_alpha()

SPRITES["github"] = pygame.image.load("gallery/sprites/github.png").convert_alpha()
SPRITES["mail"] = pygame.image.load("gallery/sprites/mail.png").convert_alpha()
SPRITES["twitter"] = pygame.image.load("gallery/sprites/twitter.png").convert_alpha()
SPRITES["telegram"] = pygame.image.load("gallery/sprites/telegram.png").convert_alpha()
SPRITES["linkedin"] = pygame.image.load("gallery/sprites/linkedin.png").convert_alpha()
SPRITES["replit"] = pygame.image.load("gallery/sprites/replit.png").convert_alpha()
SPRITES["discord"] = pygame.image.load("gallery/sprites/discord.png").convert_alpha()
SPRITES["developerContact"] = pygame.image.load(
    "gallery/sprites/developerContact.png"
).convert_alpha()


# Loading Sprites Numbers
SPRITES["numbers"] = (
    pygame.image.load("gallery/sprites/0.png").convert_alpha(),
    pygame.image.load("gallery/sprites/1.png").convert_alpha(),
    pygame.image.load("gallery/sprites/2.png").convert_alpha(),
    pygame.image.load("gallery/sprites/3.png").convert_alpha(),
    pygame.image.load("gallery/sprites/4.png").convert_alpha(),
    pygame.image.load("gallery/sprites/5.png").convert_alpha(),
    pygame.image.load("gallery/sprites/6.png").convert_alpha(),
    pygame.image.load("gallery/sprites/7.png").convert_alpha(),
    pygame.image.load("gallery/sprites/8.png").convert_alpha(),
    pygame.image.load("gallery/sprites/9.png").convert_alpha(),
)


# Loading Sprites Player/Rocket
SPRITES["player"] = (
    pygame.image.load("gallery/sprites/rocketa.png").convert_alpha(),
    pygame.image.load("gallery/sprites/rocketb.png").convert_alpha(),
)


# Loading Poles
SPRITES["pipe"] = (
    pygame.transform.flip(
        pygame.image.load("gallery/sprites/pole.png").convert_alpha(), False, True
    ),
    pygame.image.load("gallery/sprites/pole.png").convert_alpha(),
)


# Loading Sprites InGame
SPRITES["gameover"] = pygame.image.load("gallery/sprites/gameover.png").convert_alpha()
SPRITES["message"] = pygame.image.load("gallery/sprites/message.png").convert_alpha()
SPRITES["base"] = pygame.image.load("gallery/sprites/base.png").convert_alpha()
SPRITES["score"] = pygame.image.load("gallery/sprites/score.png").convert_alpha()


# Loading Sounds
pygame.mixer.music.load("gallery/sounds/opening.mp3")
SOUNDS["click"] = pygame.mixer.Sound("gallery/sounds/click.mp3")
SOUNDS["points"] = pygame.mixer.Sound("gallery/sounds/points.mp3")
SOUNDS["gameover"] = pygame.mixer.Sound("gallery/sounds/gameover.mp3")
SOUNDS["die"] = pygame.mixer.Sound("gallery/sounds/die.mp3")


# Creating Buttons
start_button = Button(66.942, 467.914, SPRITES["start"])
dev_button = Button(66.9, 531.874, SPRITES["dev"])
exit_button = Button(172.596, 531.874, SPRITES["exit"])
next_button = Button(217.965, 575.619, SPRITES["next"])
back_button = Button(29.5, 575.619, SPRITES["back"])
main_menu = Button(22.660, 591.115, SPRITES["mainmenu"])
replay = Button(221.978, 593.115, SPRITES["replay"])
github_button = Button(54.351, 200.558, SPRITES["github"])
mail_button = Button(168.969, 185.313, SPRITES["mail"])
twitter_button = Button(54.220, 326.632, SPRITES["twitter"])
telegram_button = Button(153.708, 317.475, SPRITES["telegram"])
linkedin_button = Button(217.607, 259.701, SPRITES["linkedin"])
replit_button = Button(243.417, 336.321, SPRITES["replit"])
discord_button = Button(160.298, 395.599, SPRITES["discord"])


# Setting up icon
pygame.display.set_icon(SPRITES["icon"])


# Defining main function - Level 0 Screen
def main():
    try:
        pygame.mixer.music.unpause()
    except:
        pass

    pygame.mixer.music.set_volume(1.0)

    while True:
        SCREEN.fill("black")
        SCREEN.blit(SPRITES["background"], (0, 0))
        SCREEN.blit(SPRITES["title"], (19, 47.97))

        if start_button.draw():
            pygame.mixer.Sound(SOUNDS["click"]).play()
            instructions()

        if exit_button.draw():
            pygame.mixer.Sound(SOUNDS["click"]).play()
            pygame.quit()
            sys.exit()

        if dev_button.draw():
            pygame.mixer.Sound(SOUNDS["click"]).play()
            developerContact()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# Defining mainx function - Level 02 Screen
def mainx():
    pygame.mixer.music.set_volume(0.1)

    while True:
        HTMSKS["pipe"] = (
            getHitMask(SPRITES["pipe"][0]),
            getHitMask(SPRITES["pipe"][1]),
        )

        HTMSKS["player"] = (
            getHitMask(SPRITES["player"][0]),
            getHitMask(SPRITES["player"][1]),
        )

        movement = welcomeAnimation()
        crash = mainGame(movement)
        gameOverScreen(crash)


# Loading Meathods of main Function


# Loading Instruction page - Level 01 Screen
def instructions():
    while True:
        # pygame.event.get()
        SCREEN.fill("black")
        SCREEN.blit(SPRITES["background"], (0, 0))
        SCREEN.blit(SPRITES["instructions"], (29.5, 44.979))
        SCREEN.blit(SPRITES["credits"], (33.052, 368.994))

        if next_button.draw():
            pygame.mixer.Sound(SOUNDS["click"]).play()
            mainx()

        if back_button.draw():
            pygame.mixer.Sound(SOUNDS["click"]).play()
            main()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# Loading Developer Contact Screen - Level 01 Screen
def developerContact():
    while True:
        SCREEN.fill("black")
        SCREEN.blit(SPRITES["background"], (0, 0))
        SCREEN.blit(SPRITES["developerContact"], (15.721, 52.105))

        if github_button.draw():
            pygame.mixer.music.pause()
            webbrowser.open_new("https://github.com/k-arthik-r")

        if mail_button.draw():
            pygame.mixer.music.pause()
            webbrowser.open_new(
                "https://mail.google.com/mail/u/0/?to=voidex.developer@gmail.com&fs=1&tf=cm"
            )

        if twitter_button.draw():
            pygame.mixer.music.pause()
            webbrowser.open_new(
                "https://twitter.com/r_karthik__?t=qCYUBHYTrQUKm36LYTE7zw&s=08"
            )

        if telegram_button.draw():
            pygame.mixer.music.pause()
            webbrowser.open_new("https://t.me/karthik_r_gowda")

        if linkedin_button.draw():
            pygame.mixer.music.pause()
            webbrowser.open_new("https://www.linkedin.com/in/k-arthik")

        if replit_button.draw():
            pygame.mixer.music.pause()
            webbrowser.open_new("https://replit.com/@Karthik-R-Gowda")

        if discord_button.draw():
            pygame.mixer.music.pause()
            webbrowser.open_new(
                "https://drive.google.com/file/d/14PmV-X-qTj5ZptcBfDYgs2BixPIH7Clw/view?usp=drivesdk"
            )

        if back_button.draw():
            pygame.mixer.Sound(SOUNDS["click"]).play()
            main()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# Loading Meathods of mainx function


# Loading GetHitMask Function
def getHitMask(image):
    mask = []

    for x in xrange(image.get_width()):
        mask.append([])
        for y in xrange(image.get_height()):
            mask[x].append(bool(image.get_at((x, y))[3]))
    return mask


# Loading PlayerSpace function
def playerSpace(playerSpace):
    if abs(playerSpace["val"]) == 8:
        playerSpace["dir"] *= -1
    if playerSpace["dir"] == 1:
        playerSpace["val"] += 1
    else:
        playerSpace["val"] -= 1


# Loading Random Pipe function
def getRandomPipe(score):
    PIPEGAPSIZE = 180
    if score >= 10 and score < 20:
        PIPEGAPSIZE = 160
    if score >= 20:
        PIPEGAPSIZE = 150
    if score >= 30:
        PIPEGAPSIZE = 140
    if score >= 40:
        PIPEGAPSIZE = 130
    if score >= 50:
        PIPEGAPSIZE = 120
    if score >= 500:
        PIPEGAPSIZE = 110
    if score >= 1000:
        PIPEGAPSIZE = 90
    gapY = random.randrange(0, int(BASEY * 0.45 - PIPEGAPSIZE))  # 0.6
    gapY += int(BASEY * 0.4)
    pipeHeight = SPRITES["pipe"][0].get_height()
    pipeX = SCREENWIDTH + 10

    return [
        {"x": pipeX, "y": gapY - pipeHeight},
        {"x": pipeX, "y": gapY + PIPEGAPSIZE},
    ]


# Loading Crashcheck function
def crashCheck(player, upperPipes, lowerPipes):
    pi = player["index"]
    player["w"] = SPRITES["player"][0].get_width()
    player["h"] = SPRITES["player"][0].get_height()

    if player["y"] + player["h"] >= BASEY - 1:
        pygame.mixer.Sound.play(SOUNDS["die"])
        return ["True", "True"]
    else:
        playerRect = pygame.Rect(player["x"], player["y"], player["w"], player["h"])
        pipeW = SPRITES["pipe"][0].get_width()
        pipeH = SPRITES["pipe"][0].get_height()

    for uPipe, lPipe in zip(upperPipes, lowerPipes):
        uPipeRect = pygame.Rect(uPipe["x"], uPipe["y"], pipeW, pipeH)
        lPipeRect = pygame.Rect(lPipe["x"], lPipe["y"], pipeW, pipeH)

        pHitMask = HTMSKS["player"][pi]

        uCollide = pixelCollision(playerRect, uPipeRect, pHitMask)
        lCollide = pixelCollision(playerRect, lPipeRect, pHitMask)

        if uCollide or lCollide:
            pygame.mixer.Sound.play(SOUNDS["die"])
            return [True, False]

    return [False, False]


# Loading Pixel Collision Function
def pixelCollision(rect1, rect2, hitmask1):
    rect = rect1.clip(rect2)
    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y

    for x in xrange(rect.width):
        for y in xrange(rect.height):
            if hitmask1[x1 + x][y1 + y]:
                return True
    return False


# Defing welcome animation function
def welcomeAnimation():
    playerIndex = 0
    playerIndexGen = cycle([0, 1])

    loopiterator = 0

    playerx = int(SCREENWIDTH * 0.2)
    playery = int((SCREENHEIGHT - SPRITES["player"][0].get_height()) / 2)

    messagex = messagey = 0

    basex = 0
    baseShift = (SPRITES["base"].get_width()) - SPRITES["background"].get_width()

    palyerSpaceValues = {"val": 0, "dir": 1}

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return {
                    "playery": playery + palyerSpaceValues["val"],
                    "basex": basex,
                    "playerIndexGen": playerIndexGen,
                }

        if (loopiterator + 1) % 5 == 0:
            playerIndex = next(playerIndexGen)
        loopiterator = (loopiterator + 1) % 30
        basex = -((-basex + 4) % baseShift)
        playerSpace(palyerSpaceValues)

        SCREEN.blit(SPRITES["background"], (0, 0))
        SCREEN.blit(
            SPRITES["player"][playerIndex],
            (playerx, playery + palyerSpaceValues["val"]),
        )
        SCREEN.blit(SPRITES["message"], (messagex, messagey))
        SCREEN.blit(SPRITES["base"], (basex, BASEY))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# Defining mainGame Screen
def mainGame(movement):
    score = playerIndex = loopIter = 0
    playerIndexGen = movement["playerIndexGen"]
    playerx, playery = int(SCREENWIDTH * 0.2), movement["playery"]

    basex = movement["basex"]
    baseShift = (SPRITES["base"].get_width()) - SPRITES["background"].get_width()
    newPipe1 = getRandomPipe(0)
    newPipe2 = getRandomPipe(0)

    upperPipes = [
        {"x": SCREENWIDTH + 200, "y": newPipe1[0]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH / 2), "y": newPipe2[0]["y"]},
    ]
    lowerPipes = [
        {"x": SCREENWIDTH + 200, "y": newPipe1[1]["y"]},
        {"x": SCREENWIDTH + 200 + (SCREENWIDTH / 2), "y": newPipe2[1]["y"]},
    ]
    dt = FPSCLOCK.tick(FPS) / 1000
    pipeVelX = -128 * dt

    playerVelocity = -9
    playerMaxVelocity = 10
    playerMinVelocity = -8
    playerAccelarationY = 1
    playerRotation = 45
    playerRotationVelocity = 3
    playerRotationThreshold = 20
    playerFlapAcc = -9
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > -2 * SPRITES["player"][0].get_height():
                    playerVelocity = playerFlapAcc
                    playerFlapped = True

        crashTest = crashCheck(
            {"x": playerx, "y": playery, "index": playerIndex}, upperPipes, lowerPipes
        )

        if crashTest[0]:
            return {
                "y": playery,
                "groundCrash": crashTest[1],
                "basex": basex,
                "upperPipes": upperPipes,
                "lowerPipes": lowerPipes,
                "score": score,
                "playerVelocity": playerVelocity,
                "playerRot": playerRotation,
            }

        playerMidPos = playerx + SPRITES["player"][0].get_width() / 2

        for pipe in upperPipes:
            pipeMidPos = pipe["x"] + SPRITES["pipe"][0].get_width() / 2
            if (
                pipeMidPos <= playerMidPos < pipeMidPos + 4
            ):  # if its number increases then 'abnormal inscrese' in score can be observed.
                score += 1
                pygame.mixer.Sound.play(SOUNDS["points"])

        if (loopIter + 1) % 5 == 0:
            playerIndex = next(playerIndexGen)
        loopIter = (loopIter + 1) % 30
        basex = -((-basex + 4.5) % baseShift)

        if playerRotation > -90:
            playerRotation -= playerRotationVelocity

        if playerVelocity < playerMaxVelocity and not playerFlapped:
            playerVelocity += playerAccelarationY

        if playerFlapped:
            playerFlapped = False
            playerRotation = 45

        playerHeight = SPRITES["player"][playerIndex].get_height()
        playery += min(playerVelocity, BASEY - playery - playerHeight)

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            uPipe["x"] += pipeVelX
            lPipe["x"] += pipeVelX

        if 3 > len(upperPipes) > 0 and 0 < upperPipes[0]["x"] < 5:
            newPipe = getRandomPipe(score)
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        if len(upperPipes) > 0 and upperPipes[0]["x"] < -SPRITES["pipe"][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        SCREEN.blit(SPRITES["background"], (0, 0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(SPRITES["pipe"][0], (uPipe["x"], uPipe["y"]))
            SCREEN.blit(SPRITES["pipe"][1], (lPipe["x"], lPipe["y"]))

        SCREEN.blit(SPRITES["base"], (basex, BASEY))
        # print score so player overlaps the score
        showRecurringScore(score)

        # Player rotation has a Thrust
        visibleRot = playerRotationThreshold
        if playerRotation <= playerRotationThreshold:
            visibleRot = playerRotation

        playerSurface = pygame.transform.rotate(
            SPRITES["player"][playerIndex], visibleRot
        )

        SCREEN.blit(playerSurface, (playerx, playery))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# Defining Gameover Screen Level 03 Screen
def gameOverScreen(crash):
    try:
        time.sleep(1)
    except:
        pass

    score = crash["score"]
    playerx = SCREENWIDTH * 0.2
    playery = crash["y"]
    playerHeight = SPRITES["player"][0].get_height()
    playerVelocity = crash["playerVelocity"]
    playerAccelarationY = 2
    playerRotation = crash["playerRot"]
    playerRotationVelocity = 7

    basex = crash["basex"]

    upperPipes, lowerPipes = crash["upperPipes"], crash["lowerPipes"]

    pygame.mixer.Sound.play(SOUNDS["gameover"])
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery + playerHeight >= -1:
                    return

        if playery + playerHeight < BASEY - 1:
            playery += min(playerVelocity, BASEY - playery - playerHeight)

        if playerVelocity < 15:
            playerVelocity += playerAccelarationY

        if not crash["groundCrash"]:
            if playerRotation > -90:
                playerRotation -= playerRotationVelocity

        SCREEN.blit(SPRITES["background"], (0, 0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(SPRITES["pipe"][0], (uPipe["x"], uPipe["y"]))
            SCREEN.blit(SPRITES["pipe"][1], (lPipe["x"], lPipe["y"]))

        SCREEN.blit(SPRITES["base"], (basex, BASEY))

        playerSurface = pygame.transform.rotate(SPRITES["player"][1], playerRotation)
        SCREEN.blit(playerSurface, (playerx, playery))
        SCREEN.blit(SPRITES["gameover"], (34.512, 76.195))
        SCREEN.blit(SPRITES["score"], (29.216, 384.484))

        if main_menu.draw():
            pygame.mixer.Sound.play(SOUNDS["click"])
            main()

        if replay.draw():
            pygame.mixer.Sound.play(SOUNDS["click"])
            mainx()

        showfinalScore(score)

        FPSCLOCK.tick(FPS)
        pygame.display.update()


# Function to show final Score
def showfinalScore(score):
    sscoreDigits = [int(x) for x in list(str(score))]
    totalwidth = 0
    for digit in sscoreDigits:
        totalwidth += SPRITES["numbers"][digit].get_width()

    Xoffset = 4 * ((SCREENWIDTH - totalwidth) / 5)
    for digit in sscoreDigits:
        SCREEN.blit(SPRITES["numbers"][digit], (Xoffset, 388.484))
        Xoffset += SPRITES["numbers"][digit].get_width()


# Function to show Recurring Score / Updating score
def showRecurringScore(score):
    scoreDigits = [int(x) for x in list(str(score))]
    totalWidth = 0
    for digit in scoreDigits:
        totalWidth += SPRITES["numbers"][digit].get_width()

    Xoffset = (SCREENWIDTH - totalWidth) / 2

    for digit in scoreDigits:
        SCREEN.blit(SPRITES["numbers"][digit], (Xoffset, SCREENHEIGHT * 0.1))
        Xoffset += SPRITES["numbers"][digit].get_width()


# Starts the Execution of Entire Program
if __name__ == "__main__":
    pygame.mixer.music.play(-1)
    main()
