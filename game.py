# Nainesh Chawda, Zayd Qadri, Atif Haque
# October 25th, 2021
# This program will create a obstacle course-like game

app.background=rgb(255,253,208)
app.stepsPerSecond = 20
randX = randrange(85,315)
randY = randrange(155,270)

# This section includes the groups for the title screen.
    
border = Group(
    Rect(70,90,260,50),
    Rect(70,275,260,50),
    Rect(10,135,60,50),
    Rect(330,135,60,50),
    Rect(330,240,60,50),
    Rect(10,240,60,50),
    Rect(0,180,10,60,),
    Rect(380,180,10,60),
    )
border.fill=rgb(255,253,208)

instructions = Group(
    Rect(240, 250, 120, 65, fill = 'lightGreen', border='black', borderWidth = 3),
    Label("Instructions", 301, 280, size=17, bold = True),
    )
    
start = Group (
    Rect(40,250,120,65,fill='lightGreen',border='black',borderWidth=3),
    Label('Start',100,280,fill='black',size=20, bold=True),
    )
    
title = Group(
    Label("Coin Collector", 200,95, fill='blue', size=35, bold=True),
    instructions,
    start,
    )
homePage = Group(
    instructions, start, title)
    
# This code contains what will show up if the title screen buttons are clicked.

gameBackground = Rect(0,0,400,400, fill=rgb(255,253,208), opacity=0)

closeButton = Group(
    Rect(145,300,120,65,fill='lightGreen',border='black',borderWidth=3),
    Label('Close',205,330,fill='black',size=20, bold=True),
    )
closeButton.opacity=0

instructionsText = Group(
    Label("How To Play", 200, 60, size=25, bold=True),
    Label("1. Move around using the arrow keys.", 170, 110, size = 18),
    Label("2. Collect the coins to open up the end.", 175,140,size=18),
    Label("3. You can lose by getting hit by the obstacle.", 200,170,size=18),
    Label("4. If time runs out, you automatically lose.",185,200,size=18),
    )
instructionsText.opacity=0

# This code will start the game when the button is clicked 

coin = Circle(85,165,5, fill='yellow')
coin.opacity=0
    
level = Group(
    Rect(12,185,60,55, fill='lightGreen', border='black', borderWidth = 2),
    Label("Level 1", 200,80, fill='blue', size=30, bold=True),
    Rect(70, 140, 260, 145, fill='white', border='black', borderWidth = 2),
    Line(71, 187, 71, 238, fill='lightGreen', lineWidth = 2),
    Line(329, 187, 329, 238, fill='lightGreen', lineWidth = 2),
    Rect(328,185,60,55, fill='lightGreen', border='black', borderWidth = 2),
    coin,
        )
level.opacity = 0
    
character = Rect(27, 205, 15, 15, fill='red')
character.opacity = 0
character.isHit = False
    
obstaclesTop = Group(
    Circle(90,160,7, fill='blue'),
    Circle(140,160,7, fill='blue'),
    Circle(190,160,7, fill='blue'),
    Circle(240,160,7, fill='blue'),
    Circle(290,160,7, fill='blue'),
    )
obstaclesTop.opacity=0
obstaclesTop.speedY = 3

obstaclesBottom = Group(
    Circle(115,265,7, fill='blue'),
    Circle(165,265,7, fill='blue'),
    Circle(215,265,7, fill='blue'),
    Circle(265,265,7, fill='blue'),
    Circle(314,265,7, fill='blue'),
    )
obstaclesBottom.opacity=0
obstaclesBottom.speedY = -3

obstacles = Group (obstaclesTop, obstaclesBottom)

# This code creates the page after the player wins or loses the game

gameOverBackground = Rect (0,0, 400, 400)
gameOverBackground.opacity = 0

homeButton = Group(
    Rect(43,200,120,65,fill='lightGreen',border='black',borderWidth=3),
    Label('Home',105,230,fill='black',size=20, bold=True),
    )
homeButton.opacity=0

replayButton = Group(
    Rect(235,200,120,65,fill='lightGreen',border='black',borderWidth=3),
    Label('Play Again',295,230,fill='black',size=20, bold=True),
    )
replayButton.opacity=0

gameOver = Group(
    Label ("Game Over", 200, 100, fill= 'yellow', size=35, bold=True),
    homeButton,
    replayButton,
    )
gameOver.opacity = 0

youWin = Group(
    Label ("Victory!", 200, 100, fill= 'yellow', size=35, bold=True),
    homeButton,
    replayButton,
    )
youWin.opacity = 0
    
# This onMousePress will control all clicking functions

def onMousePress(mouseX,mouseY):
    if instructions.hits(mouseX,mouseY) == True:
        gameBackground.opacity = 100
        closeButton.opacity=100
        instructionsText.opacity=100
        
    if closeButton.hits(mouseX,mouseY) == True:
        gameBackground.opacity = 0
        closeButton.opacity=0
        instructionsText.opacity=0
    
    if start.hits(mouseX,mouseY) == True:
        app.paused = False
        gameBackground.opacity=100
        level.opacity = 100
        obstaclesTop.opacity=100
        obstaclesBottom.opacity=100
        character.opacity = 100
        character.centerX = 32
        character.centerY = 212
        obstaclesTop.centerY = 160
        obstaclesBottom.centerY = 265
        coin.centerX =
        coin.centerY =
        
    if homeButton.hits(mouseX,mouseY) == True:
        gameOverBackground.opacity = 0
        gameBackground.opacity = 0
        title.opacity = 100
        start.opacity = 100
        instructions.opacity=100
        homeButton.opacity = 0
        replayButton.opacity = 0
        obstacles.opacity = 0
        level.opacity = 0
        character.opacity = 0
        gameOver.opacity = 0
        coin.opacity=0
        
        
    if replayButton.hits(mouseX,mouseY) == True:
        app.paused = False
        gameOver.opacity = 0
        gameOverBackground.opacity = 0
        homeButton.opacity = 0
        replayButton.opacity = 0
        character.centerX = 32
        character.centerY = 212
        obstaclesTop.centerY = 160
        obstaclesBottom.centerY = 265
        coin.opacity=100
    
def onKeyPress(key):
    if (key == 'enter'):
        gameBackground.opacity = 0
        closeButton.opacity= 0
        instructionsText.opacity=0

# This will make the obstacles move up and down constantly.

def onStep():
    obstaclesTop.centerY += obstaclesTop.speedY
    obstaclesBottom.centerY += obstaclesBottom.speedY
    if obstaclesTop.centerY > 265:
        obstaclesTop.speedY = -3
    if obstaclesTop.centerY < 160:
        obstaclesTop.speedY = 3
    
    if obstaclesBottom.centerY < 160:
        obstaclesBottom.speedY = 3
    if obstaclesBottom.centerY > 265:
        obstaclesBottom.speedY = -3
    
# This code will allow the arrow keys to move the character around

def onKeyHold(key):
    if 'right' in key:
        character.centerX += 6

    if 'left' in key:
        character.centerX -= 6
    
    if 'up' in key:
        character.centerY -= 6
        
    if 'down' in key:
        character.centerY += 6

    # This code will have the collision aspect in the game
    
    if (character.hitsShape(obstacles) == True):
        app.paused = True
        gameBackground.opacity = 100
        gameOver.opacity = 100
        gameOverBackground.opacity = 85
        homeButton.opacity = 100
        replayButton.opacity = 100
        
    
    if character.hitsShape(coin) == True:
        coin.opacity=0
        
    if (character.hitsShape(Rect(328,185,60,55, fill='lightGreen', border='black', borderWidth = 2, opacity = 0)) == True):
        app.paused = True
        Rect(328,185,60,55, fill='lightGreen', border='black', borderWidth = 2).opacity = 0
        gameBackground.opacity = 100
        youWin.opacity = 100
        gameOverBackground.opacity = 85
        homeButton.opacity = 100
        replayButton.opacity = 100
        
