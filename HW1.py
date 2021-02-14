import sys
import random
import math
import numpy

#Get Game Board from input
print(sys.argv)
f=open(sys.argv[1])
game = f.readlines()
gameSize = game[0].split()
gameBoard2 = []
for a in range(int(gameSize[0])):
  splitted = game[a+1].split()
  gameBoard2.append(list(splitted[0]))
gameBoard = numpy.transpose(gameBoard2)

#Game Variables
treasureLocations = { '.': [], '$' : [], '*' : [] }
completedRounds = 0
maxScore = 0
score = 0
actManMoves = ""
gameNotFinished = True
initialDirections = game[int(gameSize[0])+1].strip('\n')
DunkyLocations = game[int(gameSize[0])+2].split()
listDunkyLocations = []
runkyMoveList = game[int(gameSize[0])+3].strip('\n')
runkyCurMove = 0
dunkyCurTarget = 0
actManLocation = []
punkyLocation = []
bunkyLocation = []
dunkyLocation = []
runkyLocation = []
actManDirection = -1
punkyDirection = initialDirections[0]
bunkyDirection = initialDirections[1]
dunkyDirection = initialDirections[2]
runkyDirection = initialDirections[3]
#Get's dunky's target locations
i=1
while (i < len(DunkyLocations)):
  listDunkyLocations.append([DunkyLocations[i],DunkyLocations[i+1]])
  i+=2


#Check if player and ghost are on the same game block
def playerDead(i,j):
  if(i == punkyLocation[0] and j == punkyLocation[1]):
    gameNotFinished = True
    gameBoard[i][j] = 'X'
    return True
  elif(i == bunkyLocation[0] and j == bunkyLocation[1]):
    gameNotFinished = True
    gameBoard[i][j] = 'X'
    return True
  elif(i == dunkyLocation[0] and j == dunkyLocation[1]):
    gameNotFinished = True
    gameBoard[i][j] = 'X'
    return True
  elif(i == runkyLocation[0] and j == runkyLocation[1]):
    gameNotFinished = True
    gameBoard[i][j] = 'X'
    return True
  return False

def checkIfOtherGhostsOccupySpot(i,j):
  numGhosts = 0
  if(i == punkyLocation[0] and  j == punkyLocation[1]):
    numGhosts +=1
  if(i == bunkyLocation[0] and j == bunkyLocation[1]):
    numGhosts +=1
  if(i == dunkyLocation[0] and j == dunkyLocation[1]):
    numGhosts +=1
  if(i == runkyLocation[0] and j == runkyLocation[1]):
    numGhosts +=1
  return numGhosts

def checkIfTreasureCollected(i,j):
  for treasureLocation in treasureLocations['.']:
    if(treasureLocation[0] == i and treasureLocation[1] == j):
      return '.'
  for treasureLocation in treasureLocations['$']:
    if(treasureLocation[0] == i and treasureLocation[1] == j):
      return '$'
  for treasureLocation in treasureLocations['*']:
    if (treasureLocation[0] == i and treasureLocation[1] == j):
      return '*'
  return ' '

def findOtherGhostOnSpot(i,j):
  if(i == punkyLocation[0] and j == punkyLocation[1]):
    return 'P'
  elif(i == bunkyLocation[0] and j == bunkyLocation[1]):
    return 'B'
  elif(i == dunkyLocation[0] and j == dunkyLocation[1]):
    return 'D'
  elif(i == runkyLocation[0] and j == runkyLocation[1]):
    return 'R'
  else:
    return checkIfTreasureCollected(i,j)

def printGameBoard(board):
  printedBoard = numpy.transpose(gameBoard)
  for a in range(len(printedBoard)):
    line = ""
    for b in range(len(printedBoard[a])):
      line += printedBoard[a][b]
    print(line)
  print()

def checkNumMoves(i,j):
  numMoves = 0
  if(gameBoard[i][j-1] != '#'):
    numMoves +=1
  if(gameBoard[i+1][j] != '#'):
    numMoves +=1
  if(gameBoard[i][j+1] != '#'):
    numMoves +=1
  if(gameBoard[i-1][j] != '#'):
    numMoves +=1
  return numMoves


for i in range(len(gameBoard)):
  for j in range(len(gameBoard[i])):
    if(gameBoard[i][j] == 'A'):
      actManLocation.append(i)
      actManLocation.append(j)
    elif(gameBoard[i][j] == 'P'):
      punkyLocation.append(i)
      punkyLocation.append(j)
    elif(gameBoard[i][j] == 'B'):
      bunkyLocation.append(i)
      bunkyLocation.append(j)
    elif(gameBoard[i][j] == 'D'):
      dunkyLocation.append(i)
      dunkyLocation.append(j)
    elif(gameBoard[i][j] == 'R'):
      runkyLocation.append(i)
      runkyLocation.append(j)
    elif(gameBoard[i][j] == '.'):
      treasureLocations['.'].append([i,j])
    elif(gameBoard[i][j] == '$'):
      treasureLocations['$'].append([i,j])
    elif(gameBoard[i][j] == '*'):
      treasureLocations['*'].append([i,j])

print("SCORE : "+str(score) +"    TURN: "+str(completedRounds))
printGameBoard(gameBoard)
while gameNotFinished:
  for entity in range(5):
    if(entity == 0):  #Act-Man makes move
      if(checkNumMoves(actManLocation[0],actManLocation[1]) == 1):
        if(gameBoard[actManLocation[0]][actManLocation[1]-1] != '#'):
          gameBoard[actManLocation[0]][actManLocation[1]] = ' '
          actManLocation = [actManLocation[0],actManLocation[1]-1]
          actManMoves += 'U'
          actManDirection = 0
        elif(gameBoard[actManLocation[0]+1][actManLocation[1]] != '#'):
          gameBoard[actManLocation[0]][actManLocation[1]] = ' '
          actManLocation = [actManLocation[0]+1,actManLocation[1]]
          actManMoves += 'R'
          actManDirection = 1
        elif(gameBoard[actManLocation[0]][actManLocation[1]+1] != '#'):
          gameBoard[actManLocation[0]][actManLocation[1]] = ' '
          actManLocation = [actManLocation[0],actManLocation[1]+1]
          actManMoves += 'D'
          actManDirection = 2
        elif(gameBoard[actManLocation[0]-1][actManLocation[1]] != '#'):
          gameBoard[actManLocation[0]][actManLocation[1]] = ' '
          actManLocation = [actManLocation[0]-1,actManLocation[1]]
          actManMoves += 'L'
          actManDirection = 3
      else:
        while True:
          getMove = input()
          move = int(getMove)
          if(move == 0 and gameBoard[actManLocation[0]][actManLocation[1]-1] != '#' and actManDirection != 2):
            gameBoard[actManLocation[0]][actManLocation[1]] = ' '
            actManLocation = [actManLocation[0], actManLocation[1]-1]
            actManMoves += 'U'
            actManDirection = 0
            break
          elif(move == 1 and gameBoard[actManLocation[0]+1][actManLocation[1]] != '#' and actManDirection != 3):
            gameBoard[actManLocation[0]][actManLocation[1]] = ' '
            actManLocation = [actManLocation[0]+1, actManLocation[1]]
            actManMoves += 'R'
            actManDirection = 1
            break
          elif(move == 2 and gameBoard[actManLocation[0]][actManLocation[1]+1] != '#' and actManDirection != 0):
            gameBoard[actManLocation[0]][actManLocation[1]] = ' '
            actManLocation = [actManLocation[0], actManLocation[1]+1]
            actManMoves += 'D'
            actManDirection = 2
            break
          elif(move == 3 and gameBoard[actManLocation[0]-1][actManLocation[1]] != '#' and actManDirection != 1):
            gameBoard[actManLocation[0]][actManLocation[1]] = ' '
            actManLocation = [actManLocation[0]-1, actManLocation[1]]
            actManMoves += 'L'
            actManDirection = 3
            break
      if(playerDead(actManLocation[0],actManLocation[1])):
        break
      if(gameBoard[actManLocation[0]][actManLocation[1]] == ' '):
        gameBoard[actManLocation[0]][actManLocation[1]] = 'A'
      if(gameBoard[actManLocation[0]][actManLocation[1]] == '.'):
        score +=1
        gameBoard[actManLocation[0]][actManLocation[1]] = 'A'
      if(gameBoard[actManLocation[0]][actManLocation[1]] == '$'):
        score +=5
        gameBoard[actManLocation[0]][actManLocation[1]] = 'A'
      if(gameBoard[actManLocation[0]][actManLocation[1]] == '*'):
        score +=10
        gameBoard[actManLocation[0]][actManLocation[1]] = 'A'
      if(score == maxScore):
        gameNotFinished = False
        break

    if(entity == 1):  #Punky makes move
      if(checkNumMoves(punkyLocation[0],punkyLocation[1]) == 2 ):
        if(punkyDirection == 'U' and gameBoard[punkyLocation[0]][punkyLocation[1]-1] !='#'):
          punkyLocation = [punkyLocation[0],punkyLocation[1]-1]
          gameBoard[punkyLocation[0]][punkyLocation[1]+1] = findOtherGhostOnSpot(punkyLocation[0],punkyLocation[1]+1)
          gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
        elif(punkyDirection == 'U' and gameBoard[punkyLocation[0]][punkyLocation[1]-1] == '#'):
          if(gameBoard[punkyLocation[0]+1][punkyLocation[1]] != '#'):
            punkyLocation = [punkyLocation[0]+1,punkyLocation[1]]
            gameBoard[punkyLocation[0]-1][punkyLocation[1]] = findOtherGhostOnSpot(punkyLocation[0]-1,punkyLocation[1])
            gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
            punkyDirection = 'R'
          elif(gameBoard[punkyLocation[0]-1][punkyLocation[1]] != '#'):
            punkyLocation = [punkyLocation[0]-1,punkyLocation[1]]
            gameBoard[punkyLocation[0]+1][punkyLocation[1]] = findOtherGhostOnSpot(punkyLocation[0]+1,punkyLocation[1])
            gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
            punkyDirection = 'L'
        elif(punkyDirection == 'R' and gameBoard[punkyLocation[0]+1][punkyLocation[1]] !='#'):
          punkyLocation = [punkyLocation[0]+1,punkyLocation[1]]
          gameBoard[punkyLocation[0]-1][punkyLocation[1]] = findOtherGhostOnSpot(punkyLocation[0]-1,punkyLocation[1])
          gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
        elif(punkyDirection == 'R' and gameBoard[punkyLocation[0]+1][punkyLocation[1]] == '#'):
          if(gameBoard[punkyLocation[0]][punkyLocation[1]-1] != '#'):
            punkyLocation = [punkyLocation[0],punkyLocation[1]-1]
            gameBoard[punkyLocation[0]][punkyLocation[1]+1] = findOtherGhostOnSpot(punkyLocation[0],punkyLocation[1]+1)
            gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
            punkyDirection = 'U'
          elif(gameBoard[punkyLocation[0]][punkyLocation[1]+1] != '#'):
            punkyLocation = [punkyLocation[0],punkyLocation[1]+1]
            gameBoard[punkyLocation[0]][punkyLocation[1]-1] = findOtherGhostOnSpot(punkyLocation[0],punkyLocation[1]-1)
            gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
            punkyDirection = 'D'
        elif(punkyDirection == 'D' and gameBoard[punkyLocation[0]][punkyLocation[1]+1] !='#'):
          punkyLocation = [punkyLocation[0],punkyLocation[1]+1]
          gameBoard[punkyLocation[0]][punkyLocation[1]-1] = findOtherGhostOnSpot(punkyLocation[0],punkyLocation[1]-1)
          gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
        elif(punkyDirection == 'D' and gameBoard[punkyLocation[0]][punkyLocation[1]+1] == '#'):
          if(gameBoard[punkyLocation[0]+1][punkyLocation[1]] != '#'):
            punkyLocation = [punkyLocation[0]+1,punkyLocation[1]]
            gameBoard[punkyLocation[0]-1][punkyLocation[1]] = findOtherGhostOnSpot(punkyLocation[0]-1,punkyLocation[1])
            gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
            punkyDirection = 'R'
          elif(gameBoard[punkyLocation[0]-1][punkyLocation[1]] != '#'):
            punkyLocation = [punkyLocation[0]-1,punkyLocation[1]]
            gameBoard[punkyLocation[0]+1][punkyLocation[1]] = findOtherGhostOnSpot(punkyLocation[0]+1,punkyLocation[1])
            gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
            punkyDirection = 'L'
        elif(punkyDirection == 'L' and gameBoard[punkyLocation[0]-1][punkyLocation[1]] !='#'):
          punkyLocation = [punkyLocation[0]-1,punkyLocation[1]]
          gameBoard[punkyLocation[0]+1][punkyLocation[1]] = findOtherGhostOnSpot(punkyLocation[0]+1,punkyLocation[1])
          gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
        elif(punkyDirection == 'L' and gameBoard[punkyLocation[0]-1][punkyLocation[1]] == '#'):
          if(gameBoard[punkyLocation[0]][punkyLocation[1]-1] != '#'):
            punkyLocation = [punkyLocation[0],punkyLocation[1]-1]
            gameBoard[punkyLocation[0]][punkyLocation[1]+1] = findOtherGhostOnSpot(punkyLocation[0],punkyLocation[1]+1)
            gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
            punkyDirection = 'U'
          elif(gameBoard[punkyLocation[0]][punkyLocation[1]+1] != '#'):
            punkyLocation = [punkyLocation[0],punkyLocation[1]+1]
            gameBoard[punkyLocation[0]][punkyLocation[1]-1] = findOtherGhostOnSpot(punkyLocation[0],punkyLocation[1]-1)
            gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
            punkyDirection = 'D'
      else:
        distanceUp = 999
        distanceRight = 999
        distanceDown = 999
        distanceLeft = 999
        if(gameBoard[punkyLocation[0]][punkyLocation[1] -1] != '#'):
          distanceUp = math.sqrt(( (actManLocation[0] - punkyLocation[0])**2) + ((actManLocation[1] - punkyLocation[1]-1)**2))
        if(gameBoard[punkyLocation[0]+1][punkyLocation[1]] != '#'):
          distanceRight = math.sqrt(( (actManLocation[0] - punkyLocation[0] +1)**2) + ((actManLocation[1] - punkyLocation[1])**2))
        if(gameBoard[punkyLocation[0]][punkyLocation[1] +1] != '#'):
          distanceDown = math.sqrt(( (actManLocation[0] - punkyLocation[0])**2) + ((actManLocation[1] - punkyLocation[1]+1)**2))
        if(gameBoard[punkyLocation[0]-1][punkyLocation[1]] != '#'):
          distanceLeft = math.sqrt(( (actManLocation[0] - punkyLocation[0]-1)**2) + ((actManLocation[1] - punkyLocation[1])**2))  
        minDistance = min([distanceUp,distanceRight,distanceDown,distanceLeft])
        if(minDistance == distanceUp):
          if(checkIfOtherGhostsOccupySpot(punkyLocation[0],punkyLocation[1])==1):
            gameBoard[punkyLocation[0]][punkyLocation[1]] = checkIfTreasureCollected(punkyLocation[0],punkyLocation[1])
          punkyLocation = [punkyLocation[0],punkyLocation[1]-1]
          gameBoard[punkyLocation[0]][punkyLocation[1]+1] = findOtherGhostOnSpot(punkyLocation[0],punkyLocation[1]+1)
          gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
          punkyDirection = 'U'
        elif(minDistance == distanceRight):
          if(checkIfOtherGhostsOccupySpot(punkyLocation[0],punkyLocation[1])==1):
            gameBoard[punkyLocation[0]][punkyLocation[1]] = checkIfTreasureCollected(punkyLocation[0],punkyLocation[1])
          punkyLocation = [punkyLocation[0]+1,punkyLocation[1]]
          gameBoard[punkyLocation[0]-1][punkyLocation[1]] = findOtherGhostOnSpot(punkyLocation[0]-1,punkyLocation[1])
          gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
          punkyDirection = 'R'
        elif(minDistance == distanceDown):
          if(checkIfOtherGhostsOccupySpot(punkyLocation[0],punkyLocation[1])==1):
            gameBoard[punkyLocation[0]][punkyLocation[1]] = checkIfTreasureCollected(punkyLocation[0],punkyLocation[1])
          punkyLocation = [punkyLocation[0],punkyLocation[1]+1]
          gameBoard[punkyLocation[0]][punkyLocation[1]-1] = findOtherGhostOnSpot(punkyLocation[0],punkyLocation[1]-1)
          gameBoard[punkyLocation[0]][punkyLocation[1]] = checkIfTreasureCollected(punkyLocation[0],punkyLocation[1])
          punkyDirection = 'D'
        elif(minDistance == distanceLeft):
          if(checkIfOtherGhostsOccupySpot(punkyLocation[0],punkyLocation[1])==1):
            gameBoard[punkyLocation[0]][punkyLocation[1]] = checkIfTreasureCollected(punkyLocation[0],punkyLocation[1])
          punkyLocation = [punkyLocation[0]-1,punkyLocation[1]]
          gameBoard[punkyLocation[0]+1][punkyLocation[1]] = findOtherGhostOnSpot(punkyLocation[0]+1,punkyLocation[1])
          gameBoard[punkyLocation[0]][punkyLocation[1]] = 'P'
          punkyDirection = 'L'
      if(playerDead(actManLocation[0],actManLocation[1])):
        break

    if(entity == 2):  #Bunky makes move
      if(checkNumMoves(bunkyLocation[0],bunkyLocation[1]) == 2 ):
        if(bunkyDirection == 'U' and gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] !='#'):
          bunkyLocation = [bunkyLocation[0],bunkyLocation[1]-1]
          gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] = findOtherGhostOnSpot(bunkyLocation[0],bunkyLocation[1]+1)
          gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
        elif(bunkyDirection == 'U' and gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] == '#'):
          if(gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] != '#'):
            bunkyLocation = [bunkyLocation[0]+1,bunkyLocation[1]]
            gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] = findOtherGhostOnSpot(bunkyLocation[0]-1,bunkyLocation[1])
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
            bunkyDirection = 'R'
          elif(gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] != '#'):
            bunkyLocation = [bunkyLocation[0]-1,bunkyLocation[1]]
            gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] = findOtherGhostOnSpot(bunkyLocation[0]+1,bunkyLocation[1])
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
            bunkyDirection = 'L'
        elif(bunkyDirection == 'R' and gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] !='#'):
          bunkyLocation = [bunkyLocation[0]+1,bunkyLocation[1]]
          gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] = findOtherGhostOnSpot(bunkyLocation[0]-1,bunkyLocation[1])
          gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
        elif(bunkyDirection == 'R' and gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] == '#'):
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] != '#'):
            bunkyLocation = [bunkyLocation[0],bunkyLocation[1]-1]
            gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] = findOtherGhostOnSpot(bunkyLocation[0],bunkyLocation[1]+1)
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
            bunkyDirection = 'U'
          elif(gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] != '#'):
            bunkyLocation = [bunkyLocation[0],bunkyLocation[1]+1]
            gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] = findOtherGhostOnSpot(bunkyLocation[0],bunkyLocation[1]-1)
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
            bunkyDirection = 'D'
        elif(bunkyDirection == 'D' and gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] !='#'):
          bunkyLocation = [bunkyLocation[0],bunkyLocation[1]+1]
          gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] = findOtherGhostOnSpot(bunkyLocation[0],bunkyLocation[1]-1)
          gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
        elif(bunkyDirection == 'D' and gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] == '#'):
          if(gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] != '#'):
            bunkyLocation = [bunkyLocation[0]+1,bunkyLocation[1]]
            gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] = findOtherGhostOnSpot(bunkyLocation[0]-1,bunkyLocation[1])
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
            bunkyDirection = 'R'
          elif(gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] != '#'):
            bunkyLocation = [bunkyLocation[0]-1,bunkyLocation[1]]
            gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] = findOtherGhostOnSpot(bunkyLocation[0]+1,bunkyLocation[1])
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
            bunkyDirection = 'L'
        elif(bunkyDirection == 'L' and gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] !='#'):
          bunkyLocation = [bunkyLocation[0]-1,bunkyLocation[1]]
          gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] = findOtherGhostOnSpot(bunkyLocation[0]+1,bunkyLocation[1])
          gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
        elif(bunkyDirection == 'L' and gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] == '#'):
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] != '#'):
            bunkyLocation = [bunkyLocation[0],bunkyLocation[1]-1]
            gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] = findOtherGhostOnSpot(bunkyLocation[0],bunkyLocation[1]+1)
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
            bunkyDirection = 'U'
          elif(gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] != '#'):
            bunkyLocation = [bunkyLocation[0],bunkyLocation[1]+1]
            gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] = findOtherGhostOnSpot(bunkyLocation[0],bunkyLocation[1]-1)
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
            bunkyDirection = 'D'
      else:
        fourSpacesUp = 999
        fourSpacesRight = 999
        fourSpacesDown = 999
        fourSpacesLeft = 999
        if(actManDirection == 0):
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] != '#'):
            fourSpacesUp = math.sqrt( ((actManLocation[0] - bunkyLocation[0])**2) + (((actManLocation[1]-4) - bunkyLocation[1]-1)**2) )
          if(gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] != '#'):
            fourSpacesRight = math.sqrt( ((actManLocation[0] - bunkyLocation[0]+1)**2) + (((actManLocation[1]-4) - bunkyLocation[1])**2) )
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] != '#'):
            fourSpacesDown = math.sqrt( ((actManLocation[0] - bunkyLocation[0])**2) + (((actManLocation[1]-4) - bunkyLocation[1]+1)**2) )
          if(gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] != '#'):
            fourSpacesLeft = math.sqrt( ((actManLocation[0] - bunkyLocation[0]-1)**2) + (((actManLocation[1]-4) - bunkyLocation[1])**2) )
        elif(actManDirection == 1):
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] != '#'):
            fourSpacesUp = math.sqrt( (((actManLocation[0]+4) - bunkyLocation[0])**2) + ((actManLocation[1] - bunkyLocation[1]-1)**2) )
          if(gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] != '#'):
            fourSpacesRight = math.sqrt( (((actManLocation[0]+4) - bunkyLocation[0]+1)**2) + (((actManLocation[1]) - bunkyLocation[1])**2) )
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] != '#'):
            fourSpacesDown = math.sqrt( (((actManLocation[0]+4) - bunkyLocation[0])**2) + (((actManLocation[1]) - bunkyLocation[1]+1)**2) )
          if(gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] != '#'):
            fourSpacesLeft = math.sqrt( (((actManLocation[0]+4) - bunkyLocation[0]-1)**2) + (((actManLocation[1]) - bunkyLocation[1])**2) )
        elif(actManDirection == 2):
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] != '#'):
            fourSpacesUp = math.sqrt( ((actManLocation[0] - bunkyLocation[0])**2) + (((actManLocation[1]+4) - bunkyLocation[1]-1)**2) )
          if(gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] != '#'):
            fourSpacesRight = math.sqrt( ((actManLocation[0] - bunkyLocation[0]+1)**2) + (((actManLocation[1]+4) - bunkyLocation[1])**2) )
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] != '#'):
            fourSpacesDown = math.sqrt( ((actManLocation[0] - bunkyLocation[0])**2) + (((actManLocation[1]+4) - bunkyLocation[1]+1)**2) )
          if(gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] != '#'):
            fourSpacesLeft = math.sqrt( ((actManLocation[0] - bunkyLocation[0]-1)**2) + (((actManLocation[1]+4) - bunkyLocation[1])**2) )
        elif(actManDirection == 3):
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] != '#'):
            fourSpacesUp = math.sqrt( (((actManLocation[0]-4) - bunkyLocation[0])**2) + ((actManLocation[1] - bunkyLocation[1]-1)**2) )
          if(gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] != '#'):
            fourSpacesRight = math.sqrt( (((actManLocation[0]-4) - bunkyLocation[0]+1)**2) + (((actManLocation[1]) - bunkyLocation[1])**2) )
          if(gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] != '#'):
            fourSpacesDown = math.sqrt( (((actManLocation[0]-4) - bunkyLocation[0])**2) + (((actManLocation[1]) - bunkyLocation[1]+1)**2) )
          if(gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] != '#'):
            fourSpacesLeft = math.sqrt( (((actManLocation[0]-4) - bunkyLocation[0]-1)**2) + (((actManLocation[1]) - bunkyLocation[1])**2) )
        minDistance = min([fourSpacesUp,fourSpacesRight,fourSpacesDown,fourSpacesLeft])
        if(minDistance == fourSpacesUp):
          if(checkIfOtherGhostsOccupySpot(bunkyLocation[0],bunkyLocation[1]) == 1):
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = checkIfTreasureCollected(bunkyLocation[0],bunkyLocation[1])
          bunkyLocation = [bunkyLocation[0],bunkyLocation[1]-1]
          gameBoard[bunkyLocation[0]][bunkyLocation[1]+1] = findOtherGhostOnSpot(bunkyLocation[0],bunkyLocation[1]+1)
          gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
          bunkyDirection = 'U'
        elif(minDistance == fourSpacesRight):
          if(checkIfOtherGhostsOccupySpot(bunkyLocation[0],bunkyLocation[1]) == 1):
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = checkIfTreasureCollected(bunkyLocation[0],bunkyLocation[1])
          bunkyLocation = [bunkyLocation[0]+1,bunkyLocation[1]]
          gameBoard[bunkyLocation[0]-1][bunkyLocation[1]] = findOtherGhostOnSpot(bunkyLocation[0]-1,bunkyLocation[1])
          gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
          bunkyDirection = 'R'
        elif(minDistance == fourSpacesDown):
          if(checkIfOtherGhostsOccupySpot(bunkyLocation[0],bunkyLocation[1]) == 1):
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = checkIfTreasureCollected(bunkyLocation[0],bunkyLocation[1])
          bunkyLocation = [bunkyLocation[0],bunkyLocation[1]+1]
          gameBoard[bunkyLocation[0]][bunkyLocation[1]-1] = findOtherGhostOnSpot(bunkyLocation[0],bunkyLocation[1]-1)
          gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
          bunkyDirection = 'D'
        elif(minDistance == fourSpacesLeft):
          if(checkIfOtherGhostsOccupySpot(bunkyLocation[0],bunkyLocation[1]) == 1):
            gameBoard[bunkyLocation[0]][bunkyLocation[1]] = checkIfTreasureCollected(bunkyLocation[0],bunkyLocation[1])
          bunkyLocation = [bunkyLocation[0]-1,bunkyLocation[1]]
          gameBoard[bunkyLocation[0]+1][bunkyLocation[1]] = findOtherGhostOnSpot(bunkyLocation[0]+1,bunkyLocation[1])
          gameBoard[bunkyLocation[0]][bunkyLocation[1]] = 'B'
          bunkyDirection = 'L'
      if(playerDead(actManLocation[0],actManLocation[1])):
        break

    if(entity == 3):  #Dunky makes move
      if(checkNumMoves(dunkyLocation[0],dunkyLocation[1]) == 2 ):
        if(dunkyDirection == 'U' and gameBoard[dunkyLocation[0]][dunkyLocation[1]-1] !='#'):
          dunkyLocation = [dunkyLocation[0],dunkyLocation[1]-1]
          gameBoard[dunkyLocation[0]][dunkyLocation[1]+1] = findOtherGhostOnSpot(dunkyLocation[0],dunkyLocation[1]+1)
          gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
        elif(dunkyDirection == 'U' and gameBoard[dunkyLocation[0]][dunkyLocation[1]-1] == '#'):
          if(gameBoard[dunkyLocation[0]+1][dunkyLocation[1]] != '#'):
            dunkyLocation = [dunkyLocation[0]+1,dunkyLocation[1]]
            gameBoard[dunkyLocation[0]-1][dunkyLocation[1]] = findOtherGhostOnSpot(dunkyLocation[0]-1,dunkyLocation[1])
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
            dunkyDirection = 'R'
          elif(gameBoard[dunkyLocation[0]-1][dunkyLocation[1]] != '#'):
            dunkyLocation = [dunkyLocation[0]-1,dunkyLocation[1]]
            gameBoard[dunkyLocation[0]+1][dunkyLocation[1]] = findOtherGhostOnSpot(dunkyLocation[0]+1,dunkyLocation[1])
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
            dunkyDirection = 'L'
        elif(dunkyDirection == 'R' and gameBoard[dunkyLocation[0]+1][dunkyLocation[1]] !='#'):
          dunkyLocation = [dunkyLocation[0]+1,dunkyLocation[1]]
          gameBoard[dunkyLocation[0]-1][dunkyLocation[1]] = findOtherGhostOnSpot(dunkyLocation[0]-1,dunkyLocation[1])
          gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
        elif(dunkyDirection == 'R' and gameBoard[dunkyLocation[0]+1][dunkyLocation[1]] == '#'):
          if(gameBoard[dunkyLocation[0]][dunkyLocation[1]-1] != '#'):
            dunkyLocation = [dunkyLocation[0],dunkyLocation[1]-1]
            gameBoard[dunkyLocation[0]][dunkyLocation[1]+1] = findOtherGhostOnSpot(dunkyLocation[0],dunkyLocation[1]+1)
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
            dunkyDirection = 'U'
          elif(gameBoard[dunkyLocation[0]][dunkyLocation[1]+1] != '#'):
            dunkyLocation = [dunkyLocation[0],dunkyLocation[1]+1]
            gameBoard[dunkyLocation[0]][dunkyLocation[1]-1] = findOtherGhostOnSpot(dunkyLocation[0],dunkyLocation[1]-1)
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
            dunkyDirection = 'D'
        elif(dunkyDirection == 'D' and gameBoard[dunkyLocation[0]][dunkyLocation[1]+1] !='#'):
          dunkyLocation = [dunkyLocation[0],dunkyLocation[1]+1]
          gameBoard[dunkyLocation[0]][dunkyLocation[1]-1] = findOtherGhostOnSpot(dunkyLocation[0],dunkyLocation[1]-1)
          gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
        elif(dunkyDirection == 'D' and gameBoard[dunkyLocation[0]][dunkyLocation[1]+1] == '#'):
          if(gameBoard[dunkyLocation[0]+1][dunkyLocation[1]] != '#'):
            dunkyLocation = [dunkyLocation[0]+1,dunkyLocation[1]]
            gameBoard[dunkyLocation[0]-1][dunkyLocation[1]] = findOtherGhostOnSpot(dunkyLocation[0]-1,dunkyLocation[1])
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
            dunkyDirection = 'R'
          elif(gameBoard[dunkyLocation[0]-1][dunkyLocation[1]] != '#'):
            dunkyLocation = [dunkyLocation[0]-1,dunkyLocation[1]]
            gameBoard[dunkyLocation[0]+1][dunkyLocation[1]] = findOtherGhostOnSpot(dunkyLocation[0]+1,dunkyLocation[1])
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
            dunkyDirection = 'L'
        elif(dunkyDirection == 'L' and gameBoard[dunkyLocation[0]-1][dunkyLocation[1]] !='#'):
          dunkyLocation = [dunkyLocation[0]-1,dunkyLocation[1]]
          gameBoard[dunkyLocation[0]+1][dunkyLocation[1]] = findOtherGhostOnSpot(dunkyLocation[0]+1,dunkyLocation[1])
          gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
        elif(dunkyDirection == 'L' and gameBoard[dunkyLocation[0]-1][dunkyLocation[1]] == '#'):
          if(gameBoard[dunkyLocation[0]][dunkyLocation[1]-1] != '#'):
            dunkyLocation = [dunkyLocation[0],dunkyLocation[1]-1]
            gameBoard[dunkyLocation[0]][dunkyLocation[1]+1] = findOtherGhostOnSpot(dunkyLocation[0],dunkyLocation[1]+1)
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
            dunkyDirection = 'U'
          elif(gameBoard[dunkyLocation[0]][dunkyLocation[1]+1] != '#'):
            dunkyLocation = [dunkyLocation[0],dunkyLocation[1]+1]
            gameBoard[dunkyLocation[0]][dunkyLocation[1]-1] = findOtherGhostOnSpot(dunkyLocation[0],dunkyLocation[1]-1)
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
            dunkyDirection = 'D'
      else:
        distanceUp = 999
        distanceRight = 999
        distanceDown = 999
        distanceLeft = 999
        if(gameBoard[dunkyLocation[0]][dunkyLocation[1] -1] != '#'):
          distanceUp = math.sqrt( ((int(listDunkyLocations[dunkyCurTarget][0]) - dunkyLocation[0])**2) + ((int(listDunkyLocations[dunkyCurTarget][1]) - dunkyLocation[1] -1)**2) )
        if(gameBoard[dunkyLocation[0]+1][dunkyLocation[1]] != '#'):
          distanceRight = math.sqrt( ((int(listDunkyLocations[dunkyCurTarget][0]) - dunkyLocation[0]+1)**2) + ((int(listDunkyLocations[dunkyCurTarget][1]) - dunkyLocation[1])**2) )
        if(gameBoard[dunkyLocation[0]][dunkyLocation[1]+1] != '#'):
          distanceDown = math.sqrt( ((int(listDunkyLocations[dunkyCurTarget][0]) - dunkyLocation[0]) **2) + ((int(listDunkyLocations[dunkyCurTarget][1]) - dunkyLocation[1]+1)**2))
        if(gameBoard[dunkyLocation[0]-1][dunkyLocation[1]] != '#'):
          distanceLeft = math.sqrt( ((int(listDunkyLocations[dunkyCurTarget][0]) - dunkyLocation[0]+1)**2) + ((int(listDunkyLocations[dunkyCurTarget][1]) - dunkyLocation[1])**2))
        minDistance = min([distanceUp,distanceLeft,distanceRight,distanceDown])
        if(minDistance == distanceUp):
          if(checkIfOtherGhostsOccupySpot(dunkyLocation[0],dunkyLocation[1]) == 1):
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = checkIfTreasureCollected(dunkyLocation[0],dunkyLocation[1])
          dunkyLocation = [dunkyLocation[0],dunkyLocation[1]-1]
          gameBoard[dunkyLocation[0]][dunkyLocation[1]+1] = findOtherGhostOnSpot(dunkyLocation[0],dunkyLocation[1]+1)
          gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
          dunkyDirection = 'U'
        elif(minDistance == distanceRight):
          if(checkIfOtherGhostsOccupySpot(dunkyLocation[0],dunkyLocation[1]) == 1):
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = checkIfTreasureCollected(dunkyLocation[0],dunkyLocation[1])
          dunkyLocation = [dunkyLocation[0]+1,dunkyLocation[1]]
          gameBoard[dunkyLocation[0]-1][dunkyLocation[1]] = findOtherGhostOnSpot(dunkyLocation[0]-1,dunkyLocation[1])
          gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
          dunkyDirection = 'R'
        elif(minDistance == distanceDown):
          if(checkIfOtherGhostsOccupySpot(dunkyLocation[0],dunkyLocation[1]) == 1):
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = checkIfTreasureCollected(dunkyLocation[0],dunkyLocation[1])
          dunkyLocation = [dunkyLocation[0],dunkyLocation[1]+1]
          gameBoard[dunkyLocation[0]][dunkyLocation[1]-1] = findOtherGhostOnSpot(dunkyLocation[0],dunkyLocation[1]-1)
          gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
          dunkyDirection = 'D'
        elif(minDistance == distanceLeft):
          if(checkIfOtherGhostsOccupySpot(dunkyLocation[0],dunkyLocation[1]) == 1):
            gameBoard[dunkyLocation[0]][dunkyLocation[1]] = checkIfTreasureCollected(dunkyLocation[0],dunkyLocation[1])
          dunkyLocation = [dunkyLocation[0]-1,dunkyLocation[1]]
          gameBoard[dunkyLocation[0]+1][dunkyLocation[1]] = findOtherGhostOnSpot(dunkyLocation[0]+1,dunkyLocation[1])
          gameBoard[dunkyLocation[0]][dunkyLocation[1]] = 'D'
          dunkyDirection = 'L'
        if(listDunkyLocations[dunkyCurTarget][0] == dunkyLocation[0] and listDunkyLocations[dunkyCurTarget][1] == dunkyLocation[1]):
          dunkyCurTarget+=1
        if(dunkyCurTarget == len(listDunkyLocations)):
          dunkyCurTarget = 0
      if(playerDead(actManLocation[0],actManLocation[1])):
        break

    if(entity == 4):  #Runky makes move
      if(checkNumMoves(runkyLocation[0],runkyLocation[1]) == 2 ):
        if(runkyDirection == 'U' and gameBoard[runkyLocation[0]][runkyLocation[1]-1] !='#'):
          runkyLocation = [runkyLocation[0],runkyLocation[1]-1]
          gameBoard[runkyLocation[0]][runkyLocation[1]+1] = findOtherGhostOnSpot(runkyLocation[0],runkyLocation[1]+1)
          gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
        elif(runkyDirection == 'U' and gameBoard[runkyLocation[0]][runkyLocation[1]-1] == '#'):
          if(gameBoard[runkyLocation[0]+1][runkyLocation[1]] != '#'):
            runkyLocation = [runkyLocation[0]+1,runkyLocation[1]]
            gameBoard[runkyLocation[0]-1][runkyLocation[1]] = findOtherGhostOnSpot(runkyLocation[0]-1,runkyLocation[1])
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyDirection = 'R'
          elif(gameBoard[runkyLocation[0]-1][runkyLocation[1]] != '#'):
            runkyLocation = [runkyLocation[0]-1,runkyLocation[1]]
            gameBoard[runkyLocation[0]+1][runkyLocation[1]] = findOtherGhostOnSpot(runkyLocation[0]+1,runkyLocation[1])
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyDirection = 'L'
        elif(runkyDirection == 'R' and gameBoard[runkyLocation[0]+1][runkyLocation[1]] !='#'):
          runkyLocation = [runkyLocation[0]+1,runkyLocation[1]]
          gameBoard[runkyLocation[0]-1][runkyLocation[1]] = findOtherGhostOnSpot(runkyLocation[0]-1,runkyLocation[1])
          gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
        elif(runkyDirection == 'R' and gameBoard[runkyLocation[0]+1][runkyLocation[1]] == '#'):
          if(gameBoard[runkyLocation[0]][runkyLocation[1]-1] != '#'):
            runkyLocation = [runkyLocation[0],runkyLocation[1]-1]
            gameBoard[runkyLocation[0]][runkyLocation[1]+1] = findOtherGhostOnSpot(runkyLocation[0],runkyLocation[1]+1)
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyDirection = 'U'
          elif(gameBoard[runkyLocation[0]][runkyLocation[1]+1] != '#'):
            runkyLocation = [runkyLocation[0],runkyLocation[1]+1]
            gameBoard[runkyLocation[0]][runkyLocation[1]-1] = findOtherGhostOnSpot(runkyLocation[0],runkyLocation[1]-1)
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyDirection = 'D'
        elif(runkyDirection == 'D' and gameBoard[runkyLocation[0]][runkyLocation[1]+1] !='#'):
          runkyLocation = [runkyLocation[0],runkyLocation[1]+1]
          gameBoard[runkyLocation[0]][runkyLocation[1]-1] = findOtherGhostOnSpot(runkyLocation[0],runkyLocation[1]-1)
          gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
        elif(runkyDirection == 'D' and gameBoard[runkyLocation[0]][runkyLocation[1]+1] == '#'):
          if(gameBoard[runkyLocation[0]+1][runkyLocation[1]] != '#'):
            runkyLocation = [runkyLocation[0]+1,runkyLocation[1]]
            gameBoard[runkyLocation[0]-1][runkyLocation[1]] = findOtherGhostOnSpot(runkyLocation[0]-1,runkyLocation[1])
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyDirection = 'R'
          elif(gameBoard[runkyLocation[0]-1][runkyLocation[1]] != '#'):
            runkyLocation = [runkyLocation[0]-1,runkyLocation[1]]
            gameBoard[runkyLocation[0]+1][runkyLocation[1]] = findOtherGhostOnSpot(runkyLocation[0]+1,runkyLocation[1])
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyDirection = 'L'
        elif(runkyDirection == 'L' and gameBoard[runkyLocation[0]-1][runkyLocation[1]] !='#'):
          runkyLocation = [runkyLocation[0]-1,runkyLocation[1]]
          gameBoard[runkyLocation[0]+1][runkyLocation[1]] = findOtherGhostOnSpot(runkyLocation[0]+1,runkyLocation[1])
          gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
        elif(runkyDirection == 'L' and gameBoard[runkyLocation[0]-1][runkyLocation[1]] == '#'):
          if(gameBoard[runkyLocation[0]][runkyLocation[1]-1] != '#'):
            runkyLocation = [runkyLocation[0],runkyLocation[1]-1]
            gameBoard[runkyLocation[0]][runkyLocation[1]+1] = findOtherGhostOnSpot(runkyLocation[0],runkyLocation[1]+1)
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyDirection = 'U'
          elif(gameBoard[runkyLocation[0]][runkyLocation[1]+1] != '#'):
            runkyLocation = [runkyLocation[0],runkyLocation[1]+1]
            gameBoard[runkyLocation[0]][runkyLocation[1]-1] = findOtherGhostOnSpot(runkyLocation[0],runkyLocation[1]-1)
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyDirection = 'D'
      else:
        while True:
          move = runkyMoveList[runkyCurMove]
          if(move == 'U' and gameBoard[runkyLocation[0]][runkyLocation[1]-1] != '#'):
            if(checkIfOtherGhostsOccupySpot(runkyLocation[0],runkyLocation[1]) == 1):
              gameBoard[runkyLocation[0]][runkyLocation[1]] = checkIfTreasureCollected(runkyLocation[0],runkyLocation[1])
            runkyLocation = [runkyLocation[0],runkyLocation[1]-1]
            gameBoard[runkyLocation[0]][runkyLocation[1]+1] = findOtherGhostOnSpot(runkyLocation[0],runkyLocation[1]+1)
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyCurMove+=1
            dunkyDirection = 'U'
            break
          elif(move == 'R' and gameBoard[runkyLocation[0]+1][runkyLocation[1]] != '#'):
            if(checkIfOtherGhostsOccupySpot(runkyLocation[0],runkyLocation[1]) == 1):
              gameBoard[runkyLocation[0]][runkyLocation[1]] = checkIfTreasureCollected(runkyLocation[0],runkyLocation[1])
            runkyLocation = [runkyLocation[0]+1,runkyLocation[1]]
            gameBoard[runkyLocation[0]-1][runkyLocation[1]] = findOtherGhostOnSpot(runkyLocation[0]-1,runkyLocation[1])
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyCurMove+=1
            dunkyDirection = 'R'
            break
          elif(move == 'D' and gameBoard[runkyLocation[0]][runkyLocation[1]+1] != '#'):
            if(checkIfOtherGhostsOccupySpot(runkyLocation[0],runkyLocation[1]) == 1):
              gameBoard[runkyLocation[0]][runkyLocation[1]] = checkIfTreasureCollected(runkyLocation[0],runkyLocation[1])
            runkyLocation = [runkyLocation[0],runkyLocation[1]+1]
            gameBoard[runkyLocation[0]][runkyLocation[1]-1] = findOtherGhostOnSpot(runkyLocation[0],runkyLocation[1]-1)
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyCurMove+=1
            dunkyDirection = 'D'
            break
          elif(move == 'L' and gameBoard[runkyLocation[0]-1][runkyLocation[1]] != '#'):
            if(checkIfOtherGhostsOccupySpot(runkyLocation[0],runkyLocation[1]) == 1):
              gameBoard[runkyLocation[0]][runkyLocation[1]] = checkIfTreasureCollected(runkyLocation[0],runkyLocation[1])
            runkyLocation = [runkyLocation[0]-1,runkyLocation[1]]
            gameBoard[runkyLocation[0]+1][runkyLocation[1]] = findOtherGhostOnSpot(runkyLocation[0]+1,runkyLocation[1])
            gameBoard[runkyLocation[0]][runkyLocation[1]] = 'R'
            runkyCurMove+=1
            dunkyDirection = 'L'
            break
          else:
            runkyCurMove+=1
          if(runkyCurMove == len(runkyMoveList)):
            runkyCurMove = 0
          
      if(playerDead(actManLocation[0],actManLocation[1])):
        break
  if(playerDead(actManLocation[0],actManLocation[1])):
    break
  completedRounds+=1
  print("SCORE : "+str(score) +"    TURN: "+str(completedRounds))
  printGameBoard(gameBoard)
  if(completedRounds==9):
    gameNotFinished = False

printGameBoard(gameBoard)

finalBoard = numpy.transpose(gameBoard)
r = open(sys.argv[2],"w")
r.write(actManMoves +'\n')
r.write(str(score) + '\n')
for a in range(len(finalBoard)):
  line = ""
  for b in range(len(finalBoard[a])):
    line += finalBoard[a][b]
  r.write(line + '\n')