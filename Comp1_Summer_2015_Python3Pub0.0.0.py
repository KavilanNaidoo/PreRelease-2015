
 
BOARDDIMENSION = 8
def display_menu():
  print('Main Menu')
  print()
  print('1. Start new game')
  print('2. Load existing game')
  print('3. Play sample game')
  print('4. View high scores')
  print('5. Settings')
  print('6. Quit program')
  print()
  print('Please select an option: ', end='')

def get_menu_selection():
  Choice = input()   
  return Choice

def make_selection(Choice):
  if Choice == '1':
    play_game('n')
  elif Choice == '2':
    pass
  elif Choice == '3':
    play_game('y')
  
    


  
def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board
 
def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")
 
def GetTypeOfGame():
  valid = False
  while not valid:
      TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
      if TypeOfGame == 'y':
          valid = False
      else:
          print("Please enter Y or N")
          valid = False
  return TypeOfGame.lower()
 
def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")
 
def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False
 
def DisplayBoard(Board):
  print()
  for RankNo in range(1 , BOARDDIMENSION + 1):
    print("     -------------------------")
    print("R",RankNo,end="  ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -------------------------")
  print()
  print("     F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    
 
def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal
 
def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal
 
def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal
 
def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal
 
def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal
 
def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal
 
def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  else:
    PieceType = Board[StartRank][StartFile][1]
    PieceColour = Board[StartRank][StartFile][0]
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "W":
        MoveIsLegal = False
    else:
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal
 
def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        Board[RankNo][FileNo] = "  "
    Board[1][2] = "BG"
    Board[1][4] = "BS"
    Board[1][8] = "WG"
    Board[2][1] = "WR"
    Board[3][1] = "WS"
    Board[3][2] = "BE"
    Board[3][8] = "BE"
    Board[6][8] = "BR"
  else:
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "   
                     
def GetMove(StartSquare, FinishSquare):
  valid = False
  while not valid:
    try:
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first): "))
      if len(str(StartSquare)) == 2:
        valid = True
    except:
      ValueError
      print("That is not a valid input, please enter a two digit coordinate (e.g. '11')")
  valid = False
  while not valid:
    try:
      FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      if len(str(FinishSquare)) == 2:
        valid = True
    except:
      ValueError
      print("That is not a valid input, please enter a two digit coordinate (e.g. '11')")
  return StartSquare, FinishSquare
 
def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  Piecename = Board[StartRank][StartFile]
  Color1,Type1 = GetPieceName(Piecename)
  Piecename = Board[FinishRank][FinishFile]
  Color,Type = GetPieceName(Piecename)
  if Type != ' ':
    print()
    print("{0} {1} takes {2} {3} ".format(Color1,Type1,Color,Type))
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    print()
    print("White Reddum has been promoted to Marzaz pani")
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    print()
    print("Black Reddum has been promoted to Marzaz pani")
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
  else:
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile] 
    Board[StartRank][StartFile] = "  "
 
 
def ConfirmMove(StartSquare, FinishSquare):
  StartCoordinate1 = (str(StartSquare)[0])
  StartCoordinate2 = (str(StartSquare)[1])
  FinishCoordinate1 = (str(FinishSquare)[0])
  FinishCoordinate2 = (str(FinishSquare)[1])
  print("Move from Rank {0},File {1} to Rank {2}, File {3}? ".format(StartCoordinate1,StartCoordinate2,FinishCoordinate1,FinishCoordinate2))
  Confirmed = input("Confirm move (Yes/No)?: ")
 
  return Confirmed
 
def GetPieceName(Piecename):
  PieceColor = Piecename[0]
  PieceType = Piecename[1]
 
  if PieceColor == 'B':
    Color = 'Black'
  else:
    Color = 'White'
     
  if PieceType == 'S':
    Type = 'Sarrum'
  elif PieceType == 'M':
    Type = 'Marzaz pani'
  elif PieceType == 'N':
    Type = 'Nabu'
  elif PieceType == 'E':
    Type = 'Eltu'
  elif PieceType == 'G':
    Type = 'Gisgigir'
  elif PieceType == 'R':
    Type = 'Redum'
  else:
    Type = ' '
    
  return Color,Type

def play_game(SampleGame): 
  Board = CreateBoard() #0th index not used
  StartSquare = 0
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
##    SampleGame = input("Do you want to play the sample game (enter Y for Yes)? ")
##    SampleGame = SampleGame.lower()[0]
    while SampleGame != "y" and SampleGame != "n":
      print("please enter Y or N")
      SampleGame = input("Do you want to play the sample game (enter Y for Yes)? ")
      SampleGame = SampleGame.lower()[0]
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        confirm = "n"
        while confirm == "n":
          StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
          confirm = ConfirmMove(StartSquare,FinishSquare)
         
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
      GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
      MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
      if GameOver:
        DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"
    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)
 
if __name__== "__main__":
  display_menu()
  Choice = get_menu_selection()
  make_selection(Choice)
  