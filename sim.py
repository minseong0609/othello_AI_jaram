
def isValid(board,tile,xstart,ystart):
#tile 값      0: 흑돌       1: 백돌
    if (board[xstart][ystart] != -1 or not isOnBoard(xstart, ystart)):
        # print("occupied")
        return 0
    
    board[xstart][ystart] = tile

    if tile == 0:
        otherTile = 1
    else:
        otherTile = 0

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x,y = xstart, ystart
        x += xdirection
        y += ydirection

        if isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection

            if not isOnBoard(x,y):
                continue

            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                
                if not isOnBoard(x,y):
                    break

            if not isOnBoard(x,y):
                continue

            if board[x][y] == tile:

                while True:
                    x-=xdirection
                    y-=ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x,y])

    board[xstart][ystart] = -1
    if len(tilesToFlip) == 0:
        # print("no flip")
        return 0
    # print("ok")
    return [xstart,ystart,tilesToFlip]


def isOnBoard(x,y):
    # coordinates board limit
    return x>=0 and x<= 7 and y>=0 and y<=7

def getvalidcoordination(board,player):
    val = []
    for x in range(0,8):
        for y in range(0,8):
            temp = isValid(board,player,x,y)
        # print(type(temp))
            if temp == 0:
                continue
            val.append(temp)
    return val


def ai_stone(placeable,board):
    possible_position = getvalidcoordination(board,0)
    max = -1
    num = 0
    for i in range(len(possible_position)):
        check=0
        xpos,ypos = possible_position[i][0],possible_position[i][1]
        if([xpos,ypos] == ([1,0]or[0,1]or[1,1]or[6,0]or[7,0]or[6,1]or[6,7]or[0,6]or[1,6]or[1,7]or[6,6]or[7,6]or[6,7])):
           continue
        
        elif([xpos, ypos] == ([0,0]or[0,7]or[7,0]or[7,7])):
           return [xpos,ypos]
        
        elif (max <= len(possible_position[i][2])):
            max = len(possible_position[i][2])
            num = i
            check=1
    if(check==0):
        for i in range(len(possible_position)):
            if (max <= len(possible_position[i][2])):
                max = len(possible_position[i][2])
                num = i
            
    xpos,ypos = possible_position[i][0],possible_position[i][1]
    return [xpos,ypos]
##코드가 좀 더럽다는 생각이 드실 수 있는데 파이썬에 스위치문이 없어서 if로 구현했습니다.
##오델로에 대한 전략이나 필승법을 찾아보면 [0,0]을 먹는것이 승리할 가능성이 높지만 그 바로 옆칸들인
##[0,1], [1,1], [1,0]을 먹는다면 상대가 [0,0]을 먹을 수 있어 가능한 피하는 것이 좋습니다.
##그렇다면 알고리즘은 [0,0], [0,7], [7,7], [7,0] 바로 옆칸을 먹는 경우는 피하면서 가장 많은 수를 뒤집는
##방안을 선택해야하며 핵심인 저 4개를 먹을 수 있다면 먹는다는 선택을 해야 합니다.

##75번째 줄에서 시작하는 for문은 위의 내용대로 돌아가게 만든 것입니다.
##그런데 만약 둘 수 있는 곳이 [0,0], [0,7], [7,7], [7,0] 바로 옆칸들밖에 없다면 그 칸들 중 최선의 수를
##선택해야 합니다. 그래서 check변수를 추가했습니다.
##check가 1이라면 정상적으로 최선의 수를 찾았다는 의미이고 check가 0이라면 최선의 수를 찾지 못한 것이기에 
##그나마 괜찮은 수를 찾을 수 있도록 만들었습니다.
