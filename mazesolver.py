global gridx,gridy
class mazesolve:
    global grid,stack
    
    def __init__(self,x,y):
        global gridx,gridy,grid,flag,stack
        gridx=x
        gridy=y
        grid=[]
        flag=0
        stack=[]
        
    def creategrid(self):
        global gridy,gridx,grid
        for i in range(gridy):
            l=list(map(int,input().split()))
            grid.append(l)
            
    def printgrid(self):
        global grid
        print(grid)
    
    def solvemaze(self,posx,posy):
        global grid,gridx,gridy,flag,stack
        ret=0
        if posx==gridx-1 and posy==0:
            flag=1
            return
        if not flag==1:
            if posx+1<gridx and not grid[posy][posx+1]==0 and not  (not stack==[] and stack[-1])=="Left":
                stack.append("Right")
                defflag=1
                print("Done1")
                ret=self.solvemaze(posx+1,posy)
                if ret==0:
                    grid[posy][posx]=0
        if not flag==1:    
            if posy+1<gridy and not grid[posy+1][posx]==0 and not (not stack==[] and stack[-1])=="Up":
                stack.append("Down")
                print("Done3")
                defflag=1
                self.solvemaze(posx,posy+1)
                if ret==0:
                    grid[posy][posx]=0
        
        if not flag==1:         
            if posx-1>=0 and not grid[posy][posx-1]==0 and not (not stack==[] and stack[-1])=="Right":
                stack.append("Left")
                print("Done2")
                defflag=1
                self.solvemaze(posx-1,posy)
                if ret==0:
                    grid[posy][posx]=0
                
        if not flag==1:        
            if posy-1>=0 and not grid[posy-1][posx]==0 and not (not stack==[] and stack[-1])=="Down":
                stack.append("Up")
                print("Done4")
                defflag=1
                self.solvemaze(posx,posy-1)
                if ret==0:
                    grid[posy][posx]=0
        if not flag==1:        
            if ret==0:
                grid[posy][posx]=0
                stack.pop()
                return 0
            else:
                return 1
            
    def result(self):
        print(stack)
    
def main():
    print("Enter grid size(x,y):")
    x,y=map(int,input().split())
    ob=mazesolve(x,y)
    print("Enter grid: 1 for open block 0 for closed:")
    ob.creategrid()
    ob.solvemaze(0,gridy-1)
    ob.result()
main()
