from noise import pnoise2
from time import *
from random import *
from os import system, name
def createTheLand(Y,X):
    #create the sea
    RepresentationOfWorld = [["~" for x in range(X)] for y in range(Y)]
    scale = float(input("enter the scaling factor(200 is good default): "))
    octaves = int(input("enter the octaves (6 is good default): "))
    persistence = float(input("enter the persistence (0.5 is good default): "))
    lacunarity = float(input("enter the lacunarity (2.0 is good default): "))
    for counterY in range(0,Y):
        for counterX in range(0,X):
            RepresentationOfWorldFloat=pnoise2(counterY / scale,
                                        counterX / scale,
                                        octaves,
                                        persistence,
                                        lacunarity,
                                        repeatx=X,
                                        repeaty=Y,
                                        )
            #print(RepresentationOfWorldFloat)
            if(RepresentationOfWorldFloat<0.03):
                RepresentationOfWorld[counterY][counterX]="~"
            elif(0.03<=RepresentationOfWorldFloat<=0.07):
                RepresentationOfWorld[counterY][counterX]="#" 
            elif(RepresentationOfWorldFloat>0.07):
                RepresentationOfWorld[counterY][counterX]="~"
    for counterX in range(0,X):
        RepresentationOfWorld[0][counterX]="~"
    for counterX in range(0,X):
        RepresentationOfWorld[Y-1][counterX]="~"
    for counterY in range(0,Y):
        RepresentationOfWorld[counterY][0]="~"
    for counterY in range(0,Y):
        RepresentationOfWorld[counterY][X-1]="~"
    return RepresentationOfWorld,scale,octaves,persistence,lacunarity
def perceiveWorld(world,Y,X,S,O,P,L):
    print(X," Wide"," - ",Y," Tall","|","Seed Info: ","Scale ",S," Octaves ",O," persistence ",
            P," lacunarity ",L)
    for counterY in range(0,Y):
        for counterX in range(0,X):
            if(counterX==X):
                break
            else:
                print(world[counterY][counterX],end="")
        print("")
def createCities(world,Y,X):
    cityNumber = 15
    i=0
    while(i<cityNumber):
        suitableLocation = False
        while(suitableLocation==False):
            cityLocation=[randint(0,Y-1),randint(0,X-1)]
            try:
                if(world[cityLocation[0]][cityLocation[1]]=="#"):
                    suitableLocation=True
                    world[cityLocation[0]][cityLocation[1]]="+"
                    i=i+1
            #Should take out index error i think I fixed it by subtracting 1 from X and Y
            except IndexError:
                break
            else:
                break
def flushThePerceived():
    print("\t",">-Loading-<")
    if(name =='nt'):
        _ = system('cls')
    else:
        _ = system('clear')
def main():
    XAxis = int(input("Enter X Axis: (90 is a good defaul): ")) 
    YAxis = int(input("Enter Y Axis: (50 is a good default): "))
    #create world
    RepresentationOfWorld,scale,octaves,persistence,lacunarity=createTheLand(YAxis,XAxis)
    perceiveWorld(RepresentationOfWorld,YAxis,XAxis,scale,octaves,persistence,lacunarity)
    flushThePerceived()
    createCities(RepresentationOfWorld,YAxis,XAxis)
    perceiveWorld(RepresentationOfWorld,YAxis,XAxis,scale,octaves,persistence,lacunarity)
main()
