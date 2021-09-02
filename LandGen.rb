require 'ruby2d'
require 'perlin_noise'

class Logic
    def self.isGreater(floatValue)
        if floatValue>=0.5
            return 'Land'
        end
        if floatValue<0.5
            return 'Water'
        end
    end
    def self.generateFactionCoords(numberOfFactions)
        coords = []
        factionNumFinished = 0
        counter = 0
        while factionNumFinished<=numberOfFactions do
            xCityCoord = divisibleBy20(rand(460))
            counter=counter+1
            yCityCoord = divisibleBy20(rand(620))
            factionNumFinished= factionNumFinished+1
            Square.new(x: xCityCoord, y: yCityCoord, size: 20, color: 'black')
            
        end
        puts coords
        return coords
    end
    def self.divisibleBy20(coordinate)
        if coordinate%20 != 0
            remainder=coordinate%20
            coordinate=coordinate+(20-remainder)
            return coordinate
        end
        return coordinate
    end
end

set title: 'autoCiv', width: 640, height: 480

x=0
y=0
numOfTileX = x/20
numOfTileY = y/20
tileArray=[]
n2d =  Perlin::Noise.new 2
counter = 0
0.step(100, 0.1) do |x|
0.step(100, 0.1) do |y|
    tileType=Logic.isGreater(n2d[x, y])
    tileArray[counter]=tileType
    if counter==768
        break
    end
    counter = counter + 1
end
end
counter=0
while y<=480 do
    while x!=640 do
        if tileArray[counter]=='Land'
            Square.new(x: x, y: y, size: 20, color: 'green')
        end
        if tileArray[counter]=='Water'
            Square.new(x: x, y: y, size: 20, color: 'aqua')
        end
        x = x + 20
        counter = counter+1
    end
    x = 0
    y = y + 20
end

factions = ['orange', 'red', 'purple', 'yellow']
x=0
y=0
counter = 0
factionNumber = rand(3)
coordsOfFactions=Logic.generateFactionCoords(factionNumber)
while y<=480 do
    while x<=640 do
        x = x + 20
    end
    x = 0
    y = y + 20
end
show