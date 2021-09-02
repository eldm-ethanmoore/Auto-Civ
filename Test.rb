require 'perlin_noise'

def isGreater(floatValue)
    if floatValue>=0.5
        return "Land"
    elsif floatValue<0.5
        return "Water"
    end
end
tileArray=[]
n2d =  Perlin::Noise.new 2
counter = 0
0.step(100, 0.01) do |x|
  0.step(100, 0.01) do |y|
    tileType=isGreater(n2d[x, y])
    tileArray[counter]=tileType
    if counter==768
      break
    end
    counter = counter + 1
    puts counter
    puts tileType
    puts n2d[x, y]
  end
end
puts rand(10)