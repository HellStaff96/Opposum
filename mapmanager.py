from direct.showbase.ShowBase import ShowBase

class Mapmanager():

    def __init__(self):
        self.model = 'block'
        self.texture = 'Lana.png'
        self.colors = [
            (255, 254, 255, 1),
            (255, 254, 255, 1),
            (255, 254, 255, 1),
            (255, 254, 255, 1)
        ]

        self.startnew()
        

    def getcolor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]

    def startnew(self):
        self.land = render.attachNewNode('Land')

    def clear(self):
        self.land.removeNode()
        self.startnew()

    def loadLand(self, filename):
        self.clear()
        with open(filename, 'r') as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.add_block((x, y, z0))
                    x += 1
                y += 1
        return x, y

    def findBlocks(self, pos):
        return self.land.findAllMatches('at' + str(pos))

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True


    def findHeighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)

    def add_block(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getcolor(int(position[2]))
        self.block.setColor(self.color)

        self.block.setTag('at', str(position))



        self.block.reparentTo(self.land)
        