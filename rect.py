
''' Maggie Buchanan
    CSCI 23000
    OOP Rectangle
    '''

def main():
    print ("Rectangle a:")
    a = Rectangle(5, 7)
    print ("area:           {}".format(a.area))
    print ("perimeter:      {}".format(a.perimeter))
    
    print ("")
    print ("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    print (b.getStats())

    
class Rectangle(object):
    def __init__(self, height = 10, width = 6):
        
            self.__Height = height
            self.__Width = width

        
    def getArea(self):
        
        return (self.__Height*self.__Width)

    def getPerimeter(self):
        return (2*self.__Height+2*self.__Width)

    def setHeight(self, tall):
        self.__Height = tall

    def setWidth(self, wide):
        self.__Width = wide

    def getHeight(self):
        return self.__Height

    def getWidth(self):
        return self.__Width

    def getStats(self):
        return ("Width:    \t{}".format(self.getWidth())
                +"\nHeight:   \t{}".format(self.getHeight())
                +"\nArea:    \t{}".format(self.getArea())
                +"\nPerimeter: \t{}".format(self.getPerimeter()))

    width = property(fget = getWidth, fset = setWidth)
    height = property(fget = getHeight, fset = setHeight)
    area = property(fget = getArea)
    perimeter = property(fget = getPerimeter)

main()
