# 6)Furniture:

# Household type, total area and furniture name listThe new house has no furniture at all.
# Furniture has a name and area, of whichBed: 4 square metersWardrobe: 2 square metersTable:
# 1.5 square meters
# Add the above three pieces of furniture to the house
# When printing a house, output is required: household type, total area, remaining area,
# furniture name list.


class Home: 
    def __init__ (self, type_, area, bed, wardrobe, table):
        self.type_ = type_
        self.area = area
        self.bed = bed 
        self.wardrobe = wardrobe
        self.table = table
    def desk (self):
        print (self.type_, self.area, self.bed, self.wardrobe, self.table)

class Furniture (Home):
    def __init__ (self):
        self.bed = 4
        self.wardrobe = 2
        self.table = 1.5

    def area(self):
        return self.area

    def square (self, area):
        number = (self.bed + self.wardrobe + self.table)
        remaining_area = ( self.area - number)

info = Home ('household', 150, 'bed', 'wardrobe', 'table')
info.desk()

wood = Furniture()
wood.area()
wood.square()       
