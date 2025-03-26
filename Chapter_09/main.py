###############################################################
"""
#  Importing a single class
"""
# from class_modules import Car

# my_new_car = Car("audi", "a4", 2024)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()


###############################################################
"""
#  Storing Multiple Classes in a Module
"""
# from class_modules import ElectricCar

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()


###############################################################
"""
#  Importing Multiple Classes from a Module
"""
# from class_modules import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())


###############################################################
"""
#  Importing an Entire Module
"""
# import class_modules

# my_mustang = class_modules.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = class_modules.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())




###############################################################
"""
#  Importing All Classes from a Module
"""
# from class_modules import *

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())


###############################################################
"""
#  Importing a Module into a Module
"""
# from car_color import CarColor

# my_colory_car = CarColor('ford', 'mustang', 2024, 'yellow')

# my_colory_car.get_descriptive_name()
# my_colory_car.describe_color()



###############################################################
"""
#  Using Aliases
"""
from class_modules import ElectricCar as EC

print ("alireza")



