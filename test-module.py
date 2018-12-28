
# remove """ """ from each code block and execute independently
courses = ['History', 'Maths', 'Physics', 'CompSci']

##################
"""
import my_module   #used to import my_module from this directory
#if we want to use a component of the imported module. we use import_module_name.component_name. for ex. we will use the #function find_index from my_module in this module by using my_module.find_index and input our parameters
index = my_module.find_index(courses,'Maths')
print(index)
"""

##################
# we can also import the module with a particular name and use that name wherever as given below
"""
import my_module as mm
index = mm.find_index(courses,'Maths')
print(index)
"""

##################

# we can also import just one component(for example: function) from a module the method for which is given below
"""
from my_module import find_index, test

index = find_index(courses, 'Maths')  # no need to write the module name, we can directly write the imported
print(index)
print(test)
"""
####################

# to import everything and we dont have to write the module name.imported component
"""
from my_module import *

index = find_index(courses, 'Maths')
print(index)
print(test)
"""
####################

# to print the list of paths where  python checks for module to import and will import directly from the module name itself
"""
from my_module import find_index, test
import sys
index = find_index(courses, 'Maths')  # no need to write the module name, we can directly write the imported
print(index)
print(test)
print(sys.path)
"""
####################
# to import from a particular address
import sys
sys.path.append('/Users/rajatrathee/Desktop/my_module')
from my_module import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(sys.path)

# we can also add the path in python path environmental variable. Where we can directly import the module
# For mac: 1. Open Terminal. 2.  To use the built in text editor for terminal : nano, type: nano ~/.bash_profile 3. Anywhere on the file type - export PYTHONPATH="/Users/rajatrathee/Desktop/my_module" 4. Press ctrl+x 5. Press Y 6. Restart terminal 7. type python 8. type import my_module
