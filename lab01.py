# Import modules
import sys
from helper import *
from ruamel import yaml

class User:
    IDDD = ""
    first_name = ""
    last_name = ""
    birth_date = ""
    address = ""
    score = ""

if __name__ == "__main__":
    #########################################
    #              Procedure 1              #
    #########################################
    # Add print statement here
    print('DevNet')

    #########################################
    #              Procedure 2              #
    #########################################
    print('##################')
    print('###### YAML ######')
    print('##################')

# Open the user.yaml file as read only
with open('user.yaml', 'r') as stream:

    # Load the stream using safe_load
    user_yaml = yaml.safe_load(stream)

# Print the object type
print("Type of user_yaml variable:")
print(type(user_yaml))

# Iterate over the keys of the user_yaml and print them
print('Keys in user_yaml:')
for key in user_yaml:
    print(key)




USSS = User()

# Assign values from the user_yaml to the object user
USSS.IDDD = user_yaml['id']
USSS.first_name = user_yaml['first_name']
USSS.last_name = user_yaml['last_name']
USSS.birth_date = user_yaml['birth_date']
USSS.address = user_yaml['address']
USSS.score = user_yaml['score']

# Print the user object
print('User object:')
print(USSS)
print(XXXX)