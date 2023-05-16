#Assignment: User
# For this assignment you will create the user class and add a couple of methods!

class User:

    def __init__(self, first_name, last_name,email,age):
        self.is_rewards_member = False
        self.gold_reward_points = 0
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email





# Attributes
# On instantiation of a user, the following attributes, should be passed in as arguments:

# first_name
# last_name
# email 
# age
# Also include default attributes:

# is_rewards_member - default value of False
# gold_card_points = 0 
# Methods:
# display_info(self) - Have this method print all of the user's details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200
# spend_points(self, amount) - have this method decrease the user's points by the amount specified 
# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.