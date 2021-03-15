# Ask the user for a list of three friends
#  For Each friend , we will tell the user weather thay are nearby
#  For each nearby friend we will save their name to 'nearby_friends.txt'


# hint: readLines()


friends = input("Enter three friend names, separated by commas (no spaces, please): ").split(',')
#  ['sasha', 'sayana', 'bato']

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]
# print(people_nearby) ===> ['Sasha\n', 'Bato\n', 'Lena\n', 'Sophie\n', 'Charlie\n', 'Wilson\n', 'Nina\n', 'Harley']
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)
# print(friends_set, people_nearby_set)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them!')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()



