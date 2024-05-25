from piazza_api import Piazza
import os

mail = os.getenv('PIAZZA_EMAIL')
password = os.getenv('PIAZZA_PASSWORD')
term = "Summer 2024" # u should change this to your current term
directory = "./" # the directory  to keep all the lectures

p = Piazza()
p.user_login(mail, password)

info = p.get_user_profile()
all_lectures = info.get("all_classes")

# finding the lectures to keep up to date
curr_lectures = {}
for lecture in all_lectures:
    if all_lectures[lecture]["term"] == term:
        curr_lectures[lecture] = all_lectures[lecture]


network = {}
for lecture in curr_lectures:
    network[lecture] = p.network(lecture)
    '''print()
    print(curr_lectures[lecture]["name"])
    print(network.get_feed(100))
    print("")
    for post in network.iter_all_posts():
        print(post)
        '''

print()

