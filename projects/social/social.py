import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    # create a user.
    # user has a name
    def __init__(self, name):
        self.name = name


class SocialGraph:
    # keeps track of the connections separately
    def __init__(self):
        # num of users
        self.last_id = 0
        # user dict
        self.users = {}
        # friendship dict
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            # add  to friendship dict
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.

        if you had 10 users and you want each of those users to have an average
        of 2 friends...num_users * avg_friendships
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # use num_users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # make a list with all possible friendships
        # example
        # 5 users
        # [(1,2), (1,3), (1,4), (1,5) *DON"T WANT (2,1)* (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)]
        # empty list
        friendships = []
        # go from the first if to the last.
        # (range do not give the last..
        # +1 will enable the last is return)
        for user in range(1, self.last_id + 1):
            # friend should not start a 1.
            # should start at the next.
            # when the loop returns,  it should not go back to the last
            # visited. it should go to the friend next to the last
            # visited
            for friend in range(user + 1, num_users + 1):

                friendship = (user, friend)
                friendships.append(friendship)

        # shuffle the list
        self.fisher_yates_shuffle(friendships)

        # take as many as we need
        # how many do we need?
        total_friendships = num_users * avg_friendships

        random_friendships = friendships[:total_friendships // 2]

        # add to self.friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # use BFS because we are ask for the shortest friendship path
        # create a queue
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)


# fisher yates shuffle
# iterate through the list
# at every step choose a random index
# then swap them
