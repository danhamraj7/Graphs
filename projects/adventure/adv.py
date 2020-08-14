# understanding
# what is this asking for
# visit every single one of  500 rooms at least once
# with the fewest steps
# order of visitation does not matter
# need to keep track of where we are going
# need to keep track of where we have being
# we need a list of direction that goes e w n s


# plan
# do not use spaghetti code
# build a graph
#  pick a room
#  choose a direction to explore
#  when arrival is a room without any exit
#  backtrack to a room with an unexplored exit.
# do that until all the rooms are explored

# use
# stacks
# queues
# dfs bfs


from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development
# and testing purposes.

# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# keep track of the number of moves
total_moves = []

# when arrival is a room without any exit
# return to next unexplored room


def entry_exit(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"
    else:
        return None


def path_from_room():
    # create stack
    stack = Stack()

    # make a set to track if we visited that node before
    visited = set()

    # while visited is less than total amount of rooms
    while len(visited) < len(world.rooms):
        path = []

        # check for exits in the current room
        for exits in player.current_room.get_exits():

            # if the current room exists is not in visited
            if player.current_room.get_room_in_direction(exits) not in visited:
                # append the exits to paths
                path.append(exits)

        # add current room to visited
        if player.current_room not in visited:
            visited.add(player.current_room)

        # if length of path is greater than 0
        # randint() method returns an integer
        # number selected element from the specified range.
        if len(path) > 0:
            new_path_move = random.randint(0, len(path) - 1)

            # print(new_path_move)
            # push new path move to path
            stack.push(path[new_path_move])
            # push the player traveled to path
            player.travel(path[new_path_move])

            # print(path)
            # append path to total moves
            total_moves.append(path[new_path_move])
        else:
            # Remove from list
            last = stack.pop()
            # add the last to entry because we have to go back
            player.travel(entry_exit(last))
            # append the last to total moves to keep track
            total_moves.append(entry_exit(last))


path_from_room()
traversal_path = total_moves


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
