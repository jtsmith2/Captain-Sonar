import itertools
from collections import defaultdict

class csmap:
    def __init__(self, name, gridsize, islands):
        self.name = name
        self.gridsize = gridsize
        self.islands = islands

def find_tracks(gridsize, islands, tracklength):
    '''
    Returns the track with the max number of possible starting locations
    for a given grid, island locations, and length
    '''

    tracks = defaultdict(list)

    #Creates a generator of all possible permutations of the directions for
    #the specified length.
    for track in itertools.product('NSEW', repeat=tracklength):
        #Creates a grid, starting at (1,1) and ending at (gridsize, gridsize)
        for point in itertools.product(range(1,gridsize+1), repeat=2):
            #Checks to see if the given track is possible on the given map
            if track_possible(point, track, islands, gridsize):
                tracks[track].append(point)

    max_key = max(tracks, key= lambda x: obj_func(tracks[x]))

    return max_key, tracks[max_key]

def obj_func(point_list):
    '''
    This function takes the point list for each track and calculates
    the metric by which the "best" track is determined. Right now,
    the one that has the most possible starting points.  Another idea:
    max average distance between points.
    '''
    return len(point_list)

def track_possible(start, track, islands, gridsize):
    x,y = start

    history = [start]
    
    #(1,1) is in NW corner
    for d in track:
        if d is 'N':
            y -= 1
        elif d is 'S':
            y += 1
        elif d is 'E':
            x += 1
        else: # d is 'W'
            x -= 1

        #Check to see if the track takes us off the map
        if x == 0 or y == 0 or x > gridsize or y > gridsize:
            return False

        #Does it run into an island
        if (x,y) in islands:
            return False

        #Does it cross over itself?
        if (x,y) in history:
            return False

        history.append((x,y))

    return True

def main():

    min_track_length = 3  #shortest track to find
    max_track_length = 6  #longest track to find. Runtime gets long around 10

    maps = []
    maps.append(csmap('Turn Based Bravo Map', 10, [(4,1),(8,2),(3,4),(8,4),(3,5),(7,7),(4,9)]))

    for m in maps:
        print(m.name)
        for l in range(min_track_length, max_track_length + 1):
            print(l, find_tracks(m.gridsize, m.islands, l))

if __name__ == '__main__':
    main()
