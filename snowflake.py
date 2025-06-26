from math import atan2, degrees
from random import random

grid_width = 79
font_height_to_width = 32/14

grid_height = int(((grid_width / font_height_to_width)//2)*2+1)

max_length_sq = (grid_width//2)**2

flake = ""
for y in range(grid_height):
    line = list(" "*grid_width+"\n")
    for x in range(grid_width):
        dx = (x - grid_width//2) / (grid_width//2)
        dy = (y - grid_height//2) / (grid_height//2)
        length_sq = dx**2 + dy**2 # length squared so no need to calculate square root
        #print(x,y,dx,dy)
        angle_degrees = degrees(atan2(dy,dx)) + 90
        if angle_degrees > 180:
            angle_degrees -= 360
        #print(angle_degrees)
        #if length_sq <= max_length_sq and angle_degrees >= -30 and angle_degrees <=45:
        if length_sq == 0:
            line[x] = '~'
        elif length_sq > 0.90**2:
            line[x] = ' '
        else:
            segment_index = int(((angle_degrees + 30 + 360) %360)//60)
            octant_index = round(((angle_degrees + 360) %360)/45)%8
            #line[x] = chr(segment_index + ord('0'))
            #line[x] = "|/\\|/\\"[segment_index]
            #line[x] = "|/-\\|/-\\"[octant_index]

            if segment_index == 0:
                line[x] = "|/-\\|/-\\"[octant_index]

    flake += ''.join(line)

#print(flake)

#binary tree
root = {"origin": 0,                
        "length" : 0.75,
        "width": 0.1,
        "children":[]
        }

root["children"].append(
{"origin":0.5,
"length" : 0.5,
"width": 1,
"children":[]
}

)


flake = ""
for y in range(grid_height):
    line = list(" "*grid_width+"\n")
    for x in range(grid_width):
        dx = (x - grid_width//2) / (grid_width//2)
        dy = (y - grid_height//2) / (grid_height//2)
        length_sq = dx**2 + dy**2 # length squared so no need to calculate square root
        #print(x,y,dx,dy)
        angle_degrees = degrees(atan2(dy,dx)) + 90
        if angle_degrees > 180:
            angle_degrees -= 360
        #print(angle_degrees)
        #if length_sq <= max_length_sq and angle_degrees >= -30 and angle_degrees <=45:
        if length_sq == 0:
            line[x] = '~'
        else:
            segment_index = int(((angle_degrees + 30 + 360) %360)//60)
            octant_index = round(((angle_degrees + 360) %360)/45)%8
            octant_char = "|/-\\|/-\\"[octant_index]

            if segment_index == 0:
                #line[x] = "|/-\\|/-\\"[octant_index]

                node = root
                child = root["children"][0]

                if dx >= (0 - node["width"]) and dx <= (0 + node["width"]) and \
                   dy >= (0 - node["length"]) and dy <= (0 + node["length"]):
                    line[x] = octant_char
                elif dx >= (0 - child["width"]*node["width"]) and dx <= (0 + child["width"]*node["width"]) and \
                   dy >= (0 - child["length"]*node["length"]) and dy <= (0 + child["length"]*node["length"]):
                    line[x] = "|"


    flake += ''.join(line)

print(flake)