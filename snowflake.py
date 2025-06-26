from math import atan2, degrees

grid_width = 51
font_height_to_width = 32/14

grid_height = int(((grid_width / font_height_to_width)//2)*2+1)

max_length_sq = (grid_width//2)**2

arm_index = 0

levels = 2

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
            #line[x] = chr(segment_index + ord('0'))
            line[x] = "|/\\|/\\"[segment_index]


    flake += ''.join(line)


print(flake)

#binary tree
root = {"origin": 0,
        
        "length" : 0.5,
        "children":[]
        }

root["children"].append(
{"origin":0.5,
 "angle" : 30,
"length" : 0.1,
"children":[]
}

)