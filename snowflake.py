from math import atan2, degrees, radians, sin, cos
import random  # random, choice, randint
import time
import sys


# render preferences:
grid_width = 79 # has to be odd
font_height_to_width = 32/14 # set this to your font ratio. (in vscode I used 32/14, but on "https://www.online-python.com/" I used 20/7)
grid_height = int(((grid_width / font_height_to_width)//2)*2+1)
max_length_sq = 0.9**2


# creates a tree with random branch posititions, angles and lengths, doesn't create mirrored branches
def create_half_tree(level, number_of_levels):
    node = {"connection": 0,                
    "l" : 0,
    "w": 0,
    "angle":0,
    "children":[]        
    }

    if level == 0:
        node["connection"] = 0
    else:
        node["connection"] = random.uniform(0.1,0.9)

    if level == 0:
        node["w"] = random.uniform(0.01,0.2)
    else:
        node["w"] = random.uniform(0.5,2)

    if level == 0:
        node["l"] = random.uniform(0.1,0.9)
    else:
        node["l"] = random.uniform(0.1,0.5)
    
    
    if level == 0:
        node["angle"] = 0        
    elif level == 1:
        node["angle"] = 30
    elif level >= 2:
        node["angle"] = random.choice([30,150])

    number_of_children = random.randint(0,3)

    if level < number_of_levels:
        for i in range(number_of_children):
            child = create_half_tree(level+1, number_of_levels)
            node["children"].append(child)

    return node


# mirrors a node since all branches are symmetrical
def mirror_node(node):
    copy = node.copy()
    copy["angle"] *= -1
    return copy


# mirrors all nodes in a tree, starting at leaf nodes
def mirror_tree(node):
    for child in node["children"]:
        mirror_tree(child)

    mirror_children = [mirror_node(child) for child in node["children"]]
    node["children"] += mirror_children


# extracts all individual nodes from a tree, convertes relative dimensions into absoulte dimensions
def get_nodes(root, nodes=[],l=1,w=1, angle=0, origin=[0,0]):
    node = root.copy()
    node["children"] = []
    node["l"] *= l
    node["w"] *= w
    node["angle"] += angle

    nodes.append(node)

    x = origin[0] + sin(radians(angle)) * node["connection"] * l
    y = origin[1] - cos(radians(angle)) * node["connection"] * l
    node["origin"] = [x, y]
    
    for child in root["children"]:
        get_nodes(child,nodes, node["l"], node["w"], node["angle"], node["origin"])

    return nodes


# rotates a point around origin, used to see if a point intersects with a rotated square
def rotate(origin, point, angle):    
    ox, oy = origin
    px, py = point

    x2 = ox + cos(radians(angle)) * (px - ox) - sin(radians(angle)) * (py - oy)
    y2 = oy + sin(radians(angle)) * (px - ox) + cos(radians(angle)) * (py - oy)
    return [x2,y2]


# checks if a point intersects with a rotated square
def is_in_node(node, point):
    # rotate point around origin in opposite direction
    x,y = rotate(node["origin"],point,-node["angle"])

    # compare rotated point to rotated straightened rectangle
    return  x >= node["origin"][0] - node["w"] and x <= node["origin"][0] + node["w"] and \
            y <= node["origin"][1] and y >= node["origin"][1] - node["l"]

# create a full random tree using a seed and returns all nodes
def create_tree(seed=None):
    random.seed(seed)
    tree = create_half_tree(0, random.randint(1,3))
    mirror_tree(tree)
    nodes = get_nodes(tree)
    return nodes


# renders the nodes in ascii, an svg function is under development
def render_flake_ascii(nodes):
    flake = ""
    for y in range(grid_height):
        line = list(" "*grid_width+"\n")
        for x in range(grid_width):
            # get coordinates relative to center:
            dx = (x - grid_width//2) / (grid_width//2)
            dy = (y - grid_height//2) / (grid_height//2)
            length_sq = dx**2 + dy**2 # length squared so no need to calculate square root

            angle_degrees = degrees(atan2(dy,dx)) + 90
            if angle_degrees > 180:
                angle_degrees -= 360

            if length_sq == 0:
                line[x] = '~'
            elif length_sq > max_length_sq:
                pass 
            else:
                segment_index = int(((angle_degrees + 30 + 360) %360)//60)
                octant_index = round(((angle_degrees + 360) %360)/45)%8
                octant_array = "|/=\\|/=\\"
                octant_char = octant_array[octant_index] 

                hex_array = "|//z=\\\\N|/7z=\\\\N"

                dx2,dy2 = rotate([0,0],[dx,dy],segment_index*-60)
                for node in nodes:                
                    in_node = is_in_node(node,[dx2,dy2])
                    if in_node:
                        # octant_index = round(((node["angle"]+segment_index*60 + 360) %360)/45)%8
                        # octant_char = octant_array[octant_index]                        
                        # line[x] = octant_char

                        hex_index = round(((node["angle"]+segment_index*60 + 360) %360)/22.5)%16
                        hex_char = hex_array[hex_index]                        
                        line[x] = hex_char

                        break

        flake += ''.join(line)
    return flake


if __name__ == "__main__":
    seed = None
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
   
    if not seed:
        seed = int(time.time()*10)
    print(f"seed: {seed}")
    nodes = create_tree(seed)
    ascii_flake = render_flake_ascii(nodes)
    print(ascii_flake)