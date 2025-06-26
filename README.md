# snowflake

https://stackoverflow.com/beta/challenges/79669436/code-challenge-3-creating-ascii-art-snowflakes


```
Your submission should include:
- An explanation of your snowflake creation approach
- The code you have written to create the snowflake(s)
- An example of some snowflakes that your code has created!
- AI usage disclosure
- Instructions for how others can run your code to observe how it works
- Anything you learned or any interesting challenges you faced while coding!
```

# explanation

plate snow flake generation using ascii art

1 branch is generated, the other branches are copies that are rotated

1 branch is max 60 degrees wide, so 30 degrees on each side
there is no 30 degree ascii char so a 30 degree line has to be approximated

a rectangular grid is used, both height and with are odd length so that there is an exact center
the height in rows is lower than the width in columns since the character grid is not square

grid has odd length size so there is a center
the center is marked with a `~`

coordinates are normalized to `[-1,1]`
position and lengths of children are relative to parent, 
length can never exceed length half of parent
width can never exceed double the with of the parent
minimum 1 and maximum 3 levels are used (including root) to simplify structure and stack usage

crystal growth is not simulated, instead a tree with branch positions and dimensions is constructed using random parameters
this tree is symmetrical and 6 identical copies are used to render the snowflake

# code

Code is written in python with standard python libraries.

# example output
```
```

# AI usage disclosure
No AI was used in code generation or assistance with writing code.

# instructions

# Lessons learned

- for ascii art the height/width ratio of characters is not 1:1 and not constant and depends on font
- This Veritasium video taught me how snow crystals grow https://www.youtube.com/watch?v=ao2Jfm35XeE