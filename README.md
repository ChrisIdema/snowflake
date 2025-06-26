# snowflake




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
coordinates and lengths of

crystal growth is not simulated, instead a tree with branch positions and dimensions is constructed using random parameters
this tree is symmetrical and 6 identical copies are used to render the snowflake


# example output
```
```

# AI usage disclosure
No AI was used in code generation or assistance with writing code.