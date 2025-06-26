# snowflake

plate snow flake generation using ascii art for stackoverflow challange

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

1 branch is generated, the other 5 branches are copies that are rotated by 60 degree increments. The reason is that real snow flakes have nearly identical segments since they all form under the same conditions (temperature, pressure, humidity, airflow, etc.).

1 branch is max 60 degrees wide, so 30 degrees on each side

a rectangular grid is used, both height and with are odd length so that there is an exact center

the height in rows is lower than the width in columns since the character grid is not square. This is adjusted using `font_height_to_width`.

The center is marked with a `~`

coordinates are normalized to `[-1,1]`
position and lengths of children are relative to parent, 
length can never exceed length half of parent
width can never exceed double the with of the parent
minimum 1 and maximum 3 levels are used (including root) to simplify structure and stack usage

crystal growth is not simulated, instead a tree with branch positions and dimensions is constructed using random parameters
this tree is symmetrical and 6 identical copies are used to render the snowflake


# code

Code is written in python with standard python libraries.

# example outputs

with fixes:
```
                                      |||
                                      |||
                                      |||
                                  NNN ||| ///
                                  NNNN|||////
                                NNNNNN|||//////
              \       NN         NNNNN|||/////         //       z
            \\\\\\\ NNNNNNNN       NN/|||///       //////// zzzzzzz
                \\\\\\\NNNNNNN      NN|||//      ///////zzzzzzz
                 ===\\\\\\\NNNN       |||       ////zzzzzzz===
                 =======\\\\\\\N      |||      /zzzzzzz=======
                    =======N\\\\\\\N N|||/ /zzzzzzz========
                                \\\\\\|||zzzzzz
                                    \\\~\\\
                                zzzzzz|||\\\\\\
                    ========zzzzzzz/ /|||N N\\\\\\\N=======
                 =======zzzzzzz/      |||      N\\\\\\\=======
                 ===zzzzzzz////       |||       NNNN\\\\\\\===
                zzzzzzz///////      //|||NN      NNNNNNN\\\\\\\
            zzzzzzz ////////       ///|||/NN       NNNNNNNN \\\\\\\
              z       //         /////|||NNNNN         NN       \
                                //////|||NNNNNN
                                  ////|||NNNN
                                  /// ||| NNN
                                      |||
                                      |||
                                      |||


```

```
                                  zzz////N\\\
                                  zz/////////
                              NNNNN//////////////
                           NNNNNN///////////////////
                       \ |||NNN||//////////////////||| z
                  NNNNN\\\|||NN||||||||||||||||///|||zzz/////
           zzzNNNNNNNNNNN\     N|||||||||||||||/     z//////////\\\\
          NNNNNNNNNNNN\NNN      |||||||||||||||      //zzz===========
        NNNNNNNNNNNNN\\\\\\     |||||||||||||||     zzzzzz============/
       |||NNNNNNNNN\\\\\\\\\\\\ ||||||||||||||| zzzzzzzzzzzz==========||
       ||||NNNNNNN\\\\\\\\\\\\\\\|||||||||||||zzzzzzzzzzzzzzz=========||
         ===NNNNN\\\\\\\\\\\\\\\\\|||||||||||zzzzzzzzzzzzzzzzz========
         ====\\\\\\\\\\\\\\\\\\\\\\\|||||||zzzzzzzzzzzzzzzzzzzzz======
         ======\\\\\\\\\\\\\\\\\\\\\\|||||zzzzzzzzzzzzzzzzzzzzz=======
          \\\\\     \\\\\\\\\\\\\\\\\\|||zzzzzzzzzzzzzzzzzz     zzzzz
           \\\          \\\\\\\\\\\\\\\~\\\\\\\\\\\\\\\          \\\
          zzzzz     zzzzzzzzzzzzzzzzzz|||\\\\\\\\\\\\\\\\\\     \\\\\
         =======zzzzzzzzzzzzzzzzzzzzz|||||\\\\\\\\\\\\\\\\\\\\\\======
         ======zzzzzzzzzzzzzzzzzzzzz|||||||\\\\\\\\\\\\\\\\\\\\\\\====
         ========zzzzzzzzzzzzzzzzz|||||||||||\\\\\\\\\\\\\\\\\NNNNN===
       ||=========zzzzzzzzzzzzzzz|||||||||||||\\\\\\\\\\\\\\\NNNNNNN||||
       ||==========zzzzzzzzzzzz ||||||||||||||| \\\\\\\\\\\\NNNNNNNNN|||
        /============zzzzzz     |||||||||||||||     \\\\\\NNNNNNNNNNNNN
          ===========zzz//      |||||||||||||||      NNN\NNNNNNNNNNNN
           \\\\//////////z     /|||||||||||||||N     \NNNNNNNNNNNzzz
                  /////zzz|||///||||||||||||||||NN|||\\\NNNNN
                       z |||//////////////////||NNN||| \
                           ///////////////////NNNNNN
                              //////////////NNNNN
                                  /////////zz
                                  \\\N////zzz

```

# AI usage disclosure
No AI was used in code generation or assistance with writing code.

# instructions

```
python snowflake.py
```

# Lessons learned

- for ascii art the height/width ratio of characters is not 1:1 and not constant and depends on font
- This Veritasium video taught me how snow crystals grow https://www.youtube.com/watch?v=ao2Jfm35XeE