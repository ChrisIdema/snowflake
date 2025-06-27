# snowflake

plate snow flake generation using ascii art for stackoverflow challange

https://stackoverflow.com/beta/challenges/79669436/code-challenge-3-creating-ascii-art-snowflakes


# Explanation

Parameters for 1 segment are generated, the other 5 segments are copies that are rotated by 60 degree increments. The reason is that real snow flakes have nearly identical segments since they all form under the same conditions (temperature, pressure, humidity, airflow, etc.).

1 branch is max 60 degrees wide, so 30 degrees on each side.

A rectangular grid is used, both height and width are odd length so that there is an exact center.

The height in rows is lower than the width in columns since the character grid is not square. This is adjusted using font_height_to_width.

The center is marked with a ~

Coordinates are normalized to [-1,1].

Position and lengths of children are relative to parent. Length can never exceed length half of parent. Width can never exceed double the width of the parent. Minimum 1 and maximum 3 levels are used (including root) to simplify structure.

Crystal growth is not simulated, instead a tree with branch positions and dimensions is constructed using random parameters this tree is symmetrical and 6 identical copies are used to render the snowflake

Segments can stick through their parent segments, I haven't made a restriction for that. Should not be hard to do.

I used different ASCII characters for different growth directions.


# Code

Code is written in python with standard python libraries.

# Example outputs

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

# Instructions

```
python snowflake.py
```
Or test it out here: https://www.programiz.com/online-compiler/18t8SQgYJDB64

# Lessons learned

- for ascii art the height/width ratio of characters is not 1:1 and not constant and depends on font
- This Veritasium video taught me how snow crystals grow https://www.youtube.com/watch?v=ao2Jfm35XeE