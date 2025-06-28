# snowflake

Plate snow flake generation using ascii art in python for stackoverflow challange

https://stackoverflow.com/beta/challenges/79669436/code-challenge-3-creating-ascii-art-snowflakes


# Explanation

Parameters for 1 segment are generated, the other 5 segments are copies that are rotated by 60 degree increments. The reason is that real snow flakes have nearly identical segments since they all form under the same conditions (temperature, pressure, humidity, airflow, etc.).

1 branch is max 60 degrees wide, so 30 degrees on each side.

A rectangular grid is used, both height and width are odd length so that there is an exact center.

The height in rows is lower than the width in columns since the character grid is not square. This is adjusted using `font_height_to_width`.

The center is marked with a `~`

Coordinates are normalized to `[-1,1]`.

Position and lengths of children are relative to parent.
Length can never exceed length half of parent.
Width can never exceed double the width of the parent.
Minimum 1 and maximum 3 levels are used (including root) to simplify structure.

Crystal growth is not simulated, instead a tree with branch positions and dimensions is constructed using random parameters
this tree is symmetrical and 6 identical copies are used to render the snowflake

Segments can stick through their parent segments, I haven't made a restriction for that. Should not be hard to do.

I used different ASCII characters for different growth directions.

# Code

Code is written in python with standard python libraries.

# Example outputs

```
seed: 17511081380


                                  ||       ||
                               \\NNN||   ||///zz
                                \\NNN|||||///zz
                                  \NNN|||///z
                                  \\NN|||//zz
              ||                   N  |||  /                   ||
           \\NNN||              NNNNN\|||z/////              ||///zz
            \\NNN|||             |NNNN|||////|             |||///zz
              \NNNN|   NNN      ||NNzz|||////||      ///   |////z
       \ \\\\\\\\\\N  NNNN\\\\\   \zz||||//||   zzzzz////  /zzzzzzzzzz z
       ==========\\\\\\|NNNNN|\   ||z||||/|||   |\\////|zzzzzz==========
      zz zzzzzzzz   z\\\\\\NNN\\\\|||||||||||zzz\\\\zzzzzz\   \\\\\\\\ \\
                 =======|\\\\\\\\\    |||    zzzzzzzzz========
                 =======||\\\\\\\\\   |||   zzzzzz============
                    \\\\ z\\\\\ \\\\\\|||zzzzzz zzzzzz zzzz
                            \\      \\\~\\\      \\
                    zzzz zzzzzz zzzzzz|||\\\\\\ \\\\\z \\\\
                 ============zzzzzz   |||   \\\\\\\\\||=======
                 ========zzzzzzzzz    |||    \\\\\\\\\|=======
      \\ \\\\\\\\   \zzzzzz\\\\zzz|||||||||||\\\\NNN\\\\\\z   zzzzzzzz zz
       ==========zzzzzz|////\\|   |||/||||z||   \|NNNNN|\\\\\\==========
       z zzzzzzzzzz/  ////zzzzz   ||//||||zz\   \\\\\NNNN  N\\\\\\\\\\ \
              z////|   ///      ||////|||zzNN||      NNN   |NNNN\
            zz///|||             |////|||NNNN|             |||NNN\\
           zz///||              /////z|||\NNNNN              ||NNN\\
              ||                   /  |||  N                   ||
                                  zz//|||NN\\
                                  z///|||NNN\
                                zz///|||||NNN\\
                               zz///||   ||NNN\\
                                  ||       ||
```

```
seed: 17511082569


                                 //|||||||||NN
                                 //|||||||||NN
                          ||||||||||||||||||///||||||
                         ||||NNNNN||||||||||//////||||
                   \\ \\\||||NNNNN||||||||||z/////||||zzz zz
                 \\\ NN\\     NNNN\|||||||||z////     zz// zzz
           \\==\NNNNNNNN      \NN\\|||||||||zz//z      //////z/z==zz
          \\\\\\\NNNNNNNN||||\\\NNN|||||||||///zzz||||//////z/zzzzzzz
        \\\\\\\\\\\\\NNNNNN||| \  N|||||||||/  z |||//////zzzzzzzzzzzzz
       \\\\\\\\\\\\\\\\\\NNN       |||||||||       ///zzzzzzzzzzzzzzzzzz
       NNN\\\\\\\\\\\\\\\\\\\      |||||||||      zzzzzzzzzzzzzzzzzzz///
         \\\=\\\\\\\\\\\\\\\\\\\\  |||||||||  zzzzzzzzzzzzzzzzzzz====z
         \\======z\\\\\\\\\\\\\\\\\\|||||||zzzzzzzzzzzzzzzzzz\=======z
       \\ \=======zz==\\\\\\\\\\\\\\\|||||zzzzzzzzzzzzzzz==\\=======z zz
         \\\\   zzzzz     \\\\\\\\\\\\|||zzzzzzzzzzzz     \\\\\   zzzz
         \\\      zzz         \\\\\\\\\~\\\\\\\\\         zzz      \\\
         zzzz   \\\\\     zzzzzzzzzzzz|||\\\\\\\\\\\\     zzzzz   \\\\
       zz z=======\\==zzzzzzzzzzzzzzz|||||\\\\\\\\\\\\\\\==zz=======\ \\
         z=======\zzzzzzzzzzzzzzzzzz|||||||\\\\\\\\\\\\\\\\\\z======\\
         z====zzzzzzzzzzzzzzzzzzz  |||||||||  \\\\\\\\\\\\\\\\\\\\=\\\
       ///zzzzzzzzzzzzzzzzzzz      |||||||||      \\\\\\\\\\\\\\\\\\\NNN
       zzzzzzzzzzzzzzzzzz///       |||||||||       NNN\\\\\\\\\\\\\\\\\\
        zzzzzzzzzzzzz//////||| z  /|||||||||N  \ |||NNNNNN\\\\\\\\\\\\\
          zzzzzzz/z//////||||zzz///|||||||||NNN\\\||||NNNNNNNN\\\\\\\
           zz==z/z//////      z//zz|||||||||\\NN\      NNNNNNNN\==\\
                 zzz //zz     ////z|||||||||\NNNN     \\NN \\\
                   zz zzz||||/////z||||||||||NNNNN||||\\\ \\
                         ||||//////||||||||||NNNNN||||
                          ||||||///||||||||||||||||||
                                 NN|||||||||//
                                 NN|||||||||//
```

# svg output

<img src="./17511082569.svg">

# AI usage disclosure

No AI was used in code generation or assistance with writing code.

# Instructions

```
python snowflake.py
```
add an optional seed:
```
python snowflake.py 17511081380
```

optional svg path
```
python snowflake.py 17511081380 17511081380.svg
```

Or test it out here: https://www.online-python.com/a2dPrnBHDF

# Lessons learned

- for ascii art the height/width ratio of characters is not 1:1 and not constant and depends on font
- This Veritasium video taught me how snow crystals grow https://www.youtube.com/watch?v=ao2Jfm35XeE