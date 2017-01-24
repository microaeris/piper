---
layout: post
title: "Retro Programming with Chip8"
description: "Chip8 game for the Global Game Jam 2017"
og-image: "global_game_jam_2014/rtr-splash-crop.png"
tags: [games]
---



I went into this year's Global Game Jam knowing that I wanted to make a Chip8 game since I recently implemented an [interpretor](https://github.com/Ahris/chip8) for it. I find Chip8 especially appealing because the system is easy to understand and you can reason through all of the memory operations in your head. The games that came out of the [OctoJam](http://www.awfuljams.com/octojam-iii) were also a source of inspiration - some of the final products are seriously cool! You should check out the video they made to showcase the results.

So, the theme to this year's Global Game Jam is "waves". The game [Jordan Mecom](http://jmecom.github.io/), [Lillian Wang](https://lillworkspace.wordpress.com/), and I made was called __Piper__. Our game was inspired by Pixar's short film of the same name. Piper is a little bird who is learning to hunt for shells and goodies on the beach. But when the wave comes in, she needs to hide in the sand to avoid getting wet. The waves wash in new goodies for Piper to pick up. Your goal is to collect as many goodies as you can and to avoid getting wet.

Without further ado, you can play the game [here](http://johnearnest.github.io/Octo/index.html?gist=43849adc04c2deab31e94c5932ffbca8)!

# Challenges

Making this game was a refreshing learning experience. I wanted to write down my thoughts so others can go on to make even better Chip8 games!

## Design

The hardest part was designing a game to the constraints of the system. Balancing the game - goodies spawn near top of the screen - but going near the top of the screen is risky because you have less time to react. If you put your head down, you can't move or pick up items. So it's a balance between risk and reward. I felt like the game loop was satisfyig for how small the game is.

Memory
only 16 registers, 4k total memory. Have to save labels in flash. load and save to mem.

Collisions - draws do an xor. Sets a collision flag if a on bit is flipped off. Have to draw each sprite seperately to check for collisions. It's slow. So we didn't want to do collisions of the wave since it's a screen/bunch of sprites.


Splash screen
(show python script)
normally, you can just draw the art and import it into your game. For us, we had to convert it to binary, and then chunk it up into "tiles". A tile is an 8 by X area of the screen, where x can be anywhere from 1 to 15.

Waves
Here is the beautiful GIF Lillian drew - we never even imagined our simple graphics could look so good!

At first, we tried drawing the whole screen, but too slow. Find the smallest area we coudl draw of each frame. Find the offset. Cut into tiles, only draw the needed tiles.

Timers
Had to share one timer. so other timers just shared the values and samples the delay timer and save it to a seperate register.

Smooth animations
Have to use delay timer to cap the frame rate
Have to draw and then redraw to erase a frame in an animation
timer for bird relied on the fact that the int rolled over and decided on a frame based on the number of times the bird was drawn.

most graphics on chp8 are really primative, really happy we were able to get a cool animation and splash screen in our game!

Timing your animations has game play effects. Making waves faster looked better, but was harder to paly since players had less time to react. I freezed the frame for 30 cycles on game over so the player can register why they died. It feels a lot better to understand their mistake.

Coding
    functions don't have arguments, and you don't have a stack. gotta load them into registers first.