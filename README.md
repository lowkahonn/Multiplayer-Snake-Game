# Multiplayer-Snake-Game
It is an epic snake game, which has brought us a lot of memories, but I decided to give it a twist.
I made it a two-player game so that the joy can be shared by two people!

How To Play:
Player 1 is white in colour, movement control keys are arrow keys.
Player 2 is green in colour, movement control keys are W,A,S and D.

There will only be one food at a time, where players compete to grow longer.
If two players collide each other in the head, the player with longer body wins!
If Player 1's head collide with Player 2's body, Player 1 loses!
If Player 2's head collide with Player 1's body, Player 2 loses!

The frame per second will increase with time, to escalate the excitement, so beware!

Give it a try! :)

## How to use

### Building executables

Build .exe file for windows with pyinstaller module with flag `--onefile` for one file executable.
```console
pyinstaller snake.py --onefile
```

Then run snake.exe in your dist/ folder.

### Running with python without executables

Create a virutal environment with `virtualenv` and activate it, then install the modules required modules.
```console
virtualenv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

Then run it! 
Note: You might need to change python to python3.
```console
python snake.py
```
