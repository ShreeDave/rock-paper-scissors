# rock-paper-scissors
 In this game a player plays either 'Rock', 'Paper' or 'Scissors' and the computer tries to beat the player based on the player's previous moves. 
For every move, either the player gets 1 point or the computer gets 1 point. The game runs till either the player or the computer reaches a score of 10 points.
A player should play his/her move by entering the numbers 0, 1 and 2 where- 0 denotes 'rock', 1 denotes 'paper', and 2 denotes 'scissors'.

In the algorithm, the computer should keep a count of player moves (i.e., the counts for 0, 1 and 2) in three separate variables - count_rock, count_paper and count_scissors. The algorithm should decide the computer's move based on the following possibilities:

If count_rock  >  count_paper and count_rock  >  count_scissors, then the computer's move should be ROCK.
If count_paper  >  count_rock and count_paper  >  count_scissors, then the computer's move should be PAPER.

If count_scissors  >  count_rock and count_scissors  >  count_paper, then the computer's move should be SCISSORS.

In all other cases, the computer should play ROCK, PAPER and SCISSORS randomly.