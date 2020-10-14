![Github](https://github.com/fbugarski/iks-oks/blob/master/Screenshot%20from%202020-10-14%2011-32-47.png)

Xs Os is a paper and pencil game for two players,X and O,who take turns marking the spaces in 3x3 grid.The player who succeeds in placing three of their marks in a horizontal,vertical or diagonal row is the winner.

The following example game is won by the first player, X:  ![picture](https://upload.wikimedia.org/wikipedia/commons/1/1b/Tic-tac-toe-game-1.svg)


# Combinatorics

When considering only the state of the board, and after taking into account board symmetries (i.e. rotations and reflections), there are only 138 terminal board positions. A combinatorics study of the game shows that when "X" makes the first move every time, the game outcomes are as follows:[14]

91 distinct positions are won by (X)
44 distinct positions are won by (O)
3 distinct positions are drawn (often called a "cat's game")

# Strategy

Optimal strategy for player X if starting in a corner. In each grid, the shaded red X denotes the optimal move, and the location of O's next move gives the next subgrid to examine. Note that only two sequences of moves by O (both starting with center, top-right, left-mid) lead to a draw, with the remaining sequences leading to wins from X.

Optimal strategy for player O. Player O can only force a win or draw by playing in the centre first.
A player can play a perfect game of tic-tac-toe (to win or at least draw) if, each time it is their turn to play, they choose the first available move from the following list, as used in Newell and Simon's 1972 tic-tac-toe program.[16]

Win: If the player has two in a row, they can place a third to get three in a row.
Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
Fork: Create an opportunity where the player has two ways to win (two non-blocked lines of 2).
Blocking an opponent's fork: If there is only one possible fork for the opponent, the player should block it. Otherwise, the player should block all forks in any way that simultaneously allows them to create two in a row. Otherwise, the player should create a two in a row to force the opponent into defending, as long as it doesn't result in them creating a fork. For example, if "X" has two opposite corners and "O" has the center, "O" must not play a corner move in order to win. (Playing a corner move in this scenario creates a fork for "X" to win.)
Center: A player marks the center. (If it is the first move of the game, playing a corner move gives the second player more opportunities to make a mistake and may therefore be the better choice; however, it makes no difference between perfect players.)
Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
Empty corner: The player plays in a corner square.
Empty side: The player plays in a middle square on any of the 4 sides.
