# Guess US State Names


## Project Overview
This is a tool to learn the names of the states in the US.
 
A map of the United States is displayed.

Where the user is prompted to enter the name of a state.

With each correct entry, the name of the state would appear on the map. 

Upon exit of the game, the remaining names of the states would be saved to a file for study.
## Objectives
- Convert each user entry into title case.
- Check if the guess is among the 50 states.
- Write correct guesses onto the map.
- The user would be allowed to keep guessing until the map is filled or exits the game.
- Record the guesses in a list.
- Keep track of the score.
- Save the remaining state names to a file.

## Results
![image](https://github.com/frantzalexander/states-guessing-game/assets/128331579/d23ae497-5923-4e31-9813-9f08bbd865cb)


## Process
The project is divided into two modules:
- The Scoreboard Module
- The Main Game Module

```mermaid
flowchart TD
start(((START)))
scoreboard{Scoreboard Module}
main{Main Game Module}
write_answer[Write Answer to Map Location]
map_image[Import Map Image Data from File]
state_data[Import state data from csv File]
game[Create Game Conditions]
prompt[Prompt User for Answer]
convert[Convert User Input into Title Casing]
score[Display Score]
save[Save Remaining States to File]
finish(((END)))
start --> main
start --> scoreboard
scoreboard --> write_answer
write_answer --> main
main --> map_image
map_image --> state_data
state_data --> game
game --> prompt
prompt --> convert
convert --> score
score --> save
save --> finish
