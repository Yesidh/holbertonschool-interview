<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>




# :colombia: 0x0A-slide_line
## Goal
The goal of this task is to reproduce the 2048 game(NSFW !!) mechanics on a single horizontal line.

Given an array of integers, we want to be able to slide & merge it to the left or to the right. Identical numbers, if they are contiguous or separated by zeros, should be merged
## Prerequisites
- Write a function that slides and merges an array of integers
- Prototype: int slide_line(int *line, size_t size, int direction);
- Where line points to an array of integers containing size elements, that must be slided & merged to the direction represented by direction. direction can be either:
  - SLIDE_LEFT
  - SLIDE_RIGHT
  - If it is something else, the function must fail
  - Both macros SLIDE_LEFT and SLIDE_RIGHT must be defined in slide_line.h
- Your function must return 1 upon success, or 0 upon failure
- You are not allowed to allocate memory dynamically (malloc, calloc, …)
## Built With
- Your programs and functions will be compiled with gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic## Contributing
- You are not allowed to use global variables
- No more than 5 functions per file
## Versioning
for my learning in Holberton School
## Authors
---Yesid Gutierrez  944@holbertonshcool.com                                    
                                                                               
## Files

|             directories               |             Description                  |
|--------------------------------| ---------------------------------------- |
|**0-slide_line.c**| the main function |
|**slide_line.h**| prototype header file |
|**0-main.c**| test file|