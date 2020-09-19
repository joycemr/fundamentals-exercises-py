# fundamentals-exercises-py
# This Repo contains programming fundamentals exercises

They will challenge you to work with variables, conditionals, loops, and functions.

There are many solutions to the problems. If you are looking for more exercises look to [codewars.com](https://www.codewars.com/dashboard)

## Problem 1

Fizz Buzz

print numbers from 1 to 100. However, if the number is divisible by 3 print fizz, if the number is divisible by 5 print buzz, if the number is divisible by both 3 and 5 print fizzbuzz

OUTPUT
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz

## Problem 2

Find the odd int

https://www.codewars.com/kata/54da5a58ea159efa38000836

- given an array of integers, find the one that appears an odd number of times

test_arr1 = [1,2,3,7,7,3,1,1,1,2,6,7,6] answer: 7
test_arr2 = [10,55,55,10,12,14,12,14,55] answer: 55
test_arr3 = [1,1,2,2,3] answer: 3
test_arr4 = [5,4,68,90,4,5,4,5,4,5,90,68,90] answer: 90
test_arr5 = [1] answer: 1
test_arr6 = [2,2,1] answer: 1
test_arr7 = [3,3,3,3,3,3,3] answer: 3
test_arr8 = [4,3,4,3,4,3,4,3,4,3,4,3,4] answer: 4
test_arr9 = [1,2,3,1,2,3,1,2,3,1,2,3,1] answer: 1

## Problem 3

Stop gninnipS My sdroW!

https://www.codewars.com/kata/5264d2b162488dc400000001

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: 

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 

spinWords( "This is a test") => returns "This is a test" 

spinWords( "This is another test") => returns "This is rehtona test"


## Problem 4

Zip Arrays

Given 2 arrays of identical size you need to zip the two arrays together maintaining their order.

Example:

array_one = [1,5,2]
array_two = [3,6,4]
zipped_array = [1,3,5,6,2,4]

## Problem 5

Zip Arrays Expanded

Given any number of arrays of identical size you need to zip the arrays together maintaing their order.

Example:

array_one = [1,2,3]
array_two = [7,8,9]
array_three = [a,b,c]
zipped_array = [1,7,a,2,8,b,3,9,c]

Example:

array_one = [1,2,3]
array_two = [4,5,6]
array_three = ["red", "green", "blue"]
array_four = [0,0,0]

zipped_array = [1,4,"red",0,2,5,"green",0,3,6,"blue",0]

## Problem 6

Modify your algorithm from the previous exercise that will zip together any number of arrays with any lengths

Example:

array_one = [1,2,3]
array_two = ["horse", "dog", "cat", "fly"]
array_three = [15]
array_four = [6,7,8,9,10,11]

zipped_array = [1, "horse", 15, 6, 2, "dog", 7, 3, "cat", 8, "fly", 9, 10, 11]
