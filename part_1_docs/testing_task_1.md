### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  #  there is no "init" method


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# card.value only has 1 "=" it needs 2 like "==" as in its current form it is resigning the value instead of comparing.
# above "else" is not followed by a colon which will throw an error.
   

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
#  "card1" and "card2" aren't seperated by a comma.
# return "card" should be "card1". 
# "dif" should be "def" to define the function.
  


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
# the function isnt indented properly so is not part of the "CardGame" class.
# total is not holding any value, to add card.value you would ideally set it egual to "0".
# the returning statement is trying to add a string and a int. to sort this you could format it or set the total to a str.
# "return" isnt indented properly, it will only iterate once and return one value. it needs set back inline with "for" to complete iteration of each card and return a true value.
  
```
