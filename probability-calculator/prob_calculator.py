import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []

    for color, num in kwargs.items():
      for i in range(num):
        self.contents.append(color)

  def draw(self, numBalls):  
    if numBalls >= len(self.contents):
      return self.contents

    drawn = []

    for i in range(numBalls):
      ind = random.randint(0, len(self.contents)-1)       
      drawn.append(self.contents.pop(ind))

    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0

  for i in range(num_experiments):
    tempHat = copy.deepcopy(hat)

    results = tempHat.draw(num_balls_drawn)
    numResults = []
    
    for color in expected_balls:
      numResults.append(results.count(color))

    if numResults >= list(expected_balls.values()):
      m += 1
  
  return m/num_experiments