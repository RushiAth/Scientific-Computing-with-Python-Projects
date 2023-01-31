def arithmetic_arranger(problems, ansFlag=False):

  n = len(problems)

  #checks error condition
  if n > 5:
    return "Error: Too many problems."

  #creates lists and receives input
  firstLine, secondLine, dashes, answers = [], [], [], []
  
  splitProblems = [problems[i].split(" ") for i in range(n)]

  #loops over each problem
  for prob in splitProblems:
    #checks problem specific error conditions
    if prob[1] != '+' and prob[1] != '-':
      return "Error: Operator must be '+' or '-'."

    if not prob[0].isdigit() or not prob[2].isdigit():
      return "Error: Numbers must only contain digits."

    if len(prob[0]) > 4 or len(prob[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    #determines formatting variables
    width = max(len(prob[0]), len(prob[2])) + 1

    if prob[1] == '+':
      temp = str(int(prob[0]) + int(prob[2]))
    else:
      temp = str(int(prob[0]) - int(prob[2]))
  
    #appends formatted string to each list    
    answers.append(' ' * (width - len(temp) + 1) + temp)

    dashes.append('-' * (width + 1))

    firstLine.append(' ' * (width - len(prob[0]) + 1) + prob[0])
    secondLine.append(prob[1] + ' ' * (width - len(prob[2])) + prob[2])

  #creates return string
  arranged_problems = '    '.join(firstLine) + '\n' + '    '.join(
    secondLine) + '\n' + '    '.join(dashes) 
  
  if ansFlag:
    arranged_problems += '\n' + '    '.join(answers)

  return arranged_problems
