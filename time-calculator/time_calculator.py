def add_time(start, duration, day=-1):

  #creates variables
  n = 0
  numWeek = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
  dayNum = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
  
  #splits inputs
  time, ap = start.split(' ')
  currHour, currMin = tuple(map(int, time.split(':')))
  addHour, addMin = tuple(map(int, duration.split(':')))

  if ap == "PM":
    currHour += 12

  if day != -1:
    day = day.capitalize()
    day = dayNum[day]

  #print(f'Current Time = {currHour:2d}:{currMin:02d}')

  #adjusts current minutes
  currMin += addMin

  if currMin >= 60:
    addHour += currMin//60
    currMin %= 60  

  #adjust current hours
  currHour += addHour

  if currHour >= 24:
    n = currHour//24
    currHour %= 24

  #adjusts day
  if day != -1:
    day += n
    day %= 7
    
  # print(f'Current Time = {currHour:2d}:{currMin:02d}')
  # print(f'{n:02d}\n')

  if currHour >= 0 and currHour < 12:
    ap = "AM"
    if currHour == 0:
      currHour = 12
  else:
    ap = "PM"
    if currHour != 12:
      currHour -= 12

  currHour = str(currHour)
  currMin = f'{currMin:02d}'
  
  new_time = currHour + ":" + currMin + " " + ap

  if day != -1:
    new_time += ", " + numWeek[day]

  if n == 1:
    new_time += " (next day)"
  elif n > 1:
    new_time += " (" + str(n) + " days later)"
    
  
  return new_time