import pyautogui

#pyautogui.displayMousePosition()
button7location = pyautogui.click('E:/automate_scripts/chrome_image2.PNG')

pyautogui.PAUSE = 3
#print(button7location)
#pyautogui.click('new_tab.PNG')
pyautogui.keyDown('ctrl')  # hold down the shift key
pyautogui.press('t')     # press the left arrow key
pyautogui.keyUp('ctrl')    # release the shift key


pyautogui.typewrite('https://developer.servicenow.com\n', 0.0005)

pyautogui.PAUSE = 3
#pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

#pyautogui.click(1798, 216, 1, 1, 'left')
#clik on sign in button
pyautogui.moveTo(1798, 216, 3, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.click(1798, 216)

#username box triple click
#pyautogui.click(x, y, number_of_clicks, number of seconds, 'left')
#pyautogui.click(330, 424, 3, 0.0005, 'left')
pyautogui.moveTo(330, 424, 3, pyautogui.easeInQuad)     # start slow, end fast
#pyautogui.click(330, 424)
pyautogui.tripleClick()

pyautogui.typewrite('username\n', 0.0005)

pyautogui.typewrite('\t', 1)
#type password in password field
pyautogui.typewrite('password\n', 0.0005)

pyautogui.PAUSE = 5

#move cursor to profile dropdown to show up refresh status section
#pyautogui.click(1814, 215, 1, 1, 'left')
pyautogui.moveTo(1814, 215, 5, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.click()
pyautogui.PAUSE = 1
#now click on Refresh status by moving the cursor
pyautogui.click(500,815,1,2,'left') 
#print('done')
pyautogui.PAUSE = 10

#signout now
#pyautogui.click(1277,671,1,2,'left')
pyautogui.moveTo(1277, 671, 10, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.click(1277, 671)




#Now Refresh another instance

#pyautogui.click('new_tab.PNG')
pyautogui.keyDown('ctrl')  # hold down the shift key
pyautogui.press('t')     # press the left arrow key
pyautogui.keyUp('ctrl')    # release the shift key
pyautogui.typewrite('https://developer.servicenow.com\n', 0.0005)

pyautogui.PAUSE = 3
#pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')

#pyautogui.click(1798, 216, 1, 1, 'left')
#clik on sign in button
pyautogui.moveTo(1798, 216, 3, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.click(1798, 216)

#username box double click
#pyautogui.click(x, y, number_of_clicks, number of seconds, 'left')
pyautogui.moveTo(330, 424, 3, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.tripleClick()

pyautogui.typewrite('sainikhil013@outlook.com\n', 0.0005)

pyautogui.typewrite('\t', 1)
#type password in password field
pyautogui.typewrite('Amar@017\n', 0.0005)

pyautogui.PAUSE = 5

#move cursor to profile dropdown to show up refresh status section
#pyautogui.click(1814, 215, 1, 1, 'left')
pyautogui.moveTo(1814, 215, 5, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.click()
pyautogui.PAUSE = 1
#now click on Refresh status by moving the cursor
pyautogui.click(500,875,1,2,'left')
#print('done')
pyautogui.PAUSE = 10

#signout now
#pyautogui.click(1277,671,1,2,'left')
pyautogui.moveTo(1277, 671, 10, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.click(1277, 671)