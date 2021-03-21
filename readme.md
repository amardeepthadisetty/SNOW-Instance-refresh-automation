This script automates to refresh the servicenow instance by logging into developer.servicenow.com by typing username and password automatically and clicking on sign in and then refreshes the instance and signs out of the instance.

Steps to use the script :

1)First install python 3.8 version exectuable from python official webste and open the executable and check the option to add the path and install it.
2)Open command prompt and type these commands
pip install --upgrade pip
pip install --upgrade Pillow

3)Now install pyautogui which provides diff funcions like mouse and keyboard operations to automate the daily common tasks.

pip install pyautogui

Official docs for pyautogui:
https://pyautogui.readthedocs.io/en/latest/index.html

4) Make a screenshot of chrome icon and name it with chrome_image2.PNG. Make sure, the chrome browser is open(Or else adjust the code according to your needs)

5) Open command prompt and run the "refresh_instance.py" script by
py refresh_instance.py

6)If all went good, the script should refresh your service now instance

Extra info:
The coordinates of x and y are configured according to my screen. You need to adjust the x and y coordinates, according to your needs by using the fucntion 
pyautogui.displayMousePosition()
The above line, keeps printing the x and y coordinates, as you keep moving your mouse. So use the above function to know the coordinates and adjust it, according to your needs.