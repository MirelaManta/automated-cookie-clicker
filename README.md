# Cookie Clicker Bot
This is a Python script that automates the game __Cookie Clicker__ using the Selenium library.
## Requirements
* Python 3
* Selenium library
* Chrome browser
* ChromeDriver
## Installation
1. Clone the repository to your local machine using Git.
2. Install the Selenium library using pip.
```
pip install selenium
```
3. Download ChromeDriver and add the executable file to your PATH.

## Usage
4. Start the script by running the following command:
```
python cookie_clicker_bot.py
```
5. The script will open the game in a new Chrome window and start clicking on the cookie to earn more cookies.
6. Every 5 seconds, the script will check if there are any upgrades that can be purchased and buy the most expensive affordable upgrade.
7. After 5 minutes, the script will stop and print the number of cookies per second.
8. If you want to modify the amount of time the bot runs or how often it checks for upgrades, you can change the "timeout" and "five_min" variables in the script.
## License
This project is licensed under the __MIT License__ - see the LICENSE file for details.
