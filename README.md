# Downloads-Manager
This Python script can automatically moves files from the downloads directory to designated folders based on their extensions. Say goodbye to all the clutter!

## How it Works

#### Modules used:
- The OS module allows Python to interact with an operating systmem. In this case it is used to obtain directory paths.
- The Shutil module allows for more complex interactions with the file system. It is used here to move files to designated directories based on their extentions.

#### How to use:
1. Make sure you have Python3 installed
1. Make sure that the directory paths defined in the beginning of the program exist in your system
2. Move downloads_manager.py to your downloads directory
3. Set up a cron job that runs the program every hour by executing the following commands:
  * `~ % crontab - e`
  * Press 'i' to insert the following command into crontab
  * `~ % 0 */1 * * * cd ~/Downloads/ && python3 downloads_manager.py`
  * Press 'esc' and enter ':wq" to save your cron job
4. Say goodbye to the clutter!

#### Learn more about how to run cron jobs:
[‘crontab’ in Linux with Examples](https://crontab.guru)

## References & Citations
* [Organize-Downloads-Files](https://github.com/nitish-dev-1503/Organize-Download-Files)
* [Automation & Python: Organizing Files](https://medium.com/swlh/automation-python-organizing-files-5d2b6b933402)
* [shutil — High-level file operations](https://docs.python.org/3/library/shutil.html)
* [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
