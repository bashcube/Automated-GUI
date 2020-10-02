# Automating Tasks with GUI
  * ## Requirements:
      For Debian Based Systems, install firefox browser for opening github pages,
      and mpg123 for playing musing in the terminal.
      ```bash
      $ sudo apt-get install firefox
      $ sudo apt-get install mpg123
      ```
      Systems which use rpm packages, install the above using command:
      ```bash
      $ sudo dnf install firefox
      $ sudo dnf install mpg123
      ```
      
  * ## Usage:
      Clone the repo on your local machine using command:
      ```bash
      $ git clone https://github.com/bashcube/Automated-GUI
      ```
      Change the directory and run the pythn file using command:
      ```bash
      $ cd Automated-GUI
      $ python task.py
      ```
      
   * ## Description:
       The following python code automates three tasks 
       through simple GUI and displays the result accordingly.
       These tasks are:
       * Opening Github Account.
       * Opening Gmail Account.
       * Playing Music from the respective directory.
       The python file contains the code and the text file contains the 
       process of automating the program to start at boot.
       
   * ## Output:
      ![Here's an output of code running.](Screenshot.png)
