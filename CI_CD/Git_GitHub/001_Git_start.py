"""
git setup 
git help 

"""
##############1 Git setup ##############
git config 

#view all of your settings 
# --show-origin         show origin of config (file, standard input, blob, command line)
git config --list --show-origin

#set your identity 
#first time to do after git installation 
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com


#check your configuration setting
git config --list

#config your default text editor 
#Vim, Emacs and Notepad++ are popular text editors often used by developers on Unix-based systems like Linux and macOS or a Windows system.
$ git config --global core.editor emacs
or 
$ git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

##To set main as the default branch name
$ git config --global init.defaultBranch main

#a specific key’s value is by typing git config <key>
git config user.name
git config user.email 
git config remote.origin.url
note: can use "git config --list" to find out all keys 

#For unexpected value and you don't know why 
#query Git as to the origin for that value, and it will tell you which configuration file had the final say in setting that value
git config --show-origin rerere.autoUpdate

##############2 git help ##############
git help <verb>
git <verb> help
man git-<verb> 

git help config 
 git add -h 


