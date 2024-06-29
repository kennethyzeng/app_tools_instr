"""
Git basic 
    -configure and initialize a repository 
    -begina nd stop tracking files and files pattern
    -how to undo mistakes quickly and easily 
    -how to browse the history of your project and view changes between commit 
    -how to push and pull from remote repositories 
"""
############## 1. Getting a git repository ###############
#two ways. Method 1: clone the existing git repository from elsewhere, such as github
#use https://
git clone https://github.com/kennethyzeng  (link)

#use SSH transfer protocol 
git:// or user@server:path/to/repo.git 

#Method 2: take a local directory which is not under version control, turn it into git repository 
@CLI 
#1 CLI for case 1: don't have project yet(empty directory)
cd /Users/user/my_project     #some redirectory
git init 

#2: CLI for case 2: start version -controlling existing files
#need tracking those files and do an initial commit 
git add *.c 
git add LICENSE 
git commit -m "INitial project version"

############## 2. Recording change to the repository ###############
git status      #help to check/filter out untracked files 
git add README   #README is modified file as example. To track README file to be staged 
#git add .

#if you want to unstage file for files 
git restore --staged README   #example; to unstage one file 
#git restore -staged .      #to unstage all
or 
git reset HEAD README  #example. to unstage one file 
git reset HEAD .      #unstage all files

############## 3. Short status ###############
short status -s      
or 
short status --short


