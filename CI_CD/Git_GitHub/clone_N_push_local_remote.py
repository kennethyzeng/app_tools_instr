#1 Git is CI_CD tool 

#2 Usage 
  #check git version 
    git version 

#3 Procedure of clone your repo from github to local machine, then push back to github 
#@ local CLI 
git version 
git clone https://xxxxx.com/xxxx/xxx    #(repository link)
cd xx
ls -la
git status    
git add .   #add all file, so they are tracked
git commit - m "xxxx"

#optional
#if you want to match github's two boxes: title and description
git commit -m "xxxx" -m "xxxx"

#push file to a remote repository when my project is host(github)
git push 


#4 Username and password based access have been removed due to security reason.
Github now use GCM
Git Credential Manager (GCM) is a secure Git credential helper built on .NET that runs on Windows, macOS, and Linux.
https://github.com/git-ecosystem/git-credential-manager/blob/main/README.md

https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.4.1

#location
 /usr/local/share/gcm-core
 
 Git configuration (~/.gitconfig): 
$ git-credential-manager configure

To configure GCM for all users, run the following command to update the system Git configuration: 
$ git-credential-manager configure --system

Uninstall
If you wish to uninstall GCM, run the following script:
$ /usr/local/share/gcm-core/uninstall.sh
