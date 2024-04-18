https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/usage.md

#only need to interact with any authentication dialogs asking for credentials
git credential-manager [<command> [<args>]]

'''
get          [Git] Return a stored credential
  store        [Git] Store a credential
  erase        [Git] Erase a stored credential
  configure    Configure Git Credential Manager as the Git credential helper
  unconfigure  Unconfigure Git Credential Manager as the Git credential helper
  diagnose     Run diagnostics and gather logs to diagnose problems with Git 
               Credential Manager
  azure-repos  Commands for interacting with the Azure Repos host provider
  github       Commands for interacting with the GitHub host provider
'''

#1 Method 1: connect to github 
git credential-manager github 
git git credential-manager github login
Note: It will provide a code, ask you to click below link to enter the code for log in 
#after that, you can use your git as normal such as git push

#2 Method 2: haven't verify yet
https://mac.install.guide/git/credential-manager
    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author