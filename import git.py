import git

test = "This is a test file"
print(test)
print("This is a test addition")

remoteurl = "git@github.com:snehasiripurapu/Test.git"
#localfolder = "/codefromgit"

myrepo = git.cmd.Git(remoteurl)
myrepo.pull()