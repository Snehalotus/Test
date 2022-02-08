import git

test = "This is a test file"
print(test)

remoteurl = "git@github.com:snehasiripurapu/Test.git"
#localfolder = "/codefromgit"

myrepo = git.cmd.Git(remoteurl)
myrepo.pull()