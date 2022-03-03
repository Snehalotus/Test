import git

test = "This is a test file"
print(test)
print("This is a test addition")
print("This is test2")
print("This is test3")

remoteurl = "git@github.com:snehasiripurapu/Test.git"
#localfolder = "/codefromgit"

myrepo = git.cmd.Git(remoteurl)
myrepo.pull()
#merge ppull
