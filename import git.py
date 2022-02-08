import git


remoteurl = "git@github.com:snehasiripurapu/Test.git"
#localfolder = "/codefromgit"

myrepo = git.cmd.Git(remoteurl)
myrepo.pull()