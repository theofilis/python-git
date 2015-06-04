from git import Actor, Repo, exc
import os
from datetime import datetime

join = os.path.join

home = '/home/theofilis/Documents/personal/'
path = join(home, 'python-git')
remote_path = 'git@github.com:theofilis/python-git.git'

# Init repository
try:
    repo = Repo(path)
except exc.InvalidGitRepositoryError:
    repo = Repo.init(path)

try:
    repo.remotes.origin.exists()
except:
    origin = repo.create_remote('origin', remote_path)

index = repo.index

add_files = [] + repo.untracked_files

for u_file in repo.index.diff(None):
        add_files.append(u_file.b_path)

if add_files:
    index.add(add_files)

    author = Actor("George Theofilis", "theofilis.g@gmail.com")
    committer = Actor("George Theofilis", "theofilis.g@gmail.com")

    msg = '%s' % datetime.now().isoformat()
    print repo.index.commit(msg, author=author, committer=committer)

# SWAG
repo.remotes.origin.push(repo.head)