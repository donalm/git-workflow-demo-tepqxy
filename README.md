# Git Flow Exercise

## Getting started

This might all work on Windows, but that's untested.

Fork this project on gitlab, and clone it to your workstation.

Create a virtualenv for the modules in the dev-requirements.txt file, and enable it.

You should now be able to run `tox` and the tests for the project will run.

One of the tests will fail, and both `black and flake8 will complain

1. Create a bugfix branch, fix the failing test, and push that branch to your repo.
2. Create a merge request for that branch.
3. Create a qa branch off of main.
4. Fix the code quality issues, and push your fixes to your qa branch.
5. Create a merge request for that branch.


You're done!
