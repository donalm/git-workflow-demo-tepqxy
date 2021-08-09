# Git Flow Exercise

## Setting up.

This might all work on Windows, but that's untested.

1. Fork this project on gitlab, and clone it to your workstation.
1. Create a virtualenv called 'venv' for the modules in the dev-requirements.txt file, and enable it.

You should now be able to run `tox` in the project's base directory, and the tests for the project will run. One of the tests should fail, and both `black` and `flake8` will complain

## The exercise.

1. Create a bugfix branch, fix the failing test, and push that branch to your repo.
1. Create a merge request for that branch.
1. Create a qa branch off of main.
1. Fix the code quality issues, and push your fixes to your qa branch.
1. Create a merge request for that branch.

You're done! Thanks for stepping through this exercise.
