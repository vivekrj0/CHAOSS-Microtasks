**Microtask 2:** Produce a Python script that adds a new GitHub repository (git and GitHub issues / pull requests) to a given set of Mordred configuration files. Test it by adding at least two repositories (in two separate steps) to a GrimoireLab dashboard, producing screenshots of the results.

There is a python script which generates two files(mordred and project.json file) of the following organisation which is passed upon running the script.

Command to run :

```python3 task2.py organisation_name repository_name```

It will create two files :- * *organisation_name-repository_name.cfg* * and * *organisation_name-repository_name.json* * . Enter your user-id ,password,and API-token in organisation_name-repository_name.cfg file.

Then run the command:

```mordred -c organisation_name-repository_name.cfg```

It is assumed that elasticsearch and kibana is running.

This should add the new Github repository of any org in the initial condition.

I have added Grimoirelab-mordred repository in one step and Neovim-bot-ci repository in another step.

**Dashboard_Screenshot folder contains the visualization before and after adding of new repository.**
