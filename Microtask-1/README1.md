**Microtask-1:** Produce a Python script that produces configuration files for Mordred to analyze a complete GitHub organization, excluding repositories that are forks from other GitHub repositories. Test it with at least two GitHub organizations, producing screenshots of the resulting dashboard.

There is a python script which generates Mordred configuration as well as projects.json file.

To analyse any Github organisation:

Command to run:

```python3 task1.py organisation_name```

It will create two files :- organisation_name.cfg and organisation_name.json .
Enter your user-id ,password,and API-token in organisation_name.cfg file.

Then run the command:

```mordred -c organisation_name.cfg```

It is assumed that elasticsearch and kibana is running.

This should produce the promised dashboard, Point your web browser to your [Kibiter/Kibana instance](http://localhost:5601), click on Dashboard in the left menu,and then select any option to veiw corresponding visualizations.

**Dashboard_Screenshot folder contains the visualization of two organisations(Strace and Submitty).**
