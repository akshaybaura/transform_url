# Degreed Data Engineering Code Challenge


## Requirements
* Please spend no more than 2 hours on this challenge.
* Please use **python 3** to complete this challenge
* Please fork this repository and complete your work on a branch. When ready, open a pull request from your branch to the master branch on your fork.
  * For example, user jdoe will open a pull request from jdoe/my-branch to jdoe/master.
  * Please do not open a pull request directly against this repo.
* Please make your updates in [lib/transformer.py](lib/transformer.py). You should not need to make any changes to [main.py](main.py).
* Please do include comments in your code to help us understand your decision making (but no need to explain each line)

## Problem Background
Degreed is a lifelong learning platform that individuals and organizations use to discover learning content, build skills, and certify their expertise. In today's world, learners can find content from a wide variety of both public and private sources, including websites like Coursera, Udacity, and Pluralsight; company-specific systems known as "Learning Management Systems" (LMSs); a wide variety of public blogs and enterprise knowledge systems; and, of course, offline sources like books, classrooms, etc.

Degreed allows users to track their learning across all these sources by adding articles, videos, books, courses, events to their Degreed Profile. We track all of these as "completions," which are stored in our application database and then synchronized to our analytics data warehouse.

Across our hundreds of enterprise clients and millions of users, we've accumulated tens of millions of these completions for analysis. However, it can be really difficult to make sense of trends at that scale, especially since the source URLs for all of these systems are highly variable. The types of questions we're asking ourselves are:
* What are some of the most used websites across our user base?
* What new websites are emerging that users are learning from, that we might consider integrating with?

## Challenge
**Your challenge is to process a sample dataset of Degreed "completions" and label them by their URL hostname (e.g. `www.youtube.com` and domain (e.g. `youtube.com`).**

We don't expect this to be an incredibly sophisticated system, it's just a prototype... we're much more interested in how you tackle the problem, test your solution, and design your system overall. Let's assume we'd do things quite differentely in production, where we'd have all the supporting infrastructure too!

Use Python for this challenge, but please use whatever libraries and boilerplates you prefer to tackle these requirements:
* Import the sample dataset (feel free to manually transform the input file however you like)
* Transform each completion and compute a new field to store the URL hostname that is extracted from the "ContentUrl"
* (OPTIONAL) Similarly, also compute another new field to store the URL domain
* Output the transformed dataset to an output file (any format is fine)

These requirements are meant to be flexible and a little bit vague, so use your best judgment to design a solution that'll work without taking too long. Specifically, it's worth mentioning a few "anti"-requirements:
1. No specific requirement for the input or output file formats
2. No specific requirement for how you compute the hostname
3. No specific require around performance, runtime, etc.
4. No specific require for streaming, batch, incremental, etc.
5. No specific requirement for how to test, but we *would* prefer to see some test cases where possible

Example pseudocode:
```
python3 main.py
```

### Submitting Your Code
When you're finished, you can either email us an archive or link us to a (private) repository with your submission. We'd like you to keep your personal code private - at least for now - so that other candidates don't end up copying from (or being intimidated by!) your solution. We're not overly concerned about this, though, so you can use a public Github repo too, as long as you're OK taking it offline once we've reviewed it together. Appreciate it!

### Expectations
We don't expect you to have production-quality code for this challenge; set a timelimit for whatever time you can spare (no longer than two hours, please) and tackle the problem like you would for building a proof-of-concept solution. In other words, we definitely prefer *code quality* over *code quantity*.

### TL;DR
* Build a (simple) transform pipeline that computes the URL hostname for a dataset of completions
* Use Python for this challenge, but any libraries and tools you prefer
* Use the sample CSV dataset for input
* Submit your code as a ZIP file or a private repo; something we can review together
* Write good, clean code, but not production quality!
* Spend no more than 2 hours on this challenge - we know your time is valuable
* Use the Internet! It's not cheating to Google stuff (but do cite your sources for any code you directly copy)
* Assume requirements will change over time and we'll want to improve all of this later :)


## Dataset
The dataset can be found in the `data` directory - [Degreed Example Completions](data/Degreed_ExampleCompletions.csv).

It's a CSV file of sample data pulled from some of our internal Degreed team usage, anonymized, cleaned up, and with most of the unrelated columns removed for clarity. The schema is simply:

Column     | Description
-----------|--------------------------------------------
UserId     | ID assigned to the user in Degreed
ContentId  | ID assigned to the content item in Degreed
ContentUrl | URL where the content can be accessed

### Example Data
UserId | ContentId | ContentUrl
-------|-----------|--------------------------------------------------------------------------
6494   | 9734      | https://youtu.be/hq8UQvjXnRk
2154   | 82        | https://degreed.com/articles/jail-breaking-the-college-degree---getti...
6494   | 82        | https://degreed.com/articles/jail-breaking-the-college-degree---getti...
172    | 934       | https://www.foxbusiness.com/business-leaders/tom-siebel-employee-educ...
1066   | 7957      | https://www.nytimes.com/2019/06/07/business/economy/age-discriminatio...
5430   | 1836      | https://degreed.zoom.us/recording/share/Vxlxfv0HeHQuKP67BymYZGNhd-5IC...
3584   | 3057      | https://hbr.org/2019/06/what-happens-when-you-lose-your-mentor
3137   | 9349      | https://www.youtube.com/watch?v=4Thk0QG9xak
2154   | 2100      | https://www.kqed.org/news/11752389/ghost-ship-trial-defendant-replace...
