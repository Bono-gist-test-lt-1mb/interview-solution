# README.md for interview problem solution

## Problem Description

### The problem description can be found in the file:

    Operability Engineer Take-Home Assignment - Google Docs.pdf 

As there is no copyright statement in this file I have not included it in this repo.

### A summary of the problem statement could be:

Write a containerized api which will return the gist list for a github user. Specific cosiderations for the api's request url are contained in the problem statement document. Provide automated testing for same.



## File inventory

| Filename    | Comments                                           |
| ----------- | -------------------------------------------------- |
| Dockerfile  | Docker file to build image.                        |
| LICENSE     | MIT License file                                   |
| README.MD   | This README.MD                                     |
| gist_api.py | The api code which is built into the docker image. |
| tests.py    | The test code also built into the docker image.    |

## Installation

*Open a termianl and clone the git repo*

`git clone https://github.com/Bono-gist-test-lt-1mb/interview-solution.git`     



## Build the docker image

*cd into the folder created*

`cd interview-solution`

*Let us assume the image will be tagged interview-solution:v1.0.0 for the following instructions.*

*Build the image*

docker build -t interview-solution:v1.0.0 .

*When the image build is done. As per the instruction pdf we are running on port 8080*

## Run the container

docker run --rm --name interview-solution -p 8080:8080 interview-solution:v1.0.0

*At this point you should have a running container with outout like:*

* Serving Flask app 'gist_api'
* Debug mode: on
  
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8080
* Running on http://172.17.0.2:8080
  Press CTRL+C to quit
* Restarting with stat
* Debugger is active!
* Debugger PIN: 272-926-020

*Note your PIN and ip addresses may differ.*

 

#### Potential issues

If you get a message like "The container name "/interview-solution" is already in use by container", you need to assess if you can delete the container mentioned in the message, if you can do so, if not then use a different unque name after the --name flag in the docker run command.



## Testing

### Automated

*open a new terminal and execute the following*

`docker exec -t interview-solution python tests.py`

*You should observe output like:*

About to test User: octocat, expected count 8
User: octocat, expected count 8, received count 8
About to test User: Bono-gist-test-lt-1mb, expected count 1
User: Bono-gist-test-lt-1mb, expected count 1, received count 1
.

----------------------------------------------------------------------

Ran 1 test in 0.393s

OK

*This could be run in a shell script during a build process as a simple smoke test,*



### Manual

Use wget or curl to hit the url 

http://<your machine ip>:8080/<github user name> 

and visually inspect the output.



## Cleanup

- A ^C will stop the container interview-solution.
  The container will be automtically removed due to the --rm command line option.

- You will need to delete the docker image using
  `docker rmi interview-solution:v1.0.0`
  If you built the image multiple times you may have other images from your machine.

- You may want to remove the cloned repo.



## Version Information

| Version Name | Release Date | Semantic Version |
| ------------ | ------------ | ---------------- |
| Initial      | 21-Oct-2023  | 1.0.0            |
|              |              |                  |
|              |              |                  |



## Author

*Author info goes here*
















