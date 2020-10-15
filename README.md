# Build and Start Instructions
1. Create a `requirements.txt` file inside the repo.
2. Type in `pip freeze` in your Python virtual environment to view all of the dependencies. Copy them into `requirements.txt`. Can also type the following to copy the dependencies into the file directly: 
```
pip freeze >> requirements.txt  
```
3. Create a new `Dockerfile` and copy the following inside ('xxx' represents the file name to run after starting docker):
```
FROM python:3.7	
COPY . /app	
WORKDIR /app	
RUN pip install -r requirements.txt	
ENTRYPOINT ["python3"]	
CMD ["xxx"]
```
- So on start, docker will run: `python3 xxx` on its CLI.

4. To build, type the following: `docker build -t lab3 .`
5. To run, type the following: `docker run -it --name lab3 --rm -p 5000:5000 lab3` 



# Screenshots
![docker run](/screenshots/docker-run.jpg)

![lab4&5 title](/screenshots/lab4&5-title.jpg)

![docker image ls](/screenshots/docker-image-ls.jpg)

# Docker vs. Virtual Machine

| Docker | Virtual Machine |
|-----|-------|
|Lightweight|Heavyweight|
|All containers share the same host OS|Each VM runs in its own OS|
|OS virtualization|Hardware-level virtualization|
|Process-level isolation|Fully isolated|
|Fast startup|Slow startup|