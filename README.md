# Prerequisites
1. git, docker, docker-compose installed

# Steps
1. Clone the repo and navigate to it
```
git clone https://github.com/vireshuberoy/testforclassforma.git
cd testforclassforma
```
2. Create a .env file with the following content:
```
APPSECRETKEY=<any string>
SALT=<a salt for passwords>
```
3. Run the docker-compose commands:
```
docker-compose build
docker-compose up
```
