# djDocker
A Django Rest Application which will expose a POST endpoint. 

## Prerequisites
* Python
* Virtualenv

## Getting Started
1. Clone the repository.
2. Create virtual environment. 
```
virtualenv -p python3 venv --no-site-packages
```
3. Go to project folder
4. Activate the virtualenv on ubuntu.
```
source venv/bin/activate
```
5. Install requirements 
```
pip install -r requirements.txt
```
5. Migrate 
```
python manage.py migrate
```
6.Run project 
```
python manage.py runserver 0.0.0.0:9000
```
9.Call the endpoint to execute the POST operation.
```
http://0.0.0.0:9000/account/
```
10. Post to the endpoint using below information.
```
{
	"requestId": "A32W4ER2341",
	"accountName": "TXIuIEFCQw==",
	"amount": "aSN2QHZYeExjRE0h"
}
```
or, use CURL command to perform the POST action to the end point
```
curl -X POST 'http://0.0.0.0:9000/account/?pretty=true' -H 'Content-Type: application/json' -d '{
	"requestId": "A32W4ER2341",
	"accountName": "TXIuIEFCQw==",
	"amount": "aSN2QHZYeExjRE0h"
}'
```
# Run project with docker
## Prerequisites

Docker ➔ https://docs.docker.com/get-docker/

Docker Compose ➔ https://docs.docker.com/compose/install
1. Go to project root folder and execute below command to build docker image
```
sudo docker build -t djdocker_web .
```
2. execute below command to run the container
```
docker-compose up
```
3. Use Endpoint http://0.0.0.0:8000/account/ to execute the POST operation from docker image with below request information.
```
{
	"requestId": "A32W4ER2341",
	"accountName": "TXIuIEFCQw==",
	"amount": "aSN2QHZYeExjRE0h"
}
```
or, use CURL command to perform the POST action to the end point
```
curl -X POST 'http://0.0.0.0:8000/account/?pretty=true' -H 'Content-Type: application/json' -d '{
	"requestId": "A32W4ER2341",
	"accountName": "TXIuIEFCQw==",
	"amount": "aSN2QHZYeExjRE0h"
}'
