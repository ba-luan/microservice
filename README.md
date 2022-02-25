# Build a Python Service to Identify Whether a Post Text Is Sponsored or Not.

## Description.
This service can be used by an Online Marketing Firm to identify whether a given post_text is sponsored or non-sponsored; the post_text is an English text and may contain emojis or special characters. If the post_text contains any keyword that exists in our ads keywords database (for example #ad, #sponsored, advertisement,...), then the post_text is considered being sponsored, vice versa, non-sponsored.<br>

Our keywords database is not static and can be added new ads keywords to increase the number of vocabulary. In this demonstration, there is no specific database created, instead, the ads keywords list is created and stored in the source code.<br>

Python and [Flask](https://flask.palletsprojects.com/en/2.0.x/) are used to create the service to categorize the post_text is sponsored or not. Flask is a microframework that keeps the core simple but extensible, so we can later use it in the implementation phase.<br>

To send requests to the endpoints and to test how our service responds to those requests, we use the [Postman app](https://www.postman.com/downloads/). Postman is a very interactive and easy-to-use API platform for building and using APIs, it facilitates developers to build better APIs faster.<br>

There 3 functions in this service:
- GET method sent to `/api/vocab` endpoint will return the ads keywords list that is used to determine the post_text is sponsored or not.
- POST method sent to `/api/vocab` endpoint will add new keywords to the existing ads keywords list.
- POST method sent to `/api/prediction` endpoint will predict the post_text is sponsored or not.


## Install and Run.
- [requirements.txt](https://github.com/ba-luan/microservice/blob/main/requirements.txt) includes all the dependencies that you can re-built and run demo this project.
- [post_text_ad.py](https://github.com/ba-luan/microservice/blob/main/post_text_ad.py) is the main source code file written in python that includes the 3 main functions of the service: returning ads keywords list, adding new ads keywords, predicting if the post_text is sponsored or not.
- [Dockerfile](https://github.com/ba-luan/microservice/blob/main/Dockerfile) can be used to run the code in a container.

## Demonstrations.
After setting up the correct environment and running the app, we use the Postman app to send the requests to the service and see its responses. Postman app is used because there is no specific UI and this is how we interact with the ads prediction service.
### Return ads keywords list
![GET vocab](https://github.com/ba-luan/microservice/blob/main/image/GET_vocab.PNG)
### Add new keywords
- Add a new ads keyword to the existing vocab list.

![POST vocab01](https://github.com/ba-luan/microservice/blob/main/image/POST_vocab01.PNG)

- Add multiple new ads keywords to the existing vocab list.

![POST vocab02](https://github.com/ba-luan/microservice/blob/main/image/POST_vocab02.PNG)
### Predict post_text is sponsored or not
![POST prediction01](https://github.com/ba-luan/microservice/blob/main/image/POST_prediction01.PNG)

![POST prediction02](https://github.com/ba-luan/microservice/blob/main/image/POST_prediction02.PNG)
