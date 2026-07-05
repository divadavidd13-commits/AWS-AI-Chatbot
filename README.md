# AWS AI Chatbot

## Overview

AWS AI Chatbot is a serverless web application that provides an AI-powered conversational interface through a browser. The application uses Amazon S3 for static website hosting, Amazon API Gateway to expose REST endpoints, AWS Lambda to process requests, and the Google Gemini API to generate responses.

The primary objective of this project is to understand how serverless cloud services can be integrated with a Large Language Model (LLM) to build a lightweight, scalable, and low-maintenance chatbot.

---

## Objectives

- Design a serverless chatbot architecture using AWS.
- Understand REST API communication between frontend and backend.
- Integrate an external Large Language Model with AWS Lambda.
- Deploy a static frontend using Amazon S3.
- Build a responsive web interface using HTML, CSS, and JavaScript.
- Explore practical cloud deployment workflows.

---

## System Architecture

```
                 User
                  │
                  ▼
        Amazon S3 Static Website
                  │
                  ▼
          Amazon API Gateway
                  │
                  ▼
        AWS Lambda (Python)
                  │
                  ▼
      Google Gemini API (LLM)
                  │
                  ▼
            AI Response
                  │
                  ▼
              Web Browser
```

---

## Project Structure

```
AWS-Chatbot/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambda/
│   └── lambda_function.py
│
├── README.md
└── .gitignore
```

---

## Technologies Used

| Component | Technology |
|-----------|------------|
| Frontend | HTML5, CSS3, JavaScript |
| Hosting | Amazon S3 |
| API | Amazon API Gateway |
| Backend | AWS Lambda (Python) |
| AI Model | Google Gemini API |
| Version Control | Git & GitHub |

---

## Application Workflow

1. User enters a question in the chatbot interface.
2. JavaScript sends the request to Amazon API Gateway.
3. API Gateway invokes the AWS Lambda function.
4. Lambda forwards the prompt to the Google Gemini API.
5. Gemini generates a response.
6. Lambda returns the response through API Gateway.
7. The chatbot displays the response in the browser.

---

## Features

- Serverless architecture
- Responsive web interface
- AI-powered question answering
- REST API integration
- Markdown response rendering
- Cross-Origin Resource Sharing (CORS) support
- Lightweight frontend without external frameworks

---

## AWS Services Used

- Amazon S3
- Amazon API Gateway
- AWS Lambda
- CloudWatch Logs

---

## Design Considerations

Several design choices were made during development:

- Amazon S3 was selected to host the frontend because static website hosting is simple and cost-effective.
- AWS Lambda eliminates the need to manage servers while providing scalable backend execution.
- API Gateway acts as the communication layer between the frontend and backend.
- The frontend was intentionally developed using plain HTML, CSS, and JavaScript to minimize complexity and dependencies.
- Google Gemini API was integrated as the language model while preserving the AWS serverless architecture.

---

## Challenges Encountered

During development, Amazon Bedrock model access was unavailable because the AWS account was provisioned with zero model quotas. Instead of redesigning the application, the backend was modified to communicate with the Google Gemini API while keeping the remaining AWS architecture unchanged.

Other challenges included:

- Configuring API Gateway CORS policies
- Managing Lambda environment variables
- Debugging REST API responses
- Deploying updates to Amazon S3
- Formatting AI responses using Markdown

---

## Possible Improvements

Future enhancements may include:

- Conversation history using Amazon DynamoDB
- User authentication with Amazon Cognito
- Knowledge-base integration using Retrieval-Augmented Generation (RAG)
- Migration to Amazon Bedrock after quota activation
- Amazon CloudFront for faster content delivery
- Monitoring and analytics dashboard
- Chat session persistence
- File upload support

---

## Learning Outcomes

This project provided practical experience with:

- AWS serverless architecture
- REST API development
- Cloud deployment
- AWS Lambda programming
- API integration
- Frontend-backend communication
- AI application development
- Git and GitHub workflow

---

## Running the Project

### Frontend

Upload the contents of the `frontend` directory to an Amazon S3 bucket configured for static website hosting.

### Backend

Deploy `lambda/lambda_function.py` to AWS Lambda.

Configure the following environment variable:

```
GEMINI_API_KEY=<your_api_key>
```

Create an API Gateway endpoint and update the API URL in `script.js`.

---

## Author

Developed as a cloud computing project to explore serverless application development using AWS services and Large Language Models.

---

## License

This project is available for educational and learning purposes.
