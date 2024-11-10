# Serverless Customer Data Management Project with AWS Lambda

**Project Type**: Personal Exploration Project  
**Role**: Designer & Developer  
**Duration**: Self-paced, ongoing improvements  

## Table of Contents
1. [Project Overview](#project-overview)
2. [Objective](#objective)
3. [Project Highlights](#project-highlights)
4. [Functioning Features Implemented and Testing Methods Used](#functioning-features-implemented-and-testing-methods-used)
5. [Why I Built This](#why-i-built-this)
6. [Key Takeaways](#key-takeaways)
7. [Future Steps](#future-steps)

## Project Overview
As a Data Science student with a strong interest in cloud computing, I was eager to explore how serverless technologies can power scalable, real-time applications. Alongside my full-time studies, I took the opportunity to deepen my knowledge of AWS services—especially AWS Lambda—by working on a collaborative project with a team. This repository highlights my sole individual contribution to our team’s hands-on experience with serverless architecture, enabling us to build a fully functional application that efficiently captures and processes customer data at scale.

This project is also aligned with a **real-world case study** where our team worked as cloud consultants for **Felicity Pte Ltd**, implementing AWS-based serverless solutions for **Platinum Pte Ltd**. The project focused on building a NoSQL database for customer data storage and designing an HTML page for real-time data capture, similar to the system we were developing in this exploration.

### Case Study: Platinum Pte Ltd Project
Assume that your team (consisting of 4 to 5 members) has been appointed by a large IT service provider organization called Felicity Pte Ltd as IT cloud consultants.

A client company, Platinum Pte Ltd, has tasked Felicity Pte Ltd with implementing some requirements. Platinum Pte Ltd also wants your team to implement additional mandatory requirements, which are:

**To design and implement a new AWS serverless application architecture with the following cloud requirements:**

1. **Create a NoSQL database** to store customer data that is posted to the website. The database should have data fields to capture the customer's first name, last name, and email address.

2. **Create an HTML forms page** to capture the customer data and post it to the NoSQL database using HTTP (API Gateway). The webpage should also be able to show the current records in the NoSQL database.

## Objective
The primary aim was to experiment with AWS Lambda and gain practical skills in serverless architecture while creating something tangible. I challenged myself to build a system that captures, stores, and manages customer data in real-time, with additional functionalities like notifications and image processing—showcasing the power of serverless infrastructure for data management.

For Platinum Pte Ltd, the system aimed to meet requirements such as:
- Creating a scalable NoSQL database for customer data.
- Integrating an HTML form to collect and store customer information through AWS Lambda and API Gateway.

## Project Highlights
This project includes:
- **Data Capture**: A custom-built HTML form that captures customer details.
- **Data Storage**: Leveraging DynamoDB to store customer data with a NoSQL structure.
- **Serverless Data Posting**: Using AWS Lambda in combination with API Gateway to process and post data from the HTML form to DynamoDB in real-time.

## Functioning Features Implemented and Testing Methods Used 
Lambda Function code testing before deploying code

Test events to with default AWS Lambda function code provided.
Paste the API Gateway invoke URL, https://xv90i8653k.execute-api.us-east-1.amazonaws.com/production/status_GetCustomerInfo and https://xv90i8653k.execute-api.us-east-1.amazonaws.com/production/status_PostCustomerInfo
![image](https://github.com/user-attachments/assets/1f951786-4896-4a0e-9c70-de51c51c47b6)
![image](https://github.com/user-attachments/assets/2715bae2-a54a-4563-850b-6eb67800173e)
![image](https://github.com/user-attachments/assets/8525a3e7-b43e-4b37-aa30-3d3a8db7bdd6)

Lambda Function testing after deploying code:
After deployment using the same invoke URLs above, confirmation that new functionalities work when accessed via API Gateway.
![image](https://github.com/user-attachments/assets/13cac94b-8ca7-4a11-aa42-b362c8f378fb)
![image](https://github.com/user-attachments/assets/31632ab0-335c-4ff1-8414-bb12f575ff2c)

API Gateway testing
![image](https://github.com/user-attachments/assets/927d7534-49b8-47fc-b741-52807ed6bed2)
![image](https://github.com/user-attachments/assets/151b97fa-93b5-4b49-a633-46c53a85bfe9)
![image](https://github.com/user-attachments/assets/aecca179-f0e7-4709-a186-902338013063)
![image](https://github.com/user-attachments/assets/39218034-0b8c-466f-b887-97d54a7b61a6)

![image](https://github.com/user-attachments/assets/4afbfa99-4537-450e-9686-132b6278045b)

![image](https://github.com/user-attachments/assets/79824da0-5397-4716-924e-762beb6d48c1)
![image](https://github.com/user-attachments/assets/725a8fbb-a970-4cda-9684-aedc7b43f816)
![image](https://github.com/user-attachments/assets/387fd6db-209c-40a9-89b6-08f385ede921)
![image](https://github.com/user-attachments/assets/6fde7f53-dba0-49ed-aac6-e613ebe7c7b8)

Postman 
Another way to verify Lambda and API Gateway functionality is using Postman. For this, I cleared all profiles from DynamoDB for a clean testing environment.
![image](https://github.com/user-attachments/assets/01936156-d35d-49b1-9490-82b2f30cf1f2)
![image](https://github.com/user-attachments/assets/5302824c-c1a8-48f7-a6a4-d8535a61134e)
![image](https://github.com/user-attachments/assets/8c84289b-997b-47a5-b01c-d2b0a9c28b37)
![image](https://github.com/user-attachments/assets/8a51c78d-585e-40c5-84fe-ac82b95b3612)
![image](https://github.com/user-attachments/assets/1fe813e5-8267-4c54-b7e9-6dff9327168b)
![image](https://github.com/user-attachments/assets/5951dc31-0052-4b8c-a4e6-c2de7be07dd6)
![image](https://github.com/user-attachments/assets/4590813e-712e-42f0-a34b-56ec06895e2b)
![image](https://github.com/user-attachments/assets/0316ba71-2bd6-4a8b-a95b-05aae184905d)
![image](https://github.com/user-attachments/assets/8527d716-1c98-4e76-9cbb-9a7b5482d990)
![image](https://github.com/user-attachments/assets/c01a2b1c-1ae0-4025-abf8-4aefed45091e)

S3 bucket Form Page Hosting 
![image](https://github.com/user-attachments/assets/b7468e5e-d970-4a17-b70d-b8f05ff80172)
![image](https://github.com/user-attachments/assets/56830c30-124f-4d70-9084-76ff6ee78242)
![image](https://github.com/user-attachments/assets/24de6134-9436-4aec-827c-0eabb9e94133)

## Why I Built This
I pursued this project as a way to:
- **Expand My Technical Skills**: I wanted to explore AWS beyond my current focus in data science, integrating multiple services (Lambda, DynamoDB, S3, API Gateway) to see how they work together in a serverless ecosystem.
- **Learn Through Experimentation**: Rather than following a strict project outline, I allowed myself the freedom to experiment and make incremental improvements, learning from each step along the way.
- **Apply Concepts in Real-World Scenarios**: This project gave me the opportunity to experience the challenges of cloud infrastructure and serverless computing first-hand, broadening my perspective on scalable solutions. The requirements from **Platinum Pte Ltd** provided valuable insights into designing for real-world use cases.

## Key Takeaways
This project taught me:
- **Practical AWS Skills**: Enhanced my understanding of how to set up and optimize AWS services for real-world applications.
- **Problem-Solving**: I encountered and overcame challenges like optimizing Lambda trigger events and fine-tuning API Gateway integrations.
- **Growth Mindset**: Self-driven learning allowed me to expand my technical repertoire and gain valuable skills in cloud technologies—valuable for my data science career and beyond.

## Future Steps
I plan to continue refining this project by:
- Adding **CloudWatch monitoring** for more detailed performance insights.
- Exploring **Automated Notifications** to configure SNS notifications to alert upon data entry or file uploads.
