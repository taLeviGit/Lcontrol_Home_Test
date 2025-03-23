# Lcontrol Home Test

This repository contains automation tests and a CI/CD pipeline for the Lcontrol interview process.

## Overview
- **Stage 1**: Setup AWS Environment Setup
- **Stage 2**: Web automation tests using Java, Selenium, and Allure.
- **Stage 3**: API tests using Python, Pytest, and Requests.
- **Stage 4**: CI/CD pipeline with GitHub Actions.

## Setup Instructions

### Prerequisites
- **Java 11**: Install JDK 11 (e.g., Temurin from Adoptium).
- **Python 3.9+**: Install Python from python.org.
- **Git**: Install Git for version control.
- **Maven**: Install Maven for Java dependency management.
- **Chrome Browser**: Required for Selenium tests (installed automatically in CI).
- **Pytest**: Required for API tests

### Local Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/taLeviGit/Lcontrol_Home_Test.git
   cd Lcontrol_Home_Test

## Stage 1 - AWS Environment Setup - S3 Static Website

This document provides a complete guide for setting up an AWS environment using S3 to host a static web application, including creating an IAM User with S3 permissions and launching the application.

### Objective
Set up a free-tier AWS account and deploy a static web application using an S3 bucket, ensuring it is publicly accessible via a URL.

---

### Step-by-Step Instructions

#### 1. Create a Free AWS Account
- Navigate to `https://aws.amazon.com/free/` and sign up for an AWS Free Tier account.
- Provide an email, password, and payment details (required even for Free Tier).
- Log in to the AWS Management Console using the Root User credentials (email and password).

#### 2. Create an IAM User with S3 Permissions
- In the AWS Console, search for **"IAM"** in the top search bar and select the **IAM** service.
- Create a new IAM User:
    - Go to **"Users"** in the left menu and click **"Add users"**.
    - Enter a username (e.g., `s3-test-user`).
    - Check **"Provide user access to the AWS Management Console"**.
    - Choose **"Custom password"** and set a strong password (e.g., `MyS3Password123!`).
    - Click **"Next"**.
- Set permissions:
    - Select **"Attach policies directly"**.
    - Search for **"AmazonS3FullAccess"** in the policy list and check the box to attach it.
    - Click **"Next"** and then **"Create user"**.
- Save credentials:
    - Note the IAM User sign-in link (e.g., `https://<Account-ID>.signin.aws.amazon.com/console`).
    - Download the `.csv` file with the Access Key ID and Secret Access Key (optional, for CLI use) or manually save the username and password.

#### 3. Log in as the IAM User
- Sign out of the Root User account by clicking the username in the top-right corner and selecting **"Sign out"**.
- Open the IAM User sign-in link in a browser (e.g., `https://<Account-ID>.signin.aws.amazon.com/console`).
- Enter the IAM username (e.g., `s3-test-user`) and password (e.g., `MyS3Password123!`), then click **"Sign in"**.

#### 4. Navigate to S3
- In the AWS Console (as the IAM User), search for **"S3"** in the top search bar and select the **S3** service.

#### 5. Create an S3 Bucket
- Click the orange **"Create bucket"** button.
- Enter a unique bucket name (e.g., `my-test-bucket-123`).
    - Note: Bucket names must be globally unique across all AWS users.
- Select a region (e.g., `US East (N. Virginia) us-east-1`).
- Leave other settings as default and click **"Create bucket"** at the bottom.

#### 6. Upload the Web Application
- Click on the newly created bucket name (e.g., `my-test-bucket-123`) to enter it.
- Click **"Upload"**.
- Drag and drop or select an `index.html` file from your computer. Example content:
  ```html
  <!DOCTYPE html>
  <html>
  <head><title>Test Site</title></head>
  <body>
    <h1>Welcome to My Test Site</h1>
    <a href="#">Home</a> | <a href="mailto:talvi8942@gmail.com">Contact</a>
    <form action="#" method="post">
      <input type="text" name="username" placeholder="Username">
      <input type="submit" value="Submit">
    </form>
  </body>
  </html>
  
## Stage 2 - Automation Test Development

This document outlines the process of developing and running automated tests for the S3-hosted static web application using Selenium in Java, including configuration steps, local execution, and CI/CD integration.

---

## Purpose
Assess the ability to write functional and end-to-end automation tests for a web application.

---

## Tools Used
- **Selenium (Java)**: Web-based automation framework.
- **JUnit 5**: Testing framework.
- **Allure**: Reporting tool for generating visual test reports.

---

## Configuration Steps

### Prerequisites
- **Java 11+**: Install from [Adoptium](https://adoptium.net/).
- **Maven**: Install from [Maven](https://maven.apache.org/download.cgi) and add to PATH.
- **Chrome Browser**: Installed locally for Selenium WebDriver.
- **IntelliJ IDEA** (optional): For editing and running the project locally.

### Project Setup
1. **Create a Maven Project**:
    - Run in a terminal:
      ```bash
      mvn archetype:generate -DgroupId=com.lcontrol -DartifactId=web-test -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
    - Run in IDE terminal:
     ```
     1. mvn clean install
     2. mvn clean test
     3. mvn allure:report
     4. mvn allure:serve
     ```
    - Run in Github CI/CD:
    1. Go to Site : https://github.com/taLeviGit/Lcontrol_Home_Test/actions
    2. Press on Website Test
    3. Press on "Run WorkFlow"
    4. In the new Opened Window Press on "Run WorkFlow"

## Stage 3: Backend Test Development

### Purpose
Assess the ability to write and execute backend automation tests.

### Tools Used
- **Python**: Pytest and Requests for API testing.
- **pytest-html**: For generating test reports.

### Setup Instructions
1. **Navigate to API Tests Directory**:
   ```bash
   cd api_tests     
   ```
2. Run Tests:
 - Run in IDE Terminal:
   pytest test_api.py -v --html=report.html --self-contained-html
 - Run in Github CI/CD:
     1. Go to Site : https://github.com/taLeviGit/Lcontrol_Home_Test/actions
     2. Press on Website Test
     3. Press on "Run WorkFlow"
     4. In the new Opened Window Press on "Run WorkFlow"



## Dependencies

### Java:
  - Selenium (selenium-java:4.11.0)
  - WebDriverManager (webdrivermanager:5.5.3)
  - JUnit 5 (junit-jupiter-api:5.9.2, junit-jupiter-engine:5.9.2)
  - Allure (allure-junit5:2.24.0, allure-maven:2.12.0)
  - AspectJ (aspectjweaver:1.9.19)
### Python:
  - Pytest (pytest:8.3.2)
  - Requests (requests:2.32.3)
  - Pytest-HTML (pytest-html:4.1.1)
  - JSONSchema (jsonschema:4.23.0)

## Replication Steps
Clone the repository (see above).
Set up Java and Python environments as described.
Run the tests locally or push changes to trigger the GitHub Actions pipeline.
Check the "Actions" tab on GitHub for pipeline results and download artifacts.

## CI/CD Pipeline
Configured in .github/workflows/test.yml.
Runs on every push to main.
Executes web and API tests, generates reports, and uploads artifacts.

## Notes
Web tests use a headless Chrome browser in CI for compatibility.
API tests use jsonplaceholder.typicode.com as a mock API.

