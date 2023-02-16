# Flask REST Application 

This is a simple Flask REST application that will retrieve records on weather station data. It also includes parameters to filter data.
Please check yaml file for Swagger/OpenAPI documentation.

## Data Ingestion

For this usecase, we have a text file to ingest data. Go to your local instance and make one of your database as default. Please follow the below DDL statements for ingestion:

1. CREATE TABLE weatherStation(year VARCHAR(255), maxTemp INT, minTemp INT, precipitation INT);

2. LOAD DATA
INFILE '**Local text file directory**'
INTO TABLE demodb.weatherStation
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY 'r\n';

## Data Format Conversion

For this usecase, we have converted the year(datatype: varChar) column to date format. Below is the DDL statement for format conversion:

1. UPDATE demodb.weatherstation SET year = date_format(str_to_date(year, '%Y%m%d'), '%m-%d-%Y');

## Data Analysis

1. SELECT AVG(maxTemp) AS MaxTemp FROM weatherStation;
2. SELECT AVG(minTemp) AS MinTemp FROM weatherStation;
3. SELECT SUM(precipitation) AS TotalPrecipitation FROM weatherStation;

## Database Connection Setup

To connect to local instance, mention your hostname, username, password and database as follows:
app.config['MYSQL_HOST'] = '**Local Connection HostName**'
app.config['MYSQL_USER'] = '**Local Connection UserName**'
app.config['MYSQL_PASSWORD'] = '**Local Connection Password**'
app.config['MYSQL_DB'] = '**Local Database Name**'

## Installation

From your terminal, use the command "pip install -r requirements.txt" to install all the packages.

## Execution

From your terminal, run the command "python app.py" or "python3 app.py" to generate the localhost/server.

## Question

1. Assume you are asked to get your code running in the cloud using AWS. What tools and AWS services would you use to deploy the API, database, and a scheduled version of your data ingestion code? Write up a description of your approach.

To deploy an API, database, and a scheduled version of the data ingestion code in AWS, we can use the following services:

- Amazon Elastic Compute Cloud (EC2): This service provides scalable computing capacity in the cloud. We can use EC2 to create and launch virtual machines that run our API, database, and data ingestion code.

- Amazon Relational Database Service (RDS): This service provides a managed database service that is easy to set up, operate, and scale. We can use RDS to create and manage a relational database that stores data for our API.

- Amazon Simple Storage Service (S3): This service provides object storage for our data. We can use S3 to store the data that we ingest using our data ingestion code.

- AWS Lambda: This service allows us to run our data ingestion code in response to various triggers, such as a scheduled event. We can use Lambda to create a function that executes our code on a schedule.

- Amazon CloudWatch: This service provides monitoring and logging services for our AWS resources. We can use CloudWatch to monitor our API, database, and Lambda function.

With these services in mind, here is an approach we can use to deploy our API, database, and data ingestion code:

1. Create an EC2 instance to run our API. We can use an Amazon Machine Image (AMI) that is preconfigured with the necessary dependencies and software.

2. Create an RDS instance to host our database. We can choose the appropriate database engine, such as MySQL or PostgreSQL, and set up the necessary security groups and network access.

3. Set up the necessary security groups and network access for our EC2 instance and RDS instance.

4. Create an S3 bucket to store the data that we ingest using our data ingestion code.

5. Create a Lambda function that runs our data ingestion code on a schedule. We can use a CloudWatch event to trigger the Lambda function at the desired interval.

6. Configure CloudWatch to monitor our API, database, and Lambda function. We can set up alarms and notifications to alert us to any issues.

7. Deploy our API code to the EC2 instance and configure it to access the RDS database.

8. Test the API to ensure that it is functioning as expected.

By following this approach, we can deploy our API, database, and data ingestion code in AWS using a combination of EC2, RDS, S3, Lambda, and CloudWatch. This approach provides a scalable and reliable infrastructure for our application, while also enabling us to monitor and troubleshoot any issues that may arise.