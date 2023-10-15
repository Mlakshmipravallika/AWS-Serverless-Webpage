# AWS-Serverless-Enpoint
A serverless web application using Various AWS services like Lambda, API Gateway IAM and Dynamo DB

<h1>PROCESS 1 LAMBDA SETUP</h1>

<h3>Step 1: setting Lambda Function</h3>

1. Go to the AWS Management Console (https://aws.amazon.com/).
2. Click on "Services" and select "Lambda" under the "Compute" section.

<h3>Step 2: Create the Lambda Function</h3>

1. Click the "Create function" button.
2. Choose "Author from scratch."
3. Fill in the following details:
	  Function name: Give your function a name, for example, "my-secret-messinger-app"
	  Runtime: Select "Python 3.8" or any other Python runtime you prefer.
	  Execution role: Create a new role with basic Lambda permissions or you can select existing role if you have any
4. Click the "Create function" button
5. In the Lambda function editor, scroll down to the "Function code" section.
6. write any sample python function under lambda handler (lambda handler is a default function name) or 
7. simply copy the source code(test_python.py) from my attachment and paste it in the code section
8. verify once and click on Deploy button.

<h3>Step 3: Test the Lambda Function</h3>

1. In the Lambda function editor, click on the "Test" button.
2. Click the "Create a new test event" option.
3. Provide a name for your test(let it be simply keep it as test) event and enter a JSON payload that your Lambda function will receive as input.
4. Here's an example test event JSON for a "my-secret-messinger-app" Lambda function:
    {
        "name": "Pravallika",
        "code": "encode"
    }
5. Click the "Create" button to create the test event.
6. Select the test event you created and click the "Test" button to execute your Lambda function with the test event.
7. Your Lambda function will execute using the test event, and you can review the output and any logs in the Lambda function's monitoring section.

<h1>PROCESS 2 Creating API gateway and attaching it to your Lambda.</h1>

<h3>Step 1: Create an HTTP API Gateway</h3>

1. Go to the AWS Management Console.
2. Click on "Services" and select "API Gateway" under the "Networking & Content Delivery" section.
3. Click the "Create API" button.
4. Choose "HTTP API" and click the "Build" button.
5. Under "Configure routes," select "Add integration" and choose "Lambda function."
6. Select the Lambda function you previously created from the dropdown list.
7. set any HTTP API name if needed 
8. Click the "Create" button to create the integration.
9. configure route  as you need (in my case i am choosing method as POST, resourse path as /secretmessage) 
10. In the "Configure stages" section, you can create a new stage, for example, "prod," and configure other settings as needed or you can leave as default. 
11. Click the "Create" button to create the stage.
12. Now go to your lambda and verify API gateway trigger is attached.


<h3>Step 2: Get the API Endpoint URL</h3>

1. After deploying, you'll see the API Gateway's endpoint URL at the top of the "Stage details" section.
2. This URL is what you can use to access your API.

<h3>Step 3: Test the API</h3>

1. You can use tools like cURL, Postman, or a web browser to test your API.
2. Simply make HTTP requests to the endpoint URL, and the API Gateway will trigger your Lambda function.

That's it! You've created an HTTP API Gateway and attached it to your Lambda function.


<h1>PROCESS 3 Create Dynamo DB and configure Tables and Columns</h1>

<h3>Step 1: Create a DynamoDB Table</h3>

1. Go to the AWS Management Console.
2. Click on "Services" and select "DynamoDB" under the "Database" section.
3. Click the "Create table" button.
4. Fill in the table details:
	    Table name: Enter a name for your DynamoDB table, e.g., "my-secret-converter."
	    Primary key: Define the primary key for your table, consisting of a partition key (let it be id) and an optional sort key.
	    Provisioned or On-demand: Choose the read and write capacity mode that suits your needs.
5. Click the "Create" button to create the DynamoDB table.

<h3>Step 2: Set Up IAM Execution Role</h3>

1. In the Lambda function editor, click on "Configuration."
2. In the "Permissions" section, click on the execution role link under "Execution role."
3. In the IAM console, click the "Attach policies" button and search for policies like "AmazonDynamoDBFullAccess" to grant your Lambda function the necessary permissions.
4. Click the "Next: Review" button to review and create the role.
5. Give your role a name and add any tags (optional).
6. Click the "Create role" button to create the role and attach it to your Lambda function.
7. Now your Lambda function has the necessary permissions to access the DynamoDB table.

<h3>step 3: Configure Boto3 in your Lambda</h3>

1. You can use the  Python Boto3 in your Lambda function to interact with the DynamoDB table as needed.
2. Copy the source code(source_code2.py) from my attachment and paste it in the code section and click on deploy.

Now your whole set up is ready !!!!

Test the same endpoint using postman.(you can hit the the lambda and store the data in dynamo db)

You can use this endpoint in your UI page where ever you need !!!!!
