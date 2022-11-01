## Hosting a Static Resume Website on AWS
This resume website was developed as part of the Cloud Resume Challenge (https://cloudresumechallenge.dev/docs/the-challenge/aws/)

Technologies used for the frontend include HTML, CSS, and Vanilla JavaScript. You can find the frontend code here --> https://github.com/mercybaffour/resume

### Frontend Build & Deployment
Amazon Simple Storage Service (Amazon S3) can be used to host a static website. Basically, a simple Amazon S3 bucket can be used to function like a website. I hosted my webpage files on an Amazon container and these files are distributed behind a content distribution network (Amazon CloudFront). Because Amazon S3 website endpoints do not support HTTPS, I also used CloudFront to securely serve my website.

### Backend Build & Deployment
I created a simple serverless application using AWS SAM. This application is a Lambda-based REST API made entirely through infrastructure as code. AWS SAM is a convenient way to set up templates to provide infrastructure as code for serverless applications. My infrastructure stack consists of an API Gateway, a lambda function, and DynamoDB as my database. The lambda function is used to read from a database to determine the number of visits to my website and returns this value. The API Gateway is used as a REST endpoint to invoke the lambda function.

When my code (either frontend or backend) is pushed to GitHub, a GitHub Actions workflow will trigger a GitHub Actions CI/CD pipeline. This builds & deploys my code directly from GitHub to my AWS account.

