# Commands

Build: `sh build.sh Dockerfile latest mle-on-aws-book 3.11`

Local Deploy: `sh local_test/deploy_local.sh ${PWD}/local_test/test_dir latest mle-on-aws-book`

ECR Login: `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com`