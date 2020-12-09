# klaro.xyz

English-German bilingual dictionary, optimised for second language acquisition.

## Infra

Pre-requisites: AWS CLI v2 installed and configured with a region, and a key 
pair called 'adam' ;-). Tough luck if you're not called Adam!

Then, to create the AWS stack for the first time:

```shell
aws cloudformation create-stack --stack-name klaro --template-body file://$PWD/klaro.yaml
```

To update it once created:

```shell
aws cloudformation update-stack --stack-name klaro --template-body file://$PWD/klaro.yaml
```