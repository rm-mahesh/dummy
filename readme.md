
## Techniques to include secrets into Github Actions

### Using .env files
   1. Create a .env file in a repository.
   2. Add secrets to .env file, in a Key=Value format.
   3. To include these secrets into .yml file, we need to export this .env file. we can do it by using "export $(grep -v '^#' file_name.env | xargs) ".
   4. To print any secret in the workflow using .yml file, we can use echo "$variable_name".
   5. To inherit these secrets into a python program, we need to follow the steps below:
      1. import os 
      2. from dotenv import load_dotenv
      3. load_dotenv("provide path to .env file")
      4. VARIABLE=os.getenv("KEY")


### Using Github Action's Secrets and Variables
   1. In GitHub UI, for any repository, go to Settings -> Secrets and Variables -> Actions -> New Repository Secret -> Provide name and secret value -> Add secret.
   2. NOTE: We must have admin access for a repository, to add any secrets.
   3. To access the above created secrets and use in workflow, we need to create a step with any name(for eg. Load secrets from Github) and in the env part of the same step, we need to assign the stored secret value to any variable (eg. VARIABLE: ${{ secrets.NAME_OF_KEY }}).
   4. Now, the variable holds the value of the secret key.
   5. To access the secrets in .py file, we need to export the variables in env section of the step, in which we run python program. eg: export VARIABLE="${{ secrets.NAME_OF_KEY }}".
   6. To access the in .py file, we need to export the secrets in the step, before running the python file.
   7. NOTE: These secret values will be masked in the Github workflow logs.

### Providing Inline Secrets in .yml file
   1. Create a step to first store the secrets into Github environment, so that secrets are accessible accross the workflow.
   2. Under env, we need to store the secrets as shown: echo "KEY_NAME=KEY_VALUE" >> $GITHUB_ENV
   3. To access the secrets in any .py file, we need to follow the below steps:
    1. import os
    2. VARIABLE=os.environ.get("KEY_NAME")


### Entering Secrets manually during workflow run
   1. 