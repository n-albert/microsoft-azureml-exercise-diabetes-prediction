# microsoft-azureml-exercise-diabetes-prediction
This is an exercise from a Coursera course for the Microsoft Azure DP-100 certification. This is exercise to "Run a training script" as part of the "Build and Operate Machine Learning Solutions with Azure" module.

# Create a compute instance with the Azure CLI
In this exercise, you’ll create a compute instance with the following settings:

Compute name: Name of compute instance. Has to be unique and fewer than 24 characters.
Virtual machine size: STANDARD_DS11_V2
Compute type (instance or cluster): ComputeInstance
Azure Machine Learning workspace name: mlw-dp100-labs
Resource group: rg-dp100-labs
Use the following command to create a compute instance in your workspace. If the compute instance name contains “XXXX”, replace it with random numbers to create a unique name.

```
 az ml compute create --name "[compute-instance-name]" --size STANDARD_DS11_V2 --type ComputeInstance -w mlw-dp100-labs -g rg-dp100-labs
```

# Configure your workstation with the Azure Machine Learning studio
Though the Azure CLI is ideal for automation, you may want to review the output of the commands you executed. You can use the Azure Machine Learning studio to check whether resources and assets have been created, and to check whether jobs ran successfully or review why a job failed.

In the Azure portal, navigate to the Azure Machine Learning workspace named mlw-dp100-labs.
Select the Azure Machine Learning workspace, and in its Overview page, select Launch studio. Another tab will open in your browser to open the Azure Machine Learning studio.
Close any pop-ups that appear in the studio.

Within the Azure Machine Learning studio, navigate to the Compute page and verify that the compute instance you created exists and is running.

# Use the Python SDK to train a model
Now that you’ve verified that the necessary compute has been created, you can use the Python SDK to run a training script. You’ll install and use the Python SDK on the compute instance and train the machine learning model on the compute cluster.

1) In your compute instance, there are a number of options in the Applications field. Select the Terminal application to launch the terminal (you may need to click the ellipsis to expand the selection).

2) In the terminal, install the Python SDK on the compute instance by running the following commands in the terminal:
```
 pip uninstall azure-ai-ml
 pip install azure-ai-ml
```

3) Run the following commands to clone this Git repository to your workspace.
```
git clone https://github.com/n-albert/microsoft-azureml-exercise-diabetes-prediction.git diabetes-prediction-exercise
```

4) When the command has completed, in the Files pane, select ↻ to refresh the view and verify that a new Users/your-user-name/diabetes-prediction-exercise folder has been created.

5) To run the ScriptRunConfig properly, you need to change the working directory to that of diabetes-prediction-exercise and then run the ScriptRunConfig file.
To change the working directory:
```
cd diabetes-prediction-exercise
```
To run the ScriptRunConfig file:
```
python ScriptRunConfig.py
```
