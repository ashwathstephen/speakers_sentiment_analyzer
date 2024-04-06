# Use the base image provided by AWS for Python 3.10
FROM public.ecr.aws/lambda/python:3.10

# Copy the function code and files
COPY app.py ${LAMBDA_TASK_ROOT}
COPY audio_2_text.py ${LAMBDA_TASK_ROOT}
COPY senti_analysis.py ${LAMBDA_TASK_ROOT}
COPY htmlTemplates.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt .

# Install the Python function dependencies using pip
RUN python3.10 -m pip install -r requirements.txt

# Set the CMD to the handler function
# The file is named app.py and the function is named lambda_handler
CMD ["app.lambda_handler"]
