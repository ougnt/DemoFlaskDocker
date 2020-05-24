# Getting the base image from python (python programe installed)
From			python
# Setting environment variable
ENV			working_dir /App
# Setting working directory when lunch the docker run command
WORKDIR	${working_dir}
# Copy files to the working directory folder
COPY			requirements.txt ${working_dir}
# Install required libraries
RUN			pip install -r requirements.txt
# Copy all files to the working directory
COPY			. ${working_dir}
# Expose port 5000
EXPOSE 		5000
# Docker start command to start the website
CMD			python app.py
