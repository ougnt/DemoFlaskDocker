docker build -t ougnt/flask_app . 
docker kill demo_flask
docker rm demo_flask
REM docker run -p 5000:5000 -v scripts:/App/scripts -v view:/App/view --name demo_flask ougnt/flask
docker run -p 5000:5000  --name demo_flask ougnt/flask_app