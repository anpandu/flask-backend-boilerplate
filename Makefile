start:
		sh -c "python application.py"
test:
		sh -c "TESTING=True nose2 -v"
build:
		sh -c "docker build . -t anpandu/flask-backend-boilerplate"
build-no-cache:
		sh -c "docker build . -t anpandu/flask-backend-boilerplate --no-cache"
docker-run:
		sh -c "docker run --name flask-backend-boilerplate -p 5001:5001 anpandu/flask-backend-boilerplate"
docker-run-detach:
		sh -c "docker run -d --name flask-backend-boilerplate -p 5001:5001 anpandu/flask-backend-boilerplate"