run-http:
	cd front && python -m http.server 8000
run-mig:
	python manage.py makemigrations && python manage.py migrate
