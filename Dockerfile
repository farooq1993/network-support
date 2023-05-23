FROM python
COPY . .
EXPOSE 8000

# Create a virtual environment and activate it
RUN python3 -m venv myvenv
ENV PATH="/app/myvenv/bin:$PATH"

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run initial migrations and create a superuser
RUN python manage.py migrate && \
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
