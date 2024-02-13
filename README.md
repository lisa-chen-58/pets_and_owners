# Project Name

This project practices the use of relational database management.

## Getting Started

These instructions will help you get yoru project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python installed on your system. If not, you can download and install it from the [official Python website]().

### Installing

To set up the project environment, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the project directory.

```python
cd /path/to/your/project
```

3. Run the following command to create and activate a virtual environment using Pipenv:

```python
pipenv shell
```

4. Once inside the virtual environment, install the required dependencies by running:

```
pipenv install flask flask-bcrypt pymysql
```

### Running the Application

After installing the dependencies, you can run the Flask application by executing:

```python
python server.py
```

This will start the development server, and you can access the application in your web browser at [http://localhost:5000/](http://localhost:5000/).

### Exiting the Environment

To exit the virtual environment, simply type:

```python
exit
```

### Cleaning Up

If you want to remove the virtual environment and start fresh, you can run:

```python
pipenv --rm
```

### Additional Information

* `Pipfile` contains the list of packages required for the project.
* `Pipfile.lock` contains specific details about the package versions being used.

## Authors

* **[Lisa Chen](https://www.linkedin.com/in/lisahlchen/)**
