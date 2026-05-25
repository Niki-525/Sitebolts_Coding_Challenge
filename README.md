# SiteboltsFastAPICodingChallenge


# Python, Pydantic, and FastAPI Coding Challenge

This is the Python Backend Coding Challenge. If you're looking at this, congrats you made it past the initial round of Q&A! Here's some house-keeping notes before you jump into it:

- You can add whatever packages you need to complete the task (aiming for Python 3.11)
- Running locally is considered success, don't worry about deployment or CI/CD or anything like that. Bonus points if Docker is used successfully.
- We don't care about AI generated code as long as you understand what it's doing and why it was generated. Basically, don't just copy and paste + be prepared to explain your decisions.
- Unless told otherwise, you've got about 2 weeks to hit the objectives.

# What will you be doing?

**Objectives:**

- Create a FastAPI application with Pydantic models to serve data from the PokeAPI (https://pokeapi.co/?ref=public-apis) or an API of your choosing.
- Implement proper error handling and response codes for all endpoints
- Define Pydantic models that properly validate and structure the API data
- Implement async endpoints that handle concurrent requests efficiently
- Return the processed data as properly structured Pydantic objects in your API responses
- Handle environment variables safely (hint: see env.example)


- **Data modeling:** Implement the four endpoints described in `routers/api_processing.py` using the in-memory store provided in `store.py`. This simulates a relational database with a foreign key relationship between two collections — pokemon types (parent) and pokemon (child). You are responsible for defining the Pydantic schemas, enforcing the relationship between the two collections, and returning properly structured responses.

Bonus Points:

- Build the docker image and run the API as a container
- Don't use the standard requests library for API calls
- Implement pagination for your API endpoints with proper Pydantic schemas
- Add caching layer to improve performance of external API calls

**Additional Details**

For this challenge, you'll be building a backend API service that:

- Fetches data from an external API
- Processes and models that data with Pydantic
- Serves it through well-structured FastAPI endpoints
- Handles requests asynchronously for better performance

Make sure your code includes proper type hints, documentation, and follows FastAPI/Pydantic best practices.


# How do I submit it?
Create a fork off of this repository and then send your point of contact a link! We look forward to hearing from you.# Sitebolts_Coding_Challenge
