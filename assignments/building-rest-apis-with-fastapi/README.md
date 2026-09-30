# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with Python and FastAPI to manage a collection of items, such as tasks or books. This assignment introduces the basics of route creation, request handling, JSON responses, and CRUD operations.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a minimal FastAPI application and define the first API routes that respond with JSON data.

#### Requirements
Completed program should:

- Install and import FastAPI
- Create an app instance with `FastAPI()`
- Define a `GET /` route that returns a welcome message
- Define a `GET /health` route that returns a status object such as `{ "status": "ok" }`
- Run the app locally using Uvicorn

### 🛠️ Build CRUD Endpoints

#### Description
Add endpoints to create, read, update, and delete items from an in-memory list so the API behaves like a simple resource manager.

#### Requirements
Completed program should:

- Create a resource model using a dictionary or Pydantic model
- Implement `GET /items` to return all items
- Implement `POST /items` to add a new item
- Implement `GET /items/{item_id}` to fetch one item
- Implement `PUT` or `PATCH` to update an item
- Implement `DELETE /items/{item_id}` to remove an item
- Return appropriate JSON responses and status codes
- Handle missing items gracefully with a clear error response

### 🛠️ Add Validation and Data Modeling

#### Description
Improve the API by validating input and using typed models for cleaner request and response data.

#### Requirements
Completed program should:

- Use `BaseModel` or a similar structured model for item data
- Validate required fields such as title and description
- Return a consistent JSON response format for created and updated items
- Avoid duplicate IDs or invalid item updates
- Include at least one example request payload in the code comments or README
