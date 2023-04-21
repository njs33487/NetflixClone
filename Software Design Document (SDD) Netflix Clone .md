# Netflix Clone Project Software Design Document (SDD)

## Introduction
This document outlines the software design for a Netflix clone project. This project will use Django as the backend and React for the front end. 

## System Overview
The system will be composed of two main components: the frontend and the backend. The frontend will be built with React, while the backend will be powered by Django. The frontend will provide an interface for users to view movies, TV shows, and other content, while the backend will handle authentication, data storage, and API requests. 

## Frontend Design 
The frontend will be a single page application built using React and Redux. It will have a modern, responsive design that is optimized for mobile devices. The user interface will consist of several views: 

- Home page: Displays featured content and allows users to search for specific titles. 
- Profile page: Allows users to manage their account settings and view their watch history. 
- Content page: Displays detailed information about a selected title. 

The application will also feature a navigation bar with links to all the different views. 

## Backend Design 
The backend will be built using Django and will support authentication, data storage, and API requests. Authentication will be handled using JSON Web Tokens (JWT). Data will be stored in a relational database and accessed via Django models. The API will be built using Django REST Framework and will be responsible for handling requests from the frontend. 

## Conclusion 
This SDD outlines the software design for a Netflix clone project. The project will use Django as the backend and React for the front end. The frontend will provide an interface for users to view movies, TV shows, and other content, while the backend will handle authentication, data storage, and API requests.