# # Quick Blogs

Welcome to Quick Blogs! This is a simple blog application built with Django and Tailwind CSS, designed for users to create, manage, and interact with blog posts easily. The application is fully Dockerized and hosted on Vercel.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Quick Blogs is a user-friendly blog platform that allows users to sign up, log in, and manage their blog posts. With a responsive design powered by Tailwind CSS, users can easily navigate the application on both desktop and mobile devices.

## Features

1. **User Management:**
   - Sign up with email, username, and password.
   - Login using email/username and password.
   - Profile management to update user information.

2. **Blog Post Management:**
   - Create, read, update, and delete blog posts.
   - Posts can include a title, content (rich text editor), and optional tags.
   - View a list of all posts with pagination and single post details.

3. **Front-End:**
   - Responsive design for seamless usage on all devices.
   - Tailwind CSS for a modern and clean user interface.
   - Basic interactivity using vanilla JavaScript.

4. **Back-End:**
   - Developed using Django with a REST API for blog post management.
   - User authentication handled by Django's built-in system.

5. **Database Integration:**
   - Utilizes PostgreSQL for data management.
   - Models designed for Users and BlogPosts with appropriate relationships and constraints.

6. **Dockerization:**
   - Dockerized application with a Dockerfile and docker-compose.yml for orchestration.
   - Uses environment variables for secure configuration.

7. **Deployment:**
   - Deployed on Vercel for easy access and management.
    

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **Deployment:** Vercel

## Setup and Installation

### Prerequisites

- Docker and Docker Compose installed on your machine.
- PostgreSQL installed or access to a PostgreSQL server.

### Clone the Repository

```bash
git clone https://github.com/s4thwik/quickblogs.git

Vercel
https://quickblogs1-4gv2c9f6z-s4thwiks-projects-85b51e5a.vercel.app
