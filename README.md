# Random Tweet Redirect API

This is a simple FastAPI project that randomly selects a pre-written tweet and redirects users to a pre-filled Twitter post using the Twitter Intent API.

## Features
- Randomly selects a tweet from a predefined list
- Automatically redirects users to a pre-filled tweet on Twitter
- Uses FastAPI for lightweight API handling
- Can be deployed on services like Render for easy access

## Demo
You can try the live version of this project here:
[Random Tweet API](https://auto-tweeters.onrender.com/tweet)

## Installation
To set up the project locally, follow these steps:

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Install dependencies:
   ```sh
   pip install fastapi uvicorn
   ```
3. Run the API:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

## Usage
Once the server is running, open your browser or make a request to:
```
http://127.0.0.1:8000/tweet
```
This will redirect you to a random pre-filled tweet on Twitter.

## Deployment
You can deploy this API on services like Render, Replit, or Vercel. For Render, follow these steps:
1. Push your code to GitHub.
2. Go to [Render](https://render.com/) and create a new web service.
3. Connect your repository.
4. Set the start command:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
5. Deploy and get your API URL!

## Example QR Code Usage
Once deployed, generate a QR code with your API endpoint (`/tweet`), so users can scan and get a pre-filled tweet instantly.

