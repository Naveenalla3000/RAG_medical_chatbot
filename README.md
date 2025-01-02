# Medical Chatbot

This repository contains the source code for the Medical Chatbot, a chatbot application powered by OpenAI's GPT and Pinecone for conversational AI capabilities. This guide explains how to set up and run the application for developers on GitHub and Docker Hub.

---

## Prerequisites

Before you begin, ensure you have the following:

1. Docker installed on your system.
2. A valid API key for OpenAI, Pinecone, and other required services.
3. Environment variables properly configured (see below).

---

## Environment Variables

The application requires the following environment variables. Create a `.env` file in your project directory with the following values:

```env
OPENAI_API_KEY=sk-**
PINECONE_API_KEY=**
PINECONE_INDEX_NAME=midx
OAUTH_GITHUB_CLIENT_ID=**
OAUTH_GITHUB_CLIENT_SECRET=**
CHAINLIT_AUTH_SECRET=**
LITERAL_API_KEY=lsk_**
```

---

## Running the Application with Docker

Follow these steps to run the application using Docker:

### Step 1: Pull the Docker Image

If the image is published to Docker Hub, pull it using:

```bash
docker pull naveenalla/medical_chatbot_chatgpt_4.o
```


### Step 2: Run the Docker Container

Run the container with the `.env` file:

```bash
docker run -p 8000:8000 --env-file .env naveenalla/medical_chatbot_chatgpt_4.o
```

This will start the application and expose it on `http://localhost:8000`.

---

## Running Locally

To run the application locally without Docker, follow these steps:

1. Clone this repository:

   ```bash
   git clonehttps://github.com/Naveenalla3000/RAG_medical_chatbot.git
   cd RAG_medical_chatbot
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   conda create -n RAG_medical_chatbot_env python=3.12.8
   conda activate RAG_medical_chatbot_env
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the above environment variables.

4. Start the application:

   ```bash
   chainlit run main.py
   ```

The application will run on `http://localhost:8000`.

---

## Contributing

We welcome contributions! Feel free to submit a pull request or open an issue for any bugs or feature requests.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

