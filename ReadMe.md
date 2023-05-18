# ChatGPT Web Application

The ChatGPT Web Application is a simple web-based interface that allows users to ask questions and receive answers generated by the ChatGPT model. This README provides instructions on setting up, installing, and running the application, as well as an example of making API calls and the corresponding response format.

## Setup and Installation

To set up and install the ChatGPT Web Application, follow these steps:

1. Clone the GitHub repository:

```bash
git clone https://github.com/akashpat1098/KnowWallet_Task
```

2. Navigate to the project directory:

```bash
cd KnowWallet_Task
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

   - For Windows:

   ```bash
   venv\Scripts\activate
   ```

   - For macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Create a .env file in the project directory and add the following line, replacing `<YOUR_API_KEY>` with your actual OpenAI API key:

```
OPENAI_API_KEY=<YOUR_API_KEY>
```

## Running the Application

To run the ChatGPT Web Application, execute the following command:

```bash
python app.py
```

By default, the application runs on `http://localhost:5000`.

## API Calls and Responses

To make API calls and receive responses from the ChatGPT API, follow these steps:

1. Ensure you have an OpenAI account and an API key for the ChatGPT model.

2. Set up the .env file as mentioned in the Setup and Installation section.

3. Here's an example of making an API call to the `/submit` endpoint:

   - **Request:**

     ```
     POST /submit

     Request Body:
     {
         "question": "What is the capital of France?"
     }
     ```

   - **Response:**

     ```
     Response Body:
     {
         "answer": "The capital of France is Paris."
     }
     ```

