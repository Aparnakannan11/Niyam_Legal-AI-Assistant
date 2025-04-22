# Niyam - Legal AI Assistant

Niyam is a web application that provides users with access to legal information and AI-powered legal assistance.

## Features

* **User Authentication:** Users can register and log in to access the application.
    ![niyam-1](https://github.com/user-attachments/assets/a0daee18-88a0-490a-9c34-3b3f82f64785)

* **Chatbot:** An AI-powered chatbot assists users with legal queries related to Indian law (IPC, labor laws, etc.).
    ![niyam-2](https://github.com/user-attachments/assets/6627227c-56b9-4922-8186-61188ad45f8f)

* **Legal Documents:** A collection of downloadable and printable legal document templates.
    ![niyam-3](https://github.com/user-attachments/assets/42d0b414-055e-46f7-bcae-acc1924c5fce)

* **Password Reset:** Users can reset their passwords if forgotten.
* **User Feedback:** Users can rate their experience.

## Technologies Used

* **Frontend:**
    * React
    * React Router
    * Axios
    * @react-oauth/google (for Google Login)
    * i18next, react-i18next, i18next-http-backend, i18next-browser-languagedetector (for internationalization - Chatbot only for now)
* **Backend:**
    * Python
    * Flask
    * Flask-CORS
    * Ollama (for the AI model)
* **Database:**
    * *(Simulated - In-memory dictionary. A real database like PostgreSQL or MySQL is recommended for production.)*

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone <YOUR_GITHUB_REPOSITORY_URL>
    cd <YOUR_PROJECT_DIRECTORY>
    ```

2.  **Backend Setup (Python/Flask):**

    * Ensure you have Python installed.
    * Navigate to the `app.py` directory
    * Create a virtual environment (recommended):
        ```bash
        python -m venv venv
        source venv/bin/activate  #  On Linux/macOS
        venv\Scripts\activate  #  On Windows
        ```
    * Install backend dependencies:
        ```bash
        pip install Flask flask_cors requests google-auth
        ```
    * Run the backend:
        ```bash
        python app.py
        ```
    * **Important:** You'll need to have Ollama set up and running separately, as `app.py` connects to it. Follow the Ollama installation instructions to download and run the `gemma:2b` model (or your preferred model).

3.  **Frontend Setup (React):**

    * Ensure you have Node.js and npm installed.
    * Navigate to the project's root directory.
    * Install frontend dependencies:
        ```bash
        npm install
        ```
    * Run the frontend:
        ```bash
        npm start
        ```
    * The frontend should be accessible at `http://localhost:3000`.

4.  **Large Folder Notes:**

    * **Option 1 (Recommended): Git LFS**
        * This repository may contain large files. It is recommended to use Git LFS (Large File Storage) to manage these files efficiently.
        * Install Git LFS: `git lfs install`
        * After cloning, run: `git lfs pull` to download the large files.
    * **Option 2 (Alternative):**
        * The large folder (`large_folder`) is not included in the repository due to its size.
        * To obtain this folder, please follow these instructions: *(Provide instructions on how to download/access the large folder)*

## Important Considerations

* **Security:** The current code uses a simulated user database (an in-memory dictionary). For production, you **must** replace this with a secure and persistent database (e.g., PostgreSQL, MySQL). Implement proper password hashing and salting.
* **Error Handling:** The code includes basic error handling, but you should expand this to provide more robust error reporting and logging.
* **Scalability:** Consider the scalability of your application, especially if you expect a large number of users. You might need to optimize your backend code and database queries.
* **Ollama Setup:** Ensure that Ollama is correctly configured and running with the necessary models. The backend's performance is heavily dependent on Ollama.
* **Translation:** The chatbot page has initial support for translations using i18next. You can expand this to other parts of the application.
* **Google Login:** Make sure you have correctly configured your Google OAuth credentials.
