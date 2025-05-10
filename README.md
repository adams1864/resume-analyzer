# Resume Analyzer

## Description

The Resume Analyzer is a backend application built with Django REST Framework that helps parse and extract information from resume files (primarily PDFs). It provides API endpoints for uploading resumes, extracting text, and potentially integrating with other services for further analysis (e.g., sending data to n8n for workflow automation).

## Features

*   **User Authentication:** Secure login using JWT (JSON Web Tokens).
*   **Resume Upload:** Accepts resume files via API endpoint.
*   **PDF Extraction:** Extracts text content from PDF resumes using PDFMiner.
*   **Integration with n8n (Optional):** Sends resume data to an n8n workflow for automated processing.
*   **PostgreSQL Storage (Future):**  Intended to store extracted resume data in a PostgreSQL database.

## Technologies Used

*   Python
*   Django
*   Django REST Framework
*   djangorestframework-simplejwt
*   pdfminer.six
*   requests

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd backend
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the database:**

    *   Update the `DATABASES` settings in `backend/settings.py` with your PostgreSQL database credentials.

5.  **Run migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints

*   **`POST /login/`:**
    *   Authenticates a user and returns a JWT access token.
    *   Requires: `username`, `password` in the request body.
    *   Example:

        ```json
        {
            "username": "your_username",
            "password": "your_password"
        }
        ```

*   **`POST /upload_resume/`:**
    *   Uploads a resume file.
    *   Requires:
        *   Authentication: JWT token in the `Authorization` header (e.g., `Authorization: Bearer <your_token>`).
        *   `file`: The resume file in the `multipart/form-data`.
    *   Example (using `curl`):

        ```bash
        curl -X POST \
          http://localhost:8000/api/upload_resume/ \
          -H 'Authorization: Bearer <your_token>' \
          -H 'Content-Type: multipart/form-data' \
          -F 'file=@/path/to/your/resume.pdf'
        ```

*   **`POST /extract_pdf/`:**
    *   Extracts text from a PDF file.
    *   Requires:
        *   `file`: The PDF file in the `multipart/form-data`.
    *   Example (using `curl`):

        ```bash
        curl -X POST \
          http://localhost:8000/api/extract_pdf/ \
          -H 'Content-Type: multipart/form-data' \
          -F 'file=@/path/to/your/resume.pdf'
        ```

## n8n Integration (Optional)

The application can be integrated with n8n for automated resume processing.

1.  **Configure the n8n webhook:**

    *   Create an n8n workflow with a Webhook node that listens for POST requests.
    *   Set the "Field Name for Binary Data" to `data`.

2.  **Update the `upload_resume` view:**

    *   Ensure the `upload_resume` view in `backend/api/views.py` sends the resume file to the n8n webhook URL.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes.
4.  Write tests to ensure your changes are working correctly.
5.  Submit a pull request.

## License

[Specify the license here, e.g., MIT License]
