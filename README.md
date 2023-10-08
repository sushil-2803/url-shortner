# URL Shortener

URL Shortener is a simple web application built using Flask, Python, and MongoDB. It allows users to create shortened URLs for long links, making them easier to share. The application is deployed and can be accessed at [https://url-shortner-x6kn.onrender.com/](https://url-shortner-x6kn.onrender.com/).

## Features

- **Shorten URLs**: Create short aliases for long URLs.
- **Redirect**: Access the original long URL by using the generated short URL.
- **Statistics**: View the number of times a short URL has been accessed.

## Usage

1. Visit [https://url-shortner-x6kn.onrender.com/](https://url-shortner-x6kn.onrender.com/).
2. Enter the long URL you want to shorten.
3. Receive the shortened URL.
4. Share the shortened URL with others.

## Deployment

The URL Shortener is deployed and can be accessed at [https://url-shortner-x6kn.onrender.com/](https://url-shortner-x6kn.onrender.com/).

## Technology Stack

- **Flask**: A lightweight web application framework in Python.
- **MongoDB**: A NoSQL database for storing URL mappings.
- **Render**: Deployment platform for hosting web applications.

## Prerequisites

Before running the application locally, make sure you have the following installed:

- Python: [Download Python](https://www.python.org/downloads/)
- Flask: Install using `pip install Flask`
- MongoDB: [Download MongoDB](https://www.mongodb.com/try/download/community)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/sushil-2803/url-shortener.git
   ```

2. Navigate to the project directory:

   ```bash
   cd url-shortener
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:

     ```env
     MONGO_URI=your-mongodb-connection-uri
     ```

5. Run the application:

   ```bash
   python app.py
   ```

6. Open your browser and visit `http://localhost:5000` to access the URL Shortener.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Enjoy shortening your URLs! 🚀
