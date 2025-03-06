
---

# Sentiment Analysis Tool

**Created by Fabricio Braga**  
**Last Updated: March 6, 2025**

---

## Project Overview

This is a **Sentiment Analysis Tool** built with **Flask** and **IBM Watson Natural Language Understanding (NLU)**. The application allows users to analyze the sentiment of text input (e.g., positive, negative, or neutral). It demonstrates how to integrate AI services into web applications and deploy them using Flask.

---

## Features

- **Analyze Text Sentiment**: Enter text and get sentiment analysis results.
- **User-Friendly Interface**: Simple and intuitive web interface.
- **Error Handling**: Displays error messages for invalid inputs or API issues.

---

## Technologies Used

- **Flask**: A lightweight Python web framework.
- **IBM Watson NLU**: AI service for sentiment analysis.
- **Jinja2**: Templating engine for rendering HTML.
- **CSS**: Custom styles for a modern and minimalist design.

---

## Prerequisites

Before running the project, ensure you have the following installed:

### 1. **Python**
- Download and install Python from [https://www.python.org/](https://www.python.org/).
- Verify the installation:
  ```bash
  python3 --version
  ```

### 2. **Git (Optional)**
- Git is used for version control. You can download it from [https://git-scm.com/](https://git-scm.com/).

---

## Getting Started

Follow these steps to set up and run the project locally.

### 1. **Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/hackthegap/course-8-sentiment-analysis-tool.git
cd course-8-sentiment-analysis-tool
```

### 2. **Set Up a Virtual Environment**

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. **Install Dependencies**

Install the required dependencies:

```bash
pip install Flask ibm-watson
```

---

## Setting Up IBM Watson NLU

To use the **IBM Watson Natural Language Understanding (NLU)** service:

1. **Create an IBM Cloud Account**:
   - Sign up at [https://cloud.ibm.com/](https://cloud.ibm.com/).

2. **Create a Watson NLU Service**:
   - Go to the IBM Cloud catalog and search for "Natural Language Understanding".
   - Create a new instance of the service.

3. **Get Your API Key and Service URL**:
   - After creating the service, navigate to the "Manage" tab.
   - Copy the **API Key** and **Service URL**.

4. **Update the Application**:
   - Open `app/routes.py` and replace `'your_api_key'` and `'your_service_url'` with your actual credentials:
     ```python
     authenticator = IAMAuthenticator('your_api_key')  # Replace with your API key
     nlu = NaturalLanguageUnderstandingV1(
         version='2021-08