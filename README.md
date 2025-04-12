# Nabafat.AI Business Plan Generator

Welcome to the **Nabafat.AI Business Plan Generator**, an AI-powered web application designed to help entrepreneurs and startups create professional business plans effortlessly. Leveraging advanced AI models, this platform generates comprehensive market analyses, business strategies, financial projections, and investor pitches tailored to your business idea. Built with Flask, Tailwind CSS, and LangGraph, it offers a sleek, responsive interface to attract professionals and investors.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **AI-Powered Business Planning**: Input your business idea to generate:
  - Market analysis with industry trends and competitor insights.
  - Structured business strategy, including revenue models and growth plans.
  - Detailed financial projections with costs, revenue, and break-even points.
  - Compelling investor pitches highlighting market opportunity and ROI.
- **Professional UI**: A modern, responsive design using Tailwind CSS, optimized for desktops and mobile devices.
- **Interactive Experience**: Loading state with a spinner for form submissions to enhance user experience.
- **About Page**: Showcases Nabafat.AI’s mission to empower smart machines with vision intelligence, featuring services like AI chatbots, VR, ML, and IoT.
- **Secure Configuration**: Uses environment variables for sensitive data like API keys.

## Tech Stack
- **Backend**: Flask (Python) for routing and server-side logic.
- **Frontend**: HTML, Tailwind CSS for styling, and vanilla JavaScript for interactivity.
- **AI**: LangGraph and LangChain-Groq with Llama 3.1 8B model for generating business plan components.
- **Dependencies**: Managed via `requirements.txt`, including `python-dotenv` for secure configuration.
- **Markdown**: Converts AI-generated markdown to HTML for clean display.

## Folder Structure
```
business-plan-generator/
│
├── /static/
│   ├── /css/
│   │   └── styles.css              # Custom CSS (optional for future styling)
│   ├── /images/
│   │   ├── hero-bg.jpg             # Hero section background
│   │   ├── icon-analysis.png       # Icon for market insights
│   │   ├── icon-financials.png     # Icon for financials
│   │   ├── icon-pitch.png         # Icon for pitches
│   │   ├── icon-automation.png     # Icon for automation
│   │   ├── icon-cloud.png         # Icon for cloud infrastructure
│   │   ├── icon-security.png       # Icon for cybersecurity
│   │   └── icon-chatbot.png        # Icon for chatbots
│   └── /js/
│       └── script.js               # JavaScript for form loading state
│
├── /templates/
│   ├── index.html                  # Home page with business plan generator
│   └── about.html                  # About page for Nabafat.AI
│
├── .env                            # Environment variables (not tracked)
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

**Note**: Images are referenced externally (Unsplash, Icons8) in the templates but should be stored locally in `/static/images/` for production, as shown above.

## Prerequisites
- **Python**: Version 3.8 or higher.
- **Git**: For cloning the repository.
- **Groq API Key**: Obtain from [Groq](https://groq.com) to power the AI model.
- **Virtual Environment**: Recommended for dependency isolation.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abdull6771/business-plan-generator
   cd business-plan-generator
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the root directory:
     ```plaintext
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Replace `your_groq_api_key_here` with your actual Groq API key.

5. **Download Images** (Optional for Production):
   - Place images in `/static/images/` as listed in the folder structure.
   - Update `index.html` and `about.html` to reference local paths (e.g., `/static/images/hero-bg.jpg`).

## Usage
1. **Run the Application**:
   ```bash
   python app.py
   ```
   The app will start at `http://localhost:5000`.

2. **Navigate the App**:
   - **Home Page (`/`)**: Enter a business idea in the form to generate a business plan. The AI will produce a market analysis, strategy, financials, and pitch, displayed below the form.
   - **About Page (`/about`)**: Learn about Nabafat.AI’s mission and services, including AI chatbots, virtual reality, machine learning, and IoT solutions.

3. **Interact with the Form**:
   - Submit a business idea (e.g., “A sustainable clothing brand using recycled materials”).
   - The “Generate Plan” button will show a loading spinner (`Generating... ⌀`) while processing.
   - View the results in a clean, formatted layout.

## Contributing
We welcome contributions to enhance the Nabafat.AI Business Plan Generator! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request with a detailed description.

Please ensure your code follows PEP 8 standards and includes relevant tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Built with ❤️ by Nabafat.AI to empower entrepreneurs and innovators.
