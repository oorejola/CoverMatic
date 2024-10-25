#  CoverMatic 📝🚀


[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://covermatic.streamlit.app/)


## Overview

CoverMatic is a Cover Letter Generator web application that automatically creates personalized cover letters based on your resume and a job description. Writing cover letters can be tedious during a job search, and some say recruiters don't even read them. This project goes beyond simple templating by:

- 🔍 Identifying key skills from the job description
- 🎯 Matching relevant skills from your resume
- 🎨 Adjusting the language to fit the company's vibe
  
Say goodbye to generic cover letters and hello to tailored, compelling introductions that make you stand out! 🌟



## Prerequisites 🧰

- Python 3.7+
- OpenAI API key

## Setup 🔧


1. Clone this repository.
2. Install the required packages:
   ```
   $ pip install -r requirements.txt
   ```
3. Hard-code your OpenAI API key in the `tools.py` file (not recommended for security reasons).
   
## How to run it on your own machine

1. Install the requirements (if not done already):

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

## Usage 🏃‍♂️
1. Drag and drop a .pdf of your resume into the designated area in the app.
2. Copy and paste the job description, including requirements, qualifications, and any other relevant information, into the input field.
3. Let it bake.
4. Your personalized cover letter will be displayed and can be downloaded as needed.

## Prompt Engineering 🧠

This project utilizes advanced prompt engineering techniques to improve the quality and relevance of the generated cover letters. The `prompts/` folder contains three main prompts, each designed for a specific task in the cover letter generation process:

1. Resume Formatting Prompt:
   - Purpose: Converts various resume formats into a structured markdown format.
   - Key Features:
     * Uses markdown headers to organize sections (e.g., Experience, Education, Skills)
     * Formats contact information, experience, and education consistently
     * Preserves all original information while improving readability

2. Job Description Analysis Prompt:
   - Purpose: Extracts key information from the job description.
   - Key Features:
     * Identifies job title, company name, and summarizes main responsibilities
     * Extracts up to 5 required and 5 preferred skills/qualifications
     * Analyzes company vibe and culture based on the job description language

3. Cover Letter Generation Prompt:
   - Purpose: Creates a tailored cover letter based on the resume and job description analysis.
   - Key Features:
     * Adjusts tone based on a 1-5 scale (very formal to casual)
     * Structures the letter with an opening, skills alignment paragraphs, and closing
     * Emphasizes how the candidate's skills match the job requirements
     * Incorporates the company's vibe into the letter's style

These prompts work together to:
- Extract relevant information from your resume
- Analyze the job description for key requirements and company culture
- Structure the cover letter in a professional format
- Tailor the content to highlight your qualifications for the specific job

By using well-designed prompts, the system generates focused and effective cover letters. Users can modify these prompts in the `prompts/` folder to fine-tune the output according to their preferences or specific industry requirements.

## License 📄

See the `LICENSE` file for details.

## Contributing 💡

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer ⚠️

This tool is for assistance purposes only. Always review and personalize the generated cover letter before sending it to potential employers.
