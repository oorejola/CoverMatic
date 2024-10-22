import streamlit as st
from openai import OpenAI
from tools import read_pdf, format_resume_txt, get_job_info,generate_cover_letter
import time

# Show title and description.
st.title("📄 CoverMatic")
st.subheader("Generate a cover letter for your dream job! 🚀")
st.write(" Simply upload your resume and the job description, and let CoverMatic do the rest. :sunglasses: ")
st.write( "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). ")

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")


if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    #Let the user upload a file via `st.file_uploader`.
    uploaded_file = st.file_uploader(
        "Upload a your resume (.pdf)", type=("pdf"),
        help="Upload your resume in PDF format."
    )
    
    job_description = st.text_area(
        "Add the job description.",
        placeholder="Paste the job description here...",
        help = " Add the job description, requirements, and any other relevant information. ",
        disabled= not uploaded_file
    )

   
    if uploaded_file and job_description:
        checkpoint_text = st.empty()
            
        with st.spinner("Process running..."):
            # Checkpoint 1
            checkpoint_text.write("⏳ Loading data...")
            time.sleep(1.5)

            pdf_text = read_pdf(uploaded_file)
            job_info = get_job_info(client, job_description)

            job_title = job_info.job_title
            job_description = job_info.job_summary
            company_vibe = job_info.company_vibe
            company_name = job_info.company_name
            company_summary = job_info.company_summary
            required_skills = job_info.required_skills
            preferred_skills = job_info.preferred_skills


            checkpoint_text.write("✅ Data loaded\n ⏳ Preprocessing...")
            
            
            formated_resume = format_resume_txt(client,pdf_text)

            checkpoint_text.write("✅ Data loaded\n✅ Preprocessing complete\n⏳ Generating cover letter ...")
            
            cover_letter = generate_cover_letter(client,job_title, job_description, company_name, company_summary,company_vibe, formated_resume, required_skills,preferred_skills, tone = 4)

           
            time.sleep(1.5)
            checkpoint_text.write("✅ Data loaded\n✅ Preprocessing complete\n✅  Generating cover letter")
            

        
        time.sleep(1)
            
            # Finally clear the checkpoint text
        checkpoint_text.empty()

        st.success("Cover letter generated successfully! Best of Luck! ")
        st.divider()
        st.markdown(f"""
                {cover_letter}
                """, unsafe_allow_html=True)
