import streamlit as st
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fpdf import FPDF

# Greet the user
def greet_user():
    st.write("Hi, welcome to YouTube channel Recommendations! 😊")
    name = st.text_input("Please enter your name:")
    if name:
        st.write(f"Hi {name}, I hope you're doing awesome! 🚀")
    return name

# Choose Tech Stack
def choose_tech_stack():
    tech_stacks = [
        "Front-End", "Back-End", "UI/UX", "DevOps", "Linux", "Cloud",
        "SQL", "NoSQL", "AI/ML", "Blockchain", "CyberSecurity",
        "Python Full-Stack Development", "Java Full-Stack Development"
    ]
    return st.selectbox("Which Tech-Stack do you want to learn?", tech_stacks)

# Generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP via email
def send_email(user_email, otp):
    sender_email = "dharnidharni005@gmail.com"
    sender_password = "xvpy wriw zlwh hcbv"  # Use App Password, NOT your Gmail password

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = user_email
    message["Subject"] = "Your OTP for YouTube Channel Access"
    
    email_body = f"""
    Hello,

    Your OTP for accessing YouTube links is: {otp}

    Please enter this OTP in the application to verify.

    Thank you!
    """
    message.attach(MIMEText(email_body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, user_email, message.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")
        return False

# OTP Verification and YouTube Links Access
def verify_and_send_links():
    st.subheader("🔑 OTP Verification for YouTube Links")
    
    user_email = st.text_input("📩 Enter your email address:")
    if st.button("Send OTP", key="send_otp"):
        if user_email:
            otp = generate_otp()
            st.session_state["otp"] = otp
            if send_email(user_email, otp):
                st.success("✅ OTP sent to your email successfully!")
        else:
            st.error("❌ Please enter a valid email.")

    user_otp = st.text_input("🔢 Enter the OTP sent to your email:", max_chars=6)

    if st.button("Verify OTP", key="verify_otp"):
        if "otp" in st.session_state and user_otp == st.session_state["otp"]:
            st.success("✅ OTP verified successfully!")
            st.write("🔗 Yeah!. Now you can Download your Role details as a PDF:")
        else:
            st.error("❌ Incorrect OTP. Please try again.")

# Initialize session state
if "name" not in st.session_state:
    st.session_state["name"] = None
if "tech_stack" not in st.session_state:
    st.session_state["tech_stack"] = None

st.title("YouTube Channel Recommendation Chatbot")

# Sidebar for user input
st.sidebar.title("📜 PDF Builder")

if st.sidebar.button("PDf Previous Session", key="resume_session"):
    st.session_state["resume"] = True

name = st.sidebar.text_input("Enter your name:")
if name:
    st.session_state["name"] = name

tech_stacks = [
    "Front-End", "Back-End", "UI/UX", "DevOps", "Linux", "AWS","Cloud"
    "SQL", "NoSQL", "AI/ML", "Blockchain", "CyberSecurity",
    "Python Full-Stack Development", "Java Full-Stack Development"
]
tech_stack = st.sidebar.selectbox("Choose Your Tech Stack:", tech_stacks)
if tech_stack:
    st.session_state["tech_stack"] = tech_stack

# PDF Generation Function
def generate_pdf(name, tech_stack):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Tech Stack Guide", ln=True, align="C")
    
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Name: {name}", ln=True)
    pdf.cell(200, 10, f"Selected Tech Stack: {tech_stack}", ln=True)
    
    pdf.ln(10)
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(200, 10, "Tech Stack Overview", ln=True)

    templates = {
        "Front-End": "Front-end developers work with HTML, CSS, and JavaScript frameworks like React, Angular, or Vue.js. Link :https://www.youtube.com/c/Academind) Resume :https://www.jobhero.com/career-guides/resume/templates/ats ",
        "Back-End": "Back-end developers manage databases, APIs, and frameworks like Django, Spring Boot, and Node.js. Link: https://www.youtube.com/c/CleverProgrammer) Resume :https://www.jobhero.com/career-guides/resume/templates/ats",
        "AI/ML": "AI/ML engineers work with Python, TensorFlow, PyTorch, and deep learning techniques. Link : ",
        "CyberSecurity": "Cybersecurity experts focus on network security, cryptography, and ethical hacking. Link:https://www.youtube.com/c/HackerSploit) Resume :https://www.jobhero.com/career-guides/resume/templates/ats",
        "AWS": "AWS cloud engineers manage EC2, S3, Lambda, and cloud architecture.",
        "DevOps": 
        "Linux & Bash Scripting, Git & Version Control,CI/CD (Jenkins, GitHub Actions, GitLab CI),Containerization (Docker, Kubernetes),Cloud Platforms(AWS, Azure, GCP),Infrastructure as Code (Terraform, Ansible) Link :https://www.youtube.com/c/TheNetNinja) Resume :https://www.jobhero.com/career-guides/resume/templates/ats",
        "UI/UX":
        "UI/UX Principles & Design Thinking,Wireframing & Prototyping (Figma, Adobe XD),Typography, Color Theory, Accessibility,Interaction Design & Microanimations,Usability Testing & A/B Testing Link :https://www.youtube.com/c/AJSmart) Resume :https://www.jobhero.com/career-guides/resume/templates/ats",
        "Cloud ":
        "Cloud Fundamentals (IaaS, PaaS, SaaS),Cloud Providers (AWS, Azure, GCP),Networking & Security (VPC, IAM, Load Balancers),Serverless Computing (AWS Lambda, Azure Functions),Cloud DevOps (Terraform, CloudFormation, CI/CD),Cloud Monitoring & Cost Optimization. Link :https://www.youtube.com/c/ACloudGuru)Resume :https://www.jobhero.com/career-guides/resume/templates/ats ",
        "Blockchain" :"Baics (BC) Types of Blockchain (Public, Private, Consortium),Cryptography Basics (Hashing, Digital Signatures),Consensus Mechanisms (PoW, PoS, etc.),Cryptography & Security:SHA-256 Hashing,Public & Private Keys,Digital Signatures,Merkle Trees Smart Contracts & DApps Ethereum & Solidity Basics Deploying Smart Contracts Interacting with Web3.py ,Building Decentralized Applications (DApps) Link : https://www.youtube.com/c/DappUniversity) Resume :https://www.jobhero.com/career-guides/resume/templates/ats",
        "SQL" : "What is SQL,SQL vs NoSQL, Database Management Systems (RDBMS),Installation (MySQL, PostgreSQL, SQLite) SQL Queries , Joins & Relationships Advanced SQL , Real-World Applications Link :https://www.youtube.com/c/TraversyMedia) Resume :https://www.jobhero.com/career-guides/resume/templates/ats",
        "NoSQL" : "What is NoSQL ,SQL vs NoSQL Differences ,Types of NoSQL Databases (Key-Value, Document, Column-Family, Graph),Learn NoSQL Databases MongoDB (Document-based),Redis,Cassandra, Working with NoSQL,Real-World Applications Link : https://www.youtube.com/c/Academind) Resume :https://www.jobhero.com/career-guides/resume/templates/ats",
    }

    pdf.ln(5)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, templates.get(tech_stack, "This tech stack involves various tools and technologies."))

    return pdf

if st.sidebar.button("Generate PDF", key="generate_pdf"):
    if st.session_state["name"] and st.session_state["tech_stack"]:
        pdf = generate_pdf(st.session_state["name"], st.session_state["tech_stack"])
        pdf_output = "resume.pdf"
        pdf.output(pdf_output)

        with open(pdf_output, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
        st.sidebar.download_button(label="Download Resume PDF", data=pdf_bytes, file_name="Resume.pdf", mime="application/pdf")
        st.success("✅ Resume Generated Successfully!")
    else:
        st.sidebar.error("⚠️ Please enter your name and select a tech stack first.")

# Run chatbot
def chatbot_interface():
    user_input = st.text_input("Enter your greeting (Hi, Hello, Hey, etc.):")
    if user_input and user_input.strip().upper() in ["HI", "HELLO", "HEY"]:
        name = greet_user()
        if name:
            choose_tech_stack()
            verify_and_send_links()


if __name__ == "__main__":
    chatbot_interface()
