
import streamlit as st

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Student Registration",
    page_icon="🎓",
    layout="centered"
)

# --------------------------------
# MAIN HEADING
# --------------------------------

st.title("🎓 Student Registration Form")
st.header("Student Information")
st.subheader("Please enter your personal details")

st.divider()

# --------------------------------
# PERSONAL INFORMATION
# --------------------------------

st.subheader("1. Personal Details")

first_name = st.text_input(
    "First Name",
    placeholder="Enter first name"
)

last_name = st.text_input(
    "Last Name",
    placeholder="Enter last name"
)

# Number input for phone
phone_no = st.number_input(
    "Phone Number",
    min_value=0,
    max_value=9999999999,
    step=1,
    format="%d"
)

email = st.text_input(
    "Email Address",
    placeholder="Enter email address"
)

prn_no = st.text_input(
    "PRN Number",
    placeholder="Enter PRN number"
)

# --------------------------------
# RADIO BUTTON FOR GENDER
# --------------------------------

st.subheader("2. Gender")

gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"],
    horizontal=True
)

# --------------------------------
# SLIDER FOR AGE
# --------------------------------

st.subheader("3. Age Selection")

age = st.slider(
    "Select Your Age",
    min_value=15,
    max_value=60,
    value=20
)

# --------------------------------
# DROPDOWN BUTTON
# --------------------------------

st.subheader("4. Course Selection")

course = st.selectbox(
    "Select Your Course",
    [
        "BCA",
        "BBA",
        "BSc",
        "BCom",
        "BA",
        "MCA",
        "MBA"
    ]
)

# --------------------------------
# DATE INPUT
# --------------------------------

st.subheader("5. Date of Birth")

dob = st.date_input(
    "Select Your Date of Birth",
    value=None
)

# --------------------------------
# TEXT AREA
# --------------------------------

st.subheader("6. Address Details")

address = st.text_area(
    "Enter Your Address",
    placeholder="Enter your complete address",
    height=100
)

# --------------------------------
# CHECKBOX
# --------------------------------

st.subheader("7. Terms and Conditions")

agree = st.checkbox(
    "I agree to the Terms and Conditions"
)

st.divider()

# --------------------------------
# IMAGE UPLOADER
# --------------------------------

st.subheader("8. Upload Your Photograph")

image = st.file_uploader(
    "Upload Your Image",
    type=["jpg", "jpeg", "png"]
)

if image is not None:
    st.image(
        image,
        caption="Uploaded Student Image",
        width=200
    )

# --------------------------------
# CAMERA INPUT
# --------------------------------

st.subheader("9. Capture Your Photograph")

camera_image = st.camera_input(
    "Take a picture using your camera"
)

if camera_image is not None:
    st.image(
        camera_image,
        caption="Camera Image",
        width=200
    )

st.divider()

# --------------------------------
# RESUME FILE UPLOADER
# --------------------------------

st.subheader("10. Upload Your Resume")

resume = st.file_uploader(
    "Upload Your Resume",
    type=["pdf", "doc", "docx"]
)

if resume is not None:
    st.success("Resume uploaded successfully!")
    st.write("Resume Name:", resume.name)

st.divider()

# --------------------------------
# SUBMIT BUTTON
# --------------------------------

if st.button("Submit Registration", use_container_width=True):

    if not first_name.strip():
        st.error("Please enter your first name.")

    elif not last_name.strip():
        st.error("Please enter your last name.")

    elif phone_no == 0:
        st.error("Please enter your phone number.")

    elif len(str(phone_no)) != 10:
        st.error("Phone number must contain 10 digits.")

    elif not email.strip() or "@" not in email:
        st.error("Please enter a valid email address.")

    elif not prn_no.strip():
        st.error("Please enter your PRN number.")

    elif not agree:
        st.warning("Please accept Terms and Conditions.")

    else:

        st.success("Student Registration Successful! 🎉")

        # --------------------------------
        # DISPLAY STUDENT DETAILS
        # --------------------------------

        st.header("Student Registration Details")

        student_data = [
            {"Field": "First Name", "Value": first_name},
            {"Field": "Last Name", "Value": last_name},
            {"Field": "Phone Number", "Value": str(phone_no)},
            {"Field": "Email", "Value": email},
            {"Field": "PRN Number", "Value": prn_no},
            {"Field": "Gender", "Value": gender},
            {"Field": "Age", "Value": age},
            {"Field": "Course", "Value": course},
            {"Field": "Date of Birth", "Value": str(dob)},
            {"Field": "Address", "Value": address},
            {
                "Field": "Image",
                "Value": image.name if image else "Not uploaded"
            },
            {
                "Field": "Camera Image",
                "Value": "Captured" if camera_image else "Not captured"
            },
            {
                "Field": "Resume",
                "Value": resume.name if resume else "Not uploaded"
            }
        ]

        st.subheader("Student Information Table")

        st.table(student_data)

        st.balloons()
