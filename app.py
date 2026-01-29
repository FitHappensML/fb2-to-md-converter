# app.py (Updated)

# Import necessary libraries
import streamlit as st

# Import our core conversion function from converter.py
from converter import convert_fb2_to_txt
import credentials

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="FB2 Reader & Converter",
    page_icon="📖",
    layout="wide"
)

# --- 2. Sidebar for Controls ---
with st.sidebar:
    st.header("Controls")

    # File uploader widget
    uploaded_file = st.file_uploader(
        "Upload your FB2 file",
        type=['fb2']
    )

    # Checkbox for smart formatting now controls the *display* in the reader.
    use_smart_formatting = st.checkbox(
        "Render with smart formatting", # UPDATED: Clarified the label
        value=True,
        help="Display subtitles as headers and emphasis as italics in the reader view."
    )
    
    
    # Placeholder for the download buttons.
    download_placeholder = st.empty()

    # --- UPDATED: Thank you message & Social Links ---
    st.divider() # Adds a visual separation line
    st.markdown("### Thanks for using use this tool!")
    st.caption("Check out more useful tools & updates:")
    
    # Display links using columns for better layout
    col_social1, col_social2 = st.columns(2)
    with col_social1:
        st.link_button("Twitter", credentials.TWITTER_URL)
    with col_social2:
        st.link_button("Telegram", credentials.TELEGRAM_URL)



# --- 3. Main Area for Displaying Content ---

st.title("📖 FB2 Reader & Converter")

# Check if a file has been uploaded
if uploaded_file is not None:
    # --- File has been uploaded, process it ---
    
    try:
        fb2_content_bytes = uploaded_file.getvalue()
        fb2_content_str = fb2_content_bytes.decode('utf-8')

        # --- UPDATED: Generate both text versions upfront for efficiency ---
        # We'll generate a plain text version for .txt download
        # and a Markdown version for .md download and smart display.
        with st.spinner('Preparing your book...'):
            plain_text = convert_fb2_to_txt(fb2_content_str, smart_formatting=False)
            markdown_text = convert_fb2_to_txt(fb2_content_str, smart_formatting=True)

        # Determine which version to display based on the user's checkbox choice.
        text_for_display = markdown_text if use_smart_formatting else plain_text

        # --- Display the converted text ---
        st.markdown("---")
        st.markdown(text_for_display, unsafe_allow_html=False)
        st.markdown("---")
        
        # --- UPDATED: Add two download buttons to the sidebar ---
        # We populate the placeholder with a new header and two buttons side-by-side.
        with download_placeholder.container():
            st.header("Download Options")
            
            # Use columns to place buttons next to each other
            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    label="Download as .txt",
                    data=plain_text, # Use the plain_text version
                    file_name=f"{uploaded_file.name.split('.')[0]}.txt",
                    mime='text/plain',
                    use_container_width=True # Makes the button fill the column
                )

            with col2:
                st.download_button(
                    label="Download as .md",
                    data=markdown_text, # Use the markdown_text version
                    file_name=f"{uploaded_file.name.split('.')[0]}.md",
                    mime='text/markdown', # Use a more appropriate MIME type
                    use_container_width=True
                )

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")

else:
    # --- No file uploaded yet, show instructions ---
    st.info("Please upload an FB2 file using the sidebar to get started.")
    # UPDATED: Help text now mentions both download formats.
    st.markdown("""
    ### How to use:
    1.  **Upload a file:** Click on "Browse files" in the sidebar on the left.
    2.  **Adjust view:** Use the "Render with smart formatting" checkbox to control how the text is displayed here.
    3.  **Read:** The converted text will appear in this main area.
    4.  **Download:** Download buttons for both `.txt` and `.md` formats will appear in the sidebar.
    """)