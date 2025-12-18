import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="✨ Prompt Perfecter",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'perfected_prompt' not in st.session_state:
    st.session_state.perfected_prompt = ""
if 'history' not in st.session_state:
    st.session_state.history = []

# Meta prompt template
meta_prompt = '''
You are an expert prompt engineer. Your role is to take a user's simple prompt and rewrite it to be more detailed, specific, and effective for a generative AI.

You should enhance the prompt by:
1. Adding specific context and background.
2. Defining a clear structure or format for the desired output.
3. Specifying a tone or persona for the AI to adopt.
4. Including constraints or negative prompts to avoid unwanted content.
5. Ensuring the core intent of the original prompt is preserved and clarified.

User's Raw Prompt: "{user_prompt}"

Your Perfected Prompt:
'''

# Configure Gemini API
def configure_gemini():
    api_key = os.getenv('GOOGLE_API_KEY')
    
    # Check Streamlit secrets if env var not found (for Cloud deployment)
    if not api_key and "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]

    if not api_key:
        st.error("❌ GOOGLE_API_KEY not found. Please set it in .env file (local) or Streamlit Secrets (cloud).")
        st.stop()
    genai.configure(api_key=api_key)

# Generate perfected prompt
def perfect_prompt(user_prompt, model_name):
    try:
        model = genai.GenerativeModel(model_name)
        full_prompt = meta_prompt.format(user_prompt=user_prompt)
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Main UI
def main():
    configure_gemini()
    
    # Header
    st.markdown('<h1 class="main-header">✨ Prompt Perfecter</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Transform simple prompts into detailed, effective AI instructions</p>', unsafe_allow_html=True)
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        model_options = {
            "Gemini 2.5 Pro (Best Quality)": "gemini-2.5-pro",
            "Gemini 2.5 Flash (Fast & Balanced)": "gemini-2.5-flash",
            "Gemini Pro Latest": "gemini-pro-latest",
            "Gemini Flash Latest": "gemini-flash-latest"
        }
        
        selected_model = st.selectbox(
            "Select Model",
            options=list(model_options.keys()),
            index=1  # Default to Flash
        )
        
        st.divider()
        
        st.markdown("### 📊 Model Info")
        if "Pro" in selected_model:
            st.info("**Pro Models:**\n- Highest quality\n- 2 req/min\n- 50 req/day")
        else:
            st.info("**Flash Models:**\n- Fast & efficient\n- 15 req/min\n- 1,500 req/day")
        
        st.divider()
        
        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.session_state.perfected_prompt = ""
            st.rerun()
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Your Simple Prompt")
        user_prompt = st.text_area(
            "Enter your prompt here:",
            height=200,
            placeholder="Example: write a story about a cat",
            label_visibility="collapsed"
        )
        
        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            perfect_button = st.button("✨ Perfect My Prompt", type="primary", use_container_width=True)
        with col_btn2:
            clear_button = st.button("🔄 Clear", use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Perfected Prompt")
        
        if perfect_button and user_prompt.strip():
            with st.spinner("🔄 Perfecting your prompt..."):
                model_name = model_options[selected_model]
                perfected = perfect_prompt(user_prompt, model_name)
                st.session_state.perfected_prompt = perfected
                
                # Add to history
                st.session_state.history.append({
                    'original': user_prompt,
                    'perfected': perfected,
                    'model': selected_model
                })
        
        if clear_button:
            st.session_state.perfected_prompt = ""
        
        # Display perfected prompt
        if st.session_state.perfected_prompt:
            if st.session_state.perfected_prompt.startswith("Error:"):
                st.error(st.session_state.perfected_prompt)
            else:
                st.text_area(
                    "Perfected output:",
                    value=st.session_state.perfected_prompt,
                    height=200,
                    label_visibility="collapsed"
                )
                
                # Copy button
                st.code(st.session_state.perfected_prompt, language=None)
                st.success("✅ Prompt perfected! Copy the text above.")
        else:
            st.info("👈 Enter a prompt and click 'Perfect My Prompt' to get started!")
    
    # Examples section
    with st.expander("💡 See Examples"):
        st.markdown("""
        **Simple Prompt:**
        > write a story about a cat
        
        **Perfected Prompt:**
        > Write a heartwarming short story (800-1000 words) about a curious tabby cat named Whiskers who discovers a hidden magical garden in their backyard. Include:
        > - A clear beginning, middle, and end structure
        > - Vivid sensory descriptions of the garden
        > - Character development showing Whiskers' personality
        > - A gentle tone suitable for all ages
        > - Dialogue or internal thoughts from the cat's perspective
        > 
        > Avoid: violence, dark themes, or overly complex vocabulary
        
        ---
        
        **Simple Prompt:**
        > explain quantum computing
        
        **Perfected Prompt:**
        > Provide a comprehensive explanation of quantum computing for an intelligent high school student with basic physics knowledge. Structure your response as follows:
        > - Introduction: Define quantum computing and its significance (2-3 sentences)
        > - Core Concepts: Explain qubits, superposition, and entanglement using analogies
        > - Comparison: How it differs from classical computing
        > - Applications: 3-4 real-world use cases
        > - Future Outlook: Current limitations and potential
        > 
        > Tone: Educational but engaging
        > Avoid: Complex mathematical formulas, overly technical jargon
        """)
    
    # History section
    if st.session_state.history:
        st.divider()
        st.markdown("### 📜 Recent History")
        
        for i, item in enumerate(reversed(st.session_state.history[-5:])):
            with st.expander(f"🕐 Prompt {len(st.session_state.history) - i} - {item['model']}", expanded=False):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Original:**")
                    st.text(item['original'][:100] + "..." if len(item['original']) > 100 else item['original'])
                with col2:
                    st.markdown("**Perfected:**")
                    st.text(item['perfected'][:100] + "..." if len(item['perfected']) > 100 else item['perfected'])
    
    # Footer
    st.divider()
    st.markdown("""
        <div style='text-align: center; color: #666; padding: 1rem;'>
            <p>Made with ❤️ using Streamlit & Google Gemini</p>
            <p style='font-size: 0.8rem;'>💡 Tip: Use the perfected prompts with any AI model (ChatGPT, Claude, etc.)</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
