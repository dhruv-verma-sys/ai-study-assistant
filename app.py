"""
app.py - Streamlit User Interface for the AI Study Assistant.
Industrial Internship Training on Microsoft Azure AI Fundamentals (AI-901)
Candidate: Dhruv Verma (UID: 24BAI70426) | CSE (AIML), Chandigarh University
"""

import streamlit as st
import prompts
import foundry_client

# Sample Lecture Notes for rapid evaluation and testing
SAMPLE_NOTES = {
    "Custom (Paste your own)": "",
    "Week 1: Common AI Workloads": (
        "Artificial intelligence systems perform tasks traditionally requiring human intelligence.\n"
        "Machine learning is a subset of AI where systems learn patterns from training data rather than hand-coded rules.\n"
        "Common AI workloads in Microsoft Azure include:\n"
        "1. Generative AI: Creates novel text, code, audio, and visual media in response to natural language prompts.\n"
        "2. Agentic AI: Autonomous agents combining foundation models, reasoning loops, system prompts, and tool use to execute multi-step workflows.\n"
        "3. Text Analysis (NLP): Keyword extraction, Named Entity Recognition (NER), sentiment analysis, and extractive/abstractive summarization.\n"
        "4. Speech: Speech-to-Text (STT acoustic modeling) and Text-to-Speech (TTS neural voice synthesis).\n"
        "5. Computer Vision: Image classification, object detection, optical character recognition (OCR), and image captioning.\n"
        "6. Content Understanding: Multimodal extraction turning documents, forms, images, audio, and video into structured JSON field schemas."
    ),
    "Week 2: The Six Principles of Responsible AI": (
        "Microsoft's Responsible AI Standard establishes six foundational principles to govern AI development and deployment:\n"
        "1. Fairness: AI systems must treat all demographic groups equitably without systemic bias or disparate impact.\n"
        "2. Reliability and Safety: Systems must operate consistently within design limits, undergo rigorous adversarial testing, and include safety guardrails.\n"
        "3. Privacy and Security: Protect sensitive user data through encryption, access control (Entra ID), data minimization, and compliance with data governance.\n"
        "4. Inclusiveness: Solutions must empower everyone regardless of physical ability, background, or language, featuring screen reader support and plain language.\n"
        "5. Transparency: Inform users that they are interacting with AI, state system boundaries clearly, and disclose sources or confidence metrics.\n"
        "6. Accountability: Human developers and organizations remain answerable for outcomes, supported by human-in-the-loop oversight."
    ),
    "Week 3: Microsoft Foundry & Prompt Engineering": (
        "Microsoft Foundry provides a centralized cloud environment within Azure subscriptions for AI engineering.\n"
        "A Foundry project manages model deployments, access controls via Microsoft Entra ID, content filters, and prompt playgrounds.\n"
        "Prompt engineering relies on five critical pillars:\n"
        "- Role: Defines the persona, authority, and tone of the model.\n"
        "- Task: Concrete, unambiguous instructions of what to perform.\n"
        "- Context: Background data, lecture notes, or domain knowledge supplied to the model.\n"
        "- Format: Prescribed output architecture (e.g., numbered lists, tables, markdown).\n"
        "- Limits: Grounding boundaries instructing the model to rely only on context and refuse speculation.\n"
        "Model sampling parameters include Temperature (randomness), Top-p (nucleus probability mass), and Max Tokens (response ceiling)."
    )
}

st.set_page_config(
    page_title="AI Study Assistant | Microsoft Foundry",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.1rem;
        font-weight: 700;
        color: #0078D4;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #555555;
        margin-bottom: 20px;
    }
   .academic-badge {
    background-color: rgba(59, 130, 246, 0.15);
    border-left: 4px solid #3b82f6;
    padding: 10px 15px;
    border-radius: 6px;
    margin-bottom: 20px;
}
    .disclaimer-box {
    background-color: rgba(245, 158, 11, 0.15);
    border-left: 4px solid #f59e0b;
    padding: 12px 16px;
    border-radius: 6px;
    margin-top: 15px;
}
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown('<div class="main-header">🎓 AI Study Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Intelligent Lecture Note Transformation powered by Microsoft Azure AI Foundry</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="academic-badge">
    <strong>Author:</strong> Dhruv Verma (UID: 24BAI70426) &nbsp;|&nbsp; 
    <strong>Degree:</strong> B.E. CSE (AIML), Chandigarh University &nbsp;|&nbsp; 
    <strong>Certification:</strong> Microsoft Azure AI Fundamentals (AI-901)
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Study Mode & Settings")
    
    mode_options = {
        "summarize": "📝 Summarize Notes",
        "key_points": "📌 Key Points & Definitions",
        "practice_questions": "❓ Practice Questions & MCQs",
        "ask_question": "💡 Ask a Specific Question",
        "explain_simply": "🧠 Explain Simply (Feynman Style)"
    }
    
    selected_mode_key = st.selectbox(
        "Choose Study Mode:",
        options=list(mode_options.keys()),
        format_func=lambda x: mode_options[x],
        index=0
    )
    
    st.divider()
    st.subheader("📚 Quick Sample Presets")
    sample_choice = st.selectbox(
        "Load sample notes:",
        options=list(SAMPLE_NOTES.keys()),
        index=0
    )
    
    st.divider()
    st.subheader("🎛️ Model Parameters (Table 2.4)")
    temperature = st.slider(
        "Temperature (Randomness)",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.05,
        help="Low (0.0-0.3) for strict factual grounding; higher for varied phrasing."
    )
    
    max_tokens = st.slider(
        "Max Response Tokens",
        min_value=250,
        max_value=2500,
        value=1000,
        step=50,
        help="Upper bound on response length to control cost and latency."
    )
    
    top_p = st.slider(
        "Top-p (Nucleus Sampling)",
        min_value=0.1,
        max_value=1.0,
        value=0.9,
        step=0.05,
        help="Alternative parameter to control diversity of token sampling."
    )
    
    st.divider()
    with st.expander("🛡️ Responsible AI Principles (Table 2.12)"):
        st.markdown(
            """
            - **Fairness:** Neutral, inclusive academic phrasing.
            - **Reliability & Safety:** Strict grounding in notes; prompt boundaries.
            - **Privacy & Security:** Notes are ephemeral and not saved to disk.
            - **Inclusiveness:** Plain language explanations & screen-reader compatibility.
            - **Transparency:** Clear notice indicating AI-generated content.
            - **Accountability:** Student retains final responsibility for exam study.
            """
        )

# Main Workspace Layout
col_input, col_output = st.columns([1, 1], gap="medium")

with col_input:
    st.subheader("📥 Input Lecture Notes")
    
    default_text = SAMPLE_NOTES[sample_choice] if sample_choice != "Custom (Paste your own)" else ""
    
    notes_input = st.text_area(
        "Paste your study notes below:",
        value=default_text,
        height=320,
        placeholder="Paste your lecture transcript, textbook extract, or slide notes here..."
    )
    
    user_question = ""
    if selected_mode_key == "ask_question":
        user_question = st.text_input(
            "❓ Enter your question about the notes:",
            placeholder="e.g., What are the six principles of responsible AI?"
        )
    
    # Input stats
    char_count = len(notes_input)
    word_count = len(notes_input.split())
    st.caption(f"📊 Stats: **{word_count}** words | **{char_count}** characters")
    
    submit_btn = st.button("🚀 Generate Study Material", type="primary", use_container_width=True)

with col_output:
    st.subheader("📤 Assistant Output")
    
    if submit_btn:
        if not notes_input.strip():
            st.error("⚠️ Please paste your lecture notes before generating.")
        elif selected_mode_key == "ask_question" and not user_question.strip():
            st.warning("⚠️ Please enter a specific question in the box above.")
        else:
            with st.spinner("Processing notes with Microsoft Foundry Assistant..."):
                system_prompt = prompts.SYSTEM_PROMPTS[selected_mode_key]
                user_prompt = prompts.build_user_prompt(
                    mode=selected_mode_key,
                    notes=notes_input,
                    user_question=user_question
                )
                
                result = foundry_client.call_foundry_chat(
                    system_prompt=system_prompt,
                    user_prompt=user_prompt,
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens,
                    mode=selected_mode_key,
                    notes=notes_input,
                    user_question=user_question,
                )
                
                if result.get("success"):
                    st.success(f"Generated successfully via **{result.get('provider')}**")
                    if "warning" in result:
                        st.info(f"ℹ️ {result['warning']}")
                    
                    st.markdown(result["content"])
                    
                    # Download Button
                    st.download_button(
                        label="💾 Download Generated Notes (.md)",
                        data=result["content"],
                        file_name=f"study_assistant_{selected_mode_key}.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                    
                    # Mandatory Responsible AI Transparency Notice
                    st.markdown(
                        f"""
                        <div class="disclaimer-box">
                        {result['disclaimer']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.error(f"❌ Error: {result.get('error', 'An unexpected error occurred.')}")
    else:
        st.info("👈 Paste your lecture notes on the left and click **'Generate Study Material'** to begin.")
