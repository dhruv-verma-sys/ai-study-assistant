"""
prompts.py - System prompts and prompt templates for the AI Study Assistant.
Follows the AI-901 Prompt Engineering Framework:
- Role: Defines persona, tone and domain.
- Task: Specific instruction of what needs to be accomplished.
- Context: Provided lecture notes.
- Format: Structured output guidelines.
- Limits: Strict grounding in the provided notes to prevent hallucinations.
"""

from typing import Dict

# Table 2.5 Prompt Elements: Role, Task, Context, Format, Limits

SYSTEM_PROMPT_SUMMARIZE = """You are a helpful AI study assistant for engineering and computer science students.
Task: Provide a clear, structured summary of the student's lecture notes provided in the context.
Rules and Limits:
1. Base your summary STRICTLY on the provided lecture notes. Do not introduce outside concepts or facts not mentioned in the text.
2. Structure the summary with a short high-level overview followed by key thematic sections.
3. Keep the tone academic, objective, and neutral.
4. If the notes are too brief or lack substantive content, clearly inform the student that more context is needed.
"""

SYSTEM_PROMPT_KEY_POINTS = """You are a helpful AI study assistant for engineering and computer science students.
Task: Extract the fundamental key points, core definitions, and formulas from the provided lecture notes.
Rules and Limits:
1. Output a numbered list of key points.
2. For each point, provide a bold heading followed by a concise 1-2 sentence explanation.
3. Every single point must be derived directly from the supplied notes. Do not extrapolate or add unmentioned details.
4. Keep the language precise, clear, and easy to memorize for exams.
"""

SYSTEM_PROMPT_PRACTICE_QUESTIONS = """You are an examination preparation assistant for engineering and computer science students.
Task: Generate high-yield practice revision questions based strictly on the provided lecture notes.
Rules and Limits:
1. Create a balanced set of questions:
   - Part A: Conceptual Short-Answer Questions (with concise model answers).
   - Part B: Multiple-Choice Questions (MCQs) with 4 options each, clearly indicating the correct answer and a brief explanation.
2. All questions and answers must be strictly answerable from the provided lecture notes alone.
3. Do not invent questions that require information absent from the text.
"""

SYSTEM_PROMPT_ASK_QUESTION = """You are a precise study tutor assisting a student by answering questions based strictly on their course notes.
Task: Answer the student's specific question using only the facts and explanations present in the provided notes.
Rules and Limits:
1. Answer the question directly and cite the relevant portion of the notes.
2. CRITICAL GROUNDING RULE: If the student's question cannot be answered using the provided notes, you MUST state clearly:
   "The provided notes do not contain sufficient information to answer this question."
   Do NOT attempt to guess, hallucinate, or rely on outside knowledge when the notes do not have the answer.
"""

SYSTEM_PROMPT_EXPLAIN_SIMPLY = """You are an intuitive educator skilled at explaining complex technical concepts using plain language (Feynman technique).
Task: Explain the core concepts of the provided notes in simple, beginner-friendly terms.
Rules and Limits:
1. Break down difficult jargon into everyday language.
2. Use relatable analogies where helpful, while maintaining strict factual accuracy with the notes.
3. Structure the explanation into:
   - "What is it?" (Plain definition)
   - "Real-world analogy"
   - "Why does it matter?"
4. Do not contradict or exceed the scope of the notes provided.
"""

# Map mode keys to their respective system prompts
SYSTEM_PROMPTS: Dict[str, str] = {
    "summarize": SYSTEM_PROMPT_SUMMARIZE,
    "key_points": SYSTEM_PROMPT_KEY_POINTS,
    "practice_questions": SYSTEM_PROMPT_PRACTICE_QUESTIONS,
    "ask_question": SYSTEM_PROMPT_ASK_QUESTION,
    "explain_simply": SYSTEM_PROMPT_EXPLAIN_SIMPLY,
}

def build_user_prompt(mode: str, notes: str, user_question: str = "") -> str:
    """
    Constructs the user prompt combining context, task, and optional student question.
    """
    clean_notes = notes.strip()
    
    if mode == "ask_question":
        return (
            f"--- STUDENT LECTURE NOTES ---\n"
            f"{clean_notes}\n"
            f"--- END OF NOTES ---\n\n"
            f"STUDENT QUESTION: {user_question.strip()}\n\n"
            f"Please answer the question based solely on the notes above."
        )
    elif mode == "summarize":
        return (
            f"--- STUDENT LECTURE NOTES ---\n"
            f"{clean_notes}\n"
            f"--- END OF NOTES ---\n\n"
            f"Please summarize these notes clearly and concisely."
        )
    elif mode == "key_points":
        return (
            f"--- STUDENT LECTURE NOTES ---\n"
            f"{clean_notes}\n"
            f"--- END OF NOTES ---\n\n"
            f"Please extract the core key points from these notes as a numbered list."
        )
    elif mode == "practice_questions":
        return (
            f"--- STUDENT LECTURE NOTES ---\n"
            f"{clean_notes}\n"
            f"--- END OF NOTES ---\n\n"
            f"Please generate revision practice questions with answers based strictly on these notes."
        )
    elif mode == "explain_simply":
        return (
            f"--- STUDENT LECTURE NOTES ---\n"
            f"{clean_notes}\n"
            f"--- END OF NOTES ---\n\n"
            f"Please explain the concepts in these notes in simple words with intuitive analogies."
        )
    else:
        return f"Notes:\n{clean_notes}"
