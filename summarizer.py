import ollama

MODEL = "mistral"


def summarize_chunk(chunk):

    prompt = f"""
Summarize the following document section.

Document:
{chunk}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def generate_final_summary(chunk_summaries):

    combined = "\n\n".join(chunk_summaries)

    prompt = f"""
Using the summaries below, generate one professional report.

Use exactly these headings:

# Executive Summary

# Key Points

# Risks or Concerns

# Opportunities

# Action Items

Summaries:

{combined}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
