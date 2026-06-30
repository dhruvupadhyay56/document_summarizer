import ollama


def summarize_chunk(chunk):
    prompt = f"""
    Summarize this document chunk clearly.

    Document chunk:
    {chunk}
    """

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]


def generate_final_summary(chunk_summaries):
    combined_summaries = "\n".join(chunk_summaries)

    prompt = f"""
    Based on these chunk summaries, create a structured report.

    Format strictly as:

    Executive Summary:
    Key Points:
    Risks or Concerns:
    Opportunities:
    Action Items:

    Content:
    {combined_summaries}
    """

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
