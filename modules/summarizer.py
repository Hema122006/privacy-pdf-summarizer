from transformers import pipeline

# Load summarization model
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def generate_summary(text):

    if not text:
        return "No text found."

    if len(text) < 100:
        return text

    # BART has input length limits
    text = text[:3000]

    summary = summarizer(
        text,
        max_length=120,
        min_length=40,
        do_sample=False
    )

    return summary[0]["summary_text"]
