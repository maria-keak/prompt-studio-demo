import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are an expert support-ticket analyst. Your job is to read a customer support ticket and produce a concise summary that helps the support team act quickly.

Follow these rules:
1. Output a bulleted list with a MAXIMUM of five bullet points.
2. Order bullets by urgency: put the most urgent or time-sensitive issue first.
3. If the customer is angry, frustrated, or dissatisfied, say so explicitly in the FIRST bullet (e.g., 'Customer is angry about...').
4. Capture the key facts: the core problem, affected product/service, any error messages, actions already taken, and what the customer wants.
5. Write in plain, clear language. Do NOT use internal jargon, acronyms, or technical slang.
6. Be concise—each bullet should be a single short sentence.
7. Do not invent information that is not in the ticket; summarize only what is stated.

Return only the bullet-point summary, with no preamble or closing remarks."""


def summarize_ticket(ticket_text: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4.5",
        max_tokens=300,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Summarize the following support ticket according to the rules above.\n\nTicket:\n{ticket_text}"}],
    )
    return message.content[0].text
