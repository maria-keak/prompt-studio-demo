import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You summarize support tickets. Read the ticket and write a summary.
The summary should be useful for the support team. Mention important things like the customer plan, urgency and what they already tried."""


def summarize_ticket(ticket_text: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4.5",
        max_tokens=300,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Ticket:\n{ticket_text}"}],
    )
    return message.content[0].text
