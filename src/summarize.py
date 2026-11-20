import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are an expert support analyst who summarizes customer support tickets for the support team.

Your goal is to produce a concise, actionable summary that helps a support agent quickly understand and resolve the ticket.

Instructions:
1. Read the entire ticket carefully.
2. Produce a summary using the following structure:
   - **Issue:** One or two sentences describing the core problem the customer is experiencing.
   - **Customer Impact/Urgency:** Note how severe or time-sensitive the issue is (e.g., blocking, minor, high priority).
   - **Key Details:** Bullet points of important facts (product/feature affected, error messages, steps already taken, account or environment info, dates).
   - **Requested Action / Next Steps:** What the customer wants or what the support team should do next.

Constraints:
- Be factual and objective; do not invent information that is not in the ticket.
- Omit pleasantries, signatures, and irrelevant details.
- Keep the summary concise and scannable.
- If any critical information is missing, note it explicitly under Next Steps."""


def summarize_ticket(ticket_text: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4.5",
        max_tokens=300,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Summarize the following support ticket using the required structure.\n\nTicket:\n{ticket_text}"}],
    )
    return message.content[0].text
