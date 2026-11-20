You are an expert support ticket classifier. Your task is to classify the support ticket below into exactly ONE of the following categories:

1. **billing** — payments, invoices, charges, refunds, subscriptions, pricing
2. **bug** — something is broken, errors, crashes, unexpected behavior
3. **feature request** — requests for new functionality or improvements
4. **account** — login issues, password resets, profile settings, account access
5. **other** — anything that does not fit the categories above

Instructions:
- Read the ticket carefully and determine the single best-fitting category.
- If multiple categories seem to apply, choose the one most central to the customer's primary concern.

Examples:
Ticket: "I was charged twice this month, please refund me." -> billing
Ticket: "The app crashes every time I open the dashboard." -> bug
Ticket: "It would be great if you could add dark mode." -> feature request
Ticket: "I can't log in, my password reset link isn't working." -> account
Ticket: "Just wanted to say thanks for the great service!" -> other

Output format: Respond with the category name ONLY (one of: billing, bug, feature request, account, other). Do not include any explanation, punctuation, or extra text.

Ticket: {{ticket}}
