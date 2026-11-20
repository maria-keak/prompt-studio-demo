import OpenAI from "openai";

const client = new OpenAI();

const SYSTEM_PROMPT = `You are a helpful assistant that helps users with their questions about our product.
Be nice and friendly and answer the question the customer asked. If you don't know, say you don't know
and tell them someone from the team will get back to them.
Try to keep answers short but also include all the details the user might need, like links or steps.
Always reply in the language the customer wrote in.
Never share internal ticket numbers or staff names.`;

export async function replyToCustomer(customerName: string, question: string, plan: string) {
  const response = await client.chat.completions.create({
    model: "gpt-4o-mini",
    messages: [
      { role: "system", content: SYSTEM_PROMPT },
      { role: "user", content: `Customer ${customerName} on the ${plan} plan asks: ${question}` },
    ],
  });
  return response.choices[0].message.content;
}
