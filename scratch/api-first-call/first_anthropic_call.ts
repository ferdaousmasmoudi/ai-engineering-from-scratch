import "dotenv/config";
import Anthropic from "@anthropic-ai/sdk";

async function main() {
  const apiKey = process.env.ANTHROPIC_API_KEY;

  if (!apiKey) {
    throw new Error("ANTHROPIC_API_KEY is missing. Add it to your .env file.");
  }

  const client = new Anthropic({
    apiKey,
  });

  const response = await client.messages.create({
    model: "claude-sonnet-4-6",
    max_tokens: 256,
    messages: [
      {
        role: "user",
        content: "What is a neural network in one sentence?",
      },
    ],
  });

  const firstBlock = response.content[0];

  if (firstBlock.type === "text") {
    console.log(firstBlock.text);
  } else {
    console.log(firstBlock);
  }
}

main().catch((error) => {
  console.error("API call failed:");
  console.error(error);
  process.exit(1);
});
