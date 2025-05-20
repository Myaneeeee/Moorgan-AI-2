const apiKey =
  "1uGCfwfH0sL6uujrWLgWEV1BkCcOnUQvXkkj12GTdi0cyIULB7mqJQQJ99BEACHYHv6XJ3w3AAAAACOGatVB";
const apiVersion = "2024-04-01-preview";
const endpoint = "https://farre-mawkmksj-eastus2.cognitiveservices.azure.com/";
const modelName = "gpt-4o";
const deployment = "Moorgan";
const options = { endpoint, apiKey, deployment, apiVersion };

const client = new AzureOpenAI(options);

import { AzureOpenAI } from "openai";

export async function main() {
  const apiKey =
    "1uGCfwfH0sL6uujrWLgWEV1BkCcOnUQvXkkj12GTdi0cyIULB7mqJQQJ99BEACHYHv6XJ3w3AAAAACOGatVB";
  const apiVersion = "2024-04-01-preview";
  const options = { endpoint, apiKey, deployment, apiVersion };

  const client = new AzureOpenAI(options);

  const response = await client.chat.completions.create({
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "I am going to Paris, what should I see?" },
    ],
    max_tokens: 4096,
    temperature: 1,
    top_p: 1,
    model: modelName,
  });

  if (response?.error !== undefined && response.status !== "200") {
    throw response.error;
  }
  console.log(response.choices[0].message.content);
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
