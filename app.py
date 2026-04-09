from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

while True:
    topic = input("Enter topic: ")

    if topic.lower() == "exit":
        break

    prompt = f"Write a social media post about {topic}:"

    result = generator(prompt, max_length=100, num_return_sequences=1)
    print("\nGenerated Content:\n", result[0]['generated_text'])