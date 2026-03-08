# main.py - COMPLETE ASSISTANT (No API required)
import os
from datetime import datetime


class CodeAssistant:
    def __init__(self):
        # TASK 0: System Prompt
        self.system_prompt = "You are a helpful coding assistant."

        # TASK 1: Memory
        self.memory = []

        # TASK 2: Simple Vector DB (using dictionary)
        self.vector_db = {
            "factorial": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)",
            "fibonacci": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
            "palindrome": "def is_palindrome(s):\n    return s == s[::-1]",
            "reverse": "def reverse_string(s):\n    return s[::-1]"
        }

        # TASK 5: Self-learning storage
        self.knowledge = {}

        print("=" * 50)
        print("✅ CODE ASSISTANT - READY")
        print("=" * 50)
        print("✓ System Prompt: Active")
        print("✓ Memory: Active")
        print("✓ Vector DB: Active (5 examples)")
        print("✓ RAG: Active")
        print("✓ Router: Active")
        print("✓ Self-Learning: Active")
        print("=" * 50)

    # TASK 4: Router
    def router(self, text):
        if any(word in text.lower() for word in ['generate', 'write', 'code', 'function']):
            return "generate"
        return "explain"

    # TASK 3: RAG Generation
    def rag_generate(self, task):
        # Find similar code in vector DB
        similar = []
        for key, code in self.vector_db.items():
            if key in task.lower():
                similar.append(code)

        # Add self-learned knowledge
        for key, code in self.knowledge.items():
            if key in task.lower():
                similar.append(code)

        if similar:
            return f"📚 Found {len(similar)} examples:\n\n{similar[0]}"
        else:
            return f"❌ No examples found for: {task}"

    # TASK 5: Learn new things
    def learn(self, topic, code):
        self.knowledge[topic.lower()] = code
        self.vector_db[topic.lower()] = code
        return f"✅ Learned: {topic}"

    def run(self):
        while True:
            print("\n" + "-" * 40)
            cmd = input("You: ").strip()

            # Router
            intent = self.router(cmd)

            # Generate response
            if intent == "generate":
                response = self.rag_generate(cmd)
            else:
                response = "I can help you generate code. Try: 'generate function to reverse string'"

            print(f"\n🤖 [{intent.upper()}]: {response}")

            # TASK 1: Save to memory
            self.memory.append({
                "time": datetime.now().strftime("%H:%M"),
                "input": cmd,
                "intent": intent
            })

            # Special commands
            if cmd == "/learn":
                topic = input("Topic to learn: ")
                print("Paste your code (type 'END' on a new line when finished):")
                code_lines = []
                while True:
                    line = input()
                    if line == "END":
                        break
                    code_lines.append(line)
                code = "\n".join(code_lines)
                print(self.learn(topic, code))
            elif cmd == "/memory":
                print("\n📝 Recent Memory:")
                for m in self.memory[-5:]:
                    print(f"  [{m['time']}] {m['intent']}: {m['input'][:30]}...")
            elif cmd == "/db":
                print(f"\n📚 Vector DB: {len(self.vector_db)} items")
                print(f"📚 Knowledge: {len(self.knowledge)} items")
            elif cmd == "/exit":
                break

if __name__ == "__main__":
    app = CodeAssistant()
    print("\nCommands: /learn, /memory, /db, /exit")
    app.run()